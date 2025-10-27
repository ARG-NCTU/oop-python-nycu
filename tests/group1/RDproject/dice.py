# -*- coding: utf-8 -*-
import math, os, pygame, random
from colors import WHITE, DICE_COLORS
from settings import BASE_RANGE, BASE_FIRE_RATE, FIRE_RATE_STEP, MAX_DIE_LEVEL, ASSET_FILES, FPS
from settings import BOSS_ZONE_SLOW_DICE, FREEZE_DURATION, FREEZE_SLOW_RATIO
from projectiles import Bullet, ChainBolt

DIE_SINGLE = "single"
DIE_MULTI = "multi"
DIE_FREEZE = "freeze"
DIE_TYPES = [DIE_SINGLE, DIE_MULTI, DIE_FREEZE]

_dice_images_cache = {}

def _load_die_image(die_type):
    if die_type in _dice_images_cache:
        return _dice_images_cache[die_type]
    p = ASSET_FILES.get("dice", {}).get(die_type)
    if p and os.path.exists(os.path.join("assets", p)):
        img = pygame.image.load(os.path.join("assets", p)).convert_alpha()
        _dice_images_cache[die_type] = img
        return img
    _dice_images_cache[die_type] = None
    return None

class Die:
    """Base die: renders a colored card (or PNG), handles firing cadence."""
    def __init__(self, game, c, r, level=1):
        self.game = game
        self.c = c
        self.r = r
        self.level = level
        self.type = DIE_SINGLE
        self.range = BASE_RANGE
        self.base_fire_rate = max(12, BASE_FIRE_RATE - (self.level - 1) * FIRE_RATE_STEP)
        self.cool = 0.0
        self.image = None
        # Ensure period in seconds initialized at construction
        self.base_period_sec = self.base_fire_rate / FPS

    @property
    def x(self):
        return self.game.grid.center_of(self.c, self.r)[0]

    @property
    def y(self):
        return self.game.grid.center_of(self.c, self.r)[1]

    def set_level(self, lv):
        self.level = max(1, min(MAX_DIE_LEVEL, lv))
        self.base_fire_rate = max(8, BASE_FIRE_RATE - (self.level - 1) * FIRE_RATE_STEP)
        # Convert frame-based rate to seconds for stable timing across FPS
        self.base_period_sec = self.base_fire_rate / FPS
        self.cool = 0.0

    def can_merge_with(self, other):
        return other and (self.type == other.type) and (self.level == other.level)

    def draw(self, surf, selected):
        rect = self.game.grid.rect_at(self.c, self.r).inflate(-12, -12)
        base_col = DICE_COLORS.get(self.type, (140, 140, 160))
        pygame.draw.rect(surf, base_col, rect, border_radius=14)
        if selected:
            pygame.draw.rect(surf, WHITE, rect, width=3, border_radius=14)

        font = self.game.font_big
        lvl = font.render(f"Lv {self.level}", True, WHITE)
        surf.blit(lvl, (rect.centerx - lvl.get_width() // 2, rect.centery - lvl.get_height() // 2))

        if not self.image:
            self.image = _load_die_image(self.type)
        if self.image:
            ir = self.image.get_rect()
            scale = min(rect.w * 0.6 / ir.w, rect.h * 0.45 / ir.h)
            img = pygame.transform.smoothscale(self.image, (int(ir.w * scale), int(ir.h * scale)))
            surf.blit(img, (rect.centerx - img.get_width() // 2, rect.y + 8))

        pygame.draw.rect(surf, (255,255,255), rect, width=2, border_radius=14)
        glow = rect.copy()
        glow.h = int(rect.h * 0.35)
        highlight = pygame.Surface((glow.w, glow.h), pygame.SRCALPHA)
        highlight.fill((255, 255, 255, 42))
        surf.blit(highlight, glow.topleft)

    def update(self, dt):
        # dice period can be increased by boss zone effect
        zone_mult = 1.0
        for z in self.game.telegraphs:
            if z.in_effect_phase() and z.contains(self.x, self.y):
                zone_mult *= z.dice_period_mult
        self.cool += dt * self.game.speed_mult
        effective_period = self.base_period_sec * self.fire_rate_factor() * zone_mult
        if self.cool >= effective_period:
            self.cool = 0.0
            self.try_fire()

    def fire_rate_factor(self):
        return self.game.upgrades.fire_rate_mult.get(self.type, 1.0)

    def damage_multiplier(self):
        return self.game.upgrades.damage_mult.get(self.type, 1.0)

    def try_fire(self):
        mode = self.game.target_mode
        best = None
        bestv = None
        for e in self.game.enemies:
            if e.dead or e.reached:
                continue
            dx, dy = e.x - self.x, e.y - self.y
            d = (dx*dx + dy*dy) ** 0.5
            if d > self.range:
                continue

            if mode == "nearest":
                v = d; cond = (best is None) or (v < bestv)
            elif mode == "first":
                v = (e.idx, -d); cond = (best is None) or (v > bestv)
            elif mode == "weak":
                v = e.hp; cond = (best is None) or (v < bestv)
            else:
                v = e.hp; cond = (best is None) or (v > bestv)

            if cond:
                best = e; bestv = v

        if best:
            self.fire_at(best)

    def fire_at(self, target):
        base = 2 ** (self.level - 1)
        dmg = base * self.damage_multiplier()
        self.game.bullets.append(Bullet(self.game, self.x, self.y, target, dmg, speed_mult_provider=lambda: self.game.speed_mult))


class SingleDice(Die):
    def __init__(self, game, c, r, level=1):
        super().__init__(game, c, r, level)
        self.type = DIE_SINGLE


class MultiDice(Die):
    def __init__(self, game, c, r, level=1):
        super().__init__(game, c, r, level)
        self.type = DIE_MULTI

    def fire_at(self, target):
        jumps = max(0, self.level - 1)
        base = 2 ** (self.level - 1)
        dmg = base * self.damage_multiplier()
        self.game.bullets.append(ChainBolt(self.game, self.x, self.y, target, dmg, jumps, self.game.enemies, speed_mult_provider=lambda: self.game.speed_mult))


class FreezeDice(Die):
    def __init__(self, game, c, r, level=1):
        super().__init__(game, c, r, level)
        self.type = DIE_FREEZE

    def fire_at(self, target):
        base = 2 ** max(0, self.level - 2)
        dmg = base * self.damage_multiplier()
        self.game.bullets.append(Bullet(self.game, self.x, self.y, target, dmg, speed_mult_provider=lambda: self.game.speed_mult))
        target.apply_slow(FREEZE_SLOW_RATIO, FREEZE_DURATION + 0.2 * (self.level - 1))


def make_die(game, c, r, die_type, level=1):
    if die_type == DIE_MULTI:
        return MultiDice(game, c, r, level)
    elif die_type == DIE_FREEZE:
        return FreezeDice(game, c, r, level)
    return SingleDice(game, c, r, level)
