# -*- coding: utf-8 -*-
import math
import pygame
from colors import WHITE, ORANGE
from settings import ENEMY_SIZE

class Enemy:
    """Moves along path; center displays an integer HP number."""
    def __init__(self, path_points, hp, speed):
        self.path = list(path_points)
        self.hp = float(hp)
        self.max_hp = float(hp)
        self.speed = float(speed)
        self.dead = False
        self.reached = False
        self.idx = 0           # path index (larger = further along)
        self.x, self.y = self.path[0]
        self.money_drop = 1.0
        self.slow_ratio = 1.0
        self.slow_timer = 0.0
        self.carries_coin = False

    def apply_slow(self, ratio, duration):
        self.slow_ratio = min(self.slow_ratio, ratio)
        self.slow_timer = max(self.slow_timer, duration)

    def hit(self, dmg):
        self.hp -= dmg
        if self.hp <= 0 and not self.dead:
            self.dead = True

    def update(self, dt, speed_mult=1.0, zone_mult=1.0):
        if self.dead or self.reached or self.idx >= len(self.path) - 1:
            return
        if self.slow_timer > 0:
            self.slow_timer -= dt
            if self.slow_timer <= 0:
                self.slow_ratio = 1.0

        tx, ty = self.path[self.idx + 1]
        dx, dy = tx - self.x, ty - self.y
        dist = math.hypot(dx, dy)
        step = self.speed * self.slow_ratio * speed_mult * zone_mult * dt
        if step >= dist and dist > 0:
            self.x, self.y = tx, ty
            self.idx += 1
            if self.idx >= len(self.path) - 1:
                self.reached = True
        elif dist > 0:
            nx, ny = dx / dist, dy / dist
            self.x += nx * step
            self.y += ny * step

    def draw(self, surf, font):
        r = pygame.Rect(int(self.x - ENEMY_SIZE/2), int(self.y - ENEMY_SIZE/2), ENEMY_SIZE, ENEMY_SIZE)
        pygame.draw.rect(surf, ORANGE, r, border_radius=10)
        hp_txt = font.render(str(max(0, int(self.hp + 0.5))), True, WHITE)
        surf.blit(hp_txt, (r.centerx - hp_txt.get_width()//2, r.centery - hp_txt.get_height()//2))

class Boss(Enemy):
    def __init__(self, path_points, hp, speed):
        super().__init__(path_points, hp, speed)
        self.money_drop = 3.0
        self.ability_cd = 0.0

    def update(self, dt, speed_mult=1.0, zone_mult=1.0):
        super().update(dt, speed_mult, zone_mult)
        self.ability_cd += dt * speed_mult

    def try_ability(self, game):
        # cast a telegraph zone near grid center
        import random
        if not game or self.dead:
            return
        gx = game.grid.cols // 2
        gy = game.grid.rows // 2
        c = random.randint(max(0, gx-1), min(game.grid.cols-1, gx+1))
        r = random.randint(max(0, gy-1), min(game.grid.rows-1, gy+1))
        px, py = game.grid.center_of(c, r)
        game.spawn_telegraph(px, py)
