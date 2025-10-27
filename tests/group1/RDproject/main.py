# -*- coding: utf-8 -*-
import pygame, sys, random, math
from settings import *
from ui import Button, draw_panel, Segmented
from grid import Grid
from level_manager import LevelManager
from loadout import Loadout
from upgrades import UpgradeState
from enemy import Enemy, Boss
from dice import DIE_TYPES
from colors import WHITE, DARKER, GRAY, RED
from effects import TelegraphZone

STATE_LOBBY = "lobby"
STATE_PLAY = "play"
STATE_GAMEOVER = "gameover"
STATE_HELP = "help"
STATE_LOADOUT = "loadout"
STATE_UPGRADES = "upgrades"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 22)
        self.font_big = pygame.font.SysFont("arial", 28, bold=True)
        self.font_huge = pygame.font.SysFont("arial", 48, bold=True)

        self.state = STATE_LOBBY
        self.level_mgr = LevelManager()
        self.level = None

        self.grid = Grid(self)
        self.loadout = Loadout(["single", "multi", "freeze"])
        self.upgrades = UpgradeState()
        self.enemies = []
        self.bullets = []
        self.telegraphs = []
        self.money = START_MONEY
        self.base_hp = BASE_HP
        self.wave = -1
        self.to_spawn = 0
        self.spawn_cd = 0.0
        self.spawn_interval = 0.9
        self.is_boss_wave = False

        self.speed_index = DEFAULT_SPEED_INDEX
        self.speed_mult = GAME_SPEEDS[self.speed_index]
        self.target_mode = "nearest"  # nearest / first / weak / strong
        self.trash_active = False

        self.speed_ctrl = Segmented((SCREEN_W - 420, 24, 360, 40),
                                    ["0.5×","1×","2×","4×","8×"], self.font_big,
                                    self.speed_index, self.on_speed_change)
        self.btn_trash = Button((SCREEN_W - 820, 24, 120, 40), "Trash", self.font_big, self.toggle_trash)

        self._build_lobby()

    # --------------- Lobby ---------------
    def _build_lobby(self):
        self.buttons = []
        bx, by, bw, bh = 60, 160, 220, 50
        gap = 10
        # three levels
        for i, lvl in enumerate(self.level_mgr.levels):
            self.buttons.append(Button((bx, by + i*(bh+gap), bw, bh), f"Start: {lvl.name}", self.font_big, lambda i=i: self.start_level(i)))
        # loadout & upgrades
        self.buttons.append(Button((bx, by + 3*(bh+gap), bw, bh), "Carry Team", self.font_big, self.goto_loadout))
        self.buttons.append(Button((bx, by + 4*(bh+gap), bw, bh), "Upgrades", self.font_big, self.goto_upgrades))
        # help & quit
        self.buttons.append(Button((bx, by + 5*(bh+gap), bw, bh), "Help", self.font_big, self.goto_help))
        self.quit_btn = Button((bx, SCREEN_H - 100, bw, bh), "Quit", self.font_big, self.quit)

    def start_level(self, idx):
        self.level = self.level_mgr.get(idx)
        self.reset_runtime()
        self.state = STATE_PLAY

    def goto_help(self):
        self.state = STATE_HELP
        self.help_back = Button((24, SCREEN_H - 74, 180, 48), "Back to Lobby", self.font_big, self.back_to_lobby)

    def goto_loadout(self):
        self.state = STATE_LOADOUT
        self.loadout_back = Button((24, SCREEN_H - 74, 180, 48), "Back", self.font_big, self.back_to_lobby)

    def goto_upgrades(self):
        self.state = STATE_UPGRADES
        self.upg_back = Button((24, SCREEN_H - 74, 180, 48), "Back", self.font_big, self.back_to_lobby)

    def back_to_lobby(self):
        self.state = STATE_LOBBY
        self._build_lobby()

    def reset_runtime(self):
        self.grid = Grid(self)
        self.enemies = []
        self.bullets = []
        self.telegraphs = []
        self.money = START_MONEY
        self.base_hp = BASE_HP
        self.wave = -1
        self.to_spawn = 0
        self.spawn_cd = 0.0
        self.is_boss_wave = False
        self.trash_active = False

    # --------------- Events ---------------
    def on_speed_change(self, idx):
        self.speed_index = idx
        self.speed_mult = GAME_SPEEDS[idx]

    def toggle_trash(self):
        self.trash_active = not self.trash_active

    def handle_play(self, event):
        if event.type == pygame.KEYDOWN:
            if event.unicode in ('1','2','3','4','5'):
                idx = int(event.unicode) - 1
                self.on_speed_change(idx); return
            elif event.key == pygame.K_t:
                order = ["nearest", "first", "weak", "strong"]
                i = order.index(self.target_mode)
                self.target_mode = order[(i + 1) % len(order)]
            elif event.key == pygame.K_r:
                self.reset_runtime(); self.state = STATE_PLAY
            elif event.key == pygame.K_ESCAPE:
                self.back_to_lobby()
            elif event.key == pygame.K_n:
                if self.to_spawn <= 0 and len(self.enemies) == 0:
                    self.start_wave()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            self.grid.selected = None
            self.trash_active = False
            return
        self.speed_ctrl.handle(event)
        self.btn_trash.handle(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.grid.handle_click(event)

    def gameover_handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.reset_runtime(); self.state = STATE_PLAY
            elif event.key == pygame.K_ESCAPE:
                self.back_to_lobby()

    def help_handle(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.back_to_lobby()
        self.help_back.handle(event)

    def loadout_handle(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.back_to_lobby()
        self.loadout_back.handle(event)
        # click on chips
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            bx, by, w, h, gap = 420, 200, 220, 60, 16
            for i, t in enumerate(["single","multi","freeze"]):
                r = pygame.Rect(bx, by + i*(h+gap), w, h)
                if r.collidepoint(mx, my):
                    self.loadout.toggle(t)

    def upgrades_handle(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.back_to_lobby()
        self.upg_back.handle(event)
        # simple buttons per type & stat
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            base_x, base_y = 420, 200
            btn_w, btn_h = 220, 50
            gap_x, gap_y = 30, 16
            types = ["single","multi","freeze"]
            labels = [("Damage +10%", "dmg"), ("Fire rate +8%", "fire"), ("Cost -10%", "cost")]
            for row, t in enumerate(types):
                for col, (lab, kind) in enumerate(labels):
                    r = pygame.Rect(base_x + col*(btn_w+gap_x), base_y + row*(btn_h+gap_y), btn_w, btn_h)
                    if r.collidepoint(mx, my):
                        if kind == "dmg":
                            self.upgrades.upgrade_damage(t)
                        elif kind == "fire":
                            self.upgrades.upgrade_fire(t)
                        else:
                            self.upgrades.upgrade_cost(t)

    # --------------- Flow ---------------
    def start_wave(self):
        self.telegraphs = []
        self.wave += 1
        count, is_boss = self.level_mgr.wave_info(self.wave)
        count = int(count * self.level.difficulty)
        self.to_spawn = count
        self.spawn_cd = 0.0
        self.is_boss_wave = is_boss

    def spawn_enemy(self):
        hp = (8 + self.wave * 4) * self.level.difficulty
        speed = (36 + min(140, self.wave * 6)) * (0.9 + 0.2 * random.random())
        path = list(self.level.path)
        if self.is_boss_wave and self.to_spawn == 1:
            hp *= BOSS_HP_MULT
            e = Boss(path, hp, speed * 0.85)
        else:
            e = Enemy(path, hp, speed)
        if self.to_spawn == 1:
            e.carries_coin = True
        if len(path) == 2:
            e.y += random.randint(-60, 60)
        self.enemies.append(e)

    def spawn_telegraph(self, px, py):
        rpx = CELL_SIZE * (BOSS_DESTROY_RADIUS + 0.5)
        z = TelegraphZone(px, py, rpx, BOSS_TELEGRAPH_WARN, BOSS_DEBUFF_DURATION,
                          enemy_speed_mult=BOSS_ZONE_SLOW_ENEMY, dice_period_mult=BOSS_ZONE_SLOW_DICE)
        self.telegraphs.append(z)

    # --------------- Update ---------------
    def update(self, dt):
        if self.state != STATE_PLAY:
            return

        if self.to_spawn > 0:
            self.spawn_cd += dt * self.speed_mult
            if self.spawn_cd >= self.spawn_interval:
                self.spawn_cd = 0.0
                self.to_spawn -= 1
                self.spawn_enemy()

        # telegraphs
        for z in list(self.telegraphs):
            z.update(dt * self.speed_mult)
            if not z.active():
                self.telegraphs.remove(z)

        # enemies
        for e in list(self.enemies):
            zone_mult = 1.0
            for z in self.telegraphs:
                if z.in_effect_phase() and z.contains(e.x, e.y):
                    zone_mult *= z.enemy_speed_mult
            e.update(dt, speed_mult=self.speed_mult, zone_mult=zone_mult)
            if isinstance(e, Boss):
                if e.ability_cd >= BOSS_TELEGRAPH_WARN + BOSS_DEBUFF_DURATION + 5.0:
                    e.ability_cd = 0.0
                    e.try_ability(self)

            if e.dead:
                self.money += int(e.money_drop + self.wave)
                if getattr(e, "carries_coin", False):
                    self.upgrades.add_coin(1)
                self.enemies.remove(e)
            elif e.reached:
                self.base_hp -= 1
                self.enemies.remove(e)

        # bullets
        for b in list(self.bullets):
            if b.update(dt):
                self.bullets.remove(b)

        # dice
        self.grid.update(dt)

        # end
        if self.base_hp <= 0:
            self.state = STATE_GAMEOVER

    # --------------- Draw ---------------
    def lobby_draw(self):
        self.screen.fill(DARKER)
        left = pygame.Rect(20, 20, PANEL_W, SCREEN_H - 40)
        def _left():
            y = left.y + 70
            lines = [
                "Pick a level, or open Carry Team / Upgrades.",
                "Left click empty: place Lv1 die ($10)",
                "Left click die: select; merge same TYPE & LEVEL (+$3)",
                "Boss waves are tougher and drop more money.",
            ]
            for s in lines:
                t = self.font.render(s, True, WHITE)
                self.screen.blit(t, (left.x + 20, y)); y += 24
        draw_panel(self.screen, left, "Lobby", self.font_big, _left)

        for b in self.buttons:
            b.draw(self.screen)
        self.quit_btn.draw(self.screen)

        right = pygame.Rect(PANEL_W + 40, 20, SCREEN_W - PANEL_W - 60, SCREEN_H - 40)
        pygame.draw.rect(self.screen, (32,34,58), right, border_radius=16)

    def play_draw(self):
        self.screen.fill((18,22,30))
        if self.level:
            pygame.draw.lines(self.screen, GRAY, False, self.level.path, 6)

        self.grid.draw(self.screen)
        for e in self.enemies:
            e.draw(self.screen, self.font)
        for b in self.bullets:
            b.draw(self.screen)

        # telegraph swirl
        for z in self.telegraphs:
            color = (255, 60, 60) if not z.in_effect_phase() else (255, 120, 120)
            pygame.draw.circle(self.screen, color, (int(z.x), int(z.y)), int(z.r), width=4)
            for i in range(6):
                ang = (z.t*3 + i*math.pi/3)
                rx = int(z.x + (z.r-10) * math.cos(ang))
                ry = int(z.y + (z.r-10) * math.sin(ang))
                pygame.draw.circle(self.screen, color, (rx, ry), 6)

        panel_rect = pygame.Rect(20, 20, 300, 260)
        def _body():
            y = panel_rect.y + 60
            pairs = [
                ("Money", f"${self.money}"),
                ("Wave", str(max(0, self.wave))),
                ("Base HP", str(self.base_hp)),
                ("Speed", f"{self.speed_mult}×"),
                ("Target", {"nearest":"Nearest","first":"Front","weak":"Weak","strong":"Strong"}[self.target_mode]),
                ("Coins", str(self.upgrades.coins)),
            ]
            for name, val in pairs:
                txt = self.font.render(f"{name}: {val}", True, WHITE)
                self.screen.blit(txt, (panel_rect.x + 20, y)); y += 26

            y += 10
            tips = [
                "Hotkeys: 1~5 speed, T target, N next wave",
                "Right click cancels / exits Trash",
                "Press ESC for lobby",
            ]
            for s in tips:
                t = self.font.render(s, True, WHITE)
                self.screen.blit(t, (panel_rect.x + 20, y)); y += 22
        draw_panel(self.screen, panel_rect, "Status", self.font_big, _body)

        self.speed_ctrl.draw(self.screen)
        self.btn_trash.draw(self.screen)

        if self.to_spawn <= 0 and len(self.enemies) == 0:
            top = self.font_big.render("Press N to start next wave", True, WHITE)
            self.screen.blit(top, (GRID_X, 42))

    def gameover_draw(self):
        self.screen.fill((15,15,25))
        t = self.font_huge.render("GAME OVER", True, RED)
        self.screen.blit(t, (SCREEN_W//2 - t.get_width()//2, SCREEN_H//2 - 100))
        sub = self.font_big.render("R: Restart   ESC: Lobby", True, WHITE)
        self.screen.blit(sub, (SCREEN_W//2 - sub.get_width()//2, SCREEN_H//2))

    def help_draw(self):
        self.screen.fill((22,24,36))
        title = self.font_huge.render("Help", True, (255,255,255))
        self.screen.blit(title, (40, 60))
        lines = [
            "• Left click empty: place Lv1 die",
            "• Left click die: select / merge (same TYPE & LEVEL)",
            "• Right click: cancel selection / exit Trash",
            "• Speed: top-right control or 1~5 keys",
            "• Target mode: press T to cycle (Nearest / Front / Weak / Strong)",
            "• When field is clear press N to start next wave",
            "• R to restart; ESC for lobby",
        ]
        y = 140
        for s in lines:
            t = self.font.render(s, True, (230,230,240))
            self.screen.blit(t, (40, y)); y += 30
        self.help_back.draw(self.screen)

    def loadout_draw(self):
        self.screen.fill(DARKER)
        title = self.font_huge.render("Carry Team", True, (255,255,255))
        self.screen.blit(title, (40, 60))
        sub = self.font.render("Pick up to 5 dice types for this run (currently 3 available).", True, WHITE)
        self.screen.blit(sub, (40, 120))

        bx, by, w, h, gap = 420, 200, 220, 60, 16
        types = ["single","multi","freeze"]
        for i, t in enumerate(types):
            r = pygame.Rect(bx, by + i*(h+gap), w, h)
            active = (t in self.loadout.selected)
            self.loadout.draw_chip(self.screen, r, t, self.font_big, active)
        sel = ", ".join(self.loadout.selected) if self.loadout.selected else "(none)"
        info = self.font.render(f"Selected: {sel}", True, WHITE)
        self.screen.blit(info, (bx, by + 3*(h+gap) + 20))

        self.loadout_back.draw(self.screen)

    def upgrades_draw(self):
        self.screen.fill(DARKER)
        title = self.font_huge.render("Upgrades", True, (255,255,255))
        self.screen.blit(title, (40, 60))
        coins = self.font_big.render(f"Coins: {self.upgrades.coins}", True, WHITE)
        self.screen.blit(coins, (40, 120))
        base_x, base_y = 420, 200
        btn_w, btn_h = 220, 50
        gap_x, gap_y = 30, 16
        types = ["single","multi","freeze"]
        labels = [("Damage +10% (2c)", "dmg"), ("Fire rate +8% (2c)", "fire"), ("Cost -10% (2c)", "cost")]
        for row, t in enumerate(types):
            name = self.font_big.render(t.capitalize(), True, WHITE)
            self.screen.blit(name, (base_x - 150, base_y + row*(btn_h+gap_y) + 8))
            for col, (lab, kind) in enumerate(labels):
                r = pygame.Rect(base_x + col*(btn_w+gap_x), base_y + row*(btn_h+gap_y), btn_w, btn_h)
                Button(r, lab, self.font, lambda t=t, kind=kind: (
                    self.upgrades.upgrade_damage(t) if kind=="dmg" else
                    (self.upgrades.upgrade_fire(t) if kind=="fire" else self.upgrades.upgrade_cost(t))
                )).draw(self.screen)

        self.upg_back.draw(self.screen)

    # --------------- Frame ---------------
    def draw(self):
        if self.state == STATE_LOBBY:
            self.lobby_draw()
        elif self.state == STATE_PLAY:
            self.play_draw()
        elif self.state == STATE_GAMEOVER:
            self.gameover_draw()
        elif self.state == STATE_HELP:
            self.help_draw()
        elif self.state == STATE_LOADOUT:
            self.loadout_draw()
        elif self.state == STATE_UPGRADES:
            self.upgrades_draw()
        pygame.display.flip()

    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # don't auto-quit on game over; here only explicit window close
                    self.quit()
                if self.state == STATE_LOBBY:
                    for b in self.buttons:
                        b.handle(event)
                    self.quit_btn.handle(event)
                elif self.state == STATE_PLAY:
                    self.handle_play(event)
                elif self.state == STATE_GAMEOVER:
                    self.gameover_handle(event)
                elif self.state == STATE_HELP:
                    self.help_handle(event)
                elif self.state == STATE_LOADOUT:
                    self.loadout_handle(event)
                elif self.state == STATE_UPGRADES:
                    self.upgrades_handle(event)

            self.update(dt)
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit(0)


if __name__ == "__main__":
    Game().run()
