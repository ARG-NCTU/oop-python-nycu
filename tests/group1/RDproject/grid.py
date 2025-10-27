# -*- coding: utf-8 -*-
import pygame, random
from colors import GRAY, ACCENT
from settings import GRID_COLS, GRID_ROWS, CELL_SIZE, GRID_X, GRID_Y, DIE_COST, MERGE_REFUND, MAX_DIE_LEVEL
from dice import DIE_TYPES, make_die

class Grid:
    def __init__(self, game):
        self.game = game
        self.cols = GRID_COLS
        self.rows = GRID_ROWS
        self.cells = [[None for _ in range(self.rows)] for _ in range(self.cols)]
        self.selected = None  # (c, r)

    def in_bounds(self, c, r):
        return 0 <= c < self.cols and 0 <= r < self.rows

    def rect_at(self, c, r):
        x = GRID_X + c * CELL_SIZE
        y = GRID_Y + r * CELL_SIZE
        return pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

    def center_of(self, c, r):
        rct = self.rect_at(c, r)
        return rct.centerx, rct.centery

    def get(self, c, r):
        return self.cells[c][r]

    def set(self, c, r, obj):
        self.cells[c][r] = obj

    def remove(self, c, r):
        if self.in_bounds(c, r):
            self.set(c, r, None)

    def iterate(self):
        for c in range(self.cols):
            for r in range(self.rows):
                yield c, r, self.cells[c][r]

    def update(self, dt):
        for c, r, d in self.iterate():
            if d:
                d.update(dt)

    def draw(self, surf):
        for c in range(self.cols):
            for r in range(self.rows):
                rect = self.rect_at(c, r)
                pygame.draw.rect(surf, GRAY, rect, width=3, border_radius=10)
                die = self.get(c, r)
                if die:
                    selected = (self.selected == (c, r))
                    die.draw(surf, selected)

        mx, my = pygame.mouse.get_pos()
        if GRID_X <= mx < GRID_X + self.cols * CELL_SIZE and GRID_Y <= my < GRID_Y + self.rows * CELL_SIZE:
            hc = (mx - GRID_X) // CELL_SIZE
            hr = (my - GRID_Y) // CELL_SIZE
            pygame.draw.rect(surf, ACCENT, self.rect_at(hc, hr), width=3, border_radius=10)

    def handle_click(self, event):
        if event.button != 1:
            return
        mx, my = event.pos
        if not (GRID_X <= mx < GRID_X + self.cols * CELL_SIZE and GRID_Y <= my < GRID_Y + self.rows * CELL_SIZE):
            return
        c = (mx - GRID_X) // CELL_SIZE
        r = (my - GRID_Y) // CELL_SIZE
        clicked = self.get(c, r)

        if self.game.trash_active:
            if clicked is not None:
                self.set(c, r, None)
            self.game.trash_active = False
            self.selected = None
            return

        if clicked is None:
            if self.game.money >= DIE_COST:
                pool = self.game.loadout.selected or DIE_TYPES
                t = random.choice(pool)
                die = make_die(self.game, c, r, t, level=1)
                self.set(c, r, die)
                self.game.money -= DIE_COST
                self.selected = None
        else:
            sel = self.selected
            if sel is None:
                self.selected = (c, r)
            else:
                sc, sr = sel
                if (c, r) == (sc, sr):
                    self.selected = None
                else:
                    a = self.get(sc, sr)
                    b = clicked
                    if a and b and a.can_merge_with(b):
                        new_lv = min(a.level + 1, MAX_DIE_LEVEL)
                        ttype = a.type
                        self.set(c, r, make_die(self.game, c, r, ttype, new_lv))
                        self.set(sc, sr, None)
                        self.game.money += MERGE_REFUND
                        self.selected = None
                    else:
                        self.selected = None
