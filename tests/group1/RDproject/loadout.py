# -*- coding: utf-8 -*-
import pygame
from colors import WHITE, DICE_COLORS, DARK, ACCENT

class Loadout:
    """Holds selected dice types for a run (up to 5; default selects the first 3)."""
    def __init__(self, available_types, *, max_slots=5):
        self.available = list(available_types)
        self.max_slots = max_slots
        self.selected = list(self.available[:min(3, max_slots)])

    def toggle(self, t):
        if t in self.selected:
            self.selected.remove(t)
        else:
            if len(self.selected) < self.max_slots:
                self.selected.append(t)

    def draw_chip(self, surf, rect, t, font, active):
        color = DICE_COLORS.get(t, (150,150,150))
        pygame.draw.rect(surf, color if active else DARK, rect, border_radius=12)
        border = 4 if active else 2
        pygame.draw.rect(surf, ACCENT, rect, width=border, border_radius=12)
        s = font.render(t.capitalize(), True, WHITE)
        surf.blit(s, (rect.centerx - s.get_width()//2, rect.centery - s.get_height()//2))
