# -*- coding: utf-8 -*-
import pygame
from colors import WHITE, DARK, DARKER, GRAY, ACCENT, SLATE

class Button:
    """Basic button with hover and on-click callback."""
    def __init__(self, rect, text, font, on_click, *, bg=DARK, fg=WHITE, hover=None, radius=12, icon=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.on_click = on_click
        self.bg = bg
        self.fg = fg
        self.hover = hover or ACCENT
        self.radius = radius
        self.icon = icon
        self._hovering = False

    def handle(self, event):
        if event.type == pygame.MOUSEMOTION:
            self._hovering = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.on_click()

    def draw(self, surf):
        color = self.hover if self._hovering else self.bg
        pygame.draw.rect(surf, color, self.rect, border_radius=self.radius)
        if self.icon:
            ir = self.icon.get_rect(center=self.rect.center)
            surf.blit(self.icon, ir)
        if self.text:
            txt = self.font.render(self.text, True, self.fg)
            surf.blit(txt, (self.rect.centerx - txt.get_width() // 2,
                            self.rect.centery - txt.get_height() // 2))


class Segmented:
    """Segmented control (used for game speed)."""
    def __init__(self, rect, labels, font, index, on_change):
        self.rect = pygame.Rect(rect)
        self.labels = labels
        self.font = font
        self.index = index
        self.on_change = on_change

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                w = self.rect.w // len(self.labels)
                off = (event.pos[0] - self.rect.x) // w
                self.index = int(max(0, min(len(self.labels) - 1, off)))
                self.on_change(self.index)

    def draw(self, surf):
        n = len(self.labels)
        w = self.rect.w // n
        for i, lab in enumerate(self.labels):
            r = pygame.Rect(self.rect.x + i * w, self.rect.y, w - (0 if i == n - 1 else 1), self.rect.h)
            active = (i == self.index)
            pygame.draw.rect(surf, ACCENT if active else DARK, r, border_radius=10)
            t = self.font.render(lab, True, WHITE if active else SLATE)
            surf.blit(t, (r.centerx - t.get_width() // 2, r.centery - t.get_height() // 2))


def draw_panel(surf, rect, title, title_font, body_fn=None):
    import pygame
    from colors import WHITE, DARKER, PANEL_GRAD_TOP, PANEL_GRAD_BOTTOM

    # gradient background
    panel = pygame.Surface((rect.w, rect.h))
    for y in range(rect.h):
        t = y / max(1, rect.h - 1)
        r = int(PANEL_GRAD_TOP[0] * (1 - t) + PANEL_GRAD_BOTTOM[0] * t)
        g = int(PANEL_GRAD_TOP[1] * (1 - t) + PANEL_GRAD_BOTTOM[1] * t)
        b = int(PANEL_GRAD_TOP[2] * (1 - t) + PANEL_GRAD_BOTTOM[2] * t)
        pygame.draw.line(panel, (r, g, b), (0, y), (rect.w, y))
    panel = panel.convert()
    surf.blit(panel, rect.topleft)

    # frame
    pygame.draw.rect(surf, DARKER, rect, width=6, border_radius=18)
    pygame.draw.rect(surf, (255,255,255), rect, width=2, border_radius=18)

    if title:
        title_surf = title_font.render(title, True, WHITE)
        surf.blit(title_surf, (rect.x + 20, rect.y + 14))
    if body_fn:
        body_fn()
