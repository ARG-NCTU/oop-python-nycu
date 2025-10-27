# -*- coding: utf-8 -*-
class SlowEffect:
    def __init__(self, ratio, duration):
        self.ratio = ratio
        self.duration = duration
        self.t = 0.0

    def update(self, dt):
        self.t += dt

    @property
    def expired(self):
        return self.t >= self.duration


class TelegraphZone:
    """Circular zone that debuffs enemies and dice within (warning -> effect)."""
    def __init__(self, x, y, radius_px, warn_time, effect_time, enemy_speed_mult=0.6, dice_period_mult=1.2):
        self.x = x
        self.y = y
        self.r = radius_px
        self.warn_time = warn_time
        self.effect_time = effect_time
        self.enemy_speed_mult = enemy_speed_mult
        self.dice_period_mult = dice_period_mult
        self.t = 0.0  # time since created

    def update(self, dt):
        self.t += dt

    def active(self):
        return self.t < (self.warn_time + self.effect_time)

    def in_effect_phase(self):
        return self.t >= self.warn_time and self.t < (self.warn_time + self.effect_time)

    def contains(self, px, py):
        dx, dy = px - self.x, py - self.y
        return (dx*dx + dy*dy) <= (self.r*self.r)
