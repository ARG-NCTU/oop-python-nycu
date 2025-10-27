# -*- coding: utf-8 -*-
class UpgradeState:
    """Session-lifetime upgrades and coins."""
    def __init__(self):
        self.coins = 0
        self.damage_mult = {}
        self.fire_rate_mult = {}
        self.cost_mult = {}

    def ensure_type(self, t):
        self.damage_mult.setdefault(t, 1.0)
        self.fire_rate_mult.setdefault(t, 1.0)  # period multiplier; lower = faster
        self.cost_mult.setdefault(t, 1.0)

    def add_coin(self, n=1):
        self.coins += n

    def spend(self, cost):
        if self.coins >= cost:
            self.coins -= cost
            return True
        return False

    def upgrade_damage(self, t, *, step=0.10, cost=2):
        self.ensure_type(t)
        if self.spend(cost):
            self.damage_mult[t] *= (1.0 + step)
            return True
        return False

    def upgrade_fire(self, t, *, step=0.08, cost=2):
        self.ensure_type(t)
        if self.spend(cost):
            self.fire_rate_mult[t] *= (1.0 - step)
            return True
        return False

    def upgrade_cost(self, t, *, step=0.10, cost=2):
        self.ensure_type(t)
        if self.spend(cost):
            self.cost_mult[t] *= (1.0 - step)
            return True
        return False
