# -*- coding: utf-8 -*-
import math
import pygame
from colors import YELLOW, ORANGE, CYAN
from settings import BULLET_SPEED, CHAIN_MAX_DISTANCE

class Bullet:
    """Basic single-target projectile."""
    def __init__(self, game, x, y, target, dmg, *, speed_mult_provider=lambda:1.0):
        self.game = game
        self.x = x
        self.y = y
        self.target = target
        self.dmg = dmg
        self.base_speed = BULLET_SPEED
        self.speed_mult_provider = speed_mult_provider

    def update(self, dt):
        if not self.target or self.target.dead:
            return True

        speed = self.base_speed * self.speed_mult_provider()
        tx, ty = self.target.x, self.target.y
        dx, dy = tx - self.x, ty - self.y
        dist = math.hypot(dx, dy)
        if dist <= 0.0001:
            self.target.hit(self.dmg)
            return True

        # step reach/overrun check to avoid afterimage at high speed
        step = speed * dt
        if step >= dist:
            self.x, self.y = tx, ty
            self.target.hit(self.dmg)
            return True

        nx, ny = dx / dist, dy / dist
        self.x += nx * step
        self.y += ny * step
        return False
        
    def draw(self, surf):
        pygame.draw.circle(surf, YELLOW, (int(self.x), int(self.y)), 6)


class ChainBolt(Bullet):
    """Chains to nearby enemies (for Multi dice)."""
    def __init__(self, game, x, y, first_target, dmg, remaining_jumps, enemies, *, speed_mult_provider=lambda:1.0):
        super().__init__(game, x, y, first_target, dmg, speed_mult_provider=speed_mult_provider)
        self.remaining = remaining_jumps
        self.enemies = enemies
        self.visited = {first_target}

    def update(self, dt):
        done = super().update(dt)
        if done and self.remaining > 0:
            pivot = self.target
            if pivot and not pivot.dead:
                candidates = [e for e in self.enemies if (not e.dead) and e is not pivot and e not in self.visited]
                best = None
                bestd2 = 1e9
                for e in candidates:
                    d2 = (e.x - pivot.x) ** 2 + (e.y - pivot.y) ** 2
                    if d2 < bestd2 and d2 <= CHAIN_MAX_DISTANCE ** 2:
                        bestd2 = d2
                        best = e
                if best:
                    self.target = best
                    self.visited.add(best)
                    self.remaining -= 1
                    return False
        return done

    def draw(self, surf):
        pygame.draw.circle(surf, ORANGE, (int(self.x), int(self.y)), 6)
        pygame.draw.circle(surf, CYAN, (int(self.x), int(self.y)), 3)
