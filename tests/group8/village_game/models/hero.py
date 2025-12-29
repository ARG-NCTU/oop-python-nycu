import pygame
import config
from models.villager import Villager
import random

# --- 粒子系統類別 ---
class Particle:
    def __init__(self, x, y, color, life):
        self.x = x
        self.y = y
        self.color = color
        self.life = life
        self.max_life = life
        self.size = random.randint(2, 5)
        # 隨機飄動方向
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        self.size = max(0, self.size - 0.1)

    def draw(self, screen):
        if self.life > 0:
            alpha = int((self.life / self.max_life) * 255)
            s = pygame.Surface((int(self.size)*2, int(self.size)*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*self.color, alpha), (int(self.size), int(self.size)), int(self.size))
            screen.blit(s, (self.x - self.size, self.y - self.size))

class Hero(Villager):
    def __init__(self, engine, name, color, role="Hero"):
        super().__init__(engine, name, color, role)
        self.inventory = {"Food": 0, "Wood": 0, "Gold": 0}
        self.speed = 2.5
        self.particles = []  # 特效粒子列表

    def update(self):
        if not self.is_alive: return

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_w] or keys[pygame.K_UP]: dy = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: dy = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: dx = 1
        
        move_vec = pygame.math.Vector2(dx, dy)
        if move_vec.length() > 0:
            move_vec = move_vec.normalize()
            # 產生特效粒子
            self.spawn_effect_particles()
        
        self.dir = move_vec
        
        # 移動速度計算 (含Buff)
        current_speed = self.speed
        if hasattr(self.engine, 'active_buffs') and 'speed' in self.engine.active_buffs:
            current_speed *= self.engine.active_buffs['speed']['value']
            
        self.pos += self.dir * current_speed
        
        # 邊界限制
        self.pos.x = max(20, min(self.engine.map_width - 20, self.pos.x))
        self.pos.y = max(20, min(self.engine.map_height - 20, self.pos.y))
        
        # 飢餓更新
        if self.engine.frame_count % 60 == 0:
            self.hunger += config.HUNGER_RATE * 0.8
            
        # 更新粒子
        for p in self.particles: p.update()
        self.particles = [p for p in self.particles if p.life > 0]

    def spawn_effect_particles(self):
        """根據裝備的特效產生粒子"""
        effect = self.engine.shop_items_owned.get('hero_effect', 'none')
        
        if effect == 'none': return
        
        # 根據特效類型決定顏色
        color = (255, 255, 255)
        if effect == 'fire':
            color = random.choice([(255, 50, 0), (255, 150, 0), (255, 255, 0)]) # 紅橙黃
        elif effect == 'lightning':
            color = random.choice([(100, 200, 255), (200, 255, 255), (255, 255, 100)]) # 藍白黃
        elif effect == 'rainbow':
            hue = (pygame.time.get_ticks() // 2) % 360
            c = pygame.Color(0)
            c.hsla = (hue, 100, 50, 100)
            color = (c.r, c.g, c.b)
        
        # 隨機產生 1-2 顆粒子在腳下
        if random.random() < 0.5:
            self.particles.append(Particle(self.pos.x, self.pos.y + 10, color, 20))

    def draw(self, screen):
        # 先畫粒子 (在人物下面)
        for p in self.particles: p.draw(screen)
        
        # 再畫人物 (呼叫父類別的 draw，這樣也會吃到皮膚效果)
        super().draw(screen)
        
        # 畫個箭頭標示這是主角
        pygame.draw.polygon(screen, (255, 255, 0), 
                          [(self.pos.x, self.pos.y - 30), 
                           (self.pos.x - 5, self.pos.y - 40), 
                           (self.pos.x + 5, self.pos.y - 40)])

# --- 各種英雄子類別 ---

class SonicHero(Hero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (100, 100, 255))
        self.speed = 4.0 # 基礎速度快

class TycoonHero(Hero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (255, 215, 0))
        self.passive_timer = 0
    def update(self):
        super().update()
        self.passive_timer += 1
        if self.passive_timer > 300: # 每5秒產錢
            self.engine.gold += 1
            self.passive_timer = 0

class HealerHero(Hero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (255, 100, 255))
        self.heal_timer = 0
    def update(self):
        super().update()
        self.heal_timer += 1
        if self.heal_timer > 600: # 每10秒治療
            for v in self.engine.villagers:
                if v.is_alive: v.hunger = max(0, v.hunger - 10)
            self.heal_timer = 0
            # 記錄治療次數 (用於成就)
            if not hasattr(self.engine, 'heal_count'): self.engine.heal_count = 0
            self.engine.heal_count += 1

class BuilderHero(Hero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (150, 150, 150))
        self.build_timer = 0
    def update(self):
        super().update()
        self.build_timer += 1
        if self.build_timer > 300: # 每5秒修牆
            if self.engine.wall_hp < 1000:
                self.engine.wall_hp += 10
                # 記錄修復量
                if not hasattr(self.engine, 'builder_repairs'): self.engine.builder_repairs = 0
                self.engine.builder_repairs += 10
            self.build_timer = 0

class OracleHero(Hero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (255, 140, 0))
        # 被動：減少全體飢餓速度 (已在 Villager.update 實現，或在此處實現)
        # 這裡簡單處理：Oracle 存在時，減少食物消耗 (在 Engine 判定)