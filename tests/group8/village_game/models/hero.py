import pygame
from models.villager import Villager

# 基礎英雄類別
class PlayerHero(Villager):
    def update_movement(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        # WASD 控制
        if keys[pygame.K_w]: dy = -1
        if keys[pygame.K_s]: dy = 1
        if keys[pygame.K_a]: dx = -1
        if keys[pygame.K_d]: dx = 1
        
        if dx != 0 or dy != 0:
            length = (dx*dx + dy*dy)**0.5
            dx, dy = dx/length, dy/length
            
            # 英雄速度
            current_speed = self.speed * 1.5
            self.pos.x += dx * current_speed
            self.pos.y += dy * current_speed
            
            # 限制在視窗內
            self.pos.x = max(10, min(self.pos.x, self.engine.map_width - 10))
            self.pos.y = max(10, min(self.pos.y, self.engine.map_height - 10))

    def draw(self, screen):
        img = self.engine.assets.get('hero')
        if img:
            # 主角光環
            pygame.draw.circle(screen, (255, 255, 255), (int(self.pos.x), int(self.pos.y)), 22, 1)
            rect = img.get_rect(center=(int(self.pos.x), int(self.pos.y)))
            screen.blit(img, rect)
            # 職業顏色
            pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y) - 25), 4)
        else:
            super().draw(screen)

# 1. 速度型
class SonicHero(PlayerHero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (50, 255, 50), "Hero")
        self.speed = 2.5
        
    def update(self):
        self.update_movement() # 玩家控制
        # 殘影
        if self.engine.frame_count % 10 == 0:
             pass

# 2. 治療型
class HealerHero(PlayerHero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (255, 100, 255), "Hero")
        self.speed = 1.0
        
    def update(self):
        self.update_movement()
        # 自動治療
        if self.engine.frame_count % 120 == 0:
            for v in self.engine.villagers:
                if v.is_alive and v != self and v.hunger > 50:
                    v.hunger -= 20
                    self.engine.add_floating_text(v.pos, "Heal!", (100, 255, 255))
                    break

# 3. 經濟型
class TycoonHero(PlayerHero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (255, 215, 0), "Hero")
        self.speed = 0.9
        
    def update(self):
        self.update_movement()
        # 產黃金
        if self.engine.frame_count % 180 == 0:
            self.engine.gold += 1
            self.engine.add_floating_text(self.pos, "+1 Gold", (255, 215, 0))

# 4. 防禦型
class BuilderHero(PlayerHero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (100, 100, 100), "Hero")
        self.speed = 0.8
        
    def update(self):
        self.update_movement()
        # 修牆
        if self.engine.frame_count % 60 == 0:
            if self.engine.wall_hp < 500:
                self.engine.wall_hp += 2

# 5. 糧食型
class OracleHero(PlayerHero):
    def __init__(self, engine, name):
        super().__init__(engine, name, (255, 140, 0), "Hero")
        self.speed = 1.0
        
    def update(self):
        self.update_movement()
        # 抗餓被動 (在 engine 結算時生效)