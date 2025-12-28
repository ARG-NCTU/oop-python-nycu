import pygame
import random
import config

class Villager:
    def __init__(self, engine, name, color, role):
        self.engine = engine
        self.name = name
        self.color = color
        self.role = role 
        
        self.pos = pygame.math.Vector2(
            random.randint(50, engine.map_width-50),
            random.randint(50, engine.map_height-50)
        )
        self.dir = pygame.math.Vector2(random.choice([-1, 1]), random.choice([-1, 1])).normalize()
        
        self.speed = 1.0 if role == "Hero" else 0.9
        self.hunger = 0
        self.is_alive = True
        self.change_dir_timer = 0

        # 用來避免重疊的隨機偏移量，每個人有自己的一個「舒適區」
        self.personal_space_offset = pygame.math.Vector2(random.randint(-30, 30), random.randint(-30, 30))

    def get_nearest_resource(self, target_types):
        target = None
        min_dist = 9999
        for r in self.engine.resources:
            if r.active and r.type in target_types:
                dist = self.pos.distance_to(r.pos)
                if dist < min_dist:
                    min_dist = dist
                    target = r
        return target

    def apply_separation(self):
        """[AI 新增] 分離力：避免村民全部疊在一起"""
        separation_force = pygame.math.Vector2(0, 0)
        count = 0
        
        # 檢查附近的每個村民
        for other in self.engine.villagers:
            if other is not self and other.is_alive:
                dist = self.pos.distance_to(other.pos)
                # 如果距離太近 (小於 25 像素)
                if dist < 25: 
                    # 計算推開的向量 (從對方指向自己)
                    diff = self.pos - other.pos
                    if diff.length() > 0:
                        diff = diff.normalize()
                        # 距離越近，推力越大
                        separation_force += diff / (dist + 0.1)
                        count += 1
        
        if count > 0:
            # 施加排斥力，稍微調整強度
            if separation_force.length() > 0:
                self.pos += separation_force.normalize() * 1.5

    def update(self):
        if not self.is_alive: return

        # 1. 英雄由玩家控制 (略過 AI)
        if self.role == "Hero":
            pass 
        else:
            # --- [修正] 增加飢餓度邏輯 ---
            # 讓飢餓度隨著時間上升，觸發後續的找食物行為
            self.hunger += config.HUNGER_RATE 

            # --- 日夜作息系統 ---
            is_night = (self.engine.frame_count / config.DAY_LENGTH) > 0.7
            
            # [狀態 A] 肚子極餓：無視時間，找吃的
            if self.hunger > 60:
                food = self.get_nearest_resource(["Food"])
                if food:
                    self.move_towards(food.pos, 1.3)
                else:
                    self.wander()

            # [狀態 B] 晚上：回營火 (加入隨機偏移，避免全部擠在正中心)
            elif is_night:
                center = pygame.math.Vector2(self.engine.map_width // 2, self.engine.map_height // 2)
                # 目標是營火周圍，而不是營火正中心
                target = center + self.personal_space_offset
                
                dist = self.pos.distance_to(target)
                
                if dist > 10: 
                    self.move_towards(target, 1.1)
                else:
                    # 到了就發呆
                    self.wander()
                    # 在營火旁休息可以緩慢恢復飢餓
                    if self.engine.frame_count % 60 == 0:
                        self.hunger = max(0, self.hunger - 0.5)

            # [狀態 C] 白天：工作
            else:
                res = self.get_nearest_resource(["Wood", "Gold", "Food"])
                if res:
                    self.move_towards(res.pos, 1.0)
                else:
                    self.wander()
            
            # [關鍵] 每一幀都執行分離檢測，防止重疊
            self.apply_separation()

        # 邊界限制
        self.pos.x = max(10, min(self.pos.x, self.engine.map_width - 10))
        self.pos.y = max(10, min(self.pos.y, self.engine.map_height - 10))

        # 資源採集檢測
        pickup_range = 30 if self.role == "Hero" else 15
        
        for r in self.engine.resources:
            if r.active and self.pos.distance_to(r.pos) < pickup_range:
                # 如果村民餓了且遇到食物 -> 吃掉 (不進庫存)
                if self.role != "Hero" and r.type == "Food" and self.hunger > 60:
                    r.active = False
                    self.hunger = 0
                    self.engine.add_floating_text(self.pos, "Yummy!", (100, 255, 100))
                else:
                    # 否則收集資源 (進庫存)
                    r.active = False
                    if r.type == "Food": 
                        self.engine.food += 5
                        self.engine.add_floating_text(self.pos, "+5 Food", config.COLOR_FOOD)
                    elif r.type == "Wood": 
                        self.engine.wood += 5
                        self.engine.add_floating_text(self.pos, "+5 Wood", config.COLOR_WOOD)
                    elif r.type == "Gold": 
                        self.engine.gold += 5
                        self.engine.add_floating_text(self.pos, "+5 Gold", config.COLOR_GOLD)

    def move_towards(self, target_pos, speed_mult):
        direction = (target_pos - self.pos)
        if direction.length() > 0:
            self.dir = direction.normalize()
            self.pos += self.dir * (self.speed * speed_mult)

    def wander(self):
        self.pos += self.dir * (self.speed * 0.5) # 發呆時走慢點
        self.change_dir_timer += 1
        
        if self.pos.x <= 10 or self.pos.x >= self.engine.map_width - 10: self.dir.x *= -1
        if self.pos.y <= 10 or self.pos.y >= self.engine.map_height - 10: self.dir.y *= -1

        if self.change_dir_timer > 60: 
            self.dir = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()
            self.change_dir_timer = 0

    def draw(self, screen):
        if not self.is_alive: return
        
        img = None
        if self.role == "Hero": img = self.engine.assets.get('hero')
        else: img = self.engine.assets.get('villager')
            
        if img:
            rect = img.get_rect(center=(int(self.pos.x), int(self.pos.y)))
            screen.blit(img, rect)
            if self.hunger > 60:
                pygame.draw.circle(screen, (255, 50, 50), (int(self.pos.x) + 10, int(self.pos.y) - 15), 4)
        else:
            pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), 10)