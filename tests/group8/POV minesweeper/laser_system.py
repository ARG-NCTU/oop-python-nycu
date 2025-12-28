from ursina import *
import random
import math

# === 方向指示箭頭 ===
class DirectionArrow(Entity):
    def __init__(self, target_pos, player):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture='arrow_right', 
            color=color.red,
            scale=0.2, 
            position=(0, 0)
        )
        self.target_pos = target_pos
        self.player = player
        self.animate_color(color.yellow, duration=0.2, loop=True)

    def update(self):
        if not self.player or not self.player.enabled:
            destroy(self)
            return

        dir_vec = self.target_pos - self.player.position
        theta = math.radians(-self.player.rotation_y)
        local_x = dir_vec.x * math.cos(theta) - dir_vec.z * math.sin(theta)
        local_z = dir_vec.x * math.sin(theta) + dir_vec.z * math.cos(theta)
        angle = math.degrees(math.atan2(local_x, local_z))
        
        self.rotation_z = -angle
        
        rad = math.radians(angle)
        offset_dist = 0.45 
        self.x = math.sin(rad) * offset_dist
        self.y = math.cos(rad) * offset_dist * 1.5

# === 雷射預警物件 ===
class LaserWarning(Entity):
    def __init__(self, target_player, start_pos, game_manager_ref):
        super().__init__()
        self.start_pos = start_pos
        self.target_pos = target_player.position + Vec3(0, 1.5, 0)
        self.player = target_player
        self.gm = game_manager_ref
        
        self.source_bulb = Entity(model='sphere', color=color.red, scale=3, position=start_pos, double_sided=True)
        self.source_bulb.animate_color(color.yellow, duration=0.2, loop=True)
        
        dist = distance(start_pos, self.target_pos)
        self.beam_line = Entity(
            model='cube',
            color=color.rgba(255, 0, 0, 80),
            scale=(0.2, 0.2, dist),
            position=lerp(start_pos, self.target_pos, 0.5),
            double_sided=True
        )
        self.beam_line.look_at(self.target_pos)
        
        self.arrow = DirectionArrow(start_pos, target_player)
        
        invoke(self.fire_laser, delay=2.5)

    def fire_laser(self):
        destroy(self.source_bulb)
        destroy(self.beam_line)
        destroy(self.arrow)
        Laser(self.target_pos, self.start_pos, self.gm, self.player)
        destroy(self)

# === 實體雷射 ===
class Laser(Entity):
    def __init__(self, target_pos, start_pos, game_manager_ref, player_ref):
        super().__init__(
            model='cube',
            color=color.magenta,
            scale=(0.4, 0.4, 8),
            position=start_pos,
            double_sided=True
        )
        self.player_ref = player_ref
        self.gm_ref = game_manager_ref
        self.look_at(target_pos)
        self.speed = 40
        destroy(self, delay=5) 

    def update(self):
        self.position += self.forward * time.dt * self.speed
        if self.player_ref and distance(self.position, self.player_ref.position + Vec3(0,1,0)) < 2.0:
            # === 修改：不再直接結束遊戲，而是造成傷害 ===
            # 傳入傷害值 1，以及死亡原因 (如果這一下致死的話)
            self.gm_ref.take_damage(1, "ELIMINATED BY LASER")
            destroy(self)

# === 雷射系統管理器 ===
class LaserManager:
    def __init__(self, game_manager):
        self.gm = game_manager
        self.timer = 0
        self.interval = 5.0 
        self.active = False

    def reset(self):
        self.timer = 5.0
        self.interval = 5.0
        self.active = True

    def stop(self):
        self.active = False

    def update(self, dt):
        if not self.active or not self.gm.player or not self.gm.player.enabled:
            return

        self.timer -= dt
        if self.timer <= 0:
            self.spawn_laser()
            self.interval = max(2.5, self.interval * 0.99) 
            self.timer = self.interval

    def spawn_laser(self):
        angle = random.uniform(0, 360)
        distance = random.uniform(80, 100) 
        height = random.uniform(5, 25)
        
        spawn_pos = self.gm.player.position + Vec3(
            math.cos(math.radians(angle)) * distance,
            height,
            math.sin(math.radians(angle)) * distance
        )
        
        LaserWarning(self.gm.player, spawn_pos, self.gm)