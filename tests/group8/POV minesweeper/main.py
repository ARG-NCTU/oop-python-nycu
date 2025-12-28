from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
import random

from game_config import DIFFICULTY_SETTINGS, FONT_MAIN
from map_manager import MapManager
from laser_system import LaserManager 
from game_entities import PowerUp 
from ui_manager import UIManager 

app = Ursina()
window.fps_counter.enabled = False
window.title = "Minesweeper 3D: Stable Physics"

class GameManager(Entity):
    def __init__(self):
        super().__init__()
        self.state = 'MENU' 
        self.start_time = 0
        
        self.survival_mode = False 
        self.hardcore_mode = False 
        
        self.max_hp = 3
        self.current_hp = 3
        self.last_damage_time = 0
        self.has_shield = False
        
        self.item_timer = 0
        self.items_on_map = []
        self.best_time = 0
        
        self.ui = UIManager(self)
        self.map_manager = MapManager(self)
        self.laser_manager = LaserManager(self)
        
        self.player = None
        self.editor_cam = EditorCamera(enabled=False, ignore_paused=True)
        self.camera_mode = 'FPP'
        
        self.setup_environment()

    def setup_environment(self):
        Sky(color=color.rgb(135, 206, 235)) 
        scene.fog_density = 0 
        PointLight(parent=camera, position=(10, 20, 10), color=color.white)
        AmbientLight(color=color.rgba(120, 120, 120, 0.1))
        
        # === 關鍵修復：地板改成 Cube (厚度1) ===
        # 原本是 plane (厚度0)，跑太快會穿透導致無法跳躍
        # 現在改成厚實的 cube，物理判定會非常穩
        self.ground = Entity(
            model='cube', 
            scale=(500, 1, 500), 
            color=color.black, 
            texture='white_cube', 
            texture_scale=(200, 200), 
            collider='box', 
            position=(0, -0.5, 0) # 頂面剛好在 y=0
        )

    def start_game(self, difficulty_key):
        self.state = 'PLAYING'
        self.start_time = time.time()
        
        self.current_hp = self.max_hp
        self.has_shield = False
        self.item_timer = 10.0 
        for item in self.items_on_map: destroy(item)
        self.items_on_map = []
        
        # 重置 UI
        self.ui.reset_ui_state() # 強制重置紅屏
        self.ui.show_hud(show_hp=self.survival_mode)
        self.ui.update_hp(self.current_hp, self.max_hp)
        
        if self.survival_mode:
            self.laser_manager.reset()
            self.base_fov = 100 
        else:
            self.laser_manager.stop()
            self.base_fov = 90
        
        camera.fov = self.base_fov
        
        self.map_manager.start_new_map(difficulty_key)
        
        if self.player:
            destroy(self.player)
            self.player = None
        
        self.setup_player(self.map_manager.grid_size)

    def setup_player(self, grid_size):
        # 地板修好後，重力可以用回標準的 1.0，跳躍感會比較自然
        self.player = FirstPersonController(gravity=1.0, jump_height=2, speed=10)
        
        self.player.enabled = True
        self.player.position = (grid_size/2, 8, grid_size/2) 
        self.player.rotation = (0, 0, 0)
        mouse.locked = True
        self.camera_mode = 'FPP'
        self.editor_cam.enabled = False

    def take_damage(self, amount, reason="DIED"):
        if time.time() - self.last_damage_time < 1.0: return
            
        if self.has_shield:
            self.has_shield = False
            self.ui.show_shield_broken()
            camera.shake(duration=0.2, magnitude=1) 
            self.last_damage_time = time.time() 
            return

        self.current_hp -= amount
        self.last_damage_time = time.time()
        camera.shake(duration=0.3, magnitude=2)
        
        self.ui.update_hp(self.current_hp, self.max_hp)
        
        if self.current_hp <= 0:
            self.trigger_game_over(win=False, reason=reason)

    def spawn_powerup(self):
        grid_size = self.map_manager.grid_size
        x = random.randint(0, grid_size-1)
        z = random.randint(0, grid_size-1)
        type_name = 'heal' if random.random() > 0.3 else 'shield'
        item = PowerUp(Vec3(x, 0, z), type_name)
        self.items_on_map.append(item)

    def toggle_pause(self):
        if self.state == 'PLAYING':
            self.state = 'PAUSED'
            self.ui.pause_entity.enabled = True
            mouse.locked = False
            self.player.enabled = False
        elif self.state == 'PAUSED':
            self.state = 'PLAYING'
            self.ui.pause_entity.enabled = False
            mouse.locked = True
            self.player.enabled = True

    def trigger_game_over(self, win, reason=""):
        self.state = 'GAMEOVER'
        self.laser_manager.stop()
        camera.shake(duration=0.5, magnitude=3)
        
        for item in self.items_on_map: destroy(item)
        self.items_on_map = []
        
        current_time = int(time.time() - self.start_time)
        if self.survival_mode and current_time > self.best_time:
            self.best_time = current_time
        
        self.ui.show_game_over(win, reason, str(current_time))
        
        mouse.locked = False
        self.player.enabled = False
        self.editor_cam.enabled = False

    def return_to_menu(self):
        self.state = 'MENU'
        self.laser_manager.stop()
        self.ui.show_menu()
        self.ui.best_score_text.text = f'BEST SURVIVAL: {self.best_time}s'
        camera.fov = 90
        self.map_manager.clear_map()

    def input(self, key):
        if key == 'escape':
            if self.state in ['PLAYING', 'PAUSED']:
                self.toggle_pause()
        if key == 'v' and self.state == 'PLAYING':
            self.switch_camera_mode()

    def update(self):
        if self.state == 'PLAYING':
            elapsed = int(time.time() - self.start_time)
            self.ui.timer_text.text = f'TIME: {elapsed}'
            
            if self.player and self.player.y < -10:
                 self.player.position = (self.map_manager.grid_size/2, 20, self.map_manager.grid_size/2)
                 self.player.velocity = (0,0,0)

            if self.player and self.player.enabled:
                if held_keys['shift']:
                    self.player.speed = 16 # 衝刺速度
                    camera.fov = lerp(camera.fov, self.base_fov + 10, 4 * time.dt)
                else:
                    self.player.speed = 10 
                    camera.fov = lerp(camera.fov, self.base_fov, 4 * time.dt)
                
                # 吃道具
                for item in self.items_on_map[:]:
                    if distance(self.player.position, item.position) < 2.0:
                        if item.type_name == 'heal':
                            if self.current_hp < self.max_hp:
                                self.current_hp += 1
                                self.ui.update_hp(self.current_hp, self.max_hp)
                        elif item.type_name == 'shield':
                            self.has_shield = True
                            self.ui.shield_text.enabled = True
                        
                        self.items_on_map.remove(item)
                        destroy(item)

            if self.survival_mode:
                self.item_timer -= time.dt
                if self.item_timer <= 0:
                    self.spawn_powerup()
                    self.item_timer = random.uniform(10, 20)

            self.laser_manager.update(time.dt)
            
            if self.hardcore_mode and self.player:
                px = round(self.player.x)
                pz = round(self.player.z)
                if (px, pz) in self.map_manager.tiles:
                    tile = self.map_manager.tiles[(px, pz)]
                    if tile.is_bomb and not tile.is_revealed:
                        tile.reveal_visuals()
                        self.trigger_game_over(win=False, reason="STEPPED ON A MINE!")

    def switch_camera_mode(self):
        grid_size = self.map_manager.grid_size
        if self.camera_mode == 'FPP':
            self.camera_mode = 'TPP'
            self.player.enabled = False
            self.editor_cam.enabled = True
            self.editor_cam.position = (grid_size/2, grid_size * 1.5, grid_size/2)
            self.editor_cam.rotation = (90, 0, 0)
            mouse.locked = False
            self.ui.mode_text.text = '[V] View: Tactical (RMB move)'
        else:
            self.camera_mode = 'FPP'
            self.editor_cam.enabled = False
            self.player.enabled = True
            mouse.locked = True
            self.ui.mode_text.text = '[V] View: First Person'

game = GameManager()
app.run()
