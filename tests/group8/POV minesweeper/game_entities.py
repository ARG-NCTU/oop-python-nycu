from ursina import *
import random
from game_config import NUMBER_COLORS, FONT_MAIN

# === 道具物件 ===
class PowerUp(Entity):
    def __init__(self, pos, type_name):
        super().__init__(
            position=pos + Vec3(0, 1, 0),
            collider='box',
            scale=0.6
        )
        self.type_name = type_name
        
        if type_name == 'heal':
            self.model = 'sphere'
            self.color = color.red
            self.texture = 'white_cube'
            # === 修改：文字放大到 25 ===
            self.label = Text(parent=self, text='+HP', y=2.5, scale=25, 
                              color=color.red, billboard=True, font=FONT_MAIN)
            
        elif type_name == 'shield':
            self.model = 'diamond'
            self.color = color.cyan
            self.texture = 'white_cube'
            # === 修改：文字放大到 25 ===
            self.label = Text(parent=self, text='SHIELD', y=2.5, scale=25, 
                              color=color.cyan, billboard=True, font=FONT_MAIN)

        self.animate_y(self.y + 0.5, duration=1.5, loop=True, curve=curve.in_out_sine)
        self.animate_rotation_y(360, duration=3, loop=True)

    def update(self):
        self.rotation_y += 100 * time.dt

# === 旗子物件 ===
class FlagObj(Entity):
    def __init__(self, parent_block):
        super().__init__(parent=parent_block, position=(0, 0.5, 0))
        self.pole = Entity(parent=self, model='cube', color=color.brown, 
                           scale=(0.1, 1.2, 0.1), position=(0, 0.6, 0))
        self.cloth = Entity(parent=self, model='cube', color=color.red, 
                            scale=(0.6, 0.4, 0.05), position=(0.3, 1.0, 0), rotation_y=15)
        self.cloth.animate_rotation_y(25, duration=1, loop=True, curve=curve.in_out_sine)

# === 地雷方塊物件 ===
class MineTile(Entity): 
    def __init__(self, x, z, on_click_callback, on_flag_callback):
        super().__init__(
            parent=scene,
            position=(x, 0, z),
            model='cube',
            texture='white_cube',
            color=color.azure,
            collider='box'
        )
        self.grid_x = x
        self.grid_z = z
        self.is_bomb = False
        self.is_revealed = False
        self.is_flagged = False
        self.number = 0
        self.flag_entity = None
        self.on_click_callback = on_click_callback
        self.on_flag_callback = on_flag_callback

    def update(self):
        if not self.is_revealed:
            self.color = color.lime if self.hovered else color.azure

    def on_click(self):
        if not self.is_flagged: self.on_click_callback(self)

    def input(self, key):
        if self.hovered and key == 'right mouse down':
            self.toggle_flag()
            self.on_flag_callback()

    def toggle_flag(self):
        if self.is_revealed: return
        self.is_flagged = not self.is_flagged
        if self.is_flagged:
            self.flag_entity = FlagObj(parent_block=self)
        else:
            if self.flag_entity: destroy(self.flag_entity)

    def reveal_visuals(self):
        if self.is_revealed: return
        self.is_revealed = True
        self.color = color.light_gray
        
        self.animate_scale((1.1, 0.9, 1.1), duration=0.1, curve=curve.out_quad)
        invoke(self.animate_scale, (1, 1, 1), delay=0.1)

        if self.is_bomb:
            self.color = color.rgb(200, 50, 50)
            Entity(parent=self, model='sphere', color=color.black, scale=0.8, position=(0, 0.5, 0))
            for _ in range(20):
                e = Entity(model='cube', color=color.orange, scale=0.2, position=self.position+(0,1,0), add_to_scene_entities=True)
                e.animate_position(e.position + Vec3(random.uniform(-4,4), random.uniform(2,5), random.uniform(-4,4)), duration=0.8)
                destroy(e, delay=0.8)
        else:
            if self.number > 0:
                c = NUMBER_COLORS.get(self.number, color.black)
                t = Text(text=str(self.number), parent=self, position=(0, 0.51, 0), 
                         scale=25, color=c, billboard=True, font=FONT_MAIN,
                         origin=(0, -0.5)) 
                t.animate_scale(30, duration=0.15, curve=curve.out_bounce)
                t.animate_scale(25, duration=0.15, delay=0.15)
                
            for _ in range(4):
                e = Entity(model='cube', color=color.gray, scale=0.15, position=self.position+(0,0.5,0), add_to_scene_entities=True)
                e.animate_position(e.position + Vec3(random.uniform(-1,1), random.uniform(0.5,1.5), random.uniform(-1,1)), duration=0.4)
                destroy(e, delay=0.4)