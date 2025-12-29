from ursina import *
from game_config import DIFFICULTY_SETTINGS, FONT_MAIN

class UIManager(Entity):
    def __init__(self, game_manager):
        super().__init__()
        self.gm = game_manager 
        
        # 初始時 alpha 設為 0，避免一開始就擋住畫面
        self.low_hp_overlay = Entity(parent=camera.ui, model='quad', scale=(2, 1), color=color.red, alpha=0)

        self.timer_text = Text(text='TIME: 0', position=(-0.85, 0.45), scale=2, font=FONT_MAIN, enabled=False)
        self.mode_text = Text(text='[V] View: FPP', position=(0.55, 0.45), scale=1.2, font=FONT_MAIN, enabled=False)
        self.warning_text = Text(text='SURVIVAL MODE ACTIVE', position=(0, 0.4), origin=(0,0), scale=1.5, color=color.red, enabled=False, font=FONT_MAIN)
        self.hardcore_text = Text(text='HARDCORE: INSTANT DEATH', position=(0, 0.35), origin=(0,0), scale=1.2, color=color.magenta, enabled=False, font=FONT_MAIN)
        self.hp_text = Text(text='HP: 3/3', position=(-0.85, 0.35), scale=2, color=color.green, font=FONT_MAIN, enabled=False)
        self.sprint_text = Text(text='[SHIFT] SPRINT', position=(-0.85, -0.45), scale=1.2, color=color.yellow, font=FONT_MAIN, enabled=False)
        self.shield_text = Text(text='SHIELD ACTIVE', position=(0, -0.3), origin=(0,0), scale=2, color=color.cyan, enabled=False, font=FONT_MAIN)

        # 主選單
        self.menu_entity = Entity(parent=camera.ui, enabled=True)
        Entity(parent=self.menu_entity, model='quad', scale=(2, 1), color=color.rgba(30, 30, 40, 240))
        Text(parent=self.menu_entity, text='MINESWEEPER 3D', scale=5, y=0.35, origin=(0,0), font=FONT_MAIN)
        self.best_score_text = Text(parent=self.menu_entity, text=f'BEST SURVIVAL: 0s', scale=2, y=0.25, origin=(0,0), color=color.gold, font=FONT_MAIN)
        
        self.mode_btn = Button(parent=self.menu_entity, text='SURVIVAL: OFF', scale=(0.35, 0.08), x=-0.2, y=0.15, color=color.green)
        self.mode_btn.text_entity.font = FONT_MAIN
        self.mode_btn.on_click = self.toggle_survival_ui

        self.hardcore_btn = Button(parent=self.menu_entity, text='HARDCORE: OFF', scale=(0.35, 0.08), x=0.2, y=0.15, color=color.gray)
        self.hardcore_btn.text_entity.font = FONT_MAIN
        self.hardcore_btn.on_click = self.toggle_hardcore_ui
        
        y_pos = 0.0
        for diff_key, settings in DIFFICULTY_SETTINGS.items():
            btn = Button(parent=self.menu_entity, text=settings['label'], scale=(0.4, 0.08), y=y_pos, color=color.azure)
            from functools import partial
            btn.on_click = partial(self.gm.start_game, diff_key)
            y_pos -= 0.12

        self.pause_entity = Entity(parent=camera.ui, enabled=False)
        Entity(parent=self.pause_entity, model='quad', scale=(2, 1), color=color.rgba(0, 0, 0, 200))
        Text(parent=self.pause_entity, text='PAUSED', scale=4, y=0.2, origin=(0,0), font=FONT_MAIN)
        Button(parent=self.pause_entity, text='RESUME', scale=(0.3, 0.08), y=0.05, color=color.lime, on_click=self.gm.toggle_pause)
        Button(parent=self.pause_entity, text='QUIT GAME', scale=(0.3, 0.08), y=-0.1, color=color.red, on_click=application.quit)

        self.end_entity = Entity(parent=camera.ui, enabled=False)
        Entity(parent=self.end_entity, model='quad', scale=(2, 1), color=color.rgba(0,0,0,200))
        self.end_text = Text(parent=self.end_entity, text='', scale=4, y=0.2, origin=(0,0), font=FONT_MAIN)
        self.end_sub_text = Text(parent=self.end_entity, text='', scale=2, y=0.1, origin=(0,0), color=color.light_gray, font=FONT_MAIN)
        Button(parent=self.end_entity, text='MAIN MENU', scale=(0.3, 0.08), y=-0.1, color=color.orange, on_click=self.gm.return_to_menu)

    def toggle_survival_ui(self):
        self.gm.survival_mode = not self.gm.survival_mode
        if self.gm.survival_mode:
            self.mode_btn.text = 'SURVIVAL: ON'
            self.mode_btn.color = color.red
        else:
            self.mode_btn.text = 'SURVIVAL: OFF'
            self.mode_btn.color = color.green

    def toggle_hardcore_ui(self):
        self.gm.hardcore_mode = not self.gm.hardcore_mode
        if self.gm.hardcore_mode:
            self.hardcore_btn.text = 'HARDCORE: ON'
            self.hardcore_btn.color = color.magenta
        else:
            self.hardcore_btn.text = 'HARDCORE: OFF'
            self.hardcore_btn.color = color.gray

    # === 關鍵修正：順序已調整 ===
    def reset_ui_state(self):
        self.low_hp_overlay.animations.clear()
        # 必須先設定顏色 (因為 color.red 預設 alpha=1)
        self.low_hp_overlay.color = color.red 
        # 最後再強制設定透明度為 0
        self.low_hp_overlay.alpha = 0

    def show_hud(self, show_hp):
        self.menu_entity.enabled = False
        self.end_entity.enabled = False
        self.pause_entity.enabled = False
        
        self.timer_text.enabled = True
        self.mode_text.enabled = True
        self.sprint_text.enabled = True
        
        self.hp_text.enabled = show_hp
        self.warning_text.enabled = show_hp
        self.hardcore_text.enabled = self.gm.hardcore_mode
        self.shield_text.enabled = False
        
        # 確保進入 HUD 時清除任何殘留的紅色遮罩
        self.reset_ui_state()

    def show_menu(self):
        self.menu_entity.enabled = True
        self.end_entity.enabled = False
        self.hide_hud()

    def hide_hud(self):
        self.timer_text.enabled = False
        self.mode_text.enabled = False
        self.sprint_text.enabled = False
        self.hp_text.enabled = False
        self.warning_text.enabled = False
        self.hardcore_text.enabled = False
        self.shield_text.enabled = False
        self.reset_ui_state()

    def show_game_over(self, win, reason, time_str):
        self.hide_hud()
        self.end_text.text = 'MISSION COMPLETE' if win else 'CRITICAL FAILURE'
        self.end_text.color = color.green if win else color.red
        self.end_sub_text.text = reason if not win else f"Time: {time_str}s"
        self.end_entity.enabled = True

    def update_hp(self, current, max_hp):
        self.hp_text.text = f'HP: {current}/{max_hp}'
        if current <= 1:
            self.hp_text.color = color.red
            # 只有當動畫沒有在跑的時候才啟動，避免疊加
            if not self.low_hp_overlay.animations:
                self.low_hp_overlay.animate('alpha', 0.5, duration=0.5, loop=True, curve=curve.in_out_sine)
        else:
            self.hp_text.color = color.green
            self.reset_ui_state()

    def show_shield_broken(self):
        self.shield_text.enabled = False
        self.hp_text.color = color.cyan
        self.hp_text.text = "SHIELD BROKEN!"
        invoke(self.reset_hp_color, delay=1)
        
    def reset_hp_color(self):
        self.update_hp(self.gm.current_hp, self.gm.max_hp)