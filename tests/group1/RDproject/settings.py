# -*- coding: utf-8 -*-
# Global settings
SCREEN_W, SCREEN_H = 1280, 768
FPS = 60

# Grid
GRID_COLS, GRID_ROWS = 6, 5
CELL_SIZE = 112
GRID_X = 380
GRID_Y = 96

PANEL_W = 360

# Economy & base
DIE_COST = 10
MERGE_REFUND = 3
START_MONEY = 60
BASE_HP = 10
MAX_DIE_LEVEL = 7

# Dice balance
BASE_RANGE = 200
BASE_FIRE_RATE = 50  # smaller = faster (frame-equivalent ticks)
FIRE_RATE_STEP = 4

# Enemies
ENEMY_SIZE = 30
WAVE_BASE_COUNT = 7
WAVE_GROWTH = 3

# Boss
BOSS_HP_MULT = 4.5
BOSS_SPAWN_WAVE = 5           # every Nth wave is a boss wave
BOSS_TELEGRAPH_WARN = 0.8     # seconds warning before ability
BOSS_DEBUFF_DURATION = 3.0    # seconds slow/debuff duration
BOSS_DESTROY_RADIUS = 1       # tiles Manhattan radius (1 = 3x3)
BOSS_ZONE_SLOW_ENEMY = 0.6    # enemies speed multiplier inside zone
BOSS_ZONE_SLOW_DICE = 1.2     # dice fire period multiplier (>1 = slower)

# Projectiles
BULLET_SPEED = 660.0
CHAIN_MAX_DISTANCE = 180      # Multi chain max distance

# Slow effect (Freeze dice)
FREEZE_SLOW_RATIO = 0.55
FREEZE_DURATION = 2.2

# UI
TITLE = "Random Dice Tower Defense v2.3a (RDpro7a)"

# Game speed presets (affects enemy move, fire rate, and projectile motion)
GAME_SPEEDS = [0.5, 1.0, 2.0, 4.0, 8.0]
DEFAULT_SPEED_INDEX = 1

# Asset files (optional, looked up in assets/)
ASSET_FILES = {
    "trash": "trash.png",
    "dice": {
        "single": "dice_single.png",
        "multi": "dice_multi.png",
        "freeze": "dice_freeze.png"
    }
}
