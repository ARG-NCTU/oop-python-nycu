from ursina import color

# === 遊戲難度設定 ===
DIFFICULTY_SETTINGS = {
    'EASY': {'size': 10, 'bombs': 10, 'label': 'ROOKIE (10x10)'},
    'MEDIUM': {'size': 15, 'bombs': 35, 'label': 'VETERAN (15x15)'},
    'HARD': {'size': 20, 'bombs': 70, 'label': 'EXPERT (20x20)'}
}

# === 顏色配置 ===
COLOR_NAVY = color.rgb(0, 0, 128)
COLOR_MAROON = color.rgb(128, 0, 0)

NUMBER_COLORS = {
    1: color.rgb(65, 105, 225),   # Royal Blue
    2: color.rgb(34, 139, 34),    # Forest Green
    3: color.rgb(220, 20, 60),    # Crimson Red
    4: COLOR_NAVY,
    5: COLOR_MAROON,
    6: color.rgb(0, 128, 128),    # Teal
    7: color.black,
    8: color.gray
}

# === 字體設定 ===
# 如果你有喜歡的字體檔 (ttf)，可以放在資料夾並改這裡
FONT_MAIN = 'VeraMono.ttf'