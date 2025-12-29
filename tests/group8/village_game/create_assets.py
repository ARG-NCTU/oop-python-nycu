import pygame
import os

# 設定圖片大小與資料夾
IMG_SIZE = 32
ASSET_DIR = "assets"

if not os.path.exists(ASSET_DIR):
    os.makedirs(ASSET_DIR)

pygame.init()

def create_surface(color, shape_type):
    s = pygame.Surface((IMG_SIZE, IMG_SIZE), pygame.SRCALPHA)
    
    # 邊框
    if shape_type != "wall":
        pygame.draw.circle(s, (0,0,0, 50), (IMG_SIZE//2, IMG_SIZE-2), 10) # 陰影
    
    if shape_type == "hero":
        # 畫一個帶劍的人
        pygame.draw.circle(s, color, (16, 16), 14) # 身體
        pygame.draw.circle(s, (255, 220, 180), (16, 10), 8) # 頭
        pygame.draw.rect(s, (200, 200, 200), (22, 10, 4, 16)) # 劍刃
        pygame.draw.rect(s, (139, 69, 19), (21, 24, 6, 4)) # 劍柄
        
    elif shape_type == "villager":
        # 畫一個普通人
        pygame.draw.circle(s, color, (16, 16), 12)
        pygame.draw.circle(s, (255, 220, 180), (16, 10), 8)
        
    elif shape_type == "food":
        # 畫一顆蘋果
        pygame.draw.circle(s, (220, 20, 20), (16, 18), 10)
        pygame.draw.rect(s, (0, 150, 0), (16, 6, 6, 6)) # 葉子
        
    elif shape_type == "wood":
        # 畫木頭堆
        pygame.draw.rect(s, (100, 60, 20), (4, 10, 24, 6))
        pygame.draw.rect(s, (120, 80, 30), (6, 18, 20, 6))
        pygame.draw.circle(s, (140, 100, 50), (6, 13), 3) # 年輪
        
    elif shape_type == "gold":
        # 畫金幣/金塊
        pygame.draw.polygon(s, (255, 215, 0), [(16, 2), (28, 16), (16, 30), (4, 16)])
        pygame.draw.polygon(s, (255, 255, 200), [(16, 6), (24, 16), (16, 26), (8, 16)])
        
    elif shape_type == "wall":
        # 畫磚牆
        s.fill((100, 100, 100))
        pygame.draw.line(s, (50, 50, 50), (0, 10), (32, 10), 2)
        pygame.draw.line(s, (50, 50, 50), (0, 20), (32, 20), 2)
        pygame.draw.line(s, (50, 50, 50), (16, 0), (16, 10), 2)
        pygame.draw.line(s, (50, 50, 50), (8, 10), (8, 20), 2)
        pygame.draw.line(s, (50, 50, 50), (24, 10), (24, 20), 2)
        pygame.draw.line(s, (50, 50, 50), (16, 20), (16, 32), 2)

    return s

# 生成並存檔
assets = {
    "hero.png": ((50, 100, 255), "hero"),
    "villager.png": ((100, 200, 100), "villager"),
    "food.png": (None, "food"),
    "wood.png": (None, "wood"),
    "gold.png": (None, "gold"),
    "wall.png": (None, "wall")
}

for filename, (color, kind) in assets.items():
    surf = create_surface(color, kind)
    pygame.image.save(surf, os.path.join(ASSET_DIR, filename))

print(f"成功！已在 {ASSET_DIR} 資料夾產生 {len(assets)} 張圖片。")
pygame.quit()