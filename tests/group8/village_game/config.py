import os

# --- 視窗與地圖 ---
INITIAL_MAP_WIDTH = 960  
INITIAL_MAP_HEIGHT = 720
UI_WIDTH = 280           

# --- 顏色 (R, G, B) ---
COLOR_BG = (30, 30, 30)
COLOR_MAP = (34, 139, 34)       
COLOR_UI_BG = (40, 44, 52)      
COLOR_UI_BORDER = (70, 75, 85)  
COLOR_TEXT = (255, 255, 255)
COLOR_TEXT_SHADOW = (0, 0, 0)   

# 資源顏色
COLOR_FOOD = (0, 255, 0)        
COLOR_WOOD = (139, 69, 19)      
COLOR_GOLD = (255, 215, 0)      
COLOR_DEATH = (100, 100, 100)   
COLOR_DAMAGE = (255, 50, 50)    # [新增] 傷害數字顏色
COLOR_HEAL = (100, 255, 255)    # [新增] 治療/修復顏色

# --- 圖片設定 ---
IMG_DIR = "assets"
IMG_HERO = "hero.png"
IMG_VILLAGER = "villager.png"
IMG_FOOD = "food.png"
IMG_WOOD = "wood.png"
IMG_GOLD = "gold.png"
IMG_WALL = "wall.png"

# --- 遊戲平衡參數 ---
FPS = 60
DAY_LENGTH = 1200     
HUNGER_RATE = 0.05    

# --- 資源與繁榮度 ---
FOOD_NUTRITION = 30   
WOOD_VALUE = 5        
GOLD_VALUE = 50       

PROSPERITY_THRESHOLD = 300 
MAX_HEROES = 5             

FONT_FILE = "font.ttf"