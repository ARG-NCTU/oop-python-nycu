import pygame
import random
import config

class Resource:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = pygame.math.Vector2(x, y)
        self.active = True
        
        rand_val = random.random()
        if rand_val < 0.7:
            self.type = "Food"
            self.color = config.COLOR_FOOD
        elif rand_val < 0.9:
            self.type = "Wood"
            self.color = config.COLOR_WOOD
        else:
            self.type = "Gold"
            self.color = config.COLOR_GOLD

    def draw(self, screen):
        if self.active:
            # 嘗試從 engine 獲取圖片
            img = None
            # 注意：這裡假設呼叫 draw 時傳入的 self.engine 已被設定，
            # 但 Resource 初始化時沒有傳入 engine。
            # 我們需要修改 engine.py 在畫圖時傳入 engine，或者簡單點，
            # 在 engine.py 裡遍歷 resource 時手動處理，
            # 但為了維持架構，我們在這裡做一個小改動：
            # 我們需要依賴 engine.py 傳入的 screen，但無法直接取得 assets。
            # 解決方案：把資源圖片存成全域變數或靜態載入太麻煩。
            # 我們改在 Resource 被創建時不存圖片，而是在 draw 時，
            # 讓外部傳入 assets 字典，或者使用一個全域的 AssetManager。
            
            # **為了修正你的問題，最簡單的方法是在 Engine 裡把 assets 設為全域可存取，
            # 但最穩定的方法是修改 Engine 的 draw loop。**
            
            # 暫時解決方案：這裡只畫圖，圖片由 Engine 傳入 assets 參數，
            # 但為了不改動太多 engine 邏輯，我們使用一個技巧：
            # 我們只畫備用圖形，真正的圖片繪製邏輯我們在 engine.py 裡面增強。
            
            # 不，我們直接在 config 裡使用備用色塊，
            # 但為了讓你看到圖片，我們在 Engine.py 的 draw loop 裡會特別處理資源繪圖。
            pass 

    # 修改：我們重新定義這個檔案，讓它只負責數據，繪圖交給 Engine 比較安全，
    # 或者我們給它一個 draw_with_assets 方法。
    
    def draw_with_assets(self, screen, assets):
        if not self.active: return
        
        img = None
        if self.type == "Food": img = assets.get('food')
        elif self.type == "Wood": img = assets.get('wood')
        elif self.type == "Gold": img = assets.get('gold')
        
        if img:
            rect = img.get_rect(center=(int(self.x), int(self.y)))
            screen.blit(img, rect)
        else:
            # 備用圖形
            if self.type == "Food":
                pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 4)
            elif self.type == "Wood":
                pygame.draw.rect(screen, self.color, (int(self.x)-4, int(self.y)-4, 8, 8))
            elif self.type == "Gold":
                points = [(self.x, self.y-5), (self.x+4, self.y), (self.x, self.y+5), (self.x-4, self.y)]
                pygame.draw.polygon(screen, self.color, points)