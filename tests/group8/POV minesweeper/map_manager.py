from ursina import *
import random
from game_entities import MineTile
from game_config import DIFFICULTY_SETTINGS

class MapManager:
    def __init__(self, game_manager):
        self.gm = game_manager # 持有主管理器的引用，以便回報輸贏
        self.tiles = {}
        self.grid_size = 0
        self.bomb_count = 0
        self.is_first_click = True

    def start_new_map(self, difficulty_key):
        settings = DIFFICULTY_SETTINGS[difficulty_key]
        self.grid_size = settings['size']
        self.bomb_count = settings['bombs']
        self.is_first_click = True
        self.clear_map()
        self.create_grid_visuals()

    def clear_map(self):
        for t in self.tiles.values():
            destroy(t)
        self.tiles = {}

    def create_grid_visuals(self):
        # 生成視覺方塊，並傳入點擊時要執行的函式
        for x in range(self.grid_size):
            for z in range(self.grid_size):
                t = MineTile(x, z, 
                             on_click_callback=self.handle_tile_click, 
                             on_flag_callback=self.check_win_condition)
                self.tiles[(x, z)] = t

    def handle_tile_click(self, tile):
        if self.gm.state != 'PLAYING': return
        
        # 首點保護機制
        if self.is_first_click:
            self.generate_bombs_deferred(tile.grid_x, tile.grid_z)
            self.is_first_click = False
        
        self.reveal_recursive(tile)
        self.check_win_condition()

    def generate_bombs_deferred(self, safe_x, safe_z):
        # 延遲佈雷：避開玩家點擊的周圍九宮格
        candidates = []
        safe_zone = [(safe_x + dx, safe_z + dz) for dx in (-1,0,1) for dz in (-1,0,1)]
        
        for x in range(self.grid_size):
            for z in range(self.grid_size):
                if (x, z) not in safe_zone:
                    candidates.append((x, z))
        
        actual_bombs = random.sample(candidates, min(self.bomb_count, len(candidates)))
        
        for bx, bz in actual_bombs:
            self.tiles[(bx, bz)].is_bomb = True
            
        # 計算所有方塊的數字
        for x in range(self.grid_size):
            for z in range(self.grid_size):
                if self.tiles[(x,z)].is_bomb: continue
                count = 0
                for dx in (-1,0,1):
                    for dz in (-1,0,1):
                        nx, nz = x+dx, z+dz
                        if (nx,nz) in self.tiles and self.tiles[(nx,nz)].is_bomb:
                            count += 1
                self.tiles[(x,z)].number = count

    def reveal_recursive(self, tile):
        # 遞迴擴散 (Flood Fill)
        if tile.is_revealed or tile.is_flagged: return
        
        tile.reveal_visuals()
        
        if tile.is_bomb:
            self.gm.trigger_game_over(win=False) # 通知主管理器遊戲結束
            return
            
        if tile.number == 0:
            for dx in (-1,0,1):
                for dz in (-1,0,1):
                    nx, nz = tile.grid_x + dx, tile.grid_z + dz
                    if (nx, nz) in self.tiles:
                        neighbor = self.tiles[(nx, nz)]
                        if not neighbor.is_revealed and not neighbor.is_bomb:
                            self.reveal_recursive(neighbor)

    def check_win_condition(self):
        if self.gm.state != 'PLAYING' or self.is_first_click: return
        
        # 勝利條件：所有非炸彈都被翻開
        safe_closed_count = sum(1 for t in self.tiles.values() if not t.is_bomb and not t.is_revealed)
        
        if safe_closed_count == 0:
            self.gm.trigger_game_over(win=True) # 通知主管理器勝利