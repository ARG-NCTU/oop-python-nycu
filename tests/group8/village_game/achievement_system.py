import pygame
import json
import os
from datetime import datetime

class Achievement:
    """單個成就類別"""
    def __init__(self, id, name, description, category, rarity, condition_func, icon_color):
        self.id = id
        self.name = name
        self.description = description
        self.category = category  # 生存、戰鬥、收集、人口、事件、特殊
        self.rarity = rarity  # common, rare, epic, legendary
        self.condition_func = condition_func  # 檢查條件的函數
        self.icon_color = icon_color
        self.unlocked = False
        self.unlock_time = None
        self.progress = 0  # 進度（0-100）
        
    def check(self, engine):
        """檢查是否達成條件"""
        if self.unlocked:
            return False
        
        result = self.condition_func(engine)
        if isinstance(result, bool):
            if result:
                self.unlock(engine)
                return True
        elif isinstance(result, tuple):  # (達成, 進度)
            achieved, progress = result
            self.progress = progress
            if achieved:
                self.unlock(engine)
                return True
        return False
    
    def unlock(self, engine):
        """解鎖成就"""
        self.unlocked = True
        self.unlock_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.progress = 100
        
        # 添加到本局解鎖列表（遊戲結束後顯示）
        if hasattr(engine, 'unlocked_this_game'):
            engine.unlocked_this_game.append(self)
        
        # 保存到文件
        engine.achievement_manager.save_achievements()

class AchievementManager:
    """成就管理器"""
    def __init__(self, engine):
        self.engine = engine
        self.achievements = []
        self.save_file = "achievements.json"
        self.notification_queue = []
        self.current_notification = None
        self.notification_timer = 0
        
        self.init_achievements()
        self.load_achievements()
    
    def init_achievements(self):
        """初始化所有50個成就"""
        
        # ==================== 生存類 (10個) ====================
        
        self.achievements.append(Achievement(
            "survive_day1", "第一天", "存活到第1天",
            "生存", "common", 
            lambda e: e.day >= 1,
            (100, 200, 100)
        ))
        
        self.achievements.append(Achievement(
            "survive_day5", "活過一週", "存活到第5天",
            "生存", "common",
            lambda e: e.day >= 5,
            (100, 220, 100)
        ))
        
        self.achievements.append(Achievement(
            "survive_day10", "十日談", "存活到第10天",
            "生存", "rare",
            lambda e: e.day >= 10,
            (100, 255, 100)
        ))
        
        self.achievements.append(Achievement(
            "survive_day15", "倖存者", "成功存活15天",
            "生存", "epic",
            lambda e: e.day >= 15,
            (50, 255, 50)
        ))
        
        self.achievements.append(Achievement(
            "zero_deaths", "完美守護", "零死亡通關15天",
            "生存", "legendary",
            lambda e: e.day >= 15 and e.total_deaths == 0,
            (255, 215, 0)
        ))
        
        self.achievements.append(Achievement(
            "hard_survivor", "困難征服者", "在Hard難度存活15天",
            "生存", "epic",
            lambda e: e.day >= 15 and e.difficulty == "Hard",
            (255, 140, 0)
        ))
        
        self.achievements.append(Achievement(
            "hell_survivor", "地獄行者", "在Hell難度存活15天",
            "生存", "legendary",
            lambda e: e.day >= 15 and e.difficulty == "Hell",
            (255, 0, 0)
        ))
        
        self.achievements.append(Achievement(
            "wall_master", "城牆大師", "城牆HP達到500",
            "生存", "rare",
            lambda e: e.wall_hp >= 500,
            (150, 150, 150)
        ))
        
        self.achievements.append(Achievement(
            "wall_fortress", "堅不可摧", "城牆HP達到1000",
            "生存", "epic",
            lambda e: e.wall_hp >= 1000,
            (200, 200, 200)
        ))
        
        self.achievements.append(Achievement(
            "no_wall_damage", "銅牆鐵壁", "15天內城牆累積傷害<100",
            "生存", "legendary",
            lambda e: e.day >= 15 and e.total_wall_damage < 100,
            (255, 215, 0)
        ))
        
        # ==================== 戰鬥類 (8個) ====================
        
        self.achievements.append(Achievement(
            "first_night", "第一夜", "度過第一個夜晚",
            "戰鬥", "common",
            lambda e: e.beast_attacks >= 1,
            (100, 100, 255)
        ))
        
        self.achievements.append(Achievement(
            "10_nights", "夜間戰士", "抵禦10次野獸襲擊",
            "戰鬥", "rare",
            lambda e: e.beast_attacks >= 10,
            (150, 150, 255)
        ))
        
        self.achievements.append(Achievement(
            "15_nights", "守夜人", "抵禦15次野獸襲擊",
            "戰鬥", "epic",
            lambda e: e.beast_attacks >= 15,
            (200, 200, 255)
        ))
        
        self.achievements.append(Achievement(
            "low_damage", "防禦專家", "單次野獸襲擊傷害<20",
            "戰鬥", "rare",
            lambda e: hasattr(e, 'last_beast_damage') and e.last_beast_damage < 20,
            (100, 200, 255)
        ))
        
        self.achievements.append(Achievement(
            "wall_broken", "背水一戰", "城牆被摧毀後仍然存活",
            "戰鬥", "epic",
            lambda e: e.wall_hp == 0 and any(v.is_alive for v in e.villagers),
            (255, 100, 100)
        ))
        
        self.achievements.append(Achievement(
            "rebuild_master", "重建專家", "城牆從0修復到200+",
            "戰鬥", "rare",
            lambda e: hasattr(e, 'wall_rebuilt') and e.wall_rebuilt,
            (150, 200, 150)
        ))
        
        self.achievements.append(Achievement(
            "beast_slayer", "野獸剋星", "累積抵禦野獸傷害1000+",
            "戰鬥", "epic",
            lambda e: e.total_wall_damage >= 1000,
            (255, 50, 50)
        ))
        
        self.achievements.append(Achievement(
            "perfect_defense", "完美防禦", "連續5夜城牆無損",
            "戰鬥", "legendary",
            lambda e: hasattr(e, 'perfect_defense_streak') and e.perfect_defense_streak >= 5,
            (255, 215, 0)
        ))
        
        # ==================== 收集類 (10個) ====================
        
        self.achievements.append(Achievement(
            "first_resource", "初次收穫", "收集第一個資源",
            "收集", "common",
            lambda e: e.total_resources_collected >= 5,
            (100, 255, 100)
        ))
        
        self.achievements.append(Achievement(
            "collector_100", "小小收集家", "累積收集100資源",
            "收集", "common",
            lambda e: e.total_resources_collected >= 100,
            (150, 255, 150)
        ))
        
        self.achievements.append(Achievement(
            "collector_500", "資源大師", "累積收集500資源",
            "收集", "rare",
            lambda e: e.total_resources_collected >= 500,
            (200, 255, 200)
        ))
        
        self.achievements.append(Achievement(
            "collector_1000", "收集狂人", "累積收集1000資源",
            "收集", "epic",
            lambda e: e.total_resources_collected >= 1000,
            (100, 255, 100)
        ))
        
        self.achievements.append(Achievement(
            "food_rich", "糧倉滿溢", "糧食儲備達到200",
            "收集", "rare",
            lambda e: e.food >= 200,
            (0, 255, 0)
        ))
        
        self.achievements.append(Achievement(
            "wood_stock", "木材大亨", "木材儲備達到150",
            "收集", "rare",
            lambda e: e.wood >= 150,
            (139, 69, 19)
        ))
        
        self.achievements.append(Achievement(
            "gold_hoarder", "黃金守財奴", "黃金儲備達到100",
            "收集", "epic",
            lambda e: e.gold >= 100,
            (255, 215, 0)
        ))
        
        self.achievements.append(Achievement(
            "all_resources", "資源富豪", "同時擁有食100木100金50",
            "收集", "epic",
            lambda e: e.food >= 100 and e.wood >= 100 and e.gold >= 50,
            (255, 255, 100)
        ))
        
        self.achievements.append(Achievement(
            "efficient_collector", "效率至上", "單天收集50+資源",
            "收集", "rare",
            lambda e: hasattr(e, 'daily_collection') and e.daily_collection >= 50,
            (100, 200, 255)
        ))
        
        self.achievements.append(Achievement(
            "treasure_hunter", "尋寶獵人", "在一天內收集20個金幣",
            "收集", "epic",
            lambda e: hasattr(e, 'daily_gold') and e.daily_gold >= 20,
            (255, 215, 0)
        ))
        
        # ==================== 人口類 (8個) ====================
        
        self.achievements.append(Achievement(
            "starting_crew", "起始團隊", "擁有初始5位村民",
            "人口", "common",
            lambda e: len([v for v in e.villagers if v.is_alive]) >= 5,
            (100, 150, 255)
        ))
        
        self.achievements.append(Achievement(
            "growing_village", "成長中的村莊", "人口達到7人",
            "人口", "rare",
            lambda e: len([v for v in e.villagers if v.is_alive]) >= 7,
            (150, 150, 255)
        ))
        
        self.achievements.append(Achievement(
            "thriving_village", "繁榮村莊", "人口達到10人",
            "人口", "epic",
            lambda e: len([v for v in e.villagers if v.is_alive]) >= 10,
            (200, 150, 255)
        ))
        
        self.achievements.append(Achievement(
            "max_population", "人口爆炸", "達到最高人口12人",
            "人口", "legendary",
            lambda e: len([v for v in e.villagers if v.is_alive]) >= 12,
            (255, 100, 255)
        ))
        
        self.achievements.append(Achievement(
            "no_hunger_death", "溫飽保障", "15天內無人餓死",
            "人口", "epic",
            lambda e: e.day >= 15 and not hasattr(e, 'hunger_deaths'),
            (100, 255, 150)
        ))
        
        self.achievements.append(Achievement(
            "refugee_helper", "難民之友", "接納難民5次以上",
            "人口", "rare",
            lambda e: hasattr(e, 'refugees_accepted') and e.refugees_accepted >= 5,
            (200, 200, 100)
        ))
        
        self.achievements.append(Achievement(
            "full_health", "全員健康", "所有村民飢餓度<30",
            "人口", "rare",
            lambda e: all(v.hunger < 30 for v in e.villagers if v.is_alive),
            (100, 255, 100)
        ))
        
        self.achievements.append(Achievement(
            "lone_survivor", "孤獨倖存者", "僅剩1人時存活到第15天",
            "人口", "legendary",
            lambda e: e.day >= 15 and len([v for v in e.villagers if v.is_alive]) == 1,
            (255, 0, 0)
        ))
        
        # ==================== 事件類 (7個) ====================
        
        self.achievements.append(Achievement(
            "first_event", "初次抉擇", "完成第一個事件",
            "事件", "common",
            lambda e: e.events_completed >= 1,
            (255, 200, 100)
        ))
        
        self.achievements.append(Achievement(
            "event_master", "事件專家", "完成10個事件",
            "事件", "rare",
            lambda e: e.events_completed >= 10,
            (255, 180, 100)
        ))
        
        self.achievements.append(Achievement(
            "event_veteran", "事件老手", "完成20個事件",
            "事件", "epic",
            lambda e: e.events_completed >= 20,
            (255, 150, 100)
        ))
        
        self.achievements.append(Achievement(
            "shopper", "購物狂", "在黑市購買5次",
            "事件", "rare",
            lambda e: hasattr(e, 'shop_purchases') and e.shop_purchases >= 5,
            (255, 215, 0)
        ))
        
        self.achievements.append(Achievement(
            "gambler", "賭徒之魂", "選擇5次高風險事件",
            "事件", "epic",
            lambda e: hasattr(e, 'risky_choices') and e.risky_choices >= 5,
            (255, 0, 0)
        ))
        
        self.achievements.append(Achievement(
            "lucky_one", "幸運兒", "連續3次事件獲得好結果",
            "事件", "rare",
            lambda e: hasattr(e, 'lucky_streak') and e.lucky_streak >= 3,
            (100, 255, 255)
        ))
        
        self.achievements.append(Achievement(
            "event_avoider", "謹慎派", "15天內僅完成必要事件(<5個)",
            "事件", "rare",
            lambda e: e.day >= 15 and e.events_completed < 5,
            (200, 200, 200)
        ))
        
        # ==================== 特殊類 (7個) ====================
        
        self.achievements.append(Achievement(
            "speed_demon", "速度惡魔", "使用艾里奧通關",
            "特殊", "rare",
            lambda e: e.day >= 15 and any(v.name == "艾里奧" and v.is_alive for v in e.villagers),
            (50, 255, 50)
        ))
        
        self.achievements.append(Achievement(
            "golden_touch", "點石成金", "使用摩根累積金幣200+",
            "特殊", "rare",
            lambda e: e.gold >= 200 and any(v.name == "摩根" for v in e.villagers),
            (255, 215, 0)
        ))
        
        self.achievements.append(Achievement(
            "healer_angel", "治療天使", "使用芙蕾雅治療100次",
            "特殊", "epic",
            lambda e: hasattr(e, 'heal_count') and e.heal_count >= 100,
            (255, 100, 255)
        ))
        
        self.achievements.append(Achievement(
            "builder_legend", "建築傳奇", "使用泰坦修復城牆1000+",
            "特殊", "epic",
            lambda e: hasattr(e, 'builder_repairs') and e.builder_repairs >= 1000,
            (150, 150, 150)
        ))
        
        self.achievements.append(Achievement(
            "oracle_wisdom", "先知智慧", "使用瑟蕾絲節省糧食500+",
            "特殊", "epic",
            lambda e: hasattr(e, 'food_saved') and e.food_saved >= 500,
            (255, 140, 0)
        ))
        
        self.achievements.append(Achievement(
            "s_rank", "S級村長", "獲得S級評價",
            "特殊", "legendary",
            lambda e: hasattr(e, 'final_rank') and e.final_rank == "S",
            (255, 215, 0)
        ))
        
        self.achievements.append(Achievement(
            "completionist", "成就獵人", "解鎖所有其他成就",
            "特殊", "legendary",
            lambda e: sum(1 for a in e.achievement_manager.achievements if a.unlocked and a.id != "completionist") >= 49,
            (255, 0, 255)
        ))
    
    def check_achievements(self):
        """檢查所有成就"""
        newly_unlocked = []
        for achievement in self.achievements:
            if achievement.check(self.engine):
                newly_unlocked.append(achievement)
        return newly_unlocked
    
    def save_achievements(self):
        """保存成就到文件"""
        data = {
            "achievements": [
                {
                    "id": a.id,
                    "unlocked": a.unlocked,
                    "unlock_time": a.unlock_time,
                    "progress": a.progress
                }
                for a in self.achievements
            ],
            "last_save": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            with open(self.save_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存成就失敗: {e}")
    
    def load_achievements(self):
        """從文件讀取成就"""
        if not os.path.exists(self.save_file):
            return
        
        try:
            with open(self.save_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for saved_ach in data.get("achievements", []):
                for achievement in self.achievements:
                    if achievement.id == saved_ach["id"]:
                        achievement.unlocked = saved_ach.get("unlocked", False)
                        achievement.unlock_time = saved_ach.get("unlock_time")
                        achievement.progress = saved_ach.get("progress", 0)
                        break
        except Exception as e:
            print(f"讀取成就失敗: {e}")
    
    def get_unlock_rate(self):
        """獲取解鎖率"""
        total = len(self.achievements)
        unlocked = sum(1 for a in self.achievements if a.unlocked)
        return unlocked, total, (unlocked / total * 100) if total > 0 else 0
    
    def get_achievements_by_category(self, category=None):
        """按類別獲取成就"""
        if category is None:
            return self.achievements
        return [a for a in self.achievements if a.category == category]
    
    def get_achievements_by_rarity(self, rarity):
        """按稀有度獲取成就"""
        return [a for a in self.achievements if a.rarity == rarity]