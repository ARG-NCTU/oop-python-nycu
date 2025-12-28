import pygame
import random
import config

class EventManager:
    def __init__(self, engine):
        self.engine = engine
        self.active_event = None
        self.cooldown = 0
        
        self.showing_result = False
        self.result_text = ""
        self.result_detail = ""
        self.result_color = (255, 255, 255)
    
    def check_trigger(self):
        # 商店日 (Day 5, 10) 不觸發隨機事件
        if self.engine.day % 5 == 0: return False
        
        if self.cooldown > 0: 
            self.cooldown -= 1
            return False

        # 機率設定 (1.5% 每幀，約每 1-2 天觸發一次)
        if random.random() < 0.015:
            self.trigger_random_event()
            self.cooldown = 600 # 冷卻 10 秒，避免連續轟炸
            return True 
        return False

    def trigger_special_shop(self):
        self.active_event = {
            "title": "黑市商人",
            "desc": "『只要有錢，什麼都能買...』",
            "options": [
                {"text": "大補給 (15金 -> +200食物)", "cost": {"gold": 15}, "effect": "shop_food_bulk"},
                {"text": "建材包 (20金 -> +100木頭)", "cost": {"gold": 20}, "effect": "shop_wood_bulk"},
                {"text": "神工匠 (25金 -> +400HP)", "cost": {"gold": 25}, "effect": "shop_repair_wall"},
                {"text": "命運盲盒 (15金 -> ???)", "cost": {"gold": 15}, "effect": "shop_mystery_box"}
            ]
        }

    def trigger_random_event(self):
        # --- 擴充後的隨機事件庫 ---
        events = [
            # 1. 人口相關
            {
                "title": "流亡難民", "desc": "一群人請求庇護，你看起來像個好人。",
                "options": [
                    {"text": "接納他們 (-50 食物, +2 人口)", "cost": {"food": 50}, "effect": "event_refugees_accept"},
                    {"text": "驅逐 (無事發生)", "cost": {}, "effect": "none"}
                ]
            },
            # 2. 戰鬥相關
            {
                "title": "強盜勒索", "desc": "『交出過路費，不然就燒了你的村子！』",
                "options": [
                    {"text": "給錢消災 (-20 金)", "cost": {"gold": 20}, "effect": "event_bandit_pay"},
                    {"text": "拒絕 (50% 受傷 / 50% 反殺)", "cost": {}, "effect": "event_bandit_fight"}
                ]
            },
            # 3. 建設相關
            {
                "title": "流浪詩人", "desc": "他願意為村莊歌唱，提升士氣。",
                "options": [
                    {"text": "打賞 (-10 金 -> 牆壁修復)", "cost": {"gold": 10}, "effect": "event_bard_sing"},
                    {"text": "不需要 (無事發生)", "cost": {}, "effect": "none"}
                ]
            },
            # 4. 天災
            {
                "title": "雷暴來襲", "desc": "天空烏雲密布，情況不妙。",
                "options": [
                    {"text": "加固房屋 (-30 木 -> 平安)", "cost": {"wood": 30}, "effect": "event_storm_prep"},
                    {"text": "聽天由命 (機率損失人口或牆壁)", "cost": {}, "effect": "event_storm_ignore"}
                ]
            },
            # 5. 神祕學
            {
                "title": "神祕祭壇", "desc": "森林深處的古老祭壇。",
                "options": [
                    {"text": "獻祭食物 (-30 食物 -> 隨機獎勵)", "cost": {"food": 30}, "effect": "event_altar_food"},
                    {"text": "祈禱 (獲得祝福或詛咒)", "cost": {}, "effect": "event_altar_pray"}
                ]
            },
            # --- [NEW] 新增事件 ---
            # 6. 高風險狩獵
            {
                "title": "野獸遷徙", "desc": "大批野牛經過，這是危險也是機會。",
                "options": [
                    {"text": "全軍狩獵 (30% 死人 -> +300 食物)", "cost": {}, "effect": "event_beast_hunt"},
                    {"text": "躲起來 (安全)", "cost": {}, "effect": "none"}
                ]
            },
            # 7. 賭博藥水
            {
                "title": "瘋狂鍊金術士", "desc": "『喝下這瓶藥水，見證奇蹟！』",
                "options": [
                    {"text": "喝！ (隨機效果)", "cost": {}, "effect": "event_alchemy_drink"},
                    {"text": "趕走他", "cost": {}, "effect": "none"}
                ]
            },
            # 8. 道德抉擇
            {
                "title": "迷路的貴族", "desc": "他看起來很有錢，但受傷了且很餓。",
                "options": [
                    {"text": "治療並護送 (-60 食物 -> +100 金)", "cost": {"food": 60}, "effect": "event_noble_help"},
                    {"text": "打劫！ (+30 金, 良心不安)", "cost": {}, "effect": "event_noble_rob"}
                ]
            },
            # 9. 資源探索
            {
                "title": "古代遺跡", "desc": "村民發現了一個被掩埋的入口。",
                "options": [
                    {"text": "派人探索 (機率受傷或獲得大量資源)", "cost": {}, "effect": "event_ruins_explore"},
                    {"text": "封鎖入口 (安全)", "cost": {}, "effect": "none"}
                ]
            },
            # 10. 小額賭博
            {
                "title": "神祕流浪漢", "desc": "他想賣給你一張藏寶圖。",
                "options": [
                    {"text": "購買 (-5 金)", "cost": {"gold": 5}, "effect": "event_treasure_map"},
                    {"text": "不感興趣", "cost": {}, "effect": "none"}
                ]
            }
        ]
        self.active_event = random.choice(events)

    def handle_input(self, key):
        if self.showing_result:
            self.active_event = None
            self.showing_result = False
            return True 

        if not self.active_event: return False
        
        choice = -1
        if key == pygame.K_1: choice = 0
        elif key == pygame.K_2: choice = 1
        elif key == pygame.K_3: choice = 2
        elif key == pygame.K_4: choice = 3
        
        if choice == -1 or choice >= len(self.active_event["options"]):
            return False

        opt = self.active_event["options"][choice]
        
        # 檢查資源
        can_afford = True
        if "gold" in opt["cost"] and self.engine.gold < opt["cost"]["gold"]: can_afford = False
        if "wood" in opt["cost"] and self.engine.wood < opt["cost"]["wood"]: can_afford = False
        if "food" in opt["cost"] and self.engine.food < opt["cost"]["food"]: can_afford = False
        
        if not can_afford:
            self.set_result(False, "資源不足", "你付不起這個選項的代價！")
            self.showing_result = True
            return False 
        
        # 扣除資源
        if "gold" in opt["cost"]: self.engine.gold -= opt["cost"]["gold"]
        if "wood" in opt["cost"]: self.engine.wood -= opt["cost"]["wood"]
        if "food" in opt["cost"]: self.engine.food -= opt["cost"]["food"]
        
        self.apply_effect(opt["effect"])
        self.showing_result = True
        return False

    def set_result(self, is_good, title, detail):
        self.result_text = title
        self.result_detail = detail
        self.result_color = (100, 255, 100) if is_good else (255, 100, 100)

    def apply_effect(self, effect):
        from models.villager import Villager
        rand = random.random()

        # --- 商店效果 ---
        if effect == "shop_food_bulk": 
            self.engine.food += 200
            self.set_result(True, "購買成功", "倉庫堆滿了食物 (+200)。")
        elif effect == "shop_wood_bulk": 
            self.engine.wood += 100
            self.set_result(True, "購買成功", "獲得了大量建材 (+100)。")
        elif effect == "shop_repair_wall": 
            self.engine.wall_hp += 400
            self.set_result(True, "修復成功", "城牆看起來煥然一新 (+400 HP)。")
        elif effect == "shop_mystery_box":
            if rand < 0.4: 
                self.engine.gold += 50
                self.set_result(True, "中大獎！", "裡面全是金幣！ (+50 金)")
            elif rand < 0.7: 
                self.engine.food += 50
                self.set_result(True, "小獎", "獲得了一些乾糧 (+50 食物)。")
            else: 
                self.set_result(False, "銘謝惠顧", "箱子是空的，被騙了...")

        # --- 既有事件 ---
        elif effect == "event_refugees_accept":
            for i in range(2): 
                self.engine.villagers.append(Villager(self.engine, f"難民{i}", (200, 200, 200), "Farmer"))
            self.set_result(True, "人口增加", "村莊接納了新成員 (+2 人)。")

        elif effect == "event_bandit_pay":
            self.set_result(True, "破財消災", "強盜拿了錢離開了。")
        
        elif effect == "event_bandit_fight":
            if rand < 0.5: 
                loss = min(50, self.engine.wood)
                self.engine.wood -= loss
                self.set_result(False, "失敗", f"強盜縱火燒了倉庫，損失 {loss} 木頭。")
            else:
                self.engine.gold += 15
                self.set_result(True, "反殺！", "擊退強盜並搶回 15 金。")

        elif effect == "event_bard_sing":
            self.engine.wall_hp += 100
            self.set_result(True, "士氣高昂", "村民在歌聲中修復了城牆 (+100 HP)。")

        elif effect == "event_storm_prep":
            self.set_result(True, "準備萬全", "因為你的遠見，村莊安然無恙。")

        elif effect == "event_storm_ignore":
            if rand < 0.5:
                dmg = min(self.engine.wall_hp, 200)
                self.engine.wall_hp -= dmg
                self.set_result(False, "災害", f"閃電擊垮了部分城牆 (-{dmg} HP)。")
            else:
                self.set_result(True, "幸運", "雷暴奇蹟般地繞過了村莊。")

        elif effect == "event_altar_food":
            if rand < 0.5: 
                self.engine.wood += 50
                self.set_result(True, "森林的回饋", "祭壇旁長出了優質木材 (+50 木)。")
            else: 
                self.engine.gold += 15
                self.set_result(True, "神的恩賜", "祭壇上出現了金幣 (+15 金)。")

        elif effect == "event_altar_pray":
            if rand < 0.6: 
                self.engine.food += 80
                self.set_result(True, "祝福", "食物從天而降 (+80)。")
            else: 
                self.engine.spawn_interval += 10
                self.set_result(False, "詛咒", "土地變得貧瘠...資源生成變慢了。")

        # --- [NEW] 新增事件效果 ---
        
        elif effect == "event_beast_hunt":
            if rand < 0.3: # 30% 機率死人
                living = [v for v in self.engine.villagers if v.is_alive and v.role != "Hero"]
                if living:
                    victim = random.choice(living)
                    victim.is_alive = False
                    self.set_result(False, "狩獵失敗", f"{victim.name} 在狩獵中犧牲了...")
                else:
                    self.set_result(True, "僥倖", "雖然狩獵失敗，但無人傷亡。")
            else:
                self.engine.food += 300
                self.set_result(True, "大豐收！", "帶回了大量的肉！ (+300 食物)")

        elif effect == "event_alchemy_drink":
            dice = random.randint(1, 3)
            if dice == 1:
                self.engine.wall_hp += 300
                self.set_result(True, "硬化藥水", "城牆變得堅不可摧！ (+300 HP)")
            elif dice == 2:
                # 全體補滿飢餓
                for v in self.engine.villagers: v.hunger = 0
                self.set_result(True, "活力藥水", "所有人精神百倍！ (飢餓歸零)")
            else:
                self.engine.wall_hp = max(0, self.engine.wall_hp - 100)
                self.set_result(False, "爆炸藥水", "轟！藥水爆炸了！ (-100 牆壁)")

        elif effect == "event_noble_help":
            self.engine.gold += 100
            self.set_result(True, "慷慨的回報", "貴族為了感謝你，給了一大袋金幣 (+100)。")

        elif effect == "event_noble_rob":
            self.engine.gold += 30
            self.set_result(True, "搶劫成功", "你搶走了他的錢包 (+30)，良心有點痛。")

        elif effect == "event_ruins_explore":
            if rand < 0.4: # 40% 觸發陷阱
                dmg = min(self.engine.wall_hp, 150)
                self.engine.wall_hp -= dmg
                self.set_result(False, "觸發陷阱", f"遺跡防禦系統攻擊了村莊！ (-{dmg} 牆壁)")
            else:
                self.engine.wood += 80
                self.engine.gold += 40
                self.set_result(True, "古代寶藏", "發現了古代物資！ (+80 木, +40 金)")

        elif effect == "event_treasure_map":
            if rand < 0.5:
                self.engine.gold += 30
                self.engine.spawn_resources(10)
                self.set_result(True, "是真的！", "挖到了寶藏！ (+30 金 & 資源)")
            else:
                self.set_result(False, "廢紙一張", "地圖指向一個空洞...被騙了。")

        elif effect == "none":
            self.set_result(True, "無事發生", "你選擇了保守的作法，平安無事。")

    def draw(self, screen):
        if not self.active_event: return
        
        overlay = pygame.Surface((screen.get_width(), screen.get_height()))
        overlay.set_alpha(180); overlay.fill((0,0,0))
        screen.blit(overlay, (0,0))
        
        cx, cy = screen.get_width()//2, screen.get_height()//2
        w, h = 700, 500
        
        if self.showing_result:
            pygame.draw.rect(screen, (30, 30, 40), (cx-w//2, cy-h//2, w, h), 0, 10)
            pygame.draw.rect(screen, self.result_color, (cx-w//2, cy-h//2, w, h), 3, 10)
            
            title = self.engine.large_font.render(self.result_text, True, self.result_color)
            screen.blit(title, (cx - title.get_width()//2, cy - 50))
            detail = self.engine.font.render(self.result_detail, True, (255, 255, 255))
            screen.blit(detail, (cx - detail.get_width()//2, cy + 20))
            hint = self.engine.font.render("按 [任意鍵] 繼續", True, (150, 150, 150))
            screen.blit(hint, (cx - hint.get_width()//2, cy + h//2 - 50))
        else:
            pygame.draw.rect(screen, (30, 30, 40), (cx-w//2, cy-h//2, w, h), 0, 10)
            pygame.draw.rect(screen, (255, 215, 0), (cx-w//2, cy-h//2, w, h), 3, 10)
            
            gold_txt = self.engine.font.render(f"持有: {self.engine.gold} G", True, (255, 215, 0))
            screen.blit(gold_txt, (cx + w//2 - 160, cy - h//2 + 10))

            title = self.engine.title_font.render(self.active_event["title"], True, (255, 215, 0))
            screen.blit(title, (cx - title.get_width()//2, cy - h//2 + 30))
            
            desc = self.engine.font.render(self.active_event["desc"], True, (200, 200, 200))
            screen.blit(desc, (cx - desc.get_width()//2, cy - h//2 + 80))
            
            y = cy - h//2 + 150
            for i, opt in enumerate(self.active_event["options"]):
                color = (100, 255, 255)
                can_afford = True
                if "gold" in opt["cost"] and self.engine.gold < opt["cost"]["gold"]: can_afford = False
                if "wood" in opt["cost"] and self.engine.wood < opt["cost"]["wood"]: can_afford = False
                if "food" in opt["cost"] and self.engine.food < opt["cost"]["food"]: can_afford = False
                if not can_afford: color = (100, 100, 100)

                text = f"{i+1}. {opt['text']}"
                surf = self.engine.font.render(text, True, color)
                screen.blit(surf, (cx - w//2 + 50, y))
                y += 60