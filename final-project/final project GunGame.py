
import pygame
import sys
import math
import time
import random
import json
import os
# 初始化 Pygame
pygame.init()


# 設定視窗大小
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)


# 設定顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FONT = 50


# 重力加速度
GRAVITY = 0.6


# 設定玩家初始位置和速度
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 10
PLAYER_ACCERATION = 0.5
JUMP_HEIGHT = 13  # 跳躍高度適中
RELIVE_X  = [250, 970]
RELIVE_Y = 0
# 地板位置列表
GROUND_LEVELS = [300, 410, 525, 615]  # 示例地板高度，可以根据实际情况修改

def distance_2D(x1, y1, x2, y2):
    return math.pow(math.pow(abs(x2-x1), 2) + math.pow(abs(y1-y2), 2), 0.5)

def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def draw_init():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    initial_screen = pygame.image.load('./initial.png')  # 載入背景圖片
    intro_img = pygame.image.load('./intro.png')  
    player1_img = pygame.image.load('./player_1.png') # 載入玩家圖片
    player2_img = pygame.image.load('./player_2.png') # 載入玩家圖片
    #tips = pygame.image.load('./tap_any_bottom.png')  # 載入提示圖片
    player1_img = pygame.transform.scale(player1_img, (120, 165))
    player2_img = pygame.transform.scale(player2_img, (120, 165))
    Player1 = Player(0, 0, player1_img, 1)
    Player2 = Player(WINDOW_WIDTH, 0, player2_img, 2)
    player1_img = pygame.transform.scale(player1_img, (192, 264))
    player2_img = pygame.transform.scale(player2_img, (192, 264))
    all_players = pygame.sprite.Group()
    all_players.add(Player1, Player2)
    # 獲取圖片的原始大小
    img_width, img_height = initial_screen.get_size()
    
    # 計算圖片縮放比例
    scale = min(WINDOW_WIDTH / img_width, WINDOW_HEIGHT / img_height)
    
    # 計算縮放後的大小
    new_size = (int(img_width * scale), int(img_height * scale))
    
    # 等比例縮小圖片
    initial_screen = pygame.transform.scale(initial_screen, new_size)
    intro_img = pygame.transform.scale(intro_img, new_size)
    
    # 計算圖片在視窗中的位置，使其居中
    pos_x = (WINDOW_WIDTH - new_size[0]) // 2
    pos_y = (WINDOW_HEIGHT - new_size[1]) // 2
    screen.blit(initial_screen, (pos_x, pos_y))
    
    pygame.display.set_caption("GunGame")
    state = 0  # 0: 顯示標題, 1: 顯示說明, 2: 開始遊戲
    counttime = 0
    dir1 = "right"
    dir2 = "left"
    while state < 2:
        screen.fill((0, 0, 0))  # 清除屏幕
        screen.blit(initial_screen, (pos_x, pos_y))  # 確保背景圖片始終顯示
        counttime += 1
        speed_x = 10
        
        if state == 0:
            if counttime <= 50:
                draw_text(screen, "<Tap Any Bottom To Start>", 50, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 200)
            Player1.gravity()
            Player2.gravity()
            if Player1.rect.right > WINDOW_WIDTH:
                dir1 = "left"
            if Player1.rect.left < 0:
                dir1 = "right"
            if Player2.rect.right > WINDOW_WIDTH:
                dir2 = "left"
            if Player2.rect.left < 0:
                dir2 = "right"
            if Player1.rect.bottom > WINDOW_HEIGHT:
                Player1.speed_y = random.randint(-27, -10)
            if Player2.rect.bottom > WINDOW_HEIGHT:
                Player2.speed_y = random.randint(-27, -10)
            Player1.move_x(dir1)
            Player2.move_x(dir2)
            all_players.draw(screen)

        elif state == 1:
            screen.blit(intro_img, (pos_x, pos_y))
            draw_text(screen, "move              fire     bomb", 50, WINDOW_WIDTH / 2-250, WINDOW_HEIGHT / 2 + 250)
            draw_text(screen, "move              fire     bomb", 50, WINDOW_WIDTH / 2+345, WINDOW_HEIGHT / 2 + 250)
            if counttime <= 50:
                screen.blit(player1_img, (WINDOW_WIDTH / 2-300, WINDOW_HEIGHT / 2 + 20-220))
                screen.blit(player2_img, (WINDOW_WIDTH / 2+300, WINDOW_HEIGHT / 2 + 20-220))
            else:
                screen.blit(player1_img, (WINDOW_WIDTH / 2-300, WINDOW_HEIGHT / 2-220))
                screen.blit(player2_img, (WINDOW_WIDTH / 2+300, WINDOW_HEIGHT / 2-220))
            counttime += 1
        if counttime > 100:
            counttime = 0
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                state += 1


def draw_end(who_win):
    pygame.init()  # 初始化 Pygame
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # 載入圖片
    initial_screen = pygame.image.load('./initial.png')  # 載入背景圖片
    player1_img = pygame.image.load('./1_player.png')  # 載入玩家1圖片
    player2_img = pygame.image.load('./2_player.png')  # 載入玩家2圖片
    player_win = pygame.image.load('./player_win.png')  # 載入玩家勝利圖片
    space_img = pygame.image.load('./space.jpg')  # 載入背景圖片
    crown_img = pygame.image.load('./crown.png')
    player_1_img = pygame.image.load('./player_1.png')  # 載入玩家1圖片
    player_2_img = pygame.image.load('./player_2.png')  # 載入玩家2圖片
    player_1_img = pygame.transform.scale(player_1_img, (240, 330))
    player_2_img = pygame.transform.scale(player_2_img, (240, 330))
    crown_img = pygame.transform.scale(crown_img, (100, 100))

    # 獲取圖片的原始大小
    img_width, img_height = initial_screen.get_size()
    
    # 計算圖片縮放比例
    scale = min(WINDOW_WIDTH / img_width, WINDOW_HEIGHT / img_height)
    
    # 計算縮放後的大小
    new_size = (int(img_width * scale), int(img_height * scale))
    
    # 等比例縮小圖片
    initial_screen = pygame.transform.scale(initial_screen, new_size)
    
    # 計算圖片在視窗中的位置，使其居中
    pos_x = (WINDOW_WIDTH - new_size[0]) // 2
    pos_y = (WINDOW_HEIGHT - new_size[1]) // 2
    screen.blit(initial_screen, (pos_x, pos_y))
    
    pygame.display.set_caption("GunGame")

    # 按兩下結束函數
    state = 0  # 0: 顯示標題, 1: 顯示說明, 2: 開始遊戲
    counttime = 0
    start_ticks = pygame.time.get_ticks()  # 開始計時

    while state < 1:
        screen.fill((0, 0, 0))  # 清除屏幕
        screen.blit(space_img, (pos_x, pos_y))  # 確保背景圖片始終顯示
        
        if state == 0:
            screen.blit(player_win, (200, WINDOW_HEIGHT / 2 - 270))
            mid = 720
            if who_win == 1:
                screen.blit(player1_img, (mid + 10, WINDOW_HEIGHT / 2 - 250))
                screen.blit(player_1_img, (mid - 200, WINDOW_HEIGHT / 2 - 60))
            elif who_win == 2:
                screen.blit(player2_img, (mid, WINDOW_HEIGHT / 2 - 250))
                screen.blit(player_2_img, (mid - 200, WINDOW_HEIGHT / 2 - 60))
            screen.blit(crown_img, (mid - 120, WINDOW_HEIGHT / 2 - 120))
        pygame.display.flip()

        # 檢查事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 檢查時間是否已經超過3秒
        if pygame.time.get_ticks() - start_ticks > 10000:  # 3000 毫秒 = 3 秒
            state = 1  # 結束循環

    # 等待3秒後關閉遊戲
    pygame.quit()
    sys.exit()

# 建立遊戲場景類別
class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("GunGame")
        self.clock = pygame.time.Clock()
        self.background_img = pygame.image.load('./background.jpg') # 載入背景圖片
        self.initial_img = pygame.image.load('./initial.png') # 載入初始畫面
        self.tap_img = pygame.image.load('./tap_any_bottom.png') # 載入提示
        self.player1_img = pygame.image.load('./player_1.png') # 載入玩家圖片
        self.player2_img = pygame.image.load('./player_2.png') # 載入玩家圖片
        self.bomb_img = pygame.image.load('./bomb.png') # 載入炸彈圖片
        self.bomb_effect_img = pygame.image.load('./bomb_effect.png') # 載入爆炸特效
        self.smallgun1_img = pygame.image.load('./smallgun1.png') # 載入小槍圖片
        self.smallgun2_img = pygame.image.load('./smallgun2.png')
        self.shotgun1_img = pygame.image.load('./shotgun1.png')
        self.shotgun2_img = pygame.image.load('./shotgun2.png')
        self.sniper1_img = pygame.image.load('./sniper1.png')
        self.sniper2_img = pygame.image.load('./sniper2.png')
        self.bullet_img = pygame.transform.scale(pygame.image.load('./bullet.png'), (35,35))
        self.space_img = pygame.image.load('./space.jpg')
        self.box_img = pygame.image.load('./box.png')
        self.heart_img = pygame.transform.scale(pygame.image.load('./heart.png'), (40, 40))
        self.player1 = Player(RELIVE_X[0] , RELIVE_Y, self.player1_img, 1)
        self.player2 = Player(RELIVE_X[1] , RELIVE_Y, self.player2_img, 2)
        self.players = [self.player1, self.player2]
        self.player2.turn_img("left")
        self.player1_draw = pygame.sprite.Group()
        self.player2_draw = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.bomb_effects = pygame.sprite.Group()
        self.font = pygame.font.Font(None, FONT)
        self.font_i = pygame.font.SysFont('Arial', 60)
        self.treasure_boxes = pygame.sprite.Group() 
        self.gun_images1 = GunImage(self.player1)
        self.gun_images2 = GunImage(self.player2)
        self.lagtime_images1 = Lagtime_Image(self.player1)
        self.lagtime_images2 = Lagtime_Image(self.player2)
        self.lagtime_back1 = Lagtime_back_Image(self.player1)
        self.lagtime_back2 = Lagtime_back_Image(self.player2)
        self.player1_draw.add(self.player1, self.gun_images1, self.lagtime_back1, self.lagtime_images1)
        self.player2_draw.add(self.player2, self.gun_images2, self.lagtime_back2, self.lagtime_images2)
    def spawn_treasure_box(self):
        treasure_box = TreasureBox(random.randint(95, 1000),-100, self.box_img)
        self.player1_draw.add(treasure_box)
        self.treasure_boxes.add(treasure_box)    
        
    def run(self):
        running = True
        self.player1_press_jump = 0  # 玩家1是否按跳躍鍵
        self.player2_press_jump = 0  # 玩家2是否按跳躍鍵
        self.box_check = 0
        self.box_time = 300
        show_start_screen = True       # 顯示開始畫面
        show_end_screen = True         # 顯示結束畫面
        while running:
            if show_start_screen:
                draw_init()
                show_start_screen = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.player1.live == 0 and show_end_screen:
                assert self.player1.remain_life + self.player1.death_count == 5
                assert self.player2.remain_life + self.player2.death_count == 5
                assert self.player1.hit_count <= self.player2.shoot_count
                assert self.player2.hit_count <= self.player1.shoot_count

                self.export_player_data(self.player1, self.player2)
                draw_end(2)
                running = False
                #self.export_player_data(self.player1)
                #self.export_player_data(self.player2)
                #self.player1.restart(0)
                #self.player2.restart(1)
                #draw_init()
                #按下任意鍵回到開始畫面

            if self.player2.live == 0 and show_end_screen:
                assert self.player1.remain_life + self.player1.death_count == 5
                assert self.player2.remain_life + self.player2.death_count == 5
                assert self.player1.hit_count <= self.player2.shoot_count
                assert self.player2.hit_count <= self.player1.shoot_count
                self.export_player_data(self.player1, self.player2)
                draw_end(1)
                running = False
                #self.export_player_data(self.player1)
                #self.export_player_data(self.player2)
                #self.player1.restart(0)
                #ㄊself.player2.restavckrt(1)
                #draw_init()vdbddddsv
            #按下任意鍵回到開始畫面
                
            if self.box_check == 0:# 生成寶箱
                self.box_time -= 1
                if self.box_time == 0:
                    self.box_time = 300
                    self.spawn_treasure_box()
                    self.box_check = 1
            mkeys = pygame.key.get_pressed()
        
            if mkeys[pygame.QUIT]:
                running = False
            if mkeys[pygame.K_w]:
                self.player1.jump(self.player1_press_jump)
                self.player1_press_jump = 1
            else :
                self.player1_press_jump = 0
            if mkeys[pygame.K_UP]:
                self.player2.jump(self.player2_press_jump)
                self.player2_press_jump = 1
            else :
                self.player2_press_jump = 0
            if mkeys[pygame.K_s]:
                self.player1.move_down()
            if mkeys[pygame.K_DOWN]:
                self.player2.move_down()
            if mkeys[pygame.K_a]:
                self.player1.move_x("left")
            if mkeys[pygame.K_d]:
                self.player1.move_x("right")
            if mkeys[pygame.K_LEFT]:
                self.player2.move_x("left")
            if mkeys[pygame.K_RIGHT]:
                self.player2.move_x("right")
            if mkeys[pygame.K_v]:
                if fire1_press_check == 0:
                    self.fire_bullet(self.player1, self.player1.get_direction(), RED, self.player1.now_gun(), 1) # 玩家1發射子彈

                if self.player1.gun.numofbullet <= 0: # 子彈數量用完換成小槍
                    self.player1.gun = smallgun() 
                fire1_press_check = 1

            else :
                fire1_press_check = 0
            if mkeys[pygame.K_k]:
                if fire2_press_check == 0:
                    self.fire_bullet(self.player2, self.player2.get_direction(), YELLOW, self.player2.now_gun(), 2)
                fire2_press_check = 1
                if self.player2.gun.numofbullet <= 0:
                    self.player2.gun = smallgun()
            else :
                fire2_press_check = 0
            if mkeys[pygame.K_b]:
                if bomb_press_check1 == 0 and self.player1.minus_bomb_num():
                    self.drop_bomb(self.player1, self.bomb_img)
                bomb_press_check1 = 1
            else :
                bomb_press_check1 = 0
            if mkeys[pygame.K_l]:
                if bomb_press_check2 == 0 and self.player2.minus_bomb_num():
                    self.drop_bomb(self.player2, self.bomb_img)
                bomb_press_check2 = 1
            else :
                bomb_press_check2 = 0 

            self.player1_draw.update()
            self.player2_draw.update()
            self.bullets.update()
            self.bombs.update()
            
            # 碰撞檢測
            for bullet in self.bullets:
                if bullet.leave_check():
                    if bullet.rect.colliderect(self.player1.rect):
                        self.player1.speed_x += 2 * bullet.speed
                        self.player2.hit_count += 1
                        bullet.kill()
                    if bullet.rect.colliderect(self.player2.rect):
                        self.player2.speed_x += 2 * bullet.speed
                        self.player1.hit_count += 1
                        bullet.kill()
                if ((not bullet.rect.colliderect(self.player1.rect)) and bullet.which_player() == 1) or ((not bullet.rect.colliderect(self.player2.rect)) and bullet.which_player() == 2):
                    bullet.turn_check()
                if bullet.out() or bullet.update():
                    bullet.kill()

            for bomb in self.bombs:
                if bomb.countdown():
                    bomb_effect = Bomb_effect(bomb.rect.centerx, bomb.rect.bottom, self.bomb_effect_img)
                    self.bomb_effects.add(bomb_effect)
                    bomb.explosion(self.player1)
                    bomb.explosion(self.player2)
                    bomb.kill()
            
            for bomb_effect in self.bomb_effects:
                if bomb_effect.Countdown():
                    bomb_effect.kill()

            for treasure_box in self.treasure_boxes:
                if pygame.sprite.collide_rect(self.player1, treasure_box):
                    gun_name = treasure_box.open_box()
                    self.player1.pickup_count += 1
                    self.player1.change_gun(gun_name)
                    self.player1.change_gunlag_to_zero()
                    treasure_box.kill()
                    self.box_check = 0
                if pygame.sprite.collide_rect(self.player2, treasure_box):
                    gun_name = treasure_box.open_box()
                    self.player2.pickup_count += 1
                    self.player2.change_gun(gun_name)
                    self.player2.change_gunlag_to_zero()
                    treasure_box.kill()
                    self.box_check = 0
                if treasure_box.rect.top > WINDOW_HEIGHT:
                    treasure_box.kill()   
                    self.box_check = 0

            text_smallgun1_numofbullete = self.font_i.render("∞", True, (255, 255, 255)) #輸出左上角的字
            text_smallgun2_numofbullete = self.font_i.render("∞", True, (255, 255, 255)) 
            text_player1_ammo = self.font.render(str(self.player1.gun.numofbullet), True, (255, 255, 255)) 
            text_player2_ammo = self.font.render(str(self.player2.gun.numofbullet), True, (255, 255, 255))
            text_multiple = self.font.render("x", True, (255, 255, 255))
            self.screen.blit(self.background_img, (0, 0))  #    背景圖片
            self.bomb_effects.draw(self.screen)
            self.bullets.draw(self.screen)
            self.player1_draw.draw(self.screen)
            self.player2_draw.draw(self.screen)
            self.bombs.draw(self.screen) 
            self.draw_object(self.player1, self.player2)

            self.screen.blit(self.bullet_img , (WINDOW_WIDTH - 135 , 93))
            self.screen.blit(self.bullet_img , (10 , 93))         # 玩家1的子彈
            self.screen.blit(text_multiple,(60,95))            # 玩家1乘法符號
            self.screen.blit(text_multiple,(WINDOW_WIDTH - 85,95))
            if self.player1.gun.gun_name == "smallgun":
                self.screen.blit(text_smallgun1_numofbullete,(100,80)) # 玩家1的子彈數量
            else:
                self.screen.blit(text_player1_ammo,(100,95))
            if self.player2.gun.gun_name == "smallgun":
                self.screen.blit(text_smallgun2_numofbullete,(WINDOW_WIDTH - 45,80))
            else:
                self.screen.blit(text_player2_ammo,(WINDOW_WIDTH - 45,95))
            self.lagtime_back1.update()
            self.lagtime_back2.update()
            self.lagtime_images1.update()
            self.lagtime_images2.update()


            pygame.display.flip()

            self.clock.tick(60)

            #玩家重生
            if self.player1.rect.top > WINDOW_HEIGHT:
                self.player1.relive(0)
                self.player1.death_count += 1
                self.player1.remain_life -= 1
            if self.player2.rect.top > WINDOW_HEIGHT:
                self.player2.relive(1)
                self.player2.death_count += 1
                self.player2.remain_life -= 1

            #顯示玩家一的子彈數量
            text_bullet1 = self.font.render(str(self.player1.gun.numofbullet), True, (255, 255, 255))
            self.screen.blit(text_bullet1, (10, 10))

    # 發射子彈 
    def fire_bullet(self, player, direction, color, gun_name, which_player):
        if player.get_value("gunlag") <= 0:
            bullet = Bullet(color, player.rect.centerx, player.rect.centery, direction, gun_name, which_player)
            self.bullets.add(bullet)
            player.change_gunlag()
            gun_name = player.now_gun()
            player.speed_x -= player.gun.recoil * direction
            player.gun.numofbullet -= 1
            player.shoot_count += 1
          

    def drop_bomb(self, player, img):
        bomb = Bomb(player.rect.centerx, player.rect.centery - 65, img, player.get_direction())
        self.bombs.add(bomb)
        player.bomb_count += 1


    def draw_object(self, player1, player2):
        for i in range(player1.live):
            self.screen.blit(self.heart_img, (7 + 45 * i, 10))
        for i in range(player2.live):
            self.screen.blit(self.heart_img, (WINDOW_WIDTH - 45 * (i + 1)-3, 10))
        for i in range(player1.bomb_num):
            self.screen.blit(pygame.transform.scale(self.bomb_img, [35,35]), (10 + 45 * i, 50))
        for i in range(player2.bomb_num):
            self.screen.blit(pygame.transform.scale(self.bomb_img, [35,35]), (WINDOW_WIDTH - 45 * (i + 1), 50))



    def export_player_data(self, player1, player2):
        # 创建新的数据条目
        player_data = {
            'player1_jump_count': player1.jump_count,
            'player1_shoot_count': player1.shoot_count,
            'player1_bomb_count': player1.bomb_count,
            'player1_death_count': player1.death_count,
            'player1_hit_count': player1.hit_count,
            'player1_pickup_count': player1.pickup_count,
            'player1_remain_life': player1.remain_life,
            'player2_jump_count': player2.jump_count,
            'player2_shoot_count': player2.shoot_count,
            'player2_bomb_count': player2.bomb_count,
            'player2_death_count': player2.death_count,
            'player2_hit_count': player2.hit_count,
            'player2_pickup_count': player2.pickup_count,
            'player2_remain_life': player2.remain_life,
        }

        # 定义文件路径
        file_path = './player_data.json'

        # 检查文件是否存在
        if os.path.exists(file_path):
            # 读取现有数据
            with open(file_path, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        # 將新的数据条目添加到数据集
        data.append(player_data)

        # 将整个数据集写回文件
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)





class Physics(object):
        def __init__(self, x, y, img):
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed_x = 0
            self.speed_y = 0
            self.on_ground = False

        def gravity(self):
            self.speed_y += GRAVITY
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

        
        def update(self):
            # 應用重力
            self.speed_y += GRAVITY

            # 移動
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            # 檢查是否在地板上
            self.check_ground()

            #讓角色滑行
            self.speed_x = self.speed_x * 0.93


        def check_ground(self):
            # 找到距離玩家最近的地板
            min_distance = float('inf')
            closest_ground = None
            for ground_level in GROUND_LEVELS:
                if ground_level == GROUND_LEVELS[0] and not ((self.rect.x > 310 and self.rect.x < 570) or (self.rect.x > 680 and self.rect.x < 940)):
                    continue
                if ground_level == GROUND_LEVELS[1] and not (self.rect.x > 185 and self.rect.x < 1070):
                    continue
                if ground_level == GROUND_LEVELS[2] and not ((self.rect.x > 90 and self.rect.x < 360) or (self.rect.x > 890 and self.rect.x < 1160)):
                    continue
                if ground_level == GROUND_LEVELS[3] and not (self.rect.x > 325 and self.rect.x < 940):
                    continue
                distance = abs(self.rect.bottom - ground_level)
                if distance < min_distance:
                    min_distance = distance
                    closest_ground = ground_level
            if min_distance >= 10:
                self.on_ground = False
            if self.on_ground == True:
                if self.speed_y > 0:
                    self.speed_y = 0
                self.rect.bottom = closest_ground
            elif self.speed_y >= 0 and min_distance < self.speed_y:
                self.on_ground = True
                self.speed_y = 0
                self.rect.bottom = closest_ground

    # 建立玩家類別
class Player(pygame.sprite.Sprite, Physics):
    def __init__(self, x, y, img, playernumber):
        super().__init__()
        Physics.__init__(self, x, y, img)
        self.right_img = img
        self.left_img = pygame.transform.flip(img, True, False)
        self.on_ground = True
        self.ground_level = None  #玩家所在的地板高度
        self.bomb_num = 3
        self.double_jump = 1
        self.gunlag = 0
        self.playernumber = playernumber
        self.live = 5
        self.gun = smallgun()
        self.jump_count = 0
        self.double_jump_count = 0
        self.shoot_count = 0
        self.bomb_count = 0
        self.walk_distance = 0
        self.death_count = 0
        self.pickup_count = 0
        self.hit_count = 0
        self.remain_life = 5
                 
    def change_gunlag(self):
        self.gunlag = self.gun.lagtime

    def change_gunlag_to_zero(self):
        self.gunlag = 0

    def get_value(self, sub): # 拿來取要的值
        if sub == "x":
            return self.rect.x
        if sub == "y":
            return self.rect.y
        if sub == "bottom":
            return self.rect.bottom
        if sub == "gunlag":
            return self.gunlag
        if sub == "live":
            return self.live
        
    
    def on_ground(self): # 回傳on_ground值
        return self.on_ground

    def turn_img(self, direction):
        if direction == "left":
            self.image = self.left_img
        elif direction == "right":
            self.image = self.right_img

    def get_direction(self):
        if self.image == self.left_img:
            return -1
        else:
            return 1
    
    def update(self): # 繼承update
        Physics.update(self)
        self.gunlag -= 1

    def check_ground(self): # 繼承check_ground
        super().check_ground()

    def move_x(self, direction):
        if direction == "left":
            if self.speed_x >= -PLAYER_SPEED:
                self.speed_x -= PLAYER_ACCERATION
            self.turn_img("left")
        elif direction == "right":
            if self.speed_x <= PLAYER_SPEED:
                self.speed_x += PLAYER_ACCERATION
            self.turn_img("right")

    def jump(self, check):
        if self.on_ground:  # 只有在地面上才能跳
            self.speed_y = -JUMP_HEIGHT
            self.double_jump = 1
            self.jump_count += 1
            self.on_ground = False
        elif self.double_jump == 1 and check == 0: # 二段跳
            self.speed_y = -10
            self.double_jump_count += 1
            self.double_jump = 0

    def move_down(self):
        # 玩家要在地板上才能往下移動
        if self.on_ground:
            if not((self.rect.bottom == GROUND_LEVELS[2] and ((self.rect.x > 90 and self.rect.x < 360) or (self.rect.x > 890 and self.rect.x < 1160))) or (self.rect.bottom == GROUND_LEVELS[3] and (self.rect.x > 325 and self.rect.x < 940))):
                self.rect.y += 15
                self.check_ground()

    def minus_bomb_num(self):
        self.bomb_num -= 1
        if self.bomb_num < 0:
            return False
        else:
            return True

    def relive(self, num):
        #玩家復活
        self.rect.x = RELIVE_X[num]
        self.rect.y = RELIVE_Y
        self.on_ground = True
        self.speed_x = 0
        self.speed_y = 0
        self.bomb_num = 3
        self.gun = smallgun()
        self.live -= 1

    def restart(self, num):
        self.rect.x = RELIVE_X[num]
        self.rect.y = RELIVE_Y
        self.on_ground = True
        self.speed_x = 0
        self.speed_y = 0
        self.bomb_num = 3
        self.gun  = smallgun()
        self.live = 3

    def change_gun(self, gun_name):
        if gun_name == "smallgun":
            self.gun  = smallgun()
        elif gun_name == "shotgun":
            self.gun = shotgun()
        elif gun_name == "sniper":
            self.gun  = sniper()


    def now_gun(self):
        return self.gun.gun_name
        

# 建立槍類別
class Gun():
    def __init__(self, speed, recoil, numofbullet, lagtime):
        self.speed = speed
        self.recoil = recoil
        self.numofbullet = numofbullet
        self.lagtime = lagtime
        self.gun_name = None
        self.img1_right = None
        self.img2_right = None
        self.img1_left= None
        self.img2_left = None
        self.correction_xleft = 0   
        self.correction_yleft = 0
        self.correction_xright = 0
        self.correction_yright = 0

class smallgun(Gun):
    def __init__(self):
        super().__init__(5, 2, 100000, 1)
        self.gun_name = "smallgun"
        self.img1_right = pygame.image.load('./smallgun1.png')
        self.img2_right = pygame.image.load('./smallgun2.png')
        self.img1_left = pygame.transform.flip(self.img1_right, True, False)
        self.img2_left = pygame.transform.flip(self.img2_right, True, False)
        self.correction_xleft = -50    # 設定槍的位置
        self.correction_yleft = 40
        self.correction_xright = 20
        self.correction_yright = 40


class shotgun(Gun):
    def __init__(self):
        super().__init__(40, 8, 12, 30)
        self.gun_name = "shotgun"
        self.img1_right = pygame.image.load('./shotgun1.png')
        self.img2_right = pygame.image.load('./shotgun2.png')
        self.img1_left = pygame.transform.flip(self.img1_right, True, False)
        self.img2_left= pygame.transform.flip(self.img2_right, True, False)
        self.correction_xleft = -70       # 設定槍的位置    
        self.correction_yleft = 40
        self.correction_xright = 0
        self.correction_yright = 40

class sniper(Gun):
    def __init__(self):
        super().__init__(30, 12, 8, 100)
        self.gun_name = "sniper"
        self.img1_right = pygame.image.load('./sniper1.png')
        self.img2_right = pygame.image.load('./sniper2.png')
        self.img1_left = pygame.transform.flip(self.img1_right, True, False)
        self.img2_left = pygame.transform.flip(self.img2_right, True, False)
        self.correction_xleft = -80         # 設定槍的位置
        self.correction_yleft = 30
        self.correction_xright = 0
        self.correction_yright = 30



class GunImage(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = player.gun.img1_right
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.gun.correction_xleft
        self.rect.y = player.rect.y + player.gun.correction_yleft

    def update(self):
        direction = self.player.get_direction()
        playernumber = self.player.playernumber
        
        if direction in [-1, 1]:
            # 根據玩家面向的方向，設定槍的位置
            direction_str = 'left' if direction == -1 else 'right'
            correction_x = getattr(self.player.gun, f'correction_x{direction_str}')
            correction_y = getattr(self.player.gun, f'correction_y{direction_str}')
            
            if playernumber in [1, 2]:
                # 根據玩家的編號，設定槍的圖片
                image_attribute = f'img{playernumber}_{direction_str}'
                self.image = getattr(self.player.gun, image_attribute)
                self.rect.x = self.player.rect.x + correction_x
                self.rect.y = self.player.rect.y + correction_y

class Lagtime_Image(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.Surface([80, 12])
        self.image.fill((0,255,254))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.gun.correction_xleft
        self.rect.y = player.rect.y -35

    def update(self):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y -35
        if self.player.gunlag >= 0 and (self.player.gun.gun_name == "shotgun" or self.player.gun.gun_name == "sniper"):
            self.image = pygame.Surface([80*(self.player.gunlag/self.player.gun.lagtime), 12])
            self.image.fill((0,255,254))
            self.rect = self.image.get_rect()
            self.rect.x = self.player.rect.x
            self.rect.y = self.player.rect.y -35
        if self.player.gun.gun_name == "smallgun":
            self.rect.x = self.player.rect.x
            self.rect.y = self.player.rect.y + 5000

class Lagtime_back_Image(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.Surface([80, 12])
        self.image.fill((60,60,60))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.gun.correction_xleft
        self.rect.y = player.rect.y -35


    def update(self):
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y -35
        if self.player.gunlag >= 0 and (self.player.gun.gun_name == "shotgun" or self.player.gun.gun_name == "sniper"):
            self.image = pygame.Surface([80, 12])
            self.image.fill((60,60,60))
        else:
            self.image = pygame.Surface([80, 0])
            self.image.fill((60,60,60))
            self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y -35

        if self.player.gun.gun_name == "smallgun":
            self.rect.x = self.player.rect.x
            self.rect.y = self.player.rect.y +50000

# 建立子彈類別
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, x, y, direction, which_gun, which_player):
        super().__init__()
        self.image = pygame.Surface([15, 5])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x + 50*direction, y)
        self.direction = direction
        self.leave = False
        self.out_check = False
        self.strgun = which_gun
        if which_gun == "smallgun":
            gun = Gun(5, 8, 100000, 5)
        if which_gun == "shotgun":
            gun = Gun(15, 15, 12, 30)
        if which_gun == "sniper":
            gun = Gun(15, 30, 8, 60)
        self.speed = gun.speed * direction
        self.gun = gun
        self.creation_time = time.time()
        self.numplayer = which_player
        self.count = 10

    def which_player(self):
        return self.numplayer

    def turn_check(self):
        self.leave = True

    def fire(self):
        self.lag = self.gun.lagtime

    def leave_check(self):
        return self.leave

    def update(self):
        elapsed_time = time.time() - self.creation_time
        acceleration = 0.001
        
        self.count -= 1
        if self.strgun == "shotgun":
            if self.count <= 0:
                self.kill()
        if self.speed == 0:
            return True
        elif self.speed > 0:
            self.speed -= acceleration*elapsed_time
        elif self.speed < 0:
            self.speed += acceleration*elapsed_time
            
        self.rect.x += self.speed
        if self.rect.left > WINDOW_WIDTH + 100 or self.rect.right < -100:
            self.out_check = True
        return False

    def out(self):
        return self.out_check
    
# 建立炸彈類別
class Bomb(pygame.sprite.Sprite, Physics):
    def __init__(self, x, y, img, direction):
        super().__init__()
        Physics.__init__(self, x, y, img)
        self.rect.centerx = x
        self.speed_x = 10 * direction
        self.dir = direction
        self.time_countdown = 120
        self.fixed = 0

    def update(self): # 繼承update
        Physics.update(self)
        self.time_countdown -= 1
        
        if self.on_ground == True:
            if self.fixed == 0:
                self.fixed_x = self.rect.x
                self.fixed_y = self.rect.y
                self.fixed = 1
            self.speed_x = 0
            if self.time_countdown % 30 < 5:
                self.image = pygame.transform.scale(self.image, (60, 60))
                self.rect.x = self.fixed_x - 7.5
                self.rect.y = self.fixed_y - 7.5
            else:
                self.image = pygame.transform.scale(self.image, (45, 45))
                self.rect.x = self.fixed_x
                self.rect.y = self.fixed_y
        
        
    def countdown(self): # 炸彈倒數計時
        if self.time_countdown == 0:
            return True

    def check_ground(self): # 繼承check_ground
        super().check_ground()

    def force(self, x1, y1, player, F):
        player.speed_x += F * (player.rect.centerx - x1) / self.D
        if (player.rect.centery - y1) < 0:
            if F * (player.rect.centery - y1) / self.D <- 30:
                player.speed_y += -30
            else:
                player.speed_y += F * (player.rect.centery - y1) / self.D

    def explosion(self, player): # 爆炸
        self.D = distance_2D(self.rect.centerx, self.rect.centery, player.rect.centerx, player.rect.centery)
        if self.D < 60:
            self.force(self.rect.centerx, self.rect.centery, player, 80)
        elif self.D < 200:
            self.force(self.rect.centerx, self.rect.centery, player, 288000/math.pow(self.D, 2))

class Bomb_effect(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = x - 135
        self.rect.y = y - 180
        self.countdown = 25

    def Countdown(self):
        self.countdown -= 1
        if self.countdown == 0:
            return True
        else:
            return False

#寶箱掉落
class TreasureBox(pygame.sprite.Sprite, Physics):
    def __init__(self, x, y, box_images):
        super().__init__()
        self.image = box_images
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.guns =  ["shotgun", "sniper"]  # 槍的圖片列表
        self.speed_x = 0  # 寶箱水平速度
        self.speed_y = 0 # 寶箱下落速度

    def open_box(self):
        # 隨機獲得一把槍
        return random.choice(self.guns)
    
    def update(self):
        Physics.update(self)

# 執行遊戲
if __name__ == "__main__":
    game = Game()
    game.run()
