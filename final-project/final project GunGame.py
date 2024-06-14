
import pygame
import sys
import math
import time
import random
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
    
    initial_screen = pygame.image.load('./oop-python-nycu/final-project/initial.png')  # 載入背景圖片
    intro_img = pygame.image.load('./oop-python-nycu/final-project/intro.png')  
    player1_img = pygame.image.load('./oop-python-nycu/final-project/player_1.png') # 載入玩家圖片
    player2_img = pygame.image.load('./oop-python-nycu/final-project/player_2.png') # 載入玩家圖片
    player1_img = pygame.transform.scale(player1_img, (160, 220))
    player2_img = pygame.transform.scale(player2_img, (160, 220))
    
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
    while state < 2:
        screen.fill((0, 0, 0))  # 清除屏幕
        screen.blit(initial_screen, (pos_x, pos_y))  # 確保背景圖片始終顯示
        counttime += 1
        if state == 0:
            if counttime <= 50:
                draw_text(screen, "<Tap Any Bottom To Start>", 50, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 200)

        elif state == 1:
            screen.blit(intro_img, (pos_x, pos_y))
            if counttime <= 50:
                screen.blit(player1_img, (WINDOW_WIDTH / 2-250, WINDOW_HEIGHT / 2 + 20-100))
                screen.blit(player2_img, (WINDOW_WIDTH / 2+300, WINDOW_HEIGHT / 2 + 20-100))
            else:
                screen.blit(player1_img, (WINDOW_WIDTH / 2-250, WINDOW_HEIGHT / 2-100))
                screen.blit(player2_img, (WINDOW_WIDTH / 2+300, WINDOW_HEIGHT / 2-100))
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
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    initial_screen = pygame.image.load('./oop-python-nycu/final-project/initial.png')  # 載入背景圖片
    tips = pygame.image.load('./oop-python-nycu/final-project/tap_any_bottom.png')  # 載入提示圖片
    
    
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

    #按兩下結束函數
    state = 0  # 0: 顯示標題, 1: 顯示說明, 2: 開始遊戲
    counttime = 0
    while state < 1:
        screen.fill((0, 0, 0))  # 清除屏幕
        screen.blit(initial_screen, (pos_x, pos_y))  # 確保背景圖片始終顯示
        
        if state == 0:
            if who_win == 1:
                draw_text(screen, "Player 1 Win", 50, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100)
            elif who_win == 2:
                draw_text(screen, "Player 2 Win", 50, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 100)

        elif state == 1:
            
            counttime += 1 
            if counttime <= 50:
                draw_text(screen, "<Tap Any Bottom To Start>", 50, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 200)
            elif counttime > 100:
                counttime = 0
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                state += 1

# 建立遊戲場景類別
class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("GunGame")
        self.clock = pygame.time.Clock()
        self.background_img = pygame.image.load('./oop-python-nycu/final-project/background.jpg') # 載入背景圖片
        self.initial_img = pygame.image.load('./oop-python-nycu/final-project/initial.png') # 載入初始畫面
        self.tap_img = pygame.image.load('./oop-python-nycu/final-project/tap_any_bottom.png') # 載入提示
        self.player1_img = pygame.image.load('./oop-python-nycu/final-project/player_1.png') # 載入玩家圖片
        self.player2_img = pygame.image.load('./oop-python-nycu/final-project/player_2.png') # 載入玩家圖片
        self.bomb_img = pygame.image.load('./oop-python-nycu/final-project/bomb.png') # 載入炸彈圖片
        self.bomb_effect_img = pygame.image.load('./oop-python-nycu/final-project/bomb_effect.png') # 載入爆炸特效
        self.smallgun1_img = pygame.image.load('./oop-python-nycu/final-project/smallgun1.png') # 載入小槍圖片
        self.smallgun2_img = pygame.image.load('./oop-python-nycu/final-project/smallgun2.png')
        self.shotgun1_img = pygame.image.load('./oop-python-nycu/final-project/shotgun1.png')
        self.shotgun2_img = pygame.image.load('./oop-python-nycu/final-project/shotgun2.png')
        self.sniper1_img = pygame.image.load('./oop-python-nycu/final-project/sniper1.png')
        self.sniper2_img = pygame.image.load('./oop-python-nycu/final-project/sniper2.png')
        self.box_img = pygame.image.load('./oop-python-nycu/final-project/box.png')
        self.heart_img = pygame.transform.scale(pygame.image.load('./oop-python-nycu/final-project/heart.png'), (40, 40))
        self.player1 = Player(RELIVE_X[0] , RELIVE_Y, self.player1_img, 1)
        self.player2 = Player(RELIVE_X[1] , RELIVE_Y, self.player2_img, 2)
        self.player2.turn_img("left")
        self.player1_draw = pygame.sprite.Group()
        self.player2_draw = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.bomb_effects = pygame.sprite.Group()
        self.font = pygame.font.Font(None, FONT)
        #self.font = pygame.font.SysFont('Arial', 60)
        self.treasure_boxes = pygame.sprite.Group() 
        self.gun_images1 = GunImage(self.player1)
        self.gun_images2 = GunImage(self.player2)
        self.player1_draw.add(self.player1, self.gun_images1)
        self.player2_draw.add(self.player2, self.gun_images2)
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
                draw_end(2)
                self.player1.restart(0)
                self.player2.restart(1)
                draw_init()
                #按下任意鍵回到開始畫面

            if self.player2.live == 0 and show_end_screen:
                draw_end(1)
                self.player1.restart(0)
                self.player2.restart(1)
                draw_init()
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

                if self.player1.realgun.numofbullet <= 0: # 子彈數量用完換成小槍
                    self.player1.realgun = smallgun() 
                    self.player1.realgun.gun_name = "smallgun"
                fire1_press_check = 1

            else :
                fire1_press_check = 0
            if mkeys[pygame.K_k]:
                if fire2_press_check == 0:
                    self.fire_bullet(self.player2, self.player2.get_direction(), YELLOW, self.player2.now_gun(), 2)
                fire2_press_check = 1
                if self.player2.realgun.numofbullet <= 0:
                    self.player2.realgun = smallgun()
                    self.player2.realgun.gun_name = "smallgun"
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
                        self.player1 .speed_x +=  3 * bullet.speed
                        bullet.kill()
                    if bullet.rect.colliderect(self.player2.rect):
                        self.player2.speed_x += 3 * bullet.speed
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
                    self.player1.change_gun(gun_name)
                    treasure_box.kill()
                    self.box_check = 0
                if pygame.sprite.collide_rect(self.player2, treasure_box):
                    gun_name = treasure_box.open_box()
                    self.player2.change_gun(gun_name)
                    treasure_box.kill()
                    self.box_check = 0
                if treasure_box.rect.top > WINDOW_HEIGHT:
                    treasure_box.kill()
                    self.box_check = 0

            text_smallgun1_numofbullete = self.font.render("∞", True, (255, 255, 255)) #輸出左上角的字
            text_smallgun2_numofbullete = self.font.render("∞", True, (255, 255, 255)) 
            text_player1_ammo = self.font.render(str(self.player1.realgun.numofbullet), True, (255, 255, 255)) 
            text_player2_ammo = self.font.render(str(self.player2.realgun.numofbullet), True, (255, 255, 255))
            self.screen.blit(self.background_img, (0, 0))  #    背景圖片
            self.bomb_effects.draw(self.screen)
            self.bullets.draw(self.screen)
            self.player1_draw.draw(self.screen)
            self.player2_draw.draw(self.screen)
            self.bombs.draw(self.screen)
            self.draw_object(self.player1, self.player2)
            if self.player1.realgun.gun_name == "smallgun":
                self.font = pygame.font.SysFont('Arial', 60)
                self.screen.blit(text_smallgun1_numofbullete,(10,100))
            else:
                self.font = pygame.font.Font(None, FONT)
                self.screen.blit(text_player1_ammo,(10,100))

            if self.player2.realgun.gun_name == "smallgun":
                self.font = pygame.font.SysFont('Arial', 60)
                self.screen.blit(text_smallgun2_numofbullete,(WINDOW_WIDTH - 160,100))
            else:
                self.font = pygame.font.Font(None, FONT) 
                self.screen.blit(text_player2_ammo,(WINDOW_WIDTH - 120,100))
        

            pygame.display.flip()

            self.clock.tick(60)

            #玩家重生
            if self.player1.rect.top > WINDOW_HEIGHT:
                self.player1.relive(0)
            if self.player2.rect.top > WINDOW_HEIGHT:
                self.player2.relive(1)
            
            #顯示玩家一的子彈數量
            text_bullet1 = self.font.render(str(self.player1.realgun.numofbullet), True, (255, 255, 255))
            self.screen.blit(text_bullet1, (10, 10))

    # 發射子彈
    def fire_bullet(self, player, direction, color, gun_name, which_player):
        if player.get_value("gunlag") <= 0:
            bullet = Bullet(color, player.rect.centerx, player.rect.centery, direction, gun_name, which_player)
            self.bullets.add(bullet)
            player.change_gunlag(gun_name)
            gun_name = player.now_gun()
            if gun_name == "smallgun":
                player.speed_x -= 1 * direction
            elif gun_name == "shotgun" :
                player.speed_x -= 4 * direction
            elif gun_name == "sniper" :
                player.speed_x -= 8 * direction
            player.realgun.numofbullet -= 1
            

    def drop_bomb(self, player, img):
        bomb = Bomb(player.rect.centerx, player.rect.centery - 65, img, player.get_direction())
        self.bombs.add(bomb)


    def draw_object(self, player1, player2):
        for i in range(player1.live):
            self.screen.blit(self.heart_img, (10 + 45 * i, 10))
        for i in range(player2.live):
            self.screen.blit(self.heart_img, (WINDOW_WIDTH - 45 * (i + 1), 10))
        for i in range(player1.bomb_num):
            self.screen.blit(pygame.transform.scale(self.bomb_img, [35,35]), (10 + 45 * i, 50))
        for i in range(player2.bomb_num):
            self.screen.blit(pygame.transform.scale(self.bomb_img, [35,35]), (WINDOW_WIDTH - 45 * (i + 1), 50))

class Physics(object):
        def __init__(self, x, y, img):
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed_x = 0
            self.speed_y = 0
            self.on_ground = False
        
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
        self.live = 3
        self.realgun = smallgun()
                
    def change_gunlag(self, gun_name):
        if gun_name == "smallgun":
            self.gunlag = 5
        elif gun_name == "shotgun":
            self.gunlag = 30
        elif gun_name == "sniper":
            self.gunlag = 60

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
            self.on_ground = False
        elif self.double_jump == 1 and check == 0: # 二段跳
            self.speed_y = -10
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
        self.realgun = smallgun()
        self.live -= 1

    def restart(self, num):
        self.rect.x = RELIVE_X[num]
        self.rect.y = RELIVE_Y
        self.on_ground = True
        self.speed_x = 0
        self.speed_y = 0
        self.bomb_num = 3
        self.realgun = smallgun()
        self.live = 3

    def change_gun(self, gun_name):
        #self.gun = gun
        if gun_name == "smallgun":
            self.realgun = smallgun()
        elif gun_name == "shotgun":
            self.realgun = shotgun()
        elif gun_name == "sniper":
            self.realgun = sniper()


    def now_gun(self):
        return self.realgun.gun_name
        

# 建立槍類別
class Gun():
    def __init__(self, speed, recoil, numofbullet, lagtime):
        self.speed = speed
        self.recoil = recoil
        self.numofbullet = numofbullet
        self.lagtime = lagtime
        

class smallgun(Gun):
    def __init__(self):
        super().__init__(5, 8, 100000, 5)
        self.gun_name = "smallgun"
        self.smallgun_img1 = pygame.image.load('./oop-python-nycu/final-project/smallgun1.png')
        self.smallgun_img2 = pygame.image.load('./oop-python-nycu/final-project/smallgun2.png')
        self.smallgun_img1_turn = pygame.transform.flip(self.smallgun_img1, True, False)
        self.smallgun_img2_turn = pygame.transform.flip(self.smallgun_img2, True, False)


class shotgun(Gun):
    def __init__(self):
        super().__init__(15, 15, 12, 30)
        self.gun_name = "shotgun"
        self.shotgun_img1 = pygame.image.load('./oop-python-nycu/final-project/shotgun1.png')
        self.shotgun_img2 = pygame.image.load('./oop-python-nycu/final-project/shotgun2.png')
        self.shotgun_img1_turn = pygame.transform.flip(self.shotgun_img1, True, False)
        self.shotgun_img2_turn= pygame.transform.flip(self.shotgun_img2, True, False)


class sniper(Gun):
    def __init__(self):
        super().__init__(15, 30, 8, 60)
        self.gun_name = "sniper"
        self.sniper_img1 = pygame.image.load('./oop-python-nycu/final-project/sniper1.png')
        self.sniper_img2 = pygame.image.load('./oop-python-nycu/final-project/sniper2.png')
        self.sniper_img1_turn = pygame.transform.flip(self.sniper_img1, True, False)
        self.sniper_img2_turn = pygame.transform.flip(self.sniper_img2, True, False)




class GunImage(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        
        if self.player.playernumber == 1:
            self.image = self.player.realgun.smallgun_img1
        elif self.player.playernumber == 2:
            self.image = self.player.realgun.smallgun_img2
        self.rect = self.image.get_rect()
        

        self.rect.x = player.rect.x 
        self.rect.y = player.rect.y + 30
        
    def update(self):
        if self.player.get_direction() == -1:  # 玩家面向左
            if self.player.playernumber == 1:
                if self.player.now_gun() == "smallgun":
                    self.image = self.player.realgun.smallgun_img1_turn
                    self.rect.centerx = self.player.rect.centerx + 40*self.player.get_direction()
                    self.rect.y = self.player.rect.y + 40

                elif self.player.now_gun() == "shotgun":
                    self.image = self.player.realgun.shotgun_img1_turn
                    self.rect.x = self.player.rect.x - 70
                    self.rect.y = self.player.rect.y + 40

                elif self.player.now_gun() == "sniper":
                    self.image = self.player.realgun.sniper_img1_turn
                    self.rect.x = self.player.rect.x - 80
                    self.rect.y = self.player.rect.y + 30

            elif self.player.playernumber == 2:
                if self.player.now_gun() == "smallgun":
                    self.image = self.player.realgun.smallgun_img2_turn
                    self.rect.x = self.player.rect.x - 50
                    self.rect.y = self.player.rect.y + 40

                elif self.player.now_gun() == "shotgun":
                    self.image = self.player.realgun.shotgun_img2_turn
                    self.rect.x = self.player.rect.x - 70
                    self.rect.y = self.player.rect.y + 40

                elif self.player.now_gun() == "sniper":
                    self.image = self.player.realgun.sniper_img2_turn
                    self.rect.x = self.player.rect.x - 80
                    self.rect.y = self.player.rect.y + 30

        elif self.player.get_direction() == 1: # 玩家面向右
            if self.player.playernumber == 1:
                if self.player.now_gun() == "smallgun":
                    self.image = self.player.realgun.smallgun_img1
                    self.rect.centerx = self.player.rect.centerx + 40
                    self.rect.y = self.player.rect.y + 40

                elif self.player.now_gun() == "shotgun":
                    self.image = self.player.realgun.shotgun_img1
                    self.rect.x = self.player.rect.x 
                    self.rect.y = self.player.rect.y + 40

                elif self.player.now_gun() == "sniper":
                    self.image = self.player.realgun.sniper_img1
                    self.rect.x = self.player.rect.x
                    self.rect.y = self.player.rect.y + 30

            elif self.player.playernumber == 2:
                if self.player.now_gun() == "smallgun":
                    self.image = self.player.realgun.smallgun_img2
                    self.rect.x = self.player.rect.x + 20
                    self.rect.y = self.player.rect.y + 40

                elif self.player.now_gun() == "shotgun":
                    self.image = self.player.realgun.shotgun_img2
                    self.rect.x = self.player.rect.x
                    self.rect.y = self.player.rect.y + 40

                elif self.player.now_gun() == "sniper":
                    self.image = self.player.realgun.sniper_img2
                    self.rect.x = self.player.rect.x 
                    self.rect.y = self.player.rect.y + 30

                    #123666456

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
        
        #self.gun.numofbullet -= 1
        #if self.gun.numofbullet <= 0: # 子彈數量用完換成小槍
        
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