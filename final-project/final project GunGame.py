5/15
import pygame
import sys
import math


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
GROUND_LEVELS = [310, 410, 525, 615]  # 示例地板高度，可以根据实际情况修改

def distance_2D(x1, y1, x2, y2):
    return math.pow(math.pow(abs(x2-x1), 2) + math.pow(abs(y1-y2), 2), 0.5)

# 建立遊戲場景類別
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("GunGame")
        self.clock = pygame.time.Clock()
        self.background_img = pygame.image.load('./oop-python-nycu/final-project/background.jpg') # 載入背景圖片
        self.player1_img = pygame.image.load('./oop-python-nycu/final-project/player_1.png') # 載入玩家圖片
        self.player2_img = pygame.image.load('./oop-python-nycu/final-project/player_2.png') # 載入玩家圖片
        self.bomb_img = pygame.image.load('./oop-python-nycu/final-project/bomb.png') # 載入炸彈圖片
        self.bomb_effect_img = pygame.image.load('./oop-python-nycu/final-project/bomb_effect.png') # 載入爆炸特效
        self.player1 = Player(RELIVE_X[0] , RELIVE_Y, self.player1_img)
        self.player2 = Player(RELIVE_X[1] , RELIVE_Y, self.player2_img)
        self.player2.turn_img("left")
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.bomb_effects = pygame.sprite.Group()
        self.all_sprites.add(self.player1, self.player2)
        self.font = pygame.font.Font(None, FONT)
        
    def run(self):
        running = True
        self.player1_press_jump = 0
        self.player2_press_jump = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
            if mkeys[pygame.K_SPACE]:
                self.fire_bullet(self.player1, "up")
            if mkeys[pygame.K_RETURN]:
                self.fire_bullet(self.player2, "up")
            if mkeys[pygame.K_b]:
                if bomb_press_check1 == 0:
                    self.drop_bomb(self.player1, self.bomb_img)
                bomb_press_check1 = 1
            else :
                bomb_press_check1 = 0
            if mkeys[pygame.K_l]:
                if bomb_press_check2 == 0:
                    self.drop_bomb(self.player2, self.bomb_img)
                bomb_press_check2 = 1
            else :
                bomb_press_check2 = 0

            self.all_sprites.update()
            self.bullets.update()
            self.bombs.update()
            
            # 碰撞檢測
            for bullet in self.bullets:
                if pygame.sprite.spritecollideany(bullet, self.all_sprites):
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

            text = self.font.render(str(self.player1.get_value("x")), True, (255, 255, 255)) #輸出左上角的字（用來測試）
            self.screen.blit(self.background_img, (0, 0))  # 绘制背景图像
            self.bomb_effects.draw(self.screen)
            self.all_sprites.draw(self.screen)
            self.bullets.draw(self.screen)
            self.bombs.draw(self.screen)
            self.screen.blit(text,(10,10))
            pygame.display.flip()

            self.clock.tick(60)

            #玩家重生
            if self.player1.rect.top > WINDOW_HEIGHT:
                self.player1.relive(0)
            if self.player2.rect.top > WINDOW_HEIGHT:
                self.player2.relive(1)

    # 發射子彈
    def fire_bullet(self, player, direction):
        bullet = Bullet(BLACK, player.rect.centerx, player.rect.centery, direction)
        self.bullets.add(bullet)

    def drop_bomb(self, player, img):
        bomb = Bomb(player.rect.centerx, player.rect.centery - 65, img, player.get_direction())
        self.bombs.add(bomb)

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

            # 限制在窗口內
            # if self.rect.left < 0:
            #     self.rect.left = 0
            # elif self.rect.right > WINDOW_WIDTH:
            #     self.rect.right = WINDOW_WIDTH
        
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
                self.speed_y = 0
                self.rect.bottom = closest_ground
            elif self.speed_y >= 0 and min_distance < self.speed_y:
                self.on_ground = True
                self.speed_y = 0
                self.rect.bottom = closest_ground

    # 建立玩家類別
class Player(pygame.sprite.Sprite, Physics):
    def __init__(self, x, y, img):
        super().__init__()
        Physics.__init__(self, x, y, img)
        self.right_img = img
        self.left_img = pygame.transform.flip(img, True, False)
        self.on_ground = True
        self.ground_level = None  #玩家所在的地板高度

    def get_value(self, sub): # 拿來取要的值
        if sub == "x":
            return self.rect.x
        if sub == "y":
            return self.rect.y
        if sub == "bottom":
            return self.rect.bottom
    
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

    def relive(self, num):
        #玩家復活
        self.rect.x = RELIVE_X[num]
        self.rect.y = RELIVE_Y
        self.on_ground = True
        self.speed_x = 0
        self.speed_y = 0

# 建立子彈類別
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, x, y, direction):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

# 建立炸彈類別
class Bomb(pygame.sprite.Sprite, Physics):
    def __init__(self, x, y, img, direction):
        super().__init__()
        Physics.__init__(self, x, y, img)
        self.rect.centerx = x
        self.speed_x = 10 * direction
        self.dir = direction
        self.time_countdown = 150

    def update(self): # 繼承update
        Physics.update(self)
        self.time_countdown -= 1
        if self.on_ground == True:
            self.speed_x = 0
        else:
            self.image = pygame.transform.rotate(self.image, 2*self.dir)
        
    def countdown(self): # 炸彈倒數計時
        if self.time_countdown == 0:
            return True

    def check_ground(self): # 繼承check_ground
        super().check_ground()

    def force(self, x1, y1, player, F):
        player.speed_x += F * (player.rect.centerx - x1) / self.D
        if (player.rect.centery - y1) > 0:
            player.speed_y += F * (player.rect.centery - y1) / self.D

    def explosion(self, player): # 爆炸
        self.D = distance_2D(self.rect.centerx, self.rect.centery, player.rect.centerx, player.rect.centery)
        if self.D < 60:
            self.force(self.rect.centerx, self.rect.centery, player, 100)
        elif self.D < 200:
            self.force(self.rect.centerx, self.rect.centery, player, 360000/math.pow(self.D, 2))

class Bomb_effect(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x = x - 135
        self.rect.y = y - 190
        self.countdown = 10

    def Countdown(self):
        self.countdown -= 1
        if self.countdown == 0:
            return True
        else:
            return False


# 執行遊戲
if __name__ == "__main__":
    game = Game()
    game.run()
