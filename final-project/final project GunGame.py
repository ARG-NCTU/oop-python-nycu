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
PLAYER_SPEED = 5
JUMP_HEIGHT = 14  # 跳躍高度適中
RELIVE_X  = 900 
RELIVE_Y = 0
# 地板位置列表
GROUND_LEVELS = [310, 410, 525, 615]  # 示例地板高度，可以根据实际情况修改


# 建立遊戲場景類別
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("GunGame")
        self.clock = pygame.time.Clock()
        self.background_img = pygame.image.load('./oop-python-nycu/final-project/background.jpg') # 載入背景圖片
        self.player1_img = pygame.image.load('./oop-python-nycu/final-project/player_1.png') # 載入玩家圖片
        self.player2_img = pygame.image.load('./oop-python-nycu/final-project/player_2.png') # 載入玩家圖片
        self.player1 = Player(RELIVE_X , RELIVE_Y, self.player1_img)
        self.player2 = Player(RELIVE_X , RELIVE_Y, self.player2_img)
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.all_sprites.add(self.player1, self.player2)
        self.font = pygame.font.Font(None, FONT)
        
        
        

    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            mkeys = pygame.key.get_pressed()
            if mkeys [pygame.QUIT]:
                running = False
            if mkeys [pygame.K_w]:
                self.player1.jump()
            elif mkeys [pygame.K_UP]:
                self.player2.jump()
            elif mkeys [pygame.K_s]:
                self.player1.move_down()
            elif mkeys [pygame.K_DOWN]:
                self.player2.move_down()
            elif mkeys[pygame.K_a]:
                self.player1.speed_x = -PLAYER_SPEED
                self.player1.turn_img("left")
            elif mkeys[pygame.K_d]:
                self.player1.speed_x = PLAYER_SPEED
                self.player1.turn_img("right")
            elif mkeys[pygame.K_LEFT]:
                self.player2.speed_x = -PLAYER_SPEED
                self.player2.turn_img("left")
            elif mkeys[pygame.K_RIGHT]:
                self.player2.speed_x = PLAYER_SPEED
                self.player2.turn_img("right")
            elif mkeys[pygame.K_SPACE]:
                self.fire_bullet(self.player1, "up")
            elif mkeys[pygame.K_RETURN]:
                self.fire_bullet(self.player2, "up")
            
            #讓角色滑行
            self.player1.speed_x = self.player1.speed_x * 0.93
            self.player2.speed_x = self.player2.speed_x * 0.93

            self.all_sprites.update()
            self.bullets.update()
            
            # 碰撞檢測
            for bullet in self.bullets:
                if pygame.sprite.spritecollideany(bullet, self.all_sprites):
                    bullet.kill()

            text = self.font.render(str(self.player1.print_x()), True, (255, 255, 255))
            self.screen.blit(self.background_img, (0, 0))  # 绘制背景图像
            self.all_sprites.draw(self.screen)
            self.bullets.draw(self.screen)
            self.screen.blit(text,(10,10))
            pygame.display.flip()

            self.clock.tick(60)

            #玩家重生
            if self.player1.rect.top > WINDOW_HEIGHT:
                self.player1.relive()
            if self.player2.rect.top > WINDOW_HEIGHT:
                self.player2.relive()

    # 發射子彈
    def fire_bullet(self, player, direction):
        bullet = Bullet(BLACK, player.rect.centerx, player.rect.centery, direction)
        self.bullets.add(bullet)
    
    # 建立玩家類別
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.left_img = img
        self.right_img = pygame.transform.flip(img, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.on_ground = True
        self.ground_level = None  #玩家所在的地板高度

    def print_x(self):
        return self.rect.bottom
    
    def on_ground(self):
        return self.on_ground

    def turn_img(self, direction):
        if direction == "left":
            self.image = self.right_img
        elif direction == "right":
            self.image = self.left_img
    def update(self):
        # 應用重力
        self.speed_y += GRAVITY

        # 移動
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 檢查是否在地板上
        self.check_ground()

        # 限制在窗口內
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def jump(self):
        if self.on_ground:  # 只有在地面上才能跳
            self.speed_y = -JUMP_HEIGHT
            self.on_ground = False

    def move_down(self):
        # 玩家要在地板上才能往下移動
        if self.on_ground:
            if not((self.rect.bottom == GROUND_LEVELS[2] and ((self.rect.x > 90 and self.rect.x < 360) or (self.rect.x > 890 and self.rect.x < 1160))) or (self.rect.bottom == GROUND_LEVELS[3] and (self.rect.x > 325 and self.rect.x < 940))):
                self.rect.y += 15
                self.check_ground()

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

    def relive(self):
        #玩家復活
        self.rect.x = RELIVE_X
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

    def update(self):
        if self.direction == "up":
            self.rect.y -= PLAYER_SPEED

# 執行遊戲
if __name__ == "__main__":
    game = Game()
    game.run()
