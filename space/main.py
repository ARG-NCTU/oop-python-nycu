import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# 載入圖片
background = pygame.image.load("background.png")
player_img = pygame.image.load("player.png")
rock_img = pygame.image.load("rock.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.top = 550

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 500:
            self.rect.right = 500
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()
        self.image = rock_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 470)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(2, 8    )
        self.speedx = random.randint(-2, 2)

    def update(self):
        self.rect.y += self.speedy + random.randint(-5, 5) 
        self.rect.x += random.randint(-5, 5) + self.speedx
        if self.rect.top > 600:
            self.rect.x = random.randint(0, 470)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 0, 0))  # 填充紅色
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 建立一些石頭
for i in range(20):  # 可以根據需要調整石頭數量
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)

# 遊戲迴圈
running = True
while running:
    clock.tick(60)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 發射子彈
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
    
    # 更新遊戲
    all_sprites.update()

    # 檢測子彈和石頭的碰撞
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits:
        # 撞到後，重新生成一個石頭
        rock = Rock()
        all_sprites.add(rock)
        rocks.add(rock)

    # 畫面顯示
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    if pygame.sprite.spritecollide(player, rocks, False):
        running = False
pygame.quit()
