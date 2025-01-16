import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#載入圖片
background = pygame.image.load("background.png")
player_img = pygame.image.load("player.png")
rock_img = pygame.image.load("rock.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__() # call sprite的初始函式
        self.image = player_img
        self.rect = self.image.get_rect() # 屬性二: rect
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
        # Keep the player within the screen bounds using if-else statements
        if self.rect.left < 0:
            self.rect.left = 0
        else:
            if self.rect.right > screen.get_width():
                self.rect.right = screen.get_width()
        if self.rect.top < 0:
            self.rect.top = 0
        else:
            if self.rect.bottom > screen.get_height():
                self.rect.bottom = screen.get_height()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super(Rock, self).__init__()
        self.image = rock_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = -self.rect.height  # Generate from the top of the screen
        self.speedy = random.randint(1, 5)
        self.speedx = random.randint(-2, 2)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # 超出边界后重新定位 Rock
        if self.rect.top > screen.get_height() or self.rect.left > screen.get_width() or self.rect.right < 0:
            self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
            self.rect.y = -self.rect.height
            self.speedy = random.randint(1, 5)
            self.speedx = random.randint(-2, 2)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y  # 子弹产生的位置是在火箭的上方
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # 子弹超出屏幕后销毁
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
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
                player.shoot()

    # 更新遊戲
    all_sprites.update() # 執行所有的sprite中update函式

    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits:
        # Create a new rock for each one destroyed
        new_rock = Rock()
        all_sprites.add(new_rock)
        rocks.add(new_rock)

    # Collision detection between rocks and player
    hits = pygame.sprite.spritecollide(player, rocks, False)
    if hits:
        running = False  # End game if player collides with a rock

    # 畫面顯示
    screen.blit(background, (0, 0))
    all_sprites.draw(screen) # 畫出所有的sprite
    pygame.display.flip()

pygame.quit()