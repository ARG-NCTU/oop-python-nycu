import pygame
import sys

# 初始化pygame
pygame.init()

# 設定遊戲視窗大小
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("雙人射擊遊戲")

# 設定顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 定義角色類別
class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

# 處理遊戲邏輯
def main():
    player1 = Player(50, HEIGHT//2 - 25, 50, 50, WHITE)
    player2 = Player(WIDTH - 100, HEIGHT//2 - 25, 50, 50, WHITE)
    players = [player1, player2]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # 控制第一個玩家的移動
        if keys[pygame.K_w]:
            player1.y -= 5
        if keys[pygame.K_s]:
            player1.y += 5
        if keys[pygame.K_a]:
            player1.x -= 5
        if keys[pygame.K_d]:
            player1.x += 5

        # 控制第二個玩家的移動
        if keys[pygame.K_UP]:
            player2.y -= 5
        if keys[pygame.K_DOWN]:
            player2.y += 5
        if keys[pygame.K_LEFT]:
            player2.x -= 5
        if keys[pygame.K_RIGHT]:
            player2.x += 5

        # 確保角色在屏幕內移動
        for player in players:
            if player.x <= 0:
                player.x = 0
            if player.x >= WIDTH - player.width:
                player.x = WIDTH - player.width
            if player.y <= 0:
                player.y = 0
            if player.y >= HEIGHT - player.height:
                player.y = HEIGHT - player.height

        # 清除舊的畫面
        WIN.fill(BLACK)
        
        # 繪製角色
        for player in players:
            player.draw(WIN)

        # 更新畫面
        pygame.display.update()

        # 添加延遲以限制遊戲速度
        pygame.time.delay(30)

if __name__ == "__main__":
    main()
