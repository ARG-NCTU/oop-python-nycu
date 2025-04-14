import pygame
import random
import sys

# 遊戲參數
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_RADIUS = 20
LASER_WIDTH = 20
LASER_HEIGHT = 100
LASER_SPEED_BASE = 5

# 初始化
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laser Dodge!")
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

# 顏色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (100, 200, 255)

# 玩家設定
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# 雷射資料結構
lasers = []
spawn_timer = 0
score = 0
start_ticks = pygame.time.get_ticks()

def spawn_laser():
    side = random.choice(["left", "right"])
    y = random.randint(0, HEIGHT - LASER_HEIGHT)
    if side == "left":
        x = -LASER_WIDTH
        vx = LASER_SPEED_BASE + score // 5
    else:
        x = WIDTH
        vx = -(LASER_SPEED_BASE + score // 5)
    lasers.append(pygame.Rect(x, y, LASER_WIDTH, LASER_HEIGHT))
    return vx

laser_velocities = []

def draw_player():
    pygame.draw.circle(screen, BLUE, player_pos, PLAYER_RADIUS)

def draw_lasers():
    for laser in lasers:
        pygame.draw.rect(screen, RED, laser)

def move_lasers():
    for i in range(len(lasers)):
        lasers[i].x += laser_velocities[i]

def check_collision():
    player_rect = pygame.Rect(
        player_pos[0] - PLAYER_RADIUS,
        player_pos[1] - PLAYER_RADIUS,
        PLAYER_RADIUS * 2,
        PLAYER_RADIUS * 2
    )
    for laser in lasers:
        if player_rect.colliderect(laser):
            return True
    return False

def game_over():
    screen.fill(BLACK)
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# 遊戲主迴圈
while True:
    dt = clock.tick(FPS)
    screen.fill(BLACK)

    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 玩家移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] - PLAYER_RADIUS > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] + PLAYER_RADIUS < WIDTH:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] - PLAYER_RADIUS > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] + PLAYER_RADIUS < HEIGHT:
        player_pos[1] += player_speed

    # 雷射生成
    spawn_timer += 1
    if spawn_timer > max(20 - score // 5, 5):
        spawn_timer = 0
        vx = spawn_laser()
        laser_velocities.append(vx)

    move_lasers()

    # 刪除畫面外的雷射
    for i in reversed(range(len(lasers))):
        if lasers[i].x < -LASER_WIDTH or lasers[i].x > WIDTH + LASER_WIDTH:
            del lasers[i]
            del laser_velocities[i]

    # 碰撞偵測
    if check_collision():
        game_over()

    # 分數更新
    score = (pygame.time.get_ticks() - start_ticks) // 1000

    # 繪圖
    draw_player()
    draw_lasers()
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
