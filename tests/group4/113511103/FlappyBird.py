import pygame
import random
import sys

# --- 初始化 ---
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)

# --- 顏色設定 ---
WHITE = (255, 255, 255)
SKY = (135, 206, 250)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# --- 玩家參數 ---
bird_x = 80
bird_y = HEIGHT // 2
bird_radius = 20
bird_velocity = 0
gravity = 0.5
jump_power = -8

# --- 水管參數 ---
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
pipe_interval = 1500  # 毫秒
last_pipe_time = pygame.time.get_ticks()
pipes = []

# --- 分數 ---
score = 0
game_over = False

# --- 輔助函式 ---
def draw_bird():
    pygame.draw.circle(screen, YELLOW, (bird_x, int(bird_y)), bird_radius)

def create_pipe():
    gap_y = random.randint(100, HEIGHT - 100 - pipe_gap)
    top_rect = pygame.Rect(WIDTH, 0, pipe_width, gap_y)
    bottom_rect = pygame.Rect(WIDTH, gap_y + pipe_gap, pipe_width, HEIGHT - (gap_y + pipe_gap))
    return (top_rect, bottom_rect)

def move_pipes():
    for pair in pipes:
        pair[0].x -= pipe_speed
        pair[1].x -= pipe_speed

def draw_pipes():
    for top, bottom in pipes:
        pygame.draw.rect(screen, GREEN, top)
        pygame.draw.rect(screen, GREEN, bottom)

def check_collision():
    bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius*2, bird_radius*2)
    for top, bottom in pipes:
        if bird_rect.colliderect(top) or bird_rect.colliderect(bottom):
            return True
    if bird_y + bird_radius >= HEIGHT or bird_y - bird_radius <= 0:
        return True
    return False

# --- 主迴圈 ---
running = True
while running:
    dt = clock.tick(60)
    screen.fill(SKY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_power

    if not game_over:
        # 重力 + 位置更新
        bird_velocity += gravity
        bird_y += bird_velocity

        # 新增水管
        current_time = pygame.time.get_ticks()
        if current_time - last_pipe_time > pipe_interval:
            pipes.append(create_pipe())
            last_pipe_time = current_time

        # 移動水管
        move_pipes()

        # 清除畫面外水管，並加分
        new_pipes = []
        for pair in pipes:
            if pair[0].x + pipe_width < bird_x and "passed" not in pair:
                score += 1
                pair += ("passed",)  # 加一個標記避免重複加分
            if pair[0].x + pipe_width > 0:
                new_pipes.append(pair)
        pipes = new_pipes

        # 碰撞偵測
        if check_collision():
            game_over = True

    # 畫東西
    draw_bird()
    draw_pipes()
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("Game Over", True, RED)
        screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 30))

    pygame.display.flip()

pygame.quit()
sys.exit()