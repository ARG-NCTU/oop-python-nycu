import pygame
import random

# 初始化 pygame
pygame.init()

# 視窗大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("113511002 Breakout Game")

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (50, 200, 50)
COLORS = [WHITE, BLACK, RED, BLUE, GREEN]

# 遊戲參數
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 30
PADDLE_MAX_WIDTH = 1000
PADDLE_MIN_WIDTH = 10
BALL_RADIUS = 10
BRICK_WIDTH = 20
BRICK_HEIGHT = 10
ROWS = 8
COLS = 32
BASE_SPEED = 4
MIN_SPEED = 1
MAX_SPEED = 100

# 開始界面函數
def start_screen(final_score=None):
    global sync_paddle_and_ball
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    while True:
        screen.fill(BLACK)
        title_text = font.render("Breakout", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        if final_score is not None:
            score_text = small_font.render(f"Your score: {final_score}", True, WHITE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))
        sync_text = small_font.render(f"Sync ball and paddle: {'Yes' if sync_paddle_and_ball else 'No'} (press S to switch)", True, WHITE)
        screen.blit(sync_text, (WIDTH // 2 - sync_text.get_width() // 2, 300))
        start_text = small_font.render("Press ENTER to start the game", True, WHITE)
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 400))
        instructions = [
            "In-game controls:",
            "LEFT/RIGHT: Move paddle (if not synced)",
            "U/I: Increase/Decrease ball speed",
            "P/O: Increase/Decrease paddle size",
            "C: Change brick color",
            "B: Add new ball",
            "ESC: Quit to menu"
        ]
        y_offset = 450
        for line in instructions:
            instr_text = small_font.render(line, True, WHITE)
            screen.blit(instr_text, (WIDTH // 2 - instr_text.get_width() // 2, y_offset))
            y_offset += 30
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    sync_paddle_and_ball = not sync_paddle_and_ball
                elif event.key == pygame.K_RETURN:
                    return

# 結束畫面函數
def end_screen(status, final_score):
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    while True:
        screen.fill(BLACK)
        title_text = font.render(status, True, WHITE if status == "Victory" else RED)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))
        score_text = small_font.render(f"Your score: {final_score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 250))
        continue_text = small_font.render("Press ENTER to continue", True, WHITE)
        screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, 350))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# 遊戲選項
sync_paddle_and_ball = False
score = 0

# 主遊戲迴圈
while True:
    start_screen(final_score=score if 'score' in locals() else None)
    
    # 初始化遊戲狀態
    current_paddle_width = PADDLE_WIDTH
    paddle = pygame.Rect(WIDTH//2 - current_paddle_width//2, HEIGHT - 50, current_paddle_width, PADDLE_HEIGHT)
    balls = [pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS * 2, BALL_RADIUS * 2)]  # 改為球列表
    current_base_speed = BASE_SPEED
    ball_speeds = [(current_base_speed * random.choice((1, -1)), -current_base_speed)]  # 每個球的速度
    bricks = []
    for row in range(ROWS):
        for col in range(COLS):
            brick = pygame.Rect(col * (BRICK_WIDTH + 5), row * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append(brick)
    brick_color = random.choice(COLORS)
    score = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)
        
        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_u:  # Increase ball speed
                    old_speed = current_base_speed
                    current_base_speed = min(current_base_speed + 1, MAX_SPEED)
                    if old_speed != 0:
                        for i in range(len(ball_speeds)):
                            ball_speeds[i] = (ball_speeds[i][0] * (current_base_speed / old_speed), 
                                            (1 if ball_speeds[i][1] > 0 else -1) * current_base_speed)
                elif event.key == pygame.K_i:  # Decrease ball speed
                    old_speed = current_base_speed
                    current_base_speed = max(current_base_speed - 1, MIN_SPEED)
                    if old_speed != 0:
                        for i in range(len(ball_speeds)):
                            ball_speeds[i] = (ball_speeds[i][0] * (current_base_speed / old_speed), 
                                            (1 if ball_speeds[i][1] > 0 else -1) * current_base_speed)
                elif event.key == pygame.K_p:  # Increase paddle size
                    old_center = paddle.centerx
                    current_paddle_width = min(current_paddle_width + 20, PADDLE_MAX_WIDTH)
                    paddle.width = current_paddle_width
                    paddle.centerx = old_center
                elif event.key == pygame.K_o:  # Decrease paddle size
                    old_center = paddle.centerx
                    current_paddle_width = max(current_paddle_width - 20, PADDLE_MIN_WIDTH)
                    paddle.width = current_paddle_width
                    paddle.centerx = old_center
                elif event.key == pygame.K_c:  # Change brick color
                    brick_color = random.choice(COLORS)
                elif event.key == pygame.K_s:
                    sync_paddle_and_ball = not sync_paddle_and_ball
                elif event.key == pygame.K_b:  # Add new ball
                    new_ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS * 2, BALL_RADIUS * 2)
                    balls.append(new_ball)
                    ball_speeds.append((current_base_speed * random.choice((1, -1)), -current_base_speed))

        # 移動所有球
        for i, ball in enumerate(balls):
            ball.x += ball_speeds[i][0]
            ball.y += ball_speeds[i][1]

            # 碰到牆壁反彈
            if ball.left <= 0:
                ball_speeds[i] = (abs(ball_speeds[i][0]), ball_speeds[i][1])
            elif ball.right >= WIDTH:
                ball_speeds[i] = (-abs(ball_speeds[i][0]), ball_speeds[i][1])
            if ball.top <= 0:
                ball_speeds[i] = (ball_speeds[i][0], abs(ball_speeds[i][1]))

        # 滑板移動
        if sync_paddle_and_ball and balls:
            # 找到最底下的球（y最大的球）
            lowest_ball = max(balls, key=lambda b: b.y)
            paddle.centerx = lowest_ball.centerx
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and paddle.left > 0:
                paddle.move_ip(-8, 0)
            if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
                paddle.move_ip(8, 0)

        # 每個球的碰撞檢測
        balls_to_remove = []
        for i, ball in enumerate(balls):
            # 碰到滑板反彈
            if ball.colliderect(paddle) and ball_speeds[i][1] > 0:
                ball.y = paddle.top - BALL_RADIUS * 2
                hit_pos = (ball.centerx - paddle.centerx) / (current_paddle_width // 2)
                ball_speeds[i] = (hit_pos * current_base_speed, -current_base_speed)

            # 碰到磚塊
            for brick in bricks[:]:
                if ball.colliderect(brick):
                    overlap_left = abs(ball.right - brick.left)
                    overlap_right = abs(ball.left - brick.right)
                    overlap_top = abs(ball.bottom - brick.top)
                    overlap_bottom = abs(ball.top - brick.bottom)
                    min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                    if min_overlap == overlap_left:
                        ball_speeds[i] = (-abs(ball_speeds[i][0]), ball_speeds[i][1])
                    elif min_overlap == overlap_right:
                        ball_speeds[i] = (abs(ball_speeds[i][0]), ball_speeds[i][1])
                    elif min_overlap == overlap_top:
                        ball_speeds[i] = (ball_speeds[i][0], -abs(ball_speeds[i][1]))
                    elif min_overlap == overlap_bottom:
                        ball_speeds[i] = (ball_speeds[i][0], abs(ball_speeds[i][1]))
                    bricks.remove(brick)
                    score += 10
                    break

            # 防止球速過慢
            if abs(ball_speeds[i][0]) < 1:
                ball_speeds[i] = (1 * random.choice((1, -1)), ball_speeds[i][1])

            # 球掉出螢幕
            if ball.bottom >= HEIGHT:
                balls_to_remove.append(i)

        # 移除掉出螢幕的球
        for index in sorted(balls_to_remove, reverse=True):
            balls.pop(index)
            ball_speeds.pop(index)

        # 繪製磚塊
        for brick in bricks:
            pygame.draw.rect(screen, brick_color, brick)

        # 繪製滑板
        pygame.draw.rect(screen, BLUE, paddle)

        # 繪製所有球
        for ball in balls:
            pygame.draw.ellipse(screen, GREEN, ball)

        # 繪製分數和狀態
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        speed_text = font.render(f"Speed: {current_base_speed}", True, WHITE)
        screen.blit(speed_text, (WIDTH - 150, 10))
        paddle_text = font.render(f"Paddle: {current_paddle_width}", True, WHITE)
        screen.blit(paddle_text, (WIDTH - 150, 50))
        balls_text = font.render(f"Balls: {len(balls)}", True, WHITE)
        screen.blit(balls_text, (WIDTH - 150, 90))

        # 遊戲結束判定
        if not balls:  # 如果所有球都掉出螢幕
            running = False
            end_screen("Game Over", score)
        elif not bricks:  # 如果所有磚塊被清除
            running = False
            end_screen("Victory", score)

        # 更新畫面
        pygame.display.flip()
        clock.tick(60)