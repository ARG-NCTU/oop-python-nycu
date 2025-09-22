import pygame
import random
import platform
import asyncio
import math

def main():
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
    COLORS = [WHITE, RED, BLUE, GREEN]  # BLACK excluded to avoid invisible balls

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
    FPS = 60
    MAX_ROUNDS = 10  # 最大輪數

    # 生成磚塊的函數
    def generate_bricks():
        bricks = []
        for row in range(ROWS):
            for col in range(COLS):
                brick = pygame.Rect(col * (BRICK_WIDTH + 5), row * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
                bricks.append(brick)
        return bricks

    # 開始界面函數
    def start_screen(final_score=None, rounds_cleared=0):
        nonlocal sync_paddle_and_ball, ball_collision_enabled
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 36)
        while True:
            screen.fill(BLACK)
            title_text = font.render("Breakout", True, WHITE)
            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
            if final_score is not None:
                score_text = small_font.render(f"Your score: {final_score}", True, WHITE)
                screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))
                rounds_text = small_font.render(f"Rounds cleared: {rounds_cleared}/{MAX_ROUNDS}", True, WHITE)
                screen.blit(rounds_text, (WIDTH // 2 - rounds_text.get_width() // 2, 250))
            sync_text = small_font.render(f"Sync ball and paddle: {'Yes' if sync_paddle_and_ball else 'No'} (press S to switch)", True, WHITE)
            screen.blit(sync_text, (WIDTH // 2 - sync_text.get_width() // 2, 300))
            collision_text = small_font.render(f"Ball collision: {'On' if ball_collision_enabled else 'Off'} (press E to switch)", True, WHITE)
            screen.blit(collision_text, (WIDTH // 2 - collision_text.get_width() // 2, 330))
            start_text = small_font.render("Press ENTER to start the game", True, WHITE)
            screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 400))
            instructions = [
                "In-game controls:",
                "LEFT/RIGHT: Move paddle (if not synced)",
                "U/I: Increase/Decrease ball speed",
                "P/O: Increase/Decrease paddle size",
                "C: Change brick color",
                "B: Add new ball",
                "T: Add 10 new balls",
                "R: Reset bricks",
                "E: Toggle ball collision",
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
                    elif event.key == pygame.K_e:
                        ball_collision_enabled = not ball_collision_enabled
                    elif event.key == pygame.K_RETURN:
                        return

    # 結束畫面函數
    def end_screen(status, final_score, rounds_cleared):
        font = pygame.font.Font(None, 74)
        small_font = pygame.font.Font(None, 36)
        while True:
            screen.fill(BLACK)
            title_text = font.render(status, True, WHITE if status == "Victory" else RED)
            screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))
            score_text = small_font.render(f"Your score: {final_score}", True, WHITE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 250))
            rounds_text = small_font.render(f"Rounds cleared: {rounds_cleared}/{MAX_ROUNDS}", True, WHITE)
            screen.blit(rounds_text, (WIDTH // 2 - rounds_text.get_width() // 2, 300))
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
    ball_collision_enabled = False
    score = 0
    rounds_cleared = 0

    # 主遊戲迴圈
    while True:
        start_screen(final_score=score if 'score' in locals() else None, rounds_cleared=rounds_cleared)
        
        # 初始化遊戲狀態
        current_paddle_width = PADDLE_WIDTH
        paddle = pygame.Rect(WIDTH//2 - current_paddle_width//2, HEIGHT - 50, current_paddle_width, PADDLE_HEIGHT)
        balls = [pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS * 2, BALL_RADIUS * 2)]
        ball_colors = [random.choice(COLORS)]
        current_base_speed = BASE_SPEED
        ball_speeds = [(current_base_speed * random.choice((1, -1)), -current_base_speed)]
        bricks = generate_bricks()
        brick_color = random.choice(COLORS)
        score = 0
        rounds_cleared = 0
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
                        ball_colors.append(random.choice(COLORS))
                        ball_speeds.append((current_base_speed * random.triangular(-1, 1), -current_base_speed))
                    elif event.key == pygame.K_t:  # Add 10 new balls
                        for _ in range(10):
                            new_ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS * 2, BALL_RADIUS * 2)
                            balls.append(new_ball)
                            ball_colors.append(random.choice(COLORS))
                            ball_speeds.append((current_base_speed * random.triangular(-1, 1), -current_base_speed))
                    elif event.key == pygame.K_r:  # Reset bricks
                        bricks = generate_bricks()
                        brick_color = random.choice(COLORS)
                    elif event.key == pygame.K_e:  # Toggle ball collision
                        ball_collision_enabled = not ball_collision_enabled

            # 球與球碰撞檢測
            if ball_collision_enabled:
                for i in range(len(balls)):
                    for j in range(i + 1, len(balls)):
                        ball1, ball2 = balls[i], balls[j]
                        dx = ball1.centerx - ball2.centerx
                        dy = ball1.centery - ball2.centery
                        distance = math.sqrt(dx**2 + dy**2)
                        if distance < 2 * BALL_RADIUS:
                            # 計算碰撞後的速度（簡單的二維彈性碰撞）
                            v1x, v1y = ball_speeds[i]
                            v2x, v2y = ball_speeds[j]
                            # 交換速度分量（假設質量相同）
                            ball_speeds[i] = (v2x, v2y)
                            ball_speeds[j] = (v1x, v1y)
                            # 稍微分開球以避免連續碰撞
                            overlap = (2 * BALL_RADIUS - distance) / 2
                            if distance > 0:
                                dx /= distance
                                dy /= distance
                                ball1.x += dx * overlap
                                ball1.y += dy * overlap
                                ball2.x -= dx * overlap
                                ball2.y -= dy * overlap

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
                ball_colors.pop(index)
                ball_speeds.pop(index)

            # 繪製磚塊
            for brick in bricks:
                pygame.draw.rect(screen, brick_color, brick)

            # 繪製滑板
            pygame.draw.rect(screen, BLUE, paddle)

            # 繪製所有球
            for i, ball in enumerate(balls):
                pygame.draw.ellipse(screen, ball_colors[i], ball)

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
            rounds_text = font.render(f"Round: {rounds_cleared + 1}/{MAX_ROUNDS}", True, WHITE)
            screen.blit(rounds_text, (WIDTH - 150, 130))
            collision_text = font.render(f"Collision: {'On' if ball_collision_enabled else 'Off'}", True, WHITE)
            screen.blit(collision_text, (WIDTH - 150, 170))

            # 檢查是否清除當前輪的磚塊
            if not bricks:
                rounds_cleared += 1
                if rounds_cleared >= MAX_ROUNDS:
                    running = False
                    end_screen("Victory", score, rounds_cleared)
                else:
                    bricks = generate_bricks()
                    brick_color = random.choice(COLORS)

            # 遊戲結束判定
            if not balls:
                running = False
                end_screen("Game Over", score, rounds_cleared)

            # 更新畫面
            pygame.display.flip()
            clock.tick(FPS)

async def run():
    main()

if platform.system() == "Emscripten":
    asyncio.ensure_future(run())
else:
    if __name__ == "__main__":
        asyncio.run(run())