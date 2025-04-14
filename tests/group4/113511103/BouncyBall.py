import pygame
import math

class Ball:
    def __init__(self, screen, color, radius, pos, velocity):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos
        self.velocity = velocity

    def update(self, screen_width, screen_height):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= screen_width:
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= screen_height:
            self.velocity[1] = -self.velocity[1]

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

def detect_and_resolve_collision(ball1, ball2):
    dx = ball1.pos[0] - ball2.pos[0]
    dy = ball1.pos[1] - ball2.pos[1]
    distance = math.hypot(dx, dy)

    if distance <= ball1.radius + ball2.radius:
        # 交換速度向量 (簡易處理)
        ball1.velocity, ball2.velocity = ball2.velocity, ball1.velocity

        # 稍微調整位置，避免兩球卡住
        overlap = 0.5 * (ball1.radius + ball2.radius - distance + 1)
        norm_dx = dx / distance
        norm_dy = dy / distance
        ball1.pos[0] += norm_dx * overlap
        ball1.pos[1] += norm_dy * overlap
        ball2.pos[0] -= norm_dx * overlap
        ball2.pos[1] -= norm_dy * overlap

def main():
    pygame.init()
    screen_width, screen_height = 600, 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BouncyBall")

    ball1 = Ball(screen, (255, 255, 255), 20, [400, 300], [4, 3])
    ball2 = Ball(screen, (255, 0, 0), 30, [100, 100], [5, 2])

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # 球更新位置
        ball1.update(screen_width, screen_height)
        ball2.update(screen_width, screen_height)

        # 偵測並處理碰撞
        detect_and_resolve_collision(ball1, ball2)

        # 繪製球
        ball1.draw()
        ball2.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
