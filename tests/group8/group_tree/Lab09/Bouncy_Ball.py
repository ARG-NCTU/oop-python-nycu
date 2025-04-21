import pygame
import math

class Ball:
    def __init__(self, screen, color, radius, pos, velocity):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.mass = 1  # 假設質量為1，實際上質量不影響運動，只影響碰撞計算

    def update(self, screen_width, screen_height):
        # 更新位置
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # 檢查左右邊界，若碰到則反轉 x 軸速度
        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= screen_width:
            self.velocity[0] = -self.velocity[0]

        # 檢查上下邊界，若碰到則反轉 y 軸速度
        if self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= screen_height:
            self.velocity[1] = -self.velocity[1]

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

    def check_collision(self, other):
        # 計算兩球中心的距離
        dx = self.pos[0] - other.pos[0]
        dy = self.pos[1] - other.pos[1]
        distance = math.sqrt(dx**2 + dy**2)

        # 如果距離小於兩球半徑之和，則發生碰撞
        if distance <= self.radius + other.radius:
            # 計算碰撞法向量
            nx = dx / distance
            ny = dy / distance
            # 計算相對速度
            dvx = self.velocity[0] - other.velocity[0]
            dvy = self.velocity[1] - other.velocity[1]
            # 計算法向速度
            dot = dvx * nx + dvy * ny
            # 反彈速度
            if dot > 0:
                return
            # 更新速度
            self.velocity[0] -= dot * nx
            self.velocity[1] -= dot * ny
            other.velocity[0] += dot * nx
            other.velocity[1] += dot * ny


def main():
    pygame.init()

    # 初始化畫面
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncy Ball")

    # 創建球物件
    ball = Ball(
        screen=screen,
        color=(255, 255, 255),
        radius=30,
        pos=[2 * screen_width // 3, 2 * screen_height // 3],
        velocity=[-7, -7]
    )
    ball2 = Ball(
        screen=screen,
        color=(0, 255, 255),
        radius=20,
        pos=[screen_width // 3, screen_height // 3 - 50],
        velocity=[5, 5]
    )

    clock = pygame.time.Clock()
    running = True

    # 主迴圈：持續更新與繪製
    while running:
        # 處理事件，當使用者關閉視窗時結束程式
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 更新球的位置及反彈邏輯
        ball.update(screen_width, screen_height)
        ball2.update(screen_width, screen_height)

        # 檢查兩球是否碰撞
        ball.check_collision(ball2)

        # 繪製畫面
        screen.fill((0, 0, 0))  # 清空畫面
        ball.draw()
        ball2.draw()
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()