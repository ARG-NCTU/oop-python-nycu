
import pygame

# 建立 Ball 類別來封裝球的屬性與行為
class Ball:
    def __init__(self, screen, color, radius, pos, velocity):
        """
        screen   : pygame 的視窗 Surface
        color    : 球的顏色 (RGB)
        radius   : 球的半徑
        pos      : 球的初始位置 [x, y]
        velocity : 球在 x, y 方向上的初始速度 [vx, vy]
        """
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos
        self.velocity = velocity

    def update(self, screen_width, screen_height):
        """ 更新球的位置，並在碰到視窗邊界時反彈 """
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # 檢查左右邊界，若碰到則反轉 x 軸速度
        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= screen_width:
            self.velocity[0] = -self.velocity[0]

        # 檢查上下邊界，若碰到則反轉 y 軸速度
        if self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= screen_height:
            self.velocity[1] = -self.velocity[1]

    def draw(self):
        """ 繪製球 """
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

def main():
    # 初始化 pygame
    pygame.init()

    # 設定視窗大小
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 視窗標題
    pygame.display.set_caption("BouncyBall")

    # 建立兩顆球
    ball1 = Ball(
        screen=screen,
        color=(255, 255, 255),       # 白色
        radius=20,
        pos=[screen_width // 2, screen_height // 2],  # 初始位置放在視窗正中央
        velocity=[3, 3]             # x, y 速度
    )

    ball2 = Ball(
        screen=screen,
        color=(255, 0, 0),          # 紅色
        radius=30,
        pos=[screen_width // 4, screen_height // 4],  # 與 ball1 不同位置
        velocity=[5, 4]             # x, y 速度
    )

    clock = pygame.time.Clock()
    running = True

    while running:
        # 處理事件，當使用者關閉視窗時結束程式
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 填滿背景 (黑色)
        screen.fill((0, 0, 0))

        # 更新球的位置與繪製
        ball1.update(screen_width, screen_height)
        ball2.update(screen_width, screen_height)
        ball1.draw()
        ball2.draw()

        # 刷新畫面
        pygame.display.flip()

        # 控制更新頻率
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
