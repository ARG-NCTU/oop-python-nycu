import pygame

# Ball class
class Ball:
    def __init__(self, screen, color, radius, pos, velocity):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos
        self.velocity = velocity

    def update(self, screen_width, screen_height):
        # 移動
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # 邊界檢查
        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= screen_width:
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= screen_height:
            self.velocity[1] = -self.velocity[1]

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)


# Main class
class BouncyBallGame:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("BouncyBall")

        # 建立兩個球
        self.ball1 = Ball(self.screen, (255, 255, 255), 20, [width/2 , height/2], [3, 3])
        self.ball2 = Ball(self.screen, (255, 0, 10), 30, [300, 400], [100, 70])

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))

            # 更新並繪製兩顆球
            self.ball1.update(self.screen_width, self.screen_height)
            self.ball2.update(self.screen_width, self.screen_height)
            self.ball1.draw()
            self.ball2.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = BouncyBallGame()
    game.run()
