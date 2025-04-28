import pygame

class BALL():
    def __init__(self, ball):
        self.ball = ball
        self.screen_width = self.ball['screen'].get_width()
        self.screen_height = self.ball['screen'].get_height()
    def update_ball(self):
        self.ball['pos'][0] += self.ball['velocity'][0]
        self.ball['pos'][1] += self.ball['velocity'][1]

        if self.ball['pos'][0] - self.ball['radius'] <= 0 or self.ball['pos'][0] + self.ball['radius'] >= self.screen_width:
            self.ball['velocity'][0] = -self.ball['velocity'][0]

        if self.ball['pos'][1] - self.ball['radius'] <= 0 or self.ball['pos'][1] + self.ball['radius'] >= self.screen_height:
            self.ball['velocity'][1] = -self.ball['velocity'][1]
    def draw_ball(self):
        pygame.draw.circle(self.ball['screen'], self.ball['color'], self.ball['pos'], self.ball['radius'])

def main():
    # add your code here
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('BouncyBall')


    ball1 = {
        'screen': screen,
        'color': (255, 255, 255),
        'radius': 20,
        'pos': [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2],
        'velocity': [2, 2]
    }
    ball2 = {
        'screen': screen,
        'color': (255, 0, 0),
        'radius': 10,
        'pos': [2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2],
        'velocity': [-4, -4]
    }
    b1 = BALL(ball1)
    b2 = BALL(ball2)

    clock = pygame.time.Clock()
    running = True


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # add your code here
        screen.fill((0, 0, 0))


        b1.update_ball()
        b2.update_ball()
        b1.draw_ball()
        b2.draw_ball()

        # add your code here
        pygame.display.flip()

        clock.tick(60)

    # add your code here


if __name__ == "__main__":
    main()