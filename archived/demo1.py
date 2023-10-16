import pygame
import json
import pyivp
from random import choice

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255, 255, 255)


class Brick():
    def __init__(self, config):
        self.x = config["brick_x"]
        self.y = config["brick_y"]
        self.radius = config["brick_radius"]
        self.poly = pyivp.string_to_poly(
            "x = " + str(self.x) + ", y = " + str(self.y) + ", format = radial, radius = " + str(self.radius) + ", pts = 4")
        self.get_vertex()

    def get_vertex(self):
        self.vertex = []
        self.seg = self.poly.export_seglist()
        for i in range(self.seg.size()):
            self.vertex.append((self.seg.get_vx(i), self.seg.get_vy(i)))

    def draw(self, screen):
        pygame.draw.lines(screen, WHITE, True, self.vertex)

    def dis_to_brick(self, x, y):
        return self.poly.dist_to_poly(x, y)


class Ball():
    def __init__(self, config):
        self.x = config["ball_x"]
        self.y = config["ball_y"]
        self.x_direction = choice((-2, 2))
        self.y_direction = -2
        self.radius = config["ball_radius"]

    def move(self):
        self.x += self.x_direction
        self.y += self.y_direction
        self.contact_detect_wall()

    def bounce(self, brick):
        if self.x < brick.x - (brick.radius / 1.414):
            self.x_direction = -2
        elif self.x > brick.x + (brick.radius / 1.414):
            self.x_direction = 2
        elif self.y < brick.y - (brick.radius / 1.414):
            self.y_direction = -2
        elif self.y > brick.y + (brick.radius / 1.414):
            self.y_direction = 2

    def contact_detect_wall(self):
        if self.x + self.radius >= SCREEN_WIDTH or\
                self.x - self.radius <= 0:
            self.x_direction = -self.x_direction

        if self.y + self.radius >= SCREEN_HEIGHT or\
                self.y - self.radius <= 0:
            self.y_direction = -self.y_direction
    def contact_detect_brick(self, brick):
        if (brick.dis_to_brick(self.x, self.y) - self.radius <= 0):
            self.bounce(brick)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)


class Game():
    def __init__(self, config_file):
        # load config
        with open(config_file, "r") as f:
            config = json.load(f)
        self.ball = Ball(config["ball"])
        self.brick = Brick(config["brick"])
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.screen.fill((0, 0, 0))

            self.brick.draw(self.screen)
            self.ball.contact_detect_brick(self.brick)
            self.ball.move()
            self.ball.draw(self.screen)

            # event handler
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    self.is_running = False
            pygame.display.flip()
            self.clock.tick(50)

        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    game = Game("config.json")
    game.run()
