import pygame
import sys

#constants
SCREEN_Width = 640
SCREEN_HEIGHT = 480

class main_game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Koakuma's Adventure")
        self.screen = pygame.display.set_mode((SCREEN_Width, SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()

        self.image = pygame.image.load("data/images/clouds/cloud_1.png")
        self.image.set_colorkey((0,0,0))

        self.image_position = [100,200] 
        self.movements = [False, False]

        self.collision_area = pygame.Rect(50,50,300,400)
    def run(self):
        while True:
            self.screen.fill((14,219,248))

            img_rect = pygame.Rect(self.image_position[0], self.image_position[1], self.image.get_width(), self.image.get_height())

            if img_rect.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (255,0,0), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0,255,0), self.collision_area)

            self.image_position[0] += (self.movements[1] - self.movements[0]) * 5
            self.screen.blit(self.image, self.image_position)   

            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = False


            
            pygame.display.update()
            self.clock.tick(60)

main_game().run()