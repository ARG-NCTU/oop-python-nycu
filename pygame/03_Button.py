import pygame

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('./img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('./img/exit_btn.png').convert_alpha()

#create button instances
start_button = Button(100, 200, start_img, 0.8)
exit_button = Button(450, 200, exit_img, 0.8)

#game loop
is_running = True
while is_running:

    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        print('START')
    if exit_button.draw(screen):
        print('EXIT')

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()