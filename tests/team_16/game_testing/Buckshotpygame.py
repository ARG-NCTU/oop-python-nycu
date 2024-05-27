import pygame
import sys
import os
import pickle

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("BuckShot")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
try:
    font = pygame.font.Font(None, 36)
    description_font = pygame.font.Font(None, 24)
except pygame.error as e:
    print(f"Error loading font: {e}")
    pygame.quit()
    sys.exit()

# Load images
try:
    welcome_image = pygame.image.load('welcome.png')
    lobby_image = pygame.image.load('lobby.png')
    shop_image = pygame.image.load('shop.png')
    game_image = pygame.image.load('game.png')
    challenge_image = pygame.image.load('challenge.png')
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    sys.exit()

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback, description=""):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.description = description
        self.hovered = False

    def draw(self, screen):
        color = GRAY if self.hovered else WHITE
        pygame.draw.rect(screen, color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, 
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                self.callback()

    def draw_description(self, screen):
        if self.hovered and self.description:
            description_surface = description_font.render(self.description, True, WHITE)
            screen.blit(description_surface, (self.rect.x, self.rect.y - 30))

# Callback functions for buttons
def start_new_game():
    global current_screen
    global main_player, lobby_NPC
    main_player = player_in_lobby("Player", 0)
    lobby_NPC = [collection_manager(), shopkeeper(), host()]
    lobby_NPC[2].tutorial()
    current_screen = 'lobby'

def load_game():
    global current_screen
    global main_player, lobby_NPC
    if os.path.exists('savefile.pkl'):
        with open('savefile.pkl', 'rb') as f:
            main_player, lobby_NPC = pickle.load(f)
        current_screen = 'lobby'
    else:
        print("No saved game found")

def quit_game():
    pygame.quit()
    sys.exit()

def enter_shop():
    global current_screen
    current_screen = 'shop'

def enter_game():
    global current_screen
    current_screen = 'game'

def enter_challenge():
    global current_screen
    current_screen = 'challenge'

def return_to_lobby():
    global current_screen
    current_screen = 'lobby'

# Create buttons
welcome_buttons = [
    Button("Start New Game", 300, 200, 200, 50, start_new_game, "Start a new game."),
    Button("Load Game", 300, 300, 200, 50, load_game, "Load a saved game."),
    Button("Quit Game", 300, 400, 200, 50, quit_game, "Exit the game.")
]

lobby_buttons = [
    Button("Enter Shop", 300, 200, 200, 50, enter_shop, "Visit the shop to buy items."),
    Button("Enter Game", 300, 300, 200, 50, enter_game, "Start a new game."),
    Button("Enter Challenge", 300, 400, 200, 50, enter_challenge, "Take on a challenge.")
]

shop_buttons = [
    Button("Return to Lobby", 300, 500, 200, 50, return_to_lobby, "Return to the lobby.")
]

game_buttons = [
    Button("Return to Lobby", 300, 500, 200, 50, return_to_lobby, "Return to the lobby.")
]

challenge_buttons = [
    Button("Return to Lobby", 300, 500, 200, 50, return_to_lobby, "Return to the lobby.")
]

current_screen = 'welcome'

def resize_buttons(buttons, screen_width, screen_height):
    for button in buttons:
        button.rect.x = screen_width // 2 - button.rect.width // 2
        button.rect.y = screen_height // 2 - button.rect.height // 2 + (buttons.index(button) - 1) * 100

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
            resize_buttons(welcome_buttons, SCREEN_WIDTH, SCREEN_HEIGHT)
            resize_buttons(lobby_buttons, SCREEN_WIDTH, SCREEN_HEIGHT)
            resize_buttons(shop_buttons, SCREEN_WIDTH, SCREEN_HEIGHT)
            resize_buttons(game_buttons, SCREEN_WIDTH, SCREEN_HEIGHT)
            resize_buttons(challenge_buttons, SCREEN_WIDTH, SCREEN_HEIGHT)

        if current_screen == 'welcome':
            for button in welcome_buttons:
                button.handle_event(event)
        elif current_screen == 'lobby':
            for button in lobby_buttons:
                button.handle_event(event)
        elif current_screen == 'shop':
            for button in shop_buttons:
                button.handle_event(event)
        elif current_screen == 'game':
            for button in game_buttons:
                button.handle_event(event)
        elif current_screen == 'challenge':
            for button in challenge_buttons:
                button.handle_event(event)

    if current_screen == 'welcome':
        resized_welcome_image = pygame.transform.scale(welcome_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_welcome_image, (0, 0))
        for button in welcome_buttons:
            button.draw(screen)
            button.draw_description(screen)
    elif current_screen == 'lobby':
        resized_lobby_image = pygame.transform.scale(lobby_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_lobby_image, (0, 0))
        for button in lobby_buttons:
            button.draw(screen)
            button.draw_description(screen)
    elif current_screen == 'shop':
        resized_shop_image = pygame.transform.scale(shop_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_shop_image, (0, 0))
        for button in shop_buttons:
            button.draw(screen)
            button.draw_description(screen)
    elif current_screen == 'game':
        resized_game_image = pygame.transform.scale(game_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_game_image, (0, 0))
        for button in game_buttons:
            button.draw(screen)
            button.draw_description(screen)
    elif current_screen == 'challenge':
        resized_challenge_image = pygame.transform.scale(challenge_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_challenge_image, (0, 0))
        for button in challenge_buttons:
            button.draw(screen)
            button.draw_description(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
