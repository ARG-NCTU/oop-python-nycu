import pygame
import sys
import os
import pickle

os.chdir('/home/sam/oop-python-nycu/tests/team_16/game_testing')

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
    font = pygame.font.Font('Noto_Sans_TC/NotoSansTC-VariableFont_wght.ttf', 36)
    description_font = pygame.font.Font('Noto_Sans_TC/NotoSansTC-VariableFont_wght.ttf', 24)
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
    character_image = pygame.image.load('薩邁爾.png')
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    sys.exit()

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback, description):
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
        if self.hovered:
            description_surface = description_font.render(self.description, True, WHITE)
            screen.blit(description_surface, (self.rect.x, self.rect.y - 30))

# Callback functions for buttons
def start_new_game():
    global current_screen
    current_screen = 'enter_name'

def load_game():
    global current_screen
    if os.path.exists('savefile.pkl'):
        with open('savefile.pkl', 'rb') as f:
            global main_player, lobby_NPC
            main_player, lobby_NPC = pickle.load(f)
        current_screen = 'lobby'
    else:
        print("No saved game found!")

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
player_name = ""
tutorial_prompt = False

def resize_buttons(buttons, screen_width, screen_height):
    for button in buttons:
        button.rect.x = screen_width // 2 - button.rect.width // 2
        button.rect.y = screen_height // 2 - button.rect.height // 2 + (buttons.index(button) - 1) * 100

def display_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_dialogue_box(screen, text, character_image):
    dialogue_box_rect = pygame.Rect(50, SCREEN_HEIGHT - 150, SCREEN_WIDTH - 250, 100)
    pygame.draw.rect(screen, BLACK, dialogue_box_rect)
    pygame.draw.rect(screen, WHITE, dialogue_box_rect, 5)
    
    text_surface = description_font.render(text, True, WHITE)
    screen.blit(text_surface, (dialogue_box_rect.x + 10, dialogue_box_rect.y + 10))
    
    character_image_resized = pygame.transform.scale(character_image, (150, 300))
    screen.blit(character_image_resized, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 400))

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
        elif current_screen == 'enter_name':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name:
                    tutorial_prompt = True
                    current_screen = 'tutorial_prompt'
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
        elif current_screen == 'tutorial_prompt':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    current_screen = 'game'
                elif event.key == pygame.K_n:
                    current_screen = 'lobby'

    if current_screen == 'welcome':
        resized_welcome_image = pygame.transform.scale(welcome_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_welcome_image, (0, 0))
        for button in welcome_buttons:
            button.draw(screen)
            button.draw_description(screen)
    elif current_screen == 'lobby':
        resized_lobby_image = pygame.transform.scale(lobby_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_lobby_image, (0, 0))
        display_text(f'你的名字是 {player_name}', 50, 50)
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
    elif current_screen == 'enter_name':
        resized_welcome_image = pygame.transform.scale(welcome_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_welcome_image, (0, 0))
        draw_dialogue_box(screen, "請輸入你的名字:", character_image)
        display_text(player_name, 60, SCREEN_HEIGHT - 120)
        pygame.display.flip()
    elif current_screen == 'tutorial_prompt':
        resized_welcome_image = pygame.transform.scale(welcome_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(resized_welcome_image, (0, 0))
        draw_dialogue_box(screen, "要進行新手教學嗎? (y/n)", character_image)
        pygame.display.flip()

    pygame.display.flip()

pygame.quit()
sys.exit()
