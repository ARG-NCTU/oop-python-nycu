import pygame

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Set up the game window
window_width = 1600
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Platformer Game")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define player properties
player_face = "right"
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height
player_x_speed = 3
player_y_speed = 0
player_dash_speed = 20
player_jump_power = 5
player_is_jumping = False
player_is_dashing = False
player_super_dash = False
dash_CD = 0

# Define ground properties
ground_y = window_height - 50

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not player_is_dashing:
        player_x -= player_x_speed
        player_face = "left"
    if keys[pygame.K_RIGHT] and not player_is_dashing:
        player_x += player_x_speed
        player_face = "right"
    if keys[pygame.K_UP] and not player_is_jumping and not player_is_dashing:
        player_is_jumping = True
        player_y_speed = -player_jump_power
    if keys[pygame.K_UP] and not player_is_jumping and player_is_dashing:
        player_is_jumping = True
        player_y_speed = -player_jump_power
        player_is_dashing = False

    if keys[pygame.K_w] and dash_CD <= 0:
        player_is_dashing = True
        dash_CD = 80

    if player_is_dashing:
        if player_face == "left" and dash_CD >= 70:
            player_x -= player_dash_speed
            player_y_speed = 0
        elif player_face == "right" and dash_CD >= 70:
            player_x += player_dash_speed
            player_y_speed = 0
        else:
            player_is_dashing = False
    if player_super_dash:
        if player_face == "left":
            player_x -= player_dash_speed/2
        elif player_face == "right":
            player_x += player_dash_speed/2
        player_super_dash = False
    
    dash_CD -= 1
            


    # Apply gravity
    if not player_is_dashing:
        player_y_speed += 0.1
        player_y += player_y_speed

    # Check for ground collision
    if player_y >= ground_y - player_height:
        player_y = ground_y - player_height
        player_y_speed = 0
        player_is_jumping = False

    # Clear the window
    window.fill(WHITE)

    # Draw the player
    pygame.draw.rect(window, BLUE, (player_x, player_y, player_width, player_height))

    # Draw the ground
    pygame.draw.rect(window, BLUE, (0, ground_y, window_width, window_height - ground_y))

    # Update the display
    pygame.display.update()

    # 120 fps
    clock.tick(120)

# Quit the game
pygame.quit()