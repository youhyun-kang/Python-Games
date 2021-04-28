import pygame

pygame.init()

# Screen Size Setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title
pygame.display.set_caption("Game Name")

# Background Image Added
background = pygame.image.load("background.png")

# Charactor Added
character = pygame.image.load("character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height



# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False # Game is not running

    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # Game screen redrawn

# Close Pygame
pygame.quit()