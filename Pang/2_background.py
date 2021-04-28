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

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False # Game is not running

    # screen.fill((0, 0, 255)) # Option to fill the screen with color code
    screen.blit(background, (0, 0))

    pygame.display.update() # Game screen redrawn

# Close Pygame
pygame.quit()