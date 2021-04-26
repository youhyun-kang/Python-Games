import pygame

pygame.init()

# Screen Size Setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title
pygame.display.set_caption("Pang Game")

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False # Game is not running


# Close Pygame
pygame.quit()