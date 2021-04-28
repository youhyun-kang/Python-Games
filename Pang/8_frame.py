import pygame
#####################################################
# Initial Setup
pygame.init()

# Screen Size Setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title
pygame.display.set_caption("Game Name")

#FPS
clock = pygame.time.Clock()

#####################################################

# 1. User's Initial Game Setup (Background, Game Image, Coordinate / Location, Speed, Font etc.)

running = True
while running:
    dt = clock.tick(30)

    # 2. Event Process (Keyboard, Mouse etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

    # 3. Character Location Defined

    # 4. Case of Collision Setup

    # 5. Game Display Update / Redrawn
    pygame.display.update()

# Close Pygame
pygame.quit()