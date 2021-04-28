import random
import pygame
#####################################################
# Initial Setup
pygame.init()

# Screen Size Setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title
pygame.display.set_caption("Poopoo")

#FPS
clock = pygame.time.Clock()

#####################################################

# 1. User's Initial Game Setup (Background, Game Image, Coordinate / Location, Speed, Font etc.)

# Background
background = pygame.image.load("background.png")

# Character
character = pygame.image.load("character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 10

# Poop
poop = pygame.image.load("enemy.png")
poop_size = poop.get_rect().size 
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = random.randint(0, screen_width - poop_width)
poop_y_pos = 0
poop_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. Event Process (Keyboard, Mouse etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    # 3. Character Location Defined
    character_x_pos += to_x

    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    poop_y_pos += poop_speed

    if poop_y_pos > screen_height:
        poop_y_pos = 0
        poop_x_pos = random.randint(0, screen_width - poop_width)

    # 4. Case of Collision Setup
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos

    if character_rect.colliderect(poop_rect):
        print("COLLISION!")
        running = False

    # 5. Game Display Update / Redrawn
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(poop, (poop_x_pos, poop_y_pos))

    pygame.display.update()


# Close Pygame
pygame.quit()
