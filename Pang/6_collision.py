import pygame

pygame.init()

# Screen Size Setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen Title
pygame.display.set_caption("Game Name")

#FPS
clock = pygame.time.Clock()

# Background Image Added
background = pygame.image.load("background.png")

# Charactor Added
character = pygame.image.load("character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

# Character Speed
character_speed = 0.5

# Enemy Added
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)


# Event Loop
running = True
while running:
    dt = clock.tick(60) # set fps

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False # Game is not running

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # move character to the left
                to_x -= character_speed # to_x = to_x - 1
            elif event.key == pygame.K_RIGHT: # move character to the right
                to_x += character_speed
            elif event.key == pygame.K_UP: # move character to the up
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # move character to the down
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # Width
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Height
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # Rect Update in Case of Collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Collision Check
    if character_rect.colliderect(enemy_rect):
        print("COLLISION!")
        running = False


    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # draw enemy

    pygame.display.update() # Game screen redrawn

# Close Pygame
pygame.quit()