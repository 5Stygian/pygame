import pygame
import math
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# player vars
player_move_speed = 400
player_radius = 15
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dash_dist = 5000
touchable = True

# gui vars
## general
### fonts
main_font = pygame.font.SysFont('Corbel',35) 
## main menu
### difficulty buttons
#### easy
easy_diff_text = main_font.render('quit' , True , "rgb(0,0,0)")
easy_diff_button = 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # start dodge
            if event.key == pygame.K_SPACE and keys[pygame.K_w]:
                touchable = False
                player_pos.y -= dash_dist * dt
                touchable = True
            if event.key == pygame.K_SPACE and keys[pygame.K_s]:
                touchable = False
                player_pos.y += dash_dist * dt
                touchable = True
            if event.key == pygame.K_SPACE and keys[pygame.K_a]:
                touchable = False
                player_pos.x -= dash_dist * dt
                touchable = True
            if event.key == pygame.K_SPACE and keys[pygame.K_d]:
                touchable = False
                player_pos.x += dash_dist * dt
                touchable = True
            # end dodge
        if event.type == pygame.MOUSEBUTTONDOWN:
            # button event handling
            pass

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # save the position of the mouse every frame
    mouse_pos = pygame.mouse.get_pos() 

    # player
    pygame.draw.circle(screen, "red", player_pos, player_radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_move_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_move_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= player_move_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_move_speed * dt

    # prevents player from moving off the screen
    # credits to max knoth for writing this approximately 10 minutes after first installing pygame
    if not (0 < player_pos.x - player_radius):
        player_pos.x += abs(player_radius - player_pos.x)
    if not (player_pos.x + player_radius < screen.get_width()):
        player_pos.x -= abs(screen.get_width() - player_pos.x - player_radius)

    if not (0 < player_pos.y - player_radius):
        player_pos.y += abs(player_radius - player_pos.y)
    if not (player_pos.y + player_radius < screen.get_height()):
        player_pos.y -= abs(screen.get_height() - player_pos.y - player_radius)

    
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
