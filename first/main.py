import pygame
import math
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screen_dims = (screen.get_width(), screen.get_height())

# player vars
player_move_speed = 400
player_radius = 15
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dash_dist = 5000
touchable = True
load_player = False

# gui vars
## general
### fonts
main_font = pygame.font.SysFont('Corbel',35) 
## main menu
### difficulty buttons
#### easy
easy_diff_nonhover = (75, 201, 52)
easy_diff_hover = (78, 227, 48)
easy_diff_text = main_font.render('Easy' , True, "black")
easy_diff_dims = ()
blit_easy = False

# functions
def load():
    global load_player
    load_player = True

def start_easy():
    global blit_easy
    blit_easy = True
    load()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # start dodge
            # dodge in the direction you are currently moving
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
        
        if event.type == pygame.MOUSEBUTTONUP:
            # main menu difficulty 

            # easy
            if screen_dims[0]/2 <= mouse_pos[0] <= screen_dims[0]/2+140 and screen_dims[1]/2 <= mouse_pos[1] <= screen_dims[1]/2+40: 
                start_easy()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # save the position of the mouse_pos every frame
    mouse_pos = pygame.mouse.get_pos() 

    # loads the player when a difficulty is selected
    if load_player == True:
        pygame.draw.circle(screen, "red", player_pos, player_radius)
    else: 
        pass

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
    # player end

    # gui
    ## main menu
    ### easy
    # some of this code comes from a geeksforgeeks article about pygame buttons
    if screen_dims[0]/2 <= mouse_pos[0] <= screen_dims[0]/2+140 and screen_dims[1]/2 <= mouse_pos[1] <= screen_dims[1]/2+40: 
        pygame.draw.rect(screen,easy_diff_hover,[screen_dims[0]/2,screen_dims[1]/2,140,40]) 
    else:
        pygame.draw.rect(screen,easy_diff_nonhover,[screen_dims[0]/2,screen_dims[1]/2,140,40])
    
    easy_text = 0
    while easy_text < 1:
        screen.blit(easy_diff_text, (screen_dims[0]/2+50, screen_dims[1]/2))
        easy_text += 1
    
    if blit_easy == True:
        screen.blit(easy_diff_text, (screen_dims[0]/2+50, screen_dims[1]/2))
    else:
        pass

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
