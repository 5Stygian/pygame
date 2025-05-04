import pygame
import pygame_menu
import math

import pygame_menu.events

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

# functions
def load():
    global load_player, on_main_menu
    on_main_menu = False
    load_player = True
    print("Play button clicked")

def start_easy():
    load()

# g/ui
## main menu
on_main_menu = True
# some code comes from the pygame_menu documentation
main_menu = pygame_menu.Menu('Main Menu', screen_dims[0], screen_dims[1],
                             theme=pygame_menu.themes.THEME_SOLARIZED)

main_menu.add.button("Play", load)

# game loop
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
                print("Dodge executed | up")
            if event.key == pygame.K_SPACE and keys[pygame.K_s]:
                touchable = False
                player_pos.y += dash_dist * dt
                touchable = True
                print("Dodge executed | down")
            if event.key == pygame.K_SPACE and keys[pygame.K_a]:
                touchable = False
                player_pos.x -= dash_dist * dt
                touchable = True
                print("Dodge executed | left")
            if event.key == pygame.K_SPACE and keys[pygame.K_d]:
                touchable = False
                player_pos.x += dash_dist * dt
                touchable = True
                print("Dodge executed | right")
            # end dodge

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # player start
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
    # thanks to max knoth for writing this approximately 10 minutes after first installing pygame
    if not (0 < player_pos.x - player_radius):
        player_pos.x += abs(player_radius - player_pos.x)
    if not (player_pos.x + player_radius < screen.get_width()):
        player_pos.x -= abs(screen.get_width() - player_pos.x - player_radius)

    if not (0 < player_pos.y - player_radius):
        player_pos.y += abs(player_radius - player_pos.y)
    if not (player_pos.y + player_radius < screen.get_height()):
        player_pos.y -= abs(screen.get_height() - player_pos.y - player_radius)
    # player end
    
    # g/ui
    ## main menu
    if on_main_menu == True:
        main_menu.draw(surface=screen)
        main_menu.update(pygame.event.get())

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
