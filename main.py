import pygame
import pygame_gui

from pygame_gui.core import ObjectID

# print actions to the terminal
debug_mode = True

# pygame setup
pygame.init()
pygame.display.set_caption("Just Dodge")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screen_dims = (screen.get_width(), screen.get_height())

# player vars
player_move_speed = 400
player_radius = 15
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dodge_dist = 5000
touchable = True
load_player = False

# functions
## difficulty functions
# these control spawn rate of boxes and score gained
def start_easy():
    global difficulty
    difficulty = 1
    load()
    if debug_mode == True:
        print("Easy mode")

def start_medium():
    global difficulty
    difficulty = 2
    load()
    if debug_mode == True:
        print("Medium mode")

def start_hard():
    global difficulty
    difficulty = 3
    load()
    if debug_mode == True:
        print("Hard mode")

## general functions
def load():
    global load_player, on_main_menu
    on_main_menu = False
    load_player = True
    if debug_mode == True:
        print("Play button clicked")

# g/ui
## main menu
on_main_menu = True
# some code comes from the pygame_menu documentation
# load themes. classes are stored in seperate files to make them more readable 
manager = pygame_gui.UIManager((screen_dims[0], screen_dims[1]), theme_path="theme_basic.json")
manager.get_theme().load_theme('theme_blabel.json')
manager.get_theme().load_theme('theme_interactable_button.json')

# labels dont work for some reason so i will use buttons as labels
title = pygame_gui.elements.UIButton(
    manager=manager,
    relative_rect=pygame.Rect((screen_dims[0]/2-710, screen_dims[1]/2-360), (450, 70)),
    text='Game Title',
    object_id=ObjectID(class_id='@blabel')
)

play_button = pygame_gui.elements.UIButton(
    manager=manager,
    relative_rect=pygame.Rect((screen_dims[0]/2-635, screen_dims[1]/2), (100, 50)),
    text='Play',
    command=load,
    object_id=ObjectID(class_id='@interactable_button')
)

# GET TS WORKING LIL BRO
'''difficulty_dropdown = pygame_gui.elements.UIDropDownMenu(
    manager=manager,
    options_list=[
        "Easy",
        "Medium",
        "Hard"
    ],
    starting_option="Easy",
    relative_rect=pygame.Rect((screen_dims[0]/2-645, screen_dims[1]/2+65), (145, 55)),
    object_id=ObjectID(class_id='@difficulty_dropdown')
)'''

# game loop
print("\"Just Dodge\" vALPHA")
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        manager.process_events(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # start dodge
            # dodge in the direction you are currently moving
            if event.key == pygame.K_SPACE and keys[pygame.K_w]:
                touchable = False
                player_pos.y -= dodge_dist * dt
                touchable = True
                if debug_mode == True:
                    print("Dodge executed | up")
            if event.key == pygame.K_SPACE and keys[pygame.K_s]:
                touchable = False
                player_pos.y += dodge_dist * dt
                touchable = True
                if debug_mode == True:
                    print("Dodge executed | down")
            if event.key == pygame.K_SPACE and keys[pygame.K_a]:
                touchable = False
                player_pos.x -= dodge_dist * dt
                touchable = True
                if debug_mode == True:
                    print("Dodge executed | left")
            if event.key == pygame.K_SPACE and keys[pygame.K_d]:
                touchable = False
                player_pos.x += dodge_dist * dt
                touchable = True
                if debug_mode == True:
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
    
    # player movement
    # if a key is held, move in that direction
    # from boilerplate found in docs
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
        manager.update(dt)
        manager.draw_ui(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
