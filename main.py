import pygame
import pygameGUI # thank you max <3
import random

# print actions to the terminal
debug_mode = False

# pygame setup
pygame.init()
pygame.display.set_caption("Just Dodge")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screen_dims = (
    screen.get_width(), 
    screen.get_height()
)

# player vars
player_move_speed = 400
player_radius = 15
player_pos = pygame.Vector2(screen_dims[0]/2, screen_dims[1]/2)
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
menu_group = pygame.sprite.Group()
on_main_menu = True
font = pygame.font.Font("Rubik-VariableFont_wght.ttf", 70)

menu = pygameGUI.Menu(
    (47,86,214), 
    "Placeholder", 
    font, 
    500, 720,
    screen_dims[1]
); menu_group.add(menu)

play_button = pygameGUI.Text(
    "Play",
    font,
    (255,255,255),
    0, 0
); menu_group.add(play_button); menu.add(play_button)

# sprites
class Killbox(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
    
    def vert_lines_fullscreen(self):
        self.rect.x = 40
        self.rect.y = screen_dims[1]

    def horz_lines_fullscreen(self):
        self.rect.x = screen_dims[0]
        self.rect.y = 40

if debug_mode == True:
    print("\"Just Dodge\" vALPHA | Debug mode")
else:
    print("\"Just Dodge\" vALPHA")

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
        if event.type == pygame.MOUSEBUTTONUP:     
            pos = pygame.mouse.get_pos()     
            clickedSprites = [s for s in menu_group if s.rect.collidepoint(pos)]    
            if play_button in clickedSprites:     
                load()

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
        menu.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
