'''
THE FOLLOWING IS NOT, AND SHOULD NOT BE TAKEN AS LEGAL ADVICE. WE ARE NOT A LAW FIRM, HOWEVER, 
IF YOU WOULD EVER REQUIRE ASSISTANCE FROM AN ACTUAL LAW FIRM, WOULD YOU LOOK NO FURTHER THAN THE EagleTeam. 
BECAUSE YOU DON'T JUST NEED A LEGAL TEAM, YOU NEED THE EagleTeam.

This code is liscenced under the legally distinct Cool Code 0 v1.0 licence (CC0 v1.0). This means that the 
following product is hereby declared to be viewed as the litteral coolest thing you have ever seen. 
The writers, owners, and distributers of this code under the CC0 v1.0 license are automatically deemed 
as the most awesome people ever. Agreement to this statement is automaticly triggered upon viewing or
interacting with a product actively utilizing this license. 

Because the creators of this code are the most awesome people ever, reuse of the code under the CC0 v1.0 license 
is fully allowed. Credit must be given to the original authors of the code, along with a link to the source code
itself. Products using code taken from a product using the CC0 v1.0 license must also use the CC0 v1.0 license.
'''

import pygame
import pygameGUI # thank you max <3
import random
import datetime

# print actions to the terminal
debug_mode = True

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
start_time = datetime.datetime.now()

# player vars
player_move_speed = 400
player_radius = 15
player_pos = pygame.Vector2(screen_dims[0]/2, screen_dims[1]/2)
dodge_dist = 5000
touchable = True

# functions
## general functions
def load():
    global on_main_menu
    on_main_menu = False
    debug("Play button clicked")

def debug(debug):
    global time
    time = datetime.datetime.now()

    if debug_mode == True:
        print(f"{debug:<50} | {time.strftime("%X %f")}")
    else:
        pass

## difficulty functions
# these control spawn rate of killboxes and score gained
def start_easy():
    global difficulty
    difficulty = 1
    load()
    debug("Easy mode")

def start_medium():
    global difficulty
    difficulty = 2
    load()
    debug("Medium mode")

def start_hard():
    global difficulty
    difficulty = 3
    load()
    debug("Hard mode")

# g/ui
## main menu
menu_group = pygame.sprite.Group()
on_main_menu = True
font = pygame.font.Font("Rubik-VariableFont_wght.ttf", 70)

menu = pygameGUI.Menu(
    "Placeholder",
    (255, 255, 255),
    font, 
    500, 720,
    (47, 86, 214), 
    image=None,
    pos=(0, 0),
    hrcolor=(33, 61, 156)
); menu_group.add(menu)

play_button = pygameGUI.Text(
    "Play",
    font,
    (255, 255, 255),
    (0, 0)
); menu_group.add(play_button); menu.add(play_button)

quit_button = pygameGUI.Text(
    "Quit",
    font,
    (255,255,255),
    (0, 0)
); menu_group.add(quit_button); menu.add(quit_button)

# sprites
## killbox
class Killbox(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def vert_lines_fullscreen(self):
        # vlfs - vertical lines fullscreen
        for i in range(10):
            self.vlfs = pygame.rect.Rect(150*i, 0, 60, screen_dims[1])
            pygame.draw.rect(screen, self.color, self.vlfs)
        debug("Vert lines spawned")
    
    def horz_lines_fullscreen(self):
        debug("Horz lines spawned")

# killbox objects
vlfs = Killbox((214, 54, 101), 60, screen_dims[1])

if debug_mode == True:
    debug(f"\"Just Dodge\" vALPHA | Debug mode ({screen_dims[0]}x{screen_dims[1]})")
else:
    debug("\"Just Dodge\" vALPHA")

# game loop
## costom events
# determines which killbox to spawnm every second
killbox_spawn = 0
draw_bool = False
DRAW_CHANCE = pygame.event.custom_type()
pygame.time.set_timer(DRAW_CHANCE, 1000)
## mainloop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # dodge in the direction you are currently moving
            if event.key == pygame.K_SPACE and keys[pygame.K_w]:
                touchable = False
                player_pos.y -= dodge_dist * dt
                touchable = True
                debug("Dodge executed | up")
            if event.key == pygame.K_SPACE and keys[pygame.K_s]:
                touchable = False
                player_pos.y += dodge_dist * dt
                touchable = True
                debug("Dodge executed | down")
            if event.key == pygame.K_SPACE and keys[pygame.K_a]:
                touchable = False
                player_pos.x -= dodge_dist * dt
                touchable = True
                debug("Dodge executed | left")
            if event.key == pygame.K_SPACE and keys[pygame.K_d]:
                touchable = False
                player_pos.x += dodge_dist * dt
                touchable = True
                debug("Dodge executed | right")
        
        # gui events
        if event.type == pygame.MOUSEBUTTONUP:     
            pos = pygame.mouse.get_pos()     
            clickedSprites = [s for s in menu_group if s.rect.collidepoint(pos)]
            if on_main_menu == True:    
                if play_button in clickedSprites: load()
                if quit_button in clickedSprites: running = False
        
        # killbox events
        if event.type == DRAW_CHANCE:
            if on_main_menu == False:
                if draw_bool == True:
                    killbox_spawn = random.randint(1,10000)
                elif draw_bool == False:
                    pass
                draw_bool = False
                debug("Killbox spawn rolled")
            
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # player start
    # loads the player when a difficulty is selected
    if on_main_menu == False:
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

    # killbox spawning
    if on_main_menu == False:
        if killbox_spawn in range(1, 5001):
            debug("Vert lines spawned")
            vlfs.vert_lines_fullscreen()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

if debug_mode == True:
    print(f"{"Game closed":<50} | {time.strftime("%X %f")}  \n\ndurration (start - end): {start_time.strftime("%X %f")} - {time.strftime("%X %f")}")
pygame.quit()