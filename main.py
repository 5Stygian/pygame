'''
THE FOLLOWING IS NOT, AND SHOULD NOT BE TAKEN AS LEGAL ADVICE. WE ARE NOT A LAW FIRM, HOWEVER, 
IF YOU WOULD EVER REQUIRE ASSISTANCE FROM AN ACTUAL LAW FIRM, WOULD YOU LOOK NO FURTHER THAN THE EagleTeam. 
BECAUSE YOU DON'T JUST NEED A LEGAL TEAM, YOU NEED THE EagleTeam.

This code is licensed under the legally distinct Cool Code 0 v1.0 license (CC0 v1.0). This means that the 
following product is hereby declared to be viewed as the literal coolest thing you have ever seen. 
The writers, owners, and distributors of this code under the CC0 v1.0 license are automatically deemed 
as the most awesome people ever. Agreement to this statement is automatically triggered upon viewing or
interacting with a product actively utilizing this license. 

Because the creators of this code are the most awesome people ever, reuse of the code under the CC0 v1.0 license 
is fully allowed. Credit must be given to the original authors of the code, along with a link to the source code
itself. Products using code taken from a product using the CC0 v1.0 license must also use the CC0 v1.0 license.
'''

'''
CONTROLS:
wasd for movement
spacebar for dash
dont touch the red stuff
'''

import pygame
import pygameGUI # thank you max <3
import random
import datetime

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
start_time = datetime.datetime.now()

# player vars
player_move_speed = 400
player_radius = 10
player_rect = pygame.Rect(0, 0, player_radius*2, player_radius*2)
player_pos = pygame.Vector2(screen_dims[0]/2, screen_dims[1]/2)
dodge_dist = 5000
touchable = True

# functions
## general functions
# loads the game when the play button is clicked
def load():
    global on_main_menu
    on_main_menu = False
    debug("Play button clicked")

# ends the game
def Felo_Bit_Tool_Industrial_Bitholder_and_Driver_9_Pieces():
    global running
    running = False

# prints debugging info if debug_mode is true
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
rects = []
## killbox
class Killbox(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def vert_lines_fullscreen(self):
        # vlfs - vertical lines fullscreen
        debug("vlfs in class call 1")
        rects = []
        pygame.event.post(pygame.event.Event(KILLBOX_EVENT))
        for i in range(10):
            rect = pygame.Rect(150*i, 0, 60, screen_dims[1])
            pygame.draw.rect(screen, self.color, rect)
            rects.append(rect)
        debug("vlfs in class call 2")
        return rects
    
    def horz_lines_fullscreen(self):
        # hlfs - horizontal lines fullscreen
        debug("hlfs in class call 1")
        rects = []
        pygame.event.post(pygame.event.Event(KILLBOX_EVENT))
        for i in range(10):
            rect = pygame.Rect(0, 125*i, screen_dims[0], 60)
            pygame.draw.rect(screen, self.color, rect)
            rects.append(rect)
        debug("hlfs in class call 2")
        return rects

# killbox objects
vlfs = Killbox((214, 54, 101), 60, screen_dims[1])
hlfs = Killbox((214, 54, 101), screen_dims[0], 60)

vlfs_rect, hlfs_rect = [], []

if debug_mode == True:
    debug(f"\"Just Dodge\" vBETA | Debug mode ({screen_dims[0]}x{screen_dims[1]})")
else:
    print("\"Just Dodge\" vBETA")

# game loop
## custom events
# determines which killbox to spawn every 1.856 seconds
killbox_spawn = False
killbox_roll = 0
draw_bool = False

# events
telegraph_active = False
telegraph_type = None
telegraph_end_time = 0
telegraph_delay = 1800 # ms
KILLBOX_EVENT = pygame.event.custom_type()
DRAW_CHANCE = pygame.event.custom_type()
pygame.time.set_timer(DRAW_CHANCE, 1856)
## mainloop
while running:
    # poll for events
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
                if quit_button in clickedSprites: Felo_Bit_Tool_Industrial_Bitholder_and_Driver_9_Pieces()
        
        # killbox events
        if event.type == DRAW_CHANCE:
            if not on_main_menu:
                killbox_roll = random.randint(1, 10000)
                killbox_spawn = not killbox_spawn
                if killbox_roll in range(1, 2500):
                    debug(f"Vert lines telegraph {killbox_roll}")
                    telegraph_active = True
                    telegraph_type = 'vert'
                    telegraph_end_time = pygame.time.get_ticks() + telegraph_delay
                    pygame.time.set_timer(KILLBOX_EVENT, telegraph_delay, True)
                elif killbox_roll in range(2501, 5000):
                    debug(f"Horz lines telegraph {killbox_roll}")
                    telegraph_active = True
                    telegraph_type = 'horz'
                    telegraph_end_time = pygame.time.get_ticks() + telegraph_delay
                    pygame.time.set_timer(KILLBOX_EVENT, telegraph_delay, True)
                else:
                    debug(killbox_roll)

        # Remove the TELEGRAPH_EVENT handler entirely

        if event.type == KILLBOX_EVENT:
            if killbox_roll in range(1, 2500):
                vlfs_rect = vlfs.vert_lines_fullscreen()
            elif killbox_roll in range(2501, 5000):
                hlfs_rect = hlfs.horz_lines_fullscreen()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    # Draw telegraph if active
    if telegraph_active:
        if telegraph_type == 'vert':
            for i in range(10):
                pygame.draw.rect(screen, (112, 27, 53), (150*i, 0, 60, screen_dims[1]))
        elif telegraph_type == 'horz':
            for i in range(10):
                pygame.draw.rect(screen, (112, 27, 53), (0, 125*i, screen_dims[0], 60))
        # Disable telegraph after time is up
        if pygame.time.get_ticks() > telegraph_end_time:
            telegraph_active = False
            telegraph_type = None

    # player movement
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
    if not (0 < player_pos.x - player_radius):
        player_pos.x += abs(player_radius - player_pos.x)
    if not (player_pos.x + player_radius < screen.get_width()):
        player_pos.x -= abs(screen.get_width() - player_pos.x - player_radius)

    if not (0 < player_pos.y - player_radius):
        player_pos.y += abs(player_radius - player_pos.y)
    if not (player_pos.y + player_radius < screen.get_height()):
        player_pos.y -= abs(screen.get_height() - player_pos.y - player_radius)

    # g/ui
    if on_main_menu == True:
        menu.draw(screen)
    
    # player drawing and collision detection
    if on_main_menu == False:
        player = pygame.draw.circle(screen, "#6ddac0", player_pos, player_radius)
        # Only check collision and draw killboxes if telegraph is NOT active
        if not telegraph_active and (killbox_roll not in range(5001, 10000) and killbox_roll != 0):
            # Draw killboxes
            for v in vlfs_rect:
                pygame.draw.rect(screen, (214, 54, 101), v)
            for h in hlfs_rect:
                pygame.draw.rect(screen, (214, 54, 101), h)
            # Update player_rect position for collision
            player_rect.center = (int(player_pos.x), int(player_pos.y))
            if any(player_rect.colliderect(v) for v in vlfs_rect) or any(player_rect.colliderect(h) for h in hlfs_rect):
                vlfs_rect, hlfs_rect, rects = [], [], []
                player_pos = pygame.Vector2(screen_dims[0]/2, screen_dims[1]/2)
                killbox_roll = 0
                on_main_menu = True
                debug("Player collided with killbox")
    else:
        pass

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if debug_mode == True:
    print(f"{"Game closed":<50} | {time.strftime("%X %f")}  \n\ndurration (start - end): {start_time.strftime("%X %f")} - {time.strftime("%X %f")}\n")
pygame.quit()
