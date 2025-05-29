import pygame
import pygame.gfxdraw
import random as r

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screen_dims = (
    screen.get_width(),
    screen.get_height()
)

p1_x = 0
p1_y = 0

p2_x = 590
p2_y = 300

p3_x = 1280
p3_x_lim = 1280
p3_x_rand = r.randint(-50,50)

p3_y = 720
p3_y_lim = 720
p3_y_rand = r.randint(-50,50)

I_GB = pygame.event.custom_type()
pygame.time.set_timer(I_GB, 10)

CLEAR = pygame.event.custom_type()
pygame.time.set_timer(CLEAR, 5000)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == I_GB:
            p2_x += r.randint(-50,50)
            p2_y += r.randint(-50,50)

            p3_x_rand = r.randint(-50,50)
            if p3_x_rand > p3_x_lim:
                p3_x = 1280
            else:
                p3_x = p3_x_rand
            
            p3_y_rand = r.randint(-50,50)
            if p3_y_rand > p3_y_lim:
                p3_y = 720
            else:
                p3_y = p3_y_rand

            pygame.draw.polygon(screen, (0,0,0), [(0,0), (1280,0), (1280,720), (0,720)], 0)
        
        if event.type == CLEAR:
            pygame.draw.polygon(screen, (0,0,0), [(0,0), (1280,0), (1280,720), (0,720)], 0)
            p2_x, p2_y, p3_x, p3_y = 590, 300, 1280, 720

    pygame.gfxdraw.bezier(screen, [(p1_x,p1_y), (p2_x,p2_y), (p3_x,p3_y)], 10, (255, 255, 255))

    pygame.display.flip()

    dt = clock.tick(60) / 1000
