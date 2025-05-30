import pygame # type: ignore
import pygame.gfxdraw # type: ignore
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

p0x = 0
p0y = 0

p1x = 400
p1y = 500

p2x = screen_dims[0]
p2y = screen_dims[1]

I_GB = pygame.event.custom_type()
pygame.time.set_timer(I_GB, 1000, loops=10)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == I_GB:
        p0y = r.randint(0, 720)
        if p0y > 720:
            p0y = 720

        p2y = r.randint(0, 720)
        if p2y > 720:
            p2y = 720
            
        p1x = r.randint(0, 1280)
        if p1x > 1280:
            p1x = 1280
        p1y = r.randint(0, 720)
        if p1y > 720:
            p1y = 720
        
        screen.fill("black")
        pygame.gfxdraw.bezier(screen, [(p0x,p0y), (p1x,p1y), (p2x,p2y)], 2, (255,255,255))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()