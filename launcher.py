import pygame
import pygame_gui

# pygame setup
pygame.init()
pygame.display.set_caption("Game Launcher")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
screen_dims = (screen.get_width(), screen.get_height())

# g/ui
manager = pygame_gui.UIManager((screen_dims[0], screen_dims[1]), theme_path="theme_basic.json")

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen_dims[0]/2-50, screen_dims[1]/2), (100, 50)),
                                           text='Play',
                                           manager=manager,
                                           command=load)

# game loop
while running:
    for event in pygame.event.get():
        manager.process_events(event)
        if event.type == pygame.QUIT:
            running = False

    # update screen
    screen.fill("black")
    
    manager.update(dt)
    manager.draw_ui(screen)
    
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000

pygame.quit()
