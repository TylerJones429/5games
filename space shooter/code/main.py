import pygame
from os.path import join

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Game")
running = True

#plain surface
surf = pygame.Surface((100,200))
surf.fill("lightblue")
x = 100

#importing an image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surface.fill('darkgray')
    display_surface.blit(player_surf, (x,150))
    x += 0.1
    pygame.display.update()
pygame.quit()