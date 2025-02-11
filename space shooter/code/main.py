import pygame
from random import randint
from os.path import join

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Game")
running = True
clock = pygame.time.Clock()

star_positions = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20)]
player_direction = pygame.math.Vector2(1,1)
player_speed = 300


#imports
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20,WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick(60) / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    display_surface.fill('darkgray')
    
    #draw stars
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    #player movement
    player_rect.center += player_direction * player_speed * dt
    if player_rect.left < 0 or player_rect.right > WINDOW_WIDTH:
        player_direction[0] *= -1
    if player_rect.top < 0 or player_rect.bottom > WINDOW_HEIGHT:
        player_direction[1] *= -1
    display_surface.blit(player_surf, player_rect)

    display_surface.blit(meteor_surf,meteor_rect)
    display_surface.blit(laser_surf,laser_rect)
    pygame.display.update()
pygame.quit()