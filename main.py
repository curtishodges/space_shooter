import pygame
from os.path import join
from random import randint


#General Game Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
pygame.display.set_caption("Astriods")

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()

# Plain surface
surf = pygame.Surface((100,200))
surf.fill("purple")

# Player Surface
player_surf = pygame.image.load(join("images", "player.png")).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = 1

# Background
bg_color = "darkgray"
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]


# Meteors
meteror_surf = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteror_rect = meteror_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Laser Import
laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = meteror_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

# Game Loop

while running:

    clock.tick(60)

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing Game Start
    display_surface.fill(bg_color)

    # Generate stars in random positions using star_positions
    for star in star_positions:
        display_surface.blit(star_surf, star)

    # Meteor
    display_surface.blit(meteror_surf, meteror_rect)

    # Laser
    display_surface.blit(laser_surf, laser_rect)

    # Player Movement
    player_rect.x += player_direction * 0.4
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction *= -1
    display_surface.blit(player_surf, player_rect)


    pygame.display.update()



pygame.quit()