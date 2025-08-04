import pygame # type: ignore
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
x = 100

# Player Surface
player_surf = pygame.image.load(join("images", "player.png")).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2()
player_speed = 300

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

    dt = clock.tick() / 1000

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    
    # Input
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

    player_rect.center += player_direction * player_speed * dt

    # Drawing Game Start
    display_surface.fill(bg_color)

    # Generate stars in random positions using star_positions
    for star in star_positions:
        display_surface.blit(star_surf, star)

    # Meteor
    display_surface.blit(meteror_surf, meteror_rect)

    # Laser
    display_surface.blit(laser_surf, laser_rect)


    
    display_surface.blit(player_surf, player_rect)


    pygame.display.update()



pygame.quit()