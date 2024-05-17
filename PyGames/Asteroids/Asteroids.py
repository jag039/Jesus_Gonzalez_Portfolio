# Example file showing a basic pygame "game loop"
import pygame
import math
from SpaceShip import SpaceShip
from bullet import Bullet
from obstacle import Obstacle

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
bg = pygame.image.load("PyGames/Asteroids/images/Background.png").convert()
bg = pygame.transform.scale(bg, (1280, 720))
# DEFINING MAIN VARIABLES IN SCROLLING
scroll = 0
# HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING
tiles = math.ceil(1280 / bg.get_width()) + 1

# Setting up the player
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = SpaceShip(player_pos)


# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
projectiles = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

while running:
    i = 0
    while (i < tiles):
        screen.blit(bg, (bg.get_width()*i + scroll, 0))
        i += 1
     # FRAME FOR SCROLLING
    scroll -= 6

    # RESET THE SCROLL FRAME
    if abs(scroll) > bg.get_width():
        scroll = 0

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            player.point_at(*pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet((player.rect.x, player.rect.y + 15),
                            pygame.mouse.get_pos())
            projectiles.add(bullet)
            asteroid = Obstacle((player.rect.x, player.rect.y + 15))
            asteroids.add(asteroid)

    dt = clock.tick(60)/1000  # limits FPS to 60
    # fill the screen with a color to wipe away anything from last frame

    num = projectiles.update()
    asteroids.update()
    projectiles.draw(screen)
    all_sprites.draw(screen)
    asteroids.draw(screen)

    keys = pygame.key.get_pressed()
    player.move(keys, dt)

    pygame.display.flip()

    dt = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()
