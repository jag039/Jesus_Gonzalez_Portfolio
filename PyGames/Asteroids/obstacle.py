import pygame
import random
import math

image = pygame.image.load('PyGames/Asteroids/images/asteroid.png')


def randStart():
    x = random.random() * 1280
    y = random.random()
    if y<0.5:
        y=0
    else:
        y=720
    return (x, y)

def randSize():
    x = random.random()
    if x<0.21:
        x=32
    else:
        x = x * 150
    return (x,x)

def randAngle():
    return random.random() * 360



class Obstacle(pygame.sprite.Sprite):
    def __init__(self, dest, screen):
        super().__init__()
        self.image = pygame.transform.scale(image, randSize())
        self.image = pygame.transform.rotate(self.image, randAngle())
        self.rect = self.image.get_rect()
        self.rect.center = randStart()
        self.screen = screen

        dx = dest[0] - self.rect.x
        dy = dest[1] - self.rect.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        self.velocity = pygame.Vector2(dx / distance, dy / distance)
        self.speed = 10

    def update(self):
        if self.rect.right < 0 or self.rect.left > self.screen.get_width() or self.rect.bottom < 0 or self.rect.top > self.screen.get_height():
            self.kill()
            return
        self.rect.move_ip(self.velocity * self.speed)
        self.speed += 1
