import pygame
import random
import math

image = pygame.image.load('PyGames/Asteroids/images/asteroid.png')
screen = pygame.display.set_mode((1280, 720))


def randStart():
    x = random.random() * 1280
    y = random.random() * 720
    return (x, y)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, dest):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = randStart()

        dx = dest[0] - self.rect.x
        dy = dest[1] - self.rect.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        self.velocity = pygame.Vector2(dx / distance, dy / distance)
        self.speed = 10

    def update(self):
        if self.rect.right < 0 or self.rect.left > screen.get_width() or self.rect.bottom < 0 or self.rect.top > screen.get_height():
            return
        self.rect.move_ip(self.velocity * self.speed)
        self.image = pygame.transform.rotate(self.image, 15)
