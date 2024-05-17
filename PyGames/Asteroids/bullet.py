import pygame
import math

bullet_sheet = pygame.image.load(
    "PyGames/Asteroids/images/bulletAnimation.png")
frame_height = 16
frame_width = 16
frames = 11
list = []

for i in range(frames):
    frame_rect = pygame.Rect(0, i * frame_height, frame_width, frame_height)
    list.append(bullet_sheet.subsurface(frame_rect))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, dest):
        super().__init__()
        self.image = list[0]
        self.rect = self.image.get_rect()
        self.rect.center = position
        dx = dest[0] - position[0]
        dy = dest[1] - position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        self.velocity = pygame.Vector2(dx / distance, dy / distance)

        self.frame_index = 0
        self.speed = 20

    def update(self):
        self.rect.move_ip(self.velocity * self.speed)
        self.image = list[self.frame_index]
        self.frame_index = (self.frame_index + 1) % frames
        self.point_at(self.velocity.x, self.velocity.y)

    def point_at(self, x, y):
        angle = math.degrees(math.atan2(y, x)) - 90
        self.image = pygame.transform.rotate(list[self.frame_index], -angle)
