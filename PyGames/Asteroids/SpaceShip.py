import pygame
import math

player_image = pygame.image.load("PyGames/Asteroids/images/Hero.png")

screen = pygame.display.set_mode((1280, 720))


class SpaceShip(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, position):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = player_image
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = pygame.Vector2(0, 0)  # Initial speed vector
        self.acceleration = 5000  # Acceleration rate

    def point_at(self, x, y):
        angle = math.degrees(math.atan2(
            y - self.rect.centery, x - self.rect.centerx))
        self.image = pygame.transform.rotate(player_image, -angle)

    def wrap_around_screen(self):
        # Wrap horizontally
        if self.rect.right < 0:
            self.rect.left = 0
        elif self.rect.left > screen.get_width():
            self.rect.right = 0

        # Wrap vertically
        if self.rect.bottom < 0:
            self.rect.top = screen.get_height()
        elif self.rect.top > screen.get_height():
            self.rect.bottom = 0

    def move(self, keys, dt):
        self.speed *= 0.95  # Apply friction
        # Update speed based on key inputs
        if keys[pygame.K_w]:
            self.speed.y -= self.acceleration * dt
        if keys[pygame.K_s]:
            self.speed.y += self.acceleration * dt
        if keys[pygame.K_a]:
            self.speed.x -= self.acceleration * dt
        if keys[pygame.K_d]:
            self.speed.x += self.acceleration * dt

        # Update position based on speed
        self.rect.x += self.speed.x * dt
        self.rect.y += self.speed.y * dt

        self.wrap_around_screen()

    def shoot(self, x, y):
        frame_index = 0
        while frame_index < self.bullet_steps:
            screen.blit(self.animation_list[frame_index], (x, y))
            pygame.display.flip()
            # Adjust the delay as needed for desired frame rate
            pygame.time.delay(100)
            frame_index += 1
