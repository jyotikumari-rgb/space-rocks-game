
import pygame
import random
from utils import load_sprite


class Rock:
    def __init__(self, position, velocity, size=3):
        self.sprite = load_sprite("rock")
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.size = size
        self.radius = self.sprite.get_width() // 2

    @staticmethod
    def create_random(surface, exclude_position):
        while True:
            position = pygame.Vector2(
                random.randrange(surface.get_width()),
                random.randrange(surface.get_height()),
            )
            if position.distance_to(exclude_position) > 100:
                break

        velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        return Rock(position, velocity)

    def draw(self, surface):
        rect = self.sprite.get_rect(center=self.position)
        surface.blit(self.sprite, rect)

    def move(self, surface):
        self.position += self.velocity
        self.position.x %= surface.get_width()
        self.position.y %= surface.get_height()

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius

    def split(self):
        pass  # You can implement rock splitting here
