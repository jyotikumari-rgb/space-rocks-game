
import pygame
from utils import load_sprite
import math


class Spaceship:
    def __init__(self, position, bullets):
        self.sprite = load_sprite("spaceship")
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(0, 0)
        self.angle = 0
        self.bullets = bullets
        self.radius = self.sprite.get_width() // 2

    def draw(self, surface):
        rotated_sprite = pygame.transform.rotate(self.sprite, -self.angle)
        rect = rotated_sprite.get_rect(center=self.position)
        surface.blit(rotated_sprite, rect)

    def move(self, surface):
        self.position += self.velocity
        self.position.x %= surface.get_width()
        self.position.y %= surface.get_height()

    def rotate(self, clockwise=True):
        if clockwise:
            self.angle += 5
        else:
            self.angle -= 5

    def accelerate(self):
        angle_rad = math.radians(self.angle)
        force = pygame.Vector2(math.cos(angle_rad), math.sin(angle_rad))
        self.velocity += force * 0.25

    def shoot(self):
        angle_rad = math.radians(self.angle)
        direction = pygame.Vector2(math.cos(angle_rad), math.sin(angle_rad))
        bullet_position = self.position + direction * self.radius
        bullet_velocity = self.velocity + direction * 5
        bullet = Bullet(bullet_position, bullet_velocity)
        self.bullets.append(bullet)

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius


class Bullet:
    def __init__(self, position, velocity):
        self.sprite = load_sprite("bullet")
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.radius = self.sprite.get_width() // 2

    def draw(self, surface):
        rect = self.sprite.get_rect(center=self.position)
        surface.blit(self.sprite, rect)

    def move(self, surface):
        self.position += self.velocity

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
