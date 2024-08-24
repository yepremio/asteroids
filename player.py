import pygame
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y, radius, position=None, rotation=0):
        super.__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.rotation = rotation


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
