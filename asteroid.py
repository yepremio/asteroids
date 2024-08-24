import pygame
from pygame.draw import line
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position(), 2)

    def update(self, dt):
        velocity * dt to it's position
            move straight line
