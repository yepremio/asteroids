import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    dt = 0

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.is_collision(shot):
                    shot.kill()
                    asteroid.split()
                    self.kill()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip() # display on screen/refresh
        clock.tick(60) # limits FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

