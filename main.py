import pygame
from constants import *

def main():

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True


    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        # RENDER GAME HERE
        # flip() the display to put your work on screen/refresh
        
        pygame.display.flip()
        
        clock.tick(60) # limits FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

