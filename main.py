import pygame
from constants import *

def main():
    # pygame setup

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")

        # RENDER GAME HERE
        #
        # flip() the display to put your work on screen/refresh
        pygame.display.flip()
        
        clock.tick(60) # limits FPS to 60

if __name__ == "__main__":
    main()

