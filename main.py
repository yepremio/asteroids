import pygame
from constants import *
from player import Player

def main():

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 

    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        # RENDER GAME HERE
        player.draw(screen)

        pygame.display.flip() # display on screen/refresh
        clock.tick(60) # limits FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

