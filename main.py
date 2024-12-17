import pygame
from constants import * #wildcard import, not recomended to use, but alright for this project
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()
    dt = 0 #number of fps?

    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            #quits game if you press [X]
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        p.draw(screen)
        p.update(dt)

        #renders the screen
        pygame.display.flip()
        #param 60 means the game can't run above 60 fps
        dt = time_clock.tick(60) / 1000

if __name__ == "__main__":
    main()