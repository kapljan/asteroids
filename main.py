import pygame
from constants import * #wildcard import, not recomended to use, but alright for this project
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_clock = pygame.time.Clock()
    dt = 0 #number of fps?

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (drawable, updatable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            #quits game if you press [X]
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for u in updatable:
            u.update(dt)
        
        for d in drawable:
            d.draw(screen)

        for asteroid in asteroids:
            if asteroid.is_coliding(p):
                print("Game over!")
                return

        #renders the screen
        pygame.display.flip()
        #param 60 means the game can't run above 60 fps
        dt = time_clock.tick(60) / 1000

if __name__ == "__main__":
    main()