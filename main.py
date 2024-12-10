import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()

    #add groups to player
    Player.containers = (updatable,drawable)
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT)/2)

    while True:
        #check if game is being closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
