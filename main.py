import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

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

        for a in asteroids:
            has_collided = a.check_collisions(player)
            if has_collided:
                print("Game Over!")
                sys.exit()

        for d in drawable:
            d.draw(screen)

        #handle asteroid destruction
        for a in asteroids:
            for s in shots:
                if s.check_collisions(a):
                    a.split()
                    s.kill()

        pygame.display.flip()

        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
