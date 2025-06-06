import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return

        updatables.update(dt)
        # Handle player input
        for asteroid in asteroids:
            if asteroid.collide_with(player):
                print("Game Over")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide_with(shot):
                    shot.kill()
                    asteroid.split(asteroids)

        screen.fill("black")
        
        for sprite in drawables:
            sprite.draw(screen)

        
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
