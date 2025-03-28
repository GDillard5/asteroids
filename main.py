import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color='black')
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game Over!")
                exit()
            for shot in shots:
                if asteroid.checkCollision(shot):
                    asteroid.split()
                    shot.kill()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
