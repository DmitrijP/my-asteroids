
import sys
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    running = True
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af = AsteroidField()
    
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for obj in updatable:
            obj.update(dt)
            for a in asteroids:
                pc = a.collision(p)
                gameOver(pc)
                asteroidShotCollision(shots, a)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()

def gameOver(pc):
    if pc:
        print("Game over!")
        sys.exit() 

def asteroidShotCollision(shots, a):
    for s in shots:
        sc = a.collision(s)
        if sc:
            s.kill()
            a.split()

if __name__ == "__main__":
    main()
    

