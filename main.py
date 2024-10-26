
import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # This will break out of the main loop
        
        screen.fill(pygame.Color(0, 0, 0))
        p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        p.draw(screen)
        pygame.display.flip()
        lt = clock.tick(60)
        dt = lt / 1000

    pygame.quit()  # Properly close Pygame

if __name__ == "__main__":
    main()
    

