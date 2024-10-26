
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # This will break out of the main loop
        
        screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()

    pygame.quit()  # Properly close Pygame

if __name__ == "__main__":
    main()
    

