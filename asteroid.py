

import pygame
from circleshape import CircleShape
import constants


class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        super().__init__(x, y, self.radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface= screen, 
                           color= "white",
                           radius=self.radius,
                           center=self.position,
                           width=2)
        return super().draw(screen)
    
    def update(self, dt):
        self.position += dt * self.velocity 
        return super().update(dt)
    
    def split(self):
        self.kill()