

import pygame
from circleshape import CircleShape
import constants
import random

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
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        first = self.velocity.copy().rotate(angle)
        second = self.velocity.copy().rotate(-angle)
        newRadius = self.radius - constants.ASTEROID_MIN_RADIUS
        a = Asteroid(self.position.x, self.position.y, newRadius)
        b = Asteroid(self.position.x, self.position.y, newRadius)
        a.velocity = first * 1.2
        b.velocity = second * 1.2