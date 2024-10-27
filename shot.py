

import pygame
from circleshape import CircleShape
import constants


class Shot(CircleShape):
    containers = ()
   
    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2):
        super().__init__(position.x, position.y, constants.SHOT_RADIUS)
        self.position = position
        self.velocity = velocity
        for group in self.containers:
            group.add(self)

    
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