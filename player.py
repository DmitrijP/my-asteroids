
import pygame
from circleshape import CircleShape
import constants


class Player(CircleShape):
    rotation = 0
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        super().__init__(x, y, constants.PLAYER_RADIUS)
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 
                            pygame.Color(255,255,255),
                            self.triangle(), 
                            2)
        return super().draw(screen)
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        
        if keys[pygame.K_d]:
            self.rotate(dt)