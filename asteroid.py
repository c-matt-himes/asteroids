import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            pass
        else:
            angle_split = random.uniform(20, 50)
            new_velo = self.velocity.rotate(angle_split)
            neg_new_velo = self.velocity.rotate(angle_split * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_1.velocity = new_velo * 1.2
            new_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_2.velocity = neg_new_velo * 1.2

            
        