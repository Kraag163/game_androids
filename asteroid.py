import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (int(random.triangular(100, 255)),int(random.triangular(100, 255)),int(random.triangular(100, 255)))
        self.width = int(random.triangular(0,8))
        

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width = self.width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector_one * 1.5
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector_two * 1.3
        asteroid3 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid3.velocity = -vector_two