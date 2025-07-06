import pygame
import random
import math
from circleshape import CircleShape
import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shape_offsets = self.generate_shape()
    
    def generate_shape(self, num_points=12, jaggedness=0.4):
        # jaggedness = % of radius to deviate in/out
        offsets = []
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            # Randomize radius a bit for jagged look
            deviation = random.uniform(1 - jaggedness, 1 + jaggedness)
            r = self.radius * deviation
            x = math.cos(angle) * r
            y = math.sin(angle) * r
            offsets.append(pygame.Vector2(x, y))
        return offsets

    def draw(self, screen):
        points = [self.position + offset for offset in self.shape_offsets]
        pygame.draw.polygon(screen, "white", points, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector_1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_vector_2 * 1.2