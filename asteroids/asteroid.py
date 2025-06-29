import pygame
import random
from circleshape import CircleShape
import constants

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

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