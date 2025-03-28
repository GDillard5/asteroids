from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",center=self.position,radius=self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            spawn_vector1 = self.velocity.rotate(random_angle)
            spawn_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            spawn_asteroid1 = Asteroid(self.position[0],self.position[1],new_radius)
            spawn_asteroid1.velocity = spawn_vector1 * 1.2
            spawn_asteroid2 = Asteroid(self.position[0],self.position[1],new_radius)
            spawn_asteroid2.velocity = spawn_vector2 * 1.2
        self.kill()
