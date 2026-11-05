from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)

    def draw(self, screen, color = (255,255,255)):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
