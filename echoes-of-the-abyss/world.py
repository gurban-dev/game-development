import pygame


class World:
    def __init__(self):
        self.walls = [
            pygame.Rect(350, 200, 150, 200)
        ]

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(
                screen,
                (110, 110, 130),
                wall
            )