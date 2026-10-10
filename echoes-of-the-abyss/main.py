import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Echoes of the Abyss")

# Create a clock to control the game's frame rate.
clock = pygame.time.Clock()

running = True