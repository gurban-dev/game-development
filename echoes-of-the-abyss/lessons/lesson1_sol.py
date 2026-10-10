# Import the Pygame library into this namespace so we can use
# its functions.
import pygame

# Initialize the Pygame modules.
pygame.init()

WIDTH = 800
HEIGHT = 600

# Create an 800-by-600 game window.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title displayed at the top of the window.
pygame.display.set_caption("Echoes of the Abyss")

# Create a clock to control the game's frame rate.
clock = pygame.time.Clock()

# Set the variable that will control the main game loop.
running = True