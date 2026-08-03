import pygame
import sys

# Objective:
# Create a Pygame application that draws three ellipses on the display
# surface. Each ellipse should have a different colour, position, width,
# and height. Once you've completed the exercise, try arranging the
# ellipses so that together they resemble a simple object, such as a
# snowman, a caterpillar, or a pair of glasses.

# Initialize Pygame.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw Three Ellipses")

# Main game loop.
running = True

while running:
    # Check for events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white.
    screen.fill("white")

    # TODO:
    # Draw three ellipses here.

    # Each ellipse should have:
    # - A different colour.
    # - A different x-coordinate.
    # - A different y-coordinate.
    # - A different width.
    # - A different height.

    # Update the display.
    pygame.display.flip()

# Quit Pygame.
pygame.quit()
sys.exit()