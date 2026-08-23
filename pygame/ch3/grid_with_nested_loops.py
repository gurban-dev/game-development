import pygame
import sys

# Learning goal:
# Understand how nested for loops can create a grid of objects.
# Use row and column numbers to calculate the position of each square.
# Understand how constants control the size, spacing, and position of the grid.

# Start every Pygame module.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the title shown at the top of the window.
pygame.display.set_caption("Nested Loops Grid")

# Create a Clock object.
clock = pygame.time.Clock()

# Define some colours.
WHITE = (255, 255, 255)
NAVY = (30, 50, 100)
LIGHT_BLUE = (100, 180, 255)

# Define the grid.
NO_OF_ROWS = 5
NO_OF_COLUMNS = 8

# Define the size of each square.
BOX_SIZE = 60

# Define the gap between each square.
GAP = 10

# Position where the grid begins.
START_X = 80
START_Y = 80

# Keep the game running.
running = True

while running:

    # Check for events.
    for event in pygame.event.get():

        # Close the program if the player clicks the X button.
        if event.type == pygame.QUIT:
            running = False

    # Fill the background.
    screen.fill(NAVY)

    # Go through every row.
    for row in range(NO_OF_ROWS):

        # Go through every column.
        for column in range(NO_OF_COLUMNS):

            # Calculate the x position.
            x = START_X + column * (BOX_SIZE + GAP)

            # Calculate the y position.
            y = START_Y + row * (BOX_SIZE + GAP)

            # Draw one square.
            pygame.draw.rect(
                screen,
                LIGHT_BLUE,
                (x, y, BOX_SIZE, BOX_SIZE)
            )

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()