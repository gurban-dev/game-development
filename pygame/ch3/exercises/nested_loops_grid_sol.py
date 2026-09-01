import pygame
import sys

# Grid Builder Exercise.

# This exercise practices nested loops and grid positioning.
# The constants control the size, spacing, and position of the grid.
# The loops use those constants to draw every square automatically.

# Start every Pygame module.
pygame.init()

# Create an 800 by 600 pixel game window.
# set_mode() returns a Surface object.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Grid Builder Exercise")

# Create a Clock object for controlling the frame rate.
clock = pygame.time.Clock()

# Define the background and square colours.
BACKGROUND_COLOR = (40, 40, 40)
SQUARE_COLOR = (255, 200, 0)

# Define the number of rows and columns in the grid.
NO_OF_ROWS = 8
NO_OF_COLUMNS = 5

# Define the width and height of every square.
BOX_SIZE = 40

# Define the space between each square.
GAP = 25

# Define the position where the grid begins.
START_X = 250
START_Y = 50

# Keep the game running until the window is closed.
running = True

while running:

    # Check for events such as closing the window.
    for event in pygame.event.get():

        # Stop the program when the player closes the window.
        if event.type == pygame.QUIT:
            running = False

    # Fill the entire window with the background colour.
    screen.fill(BACKGROUND_COLOR)

    # Go through every row in the grid.
    for row in range(NO_OF_ROWS):

        # Go through every column in the current row.
        for column in range(NO_OF_COLUMNS):

            # Calculate the horizontal pixel position.
            # Each column moves by the box size plus the gap.
            x = START_X + column * (BOX_SIZE + GAP)

            # Calculate the vertical pixel position.
            # Each row moves by the box size plus the gap.
            y = START_Y + row * (BOX_SIZE + GAP)

            # Print the actual pixel position of the square.
            print(f"x: {x}, y: {y}")

            # Draw the square at its calculated position.
            pygame.draw.rect(
                screen,
                SQUARE_COLOR,
                (x, y, BOX_SIZE, BOX_SIZE)
            )

    # -Update only certain parts of the window so the new frame
    # is displayed.
    # flip() updates the entire window.
    pygame.display.update()

    # Limit the program to 60 frames per second.
    clock.tick(60)

# Shut down Pygame after the loop ends.
pygame.quit()

# Close the Python program.
sys.exit()