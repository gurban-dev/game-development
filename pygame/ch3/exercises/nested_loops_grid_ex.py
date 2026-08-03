import pygame
import sys

# Grid Builder Exercise

# Complete each task without changing the nested for loops.

# 1. Change the grid to 8 rows and 5 columns.

# 2. Change each square to 40 × 40 pixels.

# 3. Increase the gap between each square to 25 pixels.

# 4. Move the grid so it starts at (50, 150).

# 5. Choose your own background colour.

# 6. Choose your own square colour.

# 7. Instead of printing the row and column, print the pixel position
#    of each square using:
#    print(f"x = {x}, y = {y}")


# Bonus Challenge
# Create a grid with 10 columns and 8 rows that still fits completely
# inside the window. You may only change these constants:

# • ROWS
# • COLUMNS
# • BOX_SIZE
# • GAP
# • START_X
# • START_Y

# Do not change the nested for loops or the code that draws the
# squares.

# Start every Pygame module.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Grid Builder Exercise")

# Create a Clock object.
clock = pygame.time.Clock()

# Define some colours.
BACKGROUND = (40, 40, 40)
SQUARE = (255, 200, 0)

# Define the grid.
ROWS = 6
COLUMNS = 6

# Define the size of each square.
BOX_SIZE = 50

# Define the gap between each square.
GAP = 20

# Position where the grid begins.
START_X = 150
START_Y = 100

# Keep the game running.
running = True

while running:

    # Check for events.
    for event in pygame.event.get():

        # Close the program if the player clicks the X button.
        if event.type == pygame.QUIT:
            running = False

    # Fill the background.
    screen.fill(BACKGROUND)

    # Go through every row.
    for row in range(ROWS):

        # Go through every column.
        for column in range(COLUMNS):

            # Calculate the x position.
            x = START_X + column * (BOX_SIZE + GAP)

            # Calculate the y position.
            y = START_Y + row * (BOX_SIZE + GAP)

            # Print the current row and column.
            print(f"Row: {row}, Column: {column}")

            # Draw one square.
            pygame.draw.rect(
                screen,
                SQUARE,
                (x, y, BOX_SIZE, BOX_SIZE)
            )

    # Update the display.
    pygame.display.update()

    # Limit the game to 60 frames per second.
    clock.tick(60)

# Quit Pygame.
pygame.quit()

# Close the program.
sys.exit()