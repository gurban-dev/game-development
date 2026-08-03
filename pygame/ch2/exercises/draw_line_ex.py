'''
Draw a Triangle Using Three Lines

Objective:
Use pygame.draw.line() three times to create a triangle.

Requirements:
• Use three separate pygame.draw.line() calls.
• Make each line 4 pixels thick.
• Use the provided color BLUE.
• The three lines should connect to form a triangle.
'''

# Starter code:

# Import the pygame module.
import pygame

# Import the sys module so we can completely exit the program.
import sys

# Start all pygame modules.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Change the title shown at the top of the window.
pygame.display.set_caption("Triangle Exercise")

# Create some colors.
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Start the main game loop.
while True:

    # Fill the screen with white.
    screen.fill(WHITE)

    # TODO:
    # Draw the first side of the triangle.

    # TODO:
    # Draw the second side of the triangle.

    # TODO:
    # Draw the third side of the triangle.

    # Check every event.
    for event in pygame.event.get():

        # Close the program if the window is closed.
        if event.type == pygame.QUIT:
            pygame.quit()

            # Exit the Python program.
            sys.exit()

    # Update the display.
    pygame.display.flip()