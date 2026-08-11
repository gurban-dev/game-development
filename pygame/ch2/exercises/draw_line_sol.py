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

# Import the pygame module.
import pygame

# Import the sys module so we can completely exit the program.
import sys

# Start all pygame modules.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the title shown at the top of the window.
pygame.display.set_caption("Triangle Exercise - Solution")

# Create some colors.
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Store the three corners of the triangle.
top_point = (400, 150)

# (0, 0) is the top-left corner of the screen.
# Increasing X moves an object to the right.
# Increasing Y moves an object down.

bottom_left_point = (250, 400)
bottom_right_point = (550, 400)

# Start the main game loop.
while True:

    # Fill the screen with a white background.
    screen.fill(WHITE)

    # Draw the first side of the triangle.
    # This line connects the top corner to the bottom-left corner.
    pygame.draw.line(
        screen,
        BLUE,
        top_point,
        bottom_left_point,
        4
    )

    # Draw the second side of the triangle.
    # This line connects the bottom-left corner to the bottom-right corner.
    pygame.draw.line(
        screen,
        BLUE,
        bottom_left_point,
        bottom_right_point,
        4
    )

    # Draw the third side of the triangle.
    # This line connects the bottom-right corner back to the top corner.
    pygame.draw.line(
        screen,
        BLUE,
        bottom_right_point,
        top_point,
        4
    )

    # Check every event that has occurred.
    for event in pygame.event.get():

        # Close the program if the user clicks the window's close button.
        if event.type == pygame.QUIT:

            # Shut down all pygame modules.
            pygame.quit()

            # Exit the Python program.
            sys.exit()

    # Update the entire display, unlike .update() which can
    # update specific regions.
    pygame.display.flip()