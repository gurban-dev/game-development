import pygame
import sys

# Goal:
# Learn how to use pygame.draw.ellipse() to draw ellipses.

# An ellipse is like a stretched or vertically squashed circle.

# The syntax for pygame.draw.ellipse():
# pygame.draw.ellipse(surface, color, rectangle)

# surface is where to draw (usually screen)
# color is the RGB color.
# rectangle is an invisible rectangle that determines the
# ellipse's position and size.

# Start all pygame modules.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the title shown at the top of the window.
pygame.display.set_caption("Drawing an Ellipse")

# Create some colors.
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Start the main game loop.
while True:

    # Fill the screen with a white background.
    screen.fill(WHITE)

    # The rectangle is stored as:
    # (x, y, width, height)

    # In the tuple below:
    # 250 is the X-coordinate.
    # 200 is the Y-coordinate.
    # 300 is the width.
    # 150 is the height.

    # Store the invisible rectangle that defines the ellipse.
    ellipse_rectangle = (250, 200, 300, 150)

    # Pygame draws the ellipse inside this invisible rectangle,
    # which determines its position and size.
    pygame.draw.ellipse(screen, BLUE, ellipse_rectangle)

    # Check every event that has occurred.
    for event in pygame.event.get():

        # Close the program if the user clicks the window's close button.
        if event.type == pygame.QUIT:

            # Shut down all pygame modules.
            pygame.quit()

            # Exit the Python program.
            sys.exit()

    # Update the entire display since the entire screen is
    # redrawn every frame.
    pygame.display.flip()