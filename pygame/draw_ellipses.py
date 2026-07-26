import pygame
import sys

# Goal:
# Learn how to use pygame.draw.ellipse() to draw ellipses.

# An ellipse is like a stretched or vertically squashed circle.

# The syntax for pygame.draw.ellipse():
# pygame.draw.ellipse(surface, color, rectangle, line_width)

# surface is the drawing area where the ellipse will appear.

# color is the RGB color that the ellipse will be.

# rectangle is an invisible rectangle that determines the
# ellipse's position and size.


# line_width: Controls how thick the border of the ellipse is.
# 0 (the default) fills the entire ellipse with the chosen colour.

# A number greater than 0, such as 1, 3, or 5, draws only the outline
# around the ellipse instead of filling it. Larger numbers make the
# outline thicker.

# Start all pygame modules.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# 'screen' is assigned a Surface object which represents the
# window in the Python program.

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

    # Begin drawing from 250 pixels to the right of the starting
    # point and 200 pixels down from the starting point.

    # Store the invisible rectangle that defines the boundaries
    # of the ellipse.
    ellipse_rectangle = (250, 200, 300, 150)

    # Unlike pygame.draw.circle(), .ellipse() does not accept
    # a center value.

    # Pygame draws the ellipse inside this invisible rectangle,
    # which determines its position and size.

    # The second argument, BLUE, specifies the color the ellipse
    # will be filled with.

    # The fourth argument is the line width of the ellipse.
    pygame.draw.ellipse(screen, BLUE, ellipse_rectangle, 10)

    # Check every event that has occurred.
    for event in pygame.event.get():

        # Close the program if the user clicks the window's close button.
        if event.type == pygame.QUIT:

            # Shut down all pygame modules.
            pygame.quit()

            # Exit the Python program.
            sys.exit()

    # Use pygame.display.update() when only a region of the screen
    # needs to be updated.

    # Update the entire display since the entire screen is
    # redrawn every frame.
    pygame.display.flip()