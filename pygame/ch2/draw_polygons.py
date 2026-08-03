# A Polygon is a shape made from multiple straight lines.

# Examples:
# Triangle (three points)
# Square (four points)
# Pentagon (five points)

# A polygon is created by providing Pygame with a list of
# coordinate points.

# Import the pygame module.
import pygame

# Import the sys module so we can completely exit the program.
import sys

# Start all pygame modules.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the title shown at the top of the window.
pygame.display.set_caption("Polygon Spaceship")

# Create some colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# (0, 0) is the top-left corner of the screen.
# Increasing X moves an object to the right.
# Increasing Y moves an object down.

# Store the top point of the spaceship nose.

# 400 pixels to the right is horizontally centered since the
# window width is 800 pixels.
top_point = (400, 100)

# Store the bottom-left point of the spaceship nose.
left_point = (300, 300)

# Store the bottom-right point of the spaceship nose.
right_point = (500, 300)

# The order of the points matters.
# Pygame draws lines from one point to the next.
spaceship_points = [
    top_point,
    left_point,
    right_point
]

# For visualisation:
# spaceship_points = [
#     (400, 100),
#     (300, 300),
#     (500, 300)
# ]

# Start the main game loop.
while True:

    # Fill the screen with a white background.
    screen.fill(WHITE)

    # polygon() function signature from Pygame's draw module:
    # pygame.draw.polygon(surface, color, points, width=0)

    # Drawing on the screen Surface, use red and use these
    # coordinates to construct the polygon.

    # Leaving out the width argument fills the polygon.

    # Pygame connects each point with a straight line.
    # It also connects the last point back to the first point.
    pygame.draw.polygon(screen, RED, spaceship_points)

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