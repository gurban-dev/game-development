# Import the pygame module.
import pygame

# Import the sys module.
import sys

# Objective:
# Build your own robot using only Pygame's drawing functions.

# Requirements:
# Your robot must use all of the following drawing functions
# at least once.

# □ pygame.draw.rect()
#     Draw the robot's head.

# □ pygame.draw.polygon()
#     Draw the robot's body.

# □ pygame.draw.circle()
#     Draw two eyes.

# □ pygame.draw.line()
#     Draw an antenna on top of the robot's head.

# □ pygame.draw.ellipse()
#     Draw three vertically stacked energy beams beneath
#     the robot so that it appears to be floating.

#     The top beam should be the largest.
#     The middle beam should be smaller.
#     The bottom beam should be the smallest.

# Draw everything after:
#     screen.fill(BLACK)

# and before:
#     pygame.display.update()

# Start pygame.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Robot Exercise")

# Define some colours.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (170, 170, 170)
BLUE = (50, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Start the game loop.
while True:

    # Look for events.
    for event in pygame.event.get():

        # Close the window if needed.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background.
    screen.fill(BLACK)

    # -----------------------------
    # Draw your robot here.
    # -----------------------------

    # Show everything on the screen.
    pygame.display.update()