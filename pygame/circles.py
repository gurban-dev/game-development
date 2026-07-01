import pygame
import sys
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Circles")

# Goal:
# Learn how to:
# 1. Draw a circle using pygame.draw.circle().
# 2. Choose a colour for a circle.
# 3. Position a circle using its centre coordinates.
# 4. Change the size of a circle by adjusting its radius.

# Syntax:
# pygame.draw.circle(surface_obj, colour, centre, radius)

# A surface object is something that Pygame can draw on.
# In this program, the surface is the game window,
# which is stored in the screen variable.

# The centre parameter specifies the (x, y) coordinates of
# the middle of the circle.

# Unlike rectangles, circles are positioned using the coordinates
# of their centre.

# To centre the circle:

# Use integer division (//) so the result is a whole number.
# Screen coordinates should be integers.
x_pos = screen_width // 2

y_pos = screen_height // 2

# The radius is the distance from the centre of the circle
# to its edge.

# Colours are represented using RGB values:
# (Red, Green, Blue)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

radius = 200

running = True

while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

    # Fill the screen with black before drawing the next frame.
    screen.fill(BLACK)

    pygame.draw.circle(
        screen,
        GREEN,
        (x_pos, y_pos),
        radius
    )

    pygame.display.update()

pygame.quit()
sys.exit()