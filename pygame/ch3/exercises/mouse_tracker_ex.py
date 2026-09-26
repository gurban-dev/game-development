import pygame
import sys

# Instructions:
# 1. Create a Pygame window.
# 2. Create a 5 x 5 grid.
# 3. Draw each box using pygame.draw.rect().
# 4. Use a loop to draw all 25 boxes.
# 5. Use pygame.event.get() to read mouse events.

pygame.init()

WINDOWWIDTH = 500
WINDOWHEIGHT = 500
BOXSIZE = 50
GAPSIZE = 10
BOARDWIDTH = 5
BOARDHEIGHT = 5

DISPLAYSURF = pygame.display.set_mode(
    (WINDOWWIDTH, WINDOWHEIGHT)
)

pygame.display.set_caption('Box Highlighter')

def get_box_at_pixel(x, y):
    # Check every box on the board.
    for boxx in range(BOARDWIDTH):
        for box_y in range(BOARDHEIGHT):

            # Calculate the top-left pixel position of this box.
            left = boxx * (BOXSIZE + GAPSIZE)
            top = box_y * (BOXSIZE + GAPSIZE)

            # Create a rectangle representing this box.
            boxRect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Check whether the mouse position is inside this box.
            if boxRect.collidepoint(x, y):
                return boxx, box_y

    # Return None when the mouse is not over a box.
    return None, None


# Your code goes here.