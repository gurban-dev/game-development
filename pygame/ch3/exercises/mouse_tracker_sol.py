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
    for box_x in range(BOARDWIDTH):
        for box_y in range(BOARDHEIGHT):

            # Calculate the top-left pixel position of this box.
            left = box_x * (BOXSIZE + GAPSIZE)
            top = box_y * (BOXSIZE + GAPSIZE)

            # Create a rectangle representing this box.
            box_rect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Check whether the mouse position is inside this box.
            if box_rect.collidepoint(x, y):
                return box_x, box_y

    # Return None when the mouse is not over a box.
    return None, None


# Store the box currently under the mouse.
highlightedBox = None

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Get the mouse position whenever it moves.
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = event.pos

            box_x, box_y = get_box_at_pixel(mouseX, mouseY)

            if box_x is not None:
                highlightedBox = (box_x, box_y)
            else:
                highlightedBox = None

    # Fill the window with a background color.
    DISPLAYSURF.fill((30, 30, 30))

    # Draw the 5 x 5 grid.
    for box_x in range(BOARDWIDTH):
        for box_y in range(BOARDHEIGHT):

            left = box_x * (BOXSIZE + GAPSIZE)
            top = box_y * (BOXSIZE + GAPSIZE)

            box_rect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Use a different color for the highlighted box.
            if highlightedBox == (box_x, box_y):
                color = (255, 255, 0)
            else:
                color = (100, 100, 100)

            pygame.draw.rect(
                DISPLAYSURF,
                color,
                box_rect
            )

    pygame.display.update()