import pygame
import sys

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

BOARDSIZE = 4
BOXSIZE = 60
GAPSIZE = 10

BGCOLOR = (60, 60, 100)
BOXCOLOR = (255, 255, 255)
HIGHLIGHTCOLOR = (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('Highlight Box')


def leftTopCoordsOfBox(box_x, box_y):
    left = box_x * (BOXSIZE + GAPSIZE)
    top = box_y * (BOXSIZE + GAPSIZE)

    left += (WINDOWWIDTH - (BOARDSIZE * (BOXSIZE + GAPSIZE))) // 2
    top += (WINDOWHEIGHT - (BOARDSIZE * (BOXSIZE + GAPSIZE))) // 2

    return left, top


def getBoxAtPixel(x, y):
    # Check every box on the board to find the one
    # containing the mouse position.
    for box_x in range(BOARDSIZE):
        for box_y in range(BOARDSIZE):
            left, top = leftTopCoordsOfBox(box_x, box_y)

            # Create a rectangle representing the current box.
            boxRect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Check whether the mouse position is inside this box.
            if boxRect.collidepoint(x, y):
                return box_x, box_y

    # Return None values when the mouse is not over any box.
    return None, None


def drawBoard():
    # Draw every box on the board.
    for box_x in range(BOARDSIZE):
        for box_y in range(BOARDSIZE):
            left, top = leftTopCoordsOfBox(box_x, box_y)

            pygame.draw.rect(
                DISPLAYSURF,
                BOXCOLOR,
                (left, top, BOXSIZE, BOXSIZE)
            )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current position of the mouse in pixels.
    mousex, mousey = pygame.mouse.get_pos()

    # Clear the previous frame before drawing the new frame.
    DISPLAYSURF.fill(BGCOLOR)

    # Draw all of the white boxes.
    drawBoard()

    # Find which board coordinate is underneath the mouse.
    box_x, box_y = getBoxAtPixel(mousex, mousey)

    # Only draw a highlight if the mouse is actually over a box.
    if box_x is not None and box_y is not None:

        # Convert the board coordinate into a pixel coordinate.
        left, top = leftTopCoordsOfBox(box_x, box_y)

        # Draw a blue outline slightly outside the white box.
        pygame.draw.rect(
            DISPLAYSURF,
            HIGHLIGHTCOLOR,
            (left - 2, top - 2, BOXSIZE + 4, BOXSIZE + 4),
            3
        )

    # Display the newly drawn frame.
    pygame.display.update()