import pygame
import sys

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

BOXSIZE = 50
GAPSIZE = 10

BOARDWIDTH = 5
BOARDHEIGHT = 5

BGCOLOR = (60, 60, 100)
BOXCOLOR = (255, 255, 255)
HIGHLIGHTCOLOR = (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode(
    (WINDOWWIDTH, WINDOWHEIGHT)
)

pygame.display.set_caption('Mouse Tracker')


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates into screen pixel coordinates.
    left = boxx * (BOXSIZE + GAPSIZE)
    top = boxy * (BOXSIZE + GAPSIZE)

    # Return the top-left pixel position of the box.
    return left, top


def drawBoard():
    # Draw every box on the board.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)

            pygame.draw.rect(
                DISPLAYSURF,
                BOXCOLOR,
                (left, top, BOXSIZE, BOXSIZE)
            )


def getBoxAtPixel(x, y):
    # Check every box on the board.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)

            # Create a rectangle representing this box.
            boxRect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Check whether the mouse position is inside this box.
            if boxRect.collidepoint(x, y):
                return boxx, boxy

    # Return None when the mouse is not over a box.
    return None, None


while True:
    # Clear the previous frame.
    DISPLAYSURF.fill(BGCOLOR)

    # Draw the board.
    drawBoard()

    # Get the mouse's current pixel position.
    mousex, mousey = pygame.mouse.get_pos()

    # Determine which box is under the mouse.
    boxx, boxy = getBoxAtPixel(mousex, mousey)

    if boxx is not None and boxy is not None:
        # Get the pixel position of the box under the mouse.
        left, top = leftTopCoordsOfBox(boxx, boxy)

        # Draw a border around the box.
        pygame.draw.rect(
            DISPLAYSURF,
            HIGHLIGHTCOLOR,
            (left - 3, top - 3, BOXSIZE + 6, BOXSIZE + 6),
            3
        )

    # Handle Pygame events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Display everything drawn during this frame.
    pygame.display.update()