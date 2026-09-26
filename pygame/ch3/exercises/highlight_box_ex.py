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

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('Highlight Box')

# Exercise:

# When the mouse moves over a box, draw a blue outline around
# that box.

# Your program should:
# 1. Get the box under the mouse.

# 2. Check that a box was found.

# 3. Convert the box coordinate to pixel coordinates.

# 4. Draw a blue outline around the box.

# 5. Redraw the screen every frame.

# You already have these functions available:
#     getBoxAtPixel(mousex, mousey)
#     leftTopCoordsOfBox(boxx, boxy)

# Use the existing functions to determine which box the mouse
# is over and where that box should be drawn.

# The blue outline should be slightly larger than the box so
# that it appears around the outside edge of the box.


def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (BOXSIZE + GAPSIZE)
    top = boxy * (BOXSIZE + GAPSIZE)

    left += (WINDOWWIDTH - (BOARDSIZE * (BOXSIZE + GAPSIZE))) // 2
    top += (WINDOWHEIGHT - (BOARDSIZE * (BOXSIZE + GAPSIZE))) // 2

    return left, top


def getBoxAtPixel(x, y):
    for boxx in range(BOARDSIZE):
        for boxy in range(BOARDSIZE):
            left, top = leftTopCoordsOfBox(boxx, boxy)

            boxRect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            if boxRect.collidepoint(x, y):
                return boxx, boxy

    return None, None


def drawBoard():
    for boxx in range(BOARDSIZE):
        for boxy in range(BOARDSIZE):
            left, top = leftTopCoordsOfBox(boxx, boxy)

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

    mousex, mousey = pygame.mouse.get_pos()

    DISPLAYSURF.fill(BGCOLOR)

    drawBoard()

    # Get the box underneath the mouse cursor.

    # Check whether a box was found.

    # Convert the box coordinate to pixel coordinates.

    # Draw a blue outline around the box.

    pygame.display.update()