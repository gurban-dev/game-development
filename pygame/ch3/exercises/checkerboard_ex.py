import pygame
import sys

# Goal: Create a Checkerboard Pattern.

# Modify the program so that the board starts with a checkerboard pattern.

# Every other box should be green.
# The remaining boxes should stay white.

# For each box:
#     if x + y is even:
#         make it green
#     otherwise:
#         make it white

# You will need to modify the code that currently checks:
#
#     if board[x][y]:

# Use the x and y coordinates to determine which color each box
# should have.

# The goal is to practice:
# - Using x and y coordinates.
# - Working with nested loops.
# - Using conditionals.
# - Drawing different colors with Pygame.
# - Understanding the difference between board data and graphics.

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

# These values describe the size of each tile and the space
# between tiles.
BOXSIZE = 50
GAPSIZE = 10

# These values describe how many tiles the board contains
# horizontally and vertically.
BOARDWIDTH = 4
BOARDHEIGHT = 4

BGCOLOR = (60, 60, 100)
BOXCOLOR = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Checkerboard Practice')


def generateBoard():
    board = []

    for x in range(BOARDWIDTH):
        column = []

        for y in range(BOARDHEIGHT):
            column.append(False)

        board.append(column)

    return board


def drawBoard(board):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):

            left = x * (BOXSIZE + GAPSIZE)
            top = y * (BOXSIZE + GAPSIZE)

            if board[x][y]:
                color = BOXCOLOR
            else:
                color = BOXCOLOR

            pygame.draw.rect(
                DISPLAYSURF,
                color,
                (left, top, BOXSIZE, BOXSIZE)
            )


board = generateBoard()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BGCOLOR)

    drawBoard(board)

    pygame.display.update()