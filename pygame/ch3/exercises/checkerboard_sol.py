import pygame
import sys

# Goal: Create a checkerboard pattern.
# Every other square will be green, and the remaining squares
# will be white.

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

# This is the color of the window behind the board.
BGCOLOR = (60, 60, 100)

# This is the color used for the white squares.
BOXCOLOR = (255, 255, 255)

# This is the color used for the green squares.
GREENCOLOR = (0, 200, 0)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Checkerboard Practice')


def generateBoard():
    # Create an empty list that will contain the board columns.
    board = []

    # The outer loop creates each column of the board.
    for x in range(BOARDWIDTH):
        # Create an empty list for the current column.
        column = []

        # The inner loop creates each position in the column.
        for y in range(BOARDHEIGHT):
            # Store False at each position.
            # The value is not used to determine the color yet.
            column.append(False)

        # Add the completed column to the board.
        board.append(column)

    # Return the completed 2D list.
    return board


def drawBoard(board):
    # Loop through every column on the board.
    for x in range(BOARDWIDTH):

        # Loop through every row in the current column.
        for y in range(BOARDHEIGHT):

            # Convert the board coordinates into pixel coordinates.
            left = x * (BOXSIZE + GAPSIZE)
            top = y * (BOXSIZE + GAPSIZE)

            # Add the x and y coordinates together.
            # If the result is even, this square will be green.
            if (x + y) % 2 == 0:
                color = GREENCOLOR

            # If the result is odd, this square will be white.
            else:
                color = BOXCOLOR

            # Draw the square using the color we selected above.
            pygame.draw.rect(
                DISPLAYSURF,
                color,
                (left, top, BOXSIZE, BOXSIZE)
            )


# Create the board data.
board = generateBoard()

while True:

    # Check for events such as closing the window.
    for event in pygame.event.get():

        # Close the program when the user clicks the X.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen before drawing the board again.
    DISPLAYSURF.fill(BGCOLOR)

    # Draw the checkerboard.
    drawBoard(board)

    # Show the newly drawn frame.
    pygame.display.update()