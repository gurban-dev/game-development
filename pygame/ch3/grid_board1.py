import pygame

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

BOARDSIZE = 4
BOXSIZE = 60
GAPSIZE = 10

# Calculate the total pixel width of the board.
# There are BOARDSIZE boxes and BOARDSIZE - 1 gaps.
BOARD_PIXEL_WIDTH = BOARDSIZE * BOXSIZE + (BOARDSIZE - 1) * GAPSIZE

# Calculate the total pixel height of the board.
# The board is square, so the calculation is the same.
BOARD_PIXEL_HEIGHT = BOARDSIZE * BOXSIZE + (BOARDSIZE - 1) * GAPSIZE

# Calculate the empty space on the left and right sides of the board.
# Dividing by 2 gives us the amount of space on each side.
BOARD_LEFT = (WINDOWWIDTH - BOARD_PIXEL_WIDTH) // 2

# Calculate the empty space above and below the board.
# Dividing by 2 gives us the amount of space on each side.
BOARD_TOP = (WINDOWHEIGHT - BOARD_PIXEL_HEIGHT) // 2

BGCOLOR = (60, 60, 100)
BOXCOLOR = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('Grid Practice')

# The following is our game state. It isn't graphics. It is just
# information describing the board.

# board = [
#     [False, False, False, False],
#     [False, False, False, False],
#     [False, False, False, False],
#     [False, False, False, False]
# ]


def generateBoard():
    # Create one list for each column of the board.
    board = []

    for x in range(BOARDSIZE):
        # Each column starts as an empty list.
        column = []

        # Add one value for every row in this column.
        for y in range(BOARDSIZE):
            column.append(False)

        # Add the completed column to the board.
        board.append(column)

    return board


def drawBoard(board):
    # Visit every position in the 2D board.
    for x in range(BOARDSIZE):
        for y in range(BOARDSIZE):
            # Calculate the pixel position of this box.
            # BOARD_LEFT and BOARD_TOP move the entire board
            # so that it is centered inside the window.
            left = BOARD_LEFT + x * (BOXSIZE + GAPSIZE)
            top = BOARD_TOP + y * (BOXSIZE + GAPSIZE)

            # Choose the color based on the box state.
            if board[x][y]:
                color = (0, 255, 0)
            else:
                color = BOXCOLOR

            # Draw the box at its pixel position.
            pygame.draw.rect(
                DISPLAYSURF,
                color,
                (left, top, BOXSIZE, BOXSIZE)
            )


board = generateBoard()

DISPLAYSURF.fill(BGCOLOR)
drawBoard(board)
pygame.display.update()

pygame.time.wait(3000)
pygame.quit()