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
HIGHLIGHTCOLOR = (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Grid Practice')


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
            # BOARD_LEFT and BOARD_TOP center the board in the window.
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


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates into pixel coordinates.
    left = BOARD_LEFT + boxx * (BOXSIZE + GAPSIZE)
    top = BOARD_TOP + boxy * (BOXSIZE + GAPSIZE)

    return (left, top)


def getBoxAtPixel(x, y):
    # Check every box on the board.
    for boxx in range(BOARDSIZE):
        for boxy in range(BOARDSIZE):
            # Get the pixel position of this box.
            left, top = leftTopCoordsOfBox(boxx, boxy)

            # Create a rectangle covering the box.
            boxRect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Check whether the mouse position is inside it.
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)

    # The mouse is not over any box.
    return (None, None)


board = generateBoard()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos

            boxx, boxy = getBoxAtPixel(mousex, mousey)

            if boxx != None and boxy != None:
                print('Mouse is over:', boxx, boxy)

    # Clear the previous frame.
    DISPLAYSURF.fill(BGCOLOR)

    # Draw the current game state.
    drawBoard(board)

    # Show the newly drawn frame.
    pygame.display.update()