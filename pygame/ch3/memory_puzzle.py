# Source code:
# https://inventwithpython.com/memorypuzzle.py

# Guide:
# https://inventwithpython.com/pygame/chapter3.html

import random, pygame, sys

# Importing names that Pygame uses for common constants and settings
# so that you can use them directly in this program.

# pygame.locals is submodule in Pygame that contains many predefined
# constants:
# QUIT, KEYDOWN, K_SPACE, MOUSEBUTTONDOWN
from pygame.locals import *

# Set the number of times the game loop should run each second.
FPS = 30 # frames per second, the general speed of the program

# Set width and height of the Pygame window in pixels.
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Set the speed at which the boxes will be uncovered at the initial
# start of the game and later on when the player clicks on a box.
REVEAL_SPEED = 8

# Set the size of each box on the game board in pixels.
BOXSIZE = 40

# Set the space between boxes in pixels.
GAPSIZE = 10

# Set how many columns the board has.
NO_OF_COLUMNS = 10

# Set how many rows the board has.
NO_OF_ROWS = 7

assert (NO_OF_COLUMNS * NO_OF_ROWS) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOW_WIDTH - (NO_OF_COLUMNS * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOW_HEIGHT - (NO_OF_ROWS * (BOXSIZE + GAPSIZE))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= NO_OF_COLUMNS * NO_OF_ROWS, "Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Used to store x coordinate of mouse event.
    mousex = 0

    # Used to store y coordinate of mouse event.
    mousey = 0

    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()

    revealedBoxes = generateRevealedBoxesData(False)

    # Stores the (x, y) of the first box clicked.
    firstSelection = None

    DISPLAYSURF.fill(BGCOLOR)

    startGameAnimation(mainBoard)

    # Main game loop
    while True:
        mouseClicked = False

        # Draw the window
        DISPLAYSURF.fill(BGCOLOR)

        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()

                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos

                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)

        if boxx != None and boxy != None:
            # The mouse is currently over a box.
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)

            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])

                # Set the box as "revealed"
                revealedBoxes[boxx][boxy] = True

                # The current box was the first box clicked
                if firstSelection == None:
                    firstSelection = (boxx, boxy)
                # The current box was the second box clicked
                else:
                    # Check if there is a match between the two icons.
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Icons don't match. Re-cover up both selections.
                        # 1000 milliseconds = 1 sec
                        pygame.time.wait(1000)

                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])

                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False

                    # Check if all pairs found
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)

                        pygame.time.wait(2000)

                        # Reset the board
                        mainBoard = getRandomizedBoard()

                        revealedBoxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second.
                        drawBoard(mainBoard, revealedBoxes)

                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation.
                        startGameAnimation(mainBoard)

                    # Reset firstSelection variable
                    firstSelection = None

        # Redraw the screen and wait a clock tick.
        pygame.display.update()

        FPSCLOCK.tick(FPS)


# The program separates what is on the board from what the player
# can currently see.
def generateRevealedBoxesData(boolean_val):
    # Create an empty list that will contain the columns of the board.
    revealedBoxes = []

    # Create one column for each position across the board.
    for i in range(NO_OF_COLUMNS):
        # Create a column where every box starts with the same value.
        revealedBoxes.append([boolean_val] * NO_OF_ROWS)

    # 10 columns and 7 rows:
    # [
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, False, False, False],
    #     [False, False, False, False, False, False, False, False, False, False]
    # ]

    # Send the complete board of True and False values.

    # revealedBoxes[x][y] tells us whether the box at (x, y) is revealed.
    # True indicates that the box is revealed whereas False means it is not
    # revealed.
    return revealedBoxes


def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.

    # Create an empty list to store all possible icons.
    icons = []

    # Create an icon for every combination of color and shape.
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    # Randomize the order of the icons in the list.
    random.shuffle(icons)

    # Find out how many different icons we need.
    # We need two copies of every icon.
    # For example, a board with 20 spaces needs 10 pairs.
    num_icons_used = int(NO_OF_COLUMNS * NO_OF_ROWS / 2)

    # Keep only the first num_icons_used icons from the list.
    icons = icons[:num_icons_used]

    # Make a second copy of every icon so that each icon has a pair.
    icons = icons * 2

    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons.
    board = []

    for x in range(NO_OF_COLUMNS):
        column = []

        for y in range(NO_OF_ROWS):
            column.append(icons[0])

            # Remove the icons as we assign them.
            del icons[0]
        board.append(column)

    return board


def splitIntoGroupsOf(groupSize, theList):
    # Splits a list into a list of lists, where the inner lists have
    # at most groupSize number of items.
    result = []

    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])

    return result


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN

    return (left, top)


def getBoxAtPixel(x, y):
    for boxx in range(NO_OF_COLUMNS):
        for boxy in range(NO_OF_ROWS):
            left, top = leftTopCoordsOfBox(boxx, boxy)

            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)

            if boxRect.collidepoint(x, y):
                return (boxx, boxy)

    return (None, None)


def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25)
    half =    int(BOXSIZE * 0.5)

    # Get pixel coords from board coords
    left, top = leftTopCoordsOfBox(boxx, boxy)

    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(
            DISPLAYSURF,
            color,
            (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half)
        )
    elif shape == DIAMOND:
        pygame.draw.polygon(
            DISPLAYSURF,
            color,
            ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half))
        )
    elif shape == LINES:
        for i in range(0, BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))

            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))


def getShapeAndColor(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])

        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))

        shape, color = getShapeAndColor(board, box[0], box[1])

        drawIcon(shape, color, box[0], box[1])

        # Only draw the cover if there is a coverage.
        if coverage > 0:
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))

    pygame.display.update()

    FPSCLOCK.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):
    # Do the "box reveal" animation.
    for coverage in range(BOXSIZE, (-REVEAL_SPEED) - 1, -REVEAL_SPEED):
        drawBoxCovers(board, boxesToReveal, coverage)


def coverBoxesAnimation(board, boxesToCover):
    # Do the "box cover" animation.
    for coverage in range(0, BOXSIZE + REVEAL_SPEED, REVEAL_SPEED):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(NO_OF_COLUMNS):
        for boxy in range(NO_OF_ROWS):
            left, top = leftTopCoordsOfBox(boxx, boxy)

            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = getShapeAndColor(board, boxx, boxy)

                drawIcon(shape, color, boxx, boxy)


def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)

    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)


def startGameAnimation(board):
    # Randomly reveal the boxes 8 at a time.
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []

    for x in range(NO_OF_COLUMNS):
        for y in range(NO_OF_ROWS):
            boxes.append( (x, y) )

    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)

    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)


def gameWonAnimation(board):
    # flash the background color when the player has won
    coveredBoxes = generateRevealedBoxesData(True)

    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range(13):
        # Swap colors
        color1, color2 = color2, color1

        DISPLAYSURF.fill(color1)

        drawBoard(board, coveredBoxes)

        pygame.display.update()

        pygame.time.wait(300)


def hasWon(revealedBoxes):
    # Returns True if all the boxes have been revealed, otherwise False.
    for i in revealedBoxes:
        # If any boxes are covered.
        if False in i:
            return False
    return True


if __name__ == '__main__':
    main()