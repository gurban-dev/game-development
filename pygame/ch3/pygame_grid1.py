import pygame
import sys

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

# Tell the student that these values describe the overall screen,
# so giving them names makes the rest of the program easier to read.
BOXSIZE = 50
GAPSIZE = 10

BOARDWIDTH = 5
BOARDHEIGHT = 5

# Explain that these constants describe the board's appearance,
# rather than its geometry or behavior.
BGCOLOR = (60, 60, 100)
BOXCOLOR = (255, 255, 255)
HIGHLIGHTCOLOR = (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode(
    (WINDOWWIDTH, WINDOWHEIGHT)
)

pygame.display.set_caption('Mouse Tracker')


# Tell the student that the board uses small coordinates like
# (0, 0), (1, 0), and (2, 0), while Pygame needs actual pixel
# coordinates. This function translates between those two systems.
def left_top_coords_of_box(box_x, box_y):

    # Calculate the total width and height of the board.
    board_width = (
        BOARDWIDTH * BOXSIZE
        + (BOARDWIDTH - 1) * GAPSIZE
    )

    board_height = (
        BOARDHEIGHT * BOXSIZE
        + (BOARDHEIGHT - 1) * GAPSIZE
    )

    # Calculate where the board should start so it is centered.
    board_left = (WINDOWWIDTH - board_width) // 2
    board_top = (WINDOWHEIGHT - board_height) // 2

    # Calculate the position of the current square within the board.
    left = board_left + box_x * (BOXSIZE + GAPSIZE)
    top = board_top + box_y * (BOXSIZE + GAPSIZE)

    return left, top


# Tell the student that this function has one job: draw every
# square that makes up the board.
def draw_board():

    # Explain that range(BOARDWIDTH) gives us 0 through 4.
    # Those are the five possible x positions on our board.
    for box_x in range(BOARDWIDTH):

        # Explain that for each column, we visit every row.
        # The nested loop is what lets us visit every combination
        # of x and y coordinates.
        for box_y in range(BOARDHEIGHT):

            # Explain that we first convert the board coordinate
            # into the pixel coordinate where the rectangle belongs.
            left, top = left_top_coords_of_box(box_x, box_y)

            # Now connect the coordinate calculation to drawing:
            # Pygame receives the pixel position and the box dimensions,
            # and draws one rectangle at that location.
            pygame.draw.rect(
                DISPLAYSURF,
                BOXCOLOR,
                (left, top, BOXSIZE, BOXSIZE)
            )

# Tell the student that a function only does something when we
# actually call it, so this is where the main loop will repeatedly
# ask the function to draw the board.
while True:

    # Explain that each frame starts by clearing the previous frame.
    # Otherwise old drawings would remain on the screen.
    DISPLAYSURF.fill(BGCOLOR)

    # Explain that the function now draws all 25 boxes.
    draw_board()

    # For now, we are not doing anything with the mouse.
    # We will add interaction after the student understands the grid.

    # Tell the student that Pygame applications need to process
    # events so that the operating system can communicate with them.
    for event in pygame.event.get():

        # Explain that closing the window produces a QUIT event.
        if event.type == pygame.QUIT:

            # Tell the student that pygame.quit() shuts down Pygame
            # before sys.exit() terminates the Python program.
            pygame.quit()

            sys.exit()

    pygame.display.update()