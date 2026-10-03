import pygame
import sys

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# These values describe the overall screen, so giving them names
# makes the rest of the program easier to read.
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
    (WINDOW_WIDTH, WINDOW_HEIGHT)
)

pygame.display.set_caption('Mouse Tracker')


# The board uses small coordinates like (0, 0), (1, 0), and (2, 0),
# while Pygame needs actual pixel coordinates. This function
# translates between those two systems.
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

    # box_x represents the horizontal position of a box on the board.
    # It does not represent a pixel position.
    # It tells us which column the box is in.

    # WINDOW_WIDTH is 400 pixels wide, but the board is 290 pixels
    # wide. So we have 110 pixels of unused space. Dividing that
    # by 2 gives us 55 pixels on each side.
    board_left = (WINDOW_WIDTH - board_width) // 2
    board_top = (WINDOW_HEIGHT - board_height) // 2

    # We're multiplying by box_x because box-x tells us how many
    # box-and_gap distances we need to move from the left edge of
    # the window. It we're starting from column 0, we move zero times.
    # If we're at column 1, we move once.
    left = board_left + box_x * (BOXSIZE + GAPSIZE)
    top = board_top + box_y * (BOXSIZE + GAPSIZE)

    # The first box starts at pixel 0.

    # ----------
    # | Box 0  |
    # |        |
    # ----------

    # box_x = 0

    # left = board_left + 0 * (50 + 10)
    #      = 0


    # Box 0 ends at pixel 50.
    # The 10-pixel gap comes next.

    # 0       50  60       110
    # ----------  ---------- 
    # |  Box 0 |  |  Box 1 |
    # |        |  |        |
    # ----------  ----------

    # For Box 1:
    # box_x = 1

    # left = board_left + 1 * (50 + 10)
    #      = 60

    return left, top

# This function has one job: draw every square that makes up
# the board.
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

def get_box_at_pixel(x, y):
    # Check every box on the board.
    for box_x in range(BOARDWIDTH):
        for box_y in range(BOARDHEIGHT):
            # Get the pixel position of this box.
            left, top = left_top_coords_of_box(box_x, box_y)

            # Create a rectangle covering the box.
            box_rect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Check whether the mouse position is inside it.

            # collidepoint(x, y) checks whether a point is inside
            # a rectangle.
            if box_rect.collidepoint(x, y):
                return (box_x, box_y)

    # The mouse is not over any box.
    return (None, None)

# The main loop will repeatedly ask the function to draw the board.
while True:

    # Explain that each frame starts by clearing the previous frame.
    # Otherwise old drawings would remain on the screen.
    DISPLAYSURF.fill(BGCOLOR)

    # Explain that the function now draws all 25 boxes.
    draw_board()

    # For now, we are not doing anything with the mouse.
    # We will add interaction after the student understands the grid.

    # Pygame applications need to process events so that the operating
    # system can communicate with them.

    # event is an object that Pygame gives us representing that
    # something happened.

    # pygame.event.get() gives us a collection of all the events
    # that are waiting to be processed.
    for event in pygame.event.get():

        # Explain that closing the window produces a QUIT event.
        if event.type == pygame.QUIT:

            # pygame.quit() shuts down Pygame before sys.exit()
            # terminates the Python program.
            pygame.quit()

            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            # .pos is an attribute of the Pygame event object
            # that contains the mouse's position.

            # event.pos returns a tuple: (x, y)

            # E.g.
            # (180, 140)

            # mouse_x is 180
            # mouse_y is 140
            mouse_x, mouse_y = event.pos

            box_x, box_y = get_box_at_pixel(mouse_x, mouse_y)

            if box_x != None and box_y != None:
                print(f'Mouse is over: ({box_x}, {box_y})')

    pygame.display.update()