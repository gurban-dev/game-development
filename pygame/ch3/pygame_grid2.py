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

# Calculate the total pixel width of the board, including the
# gaps between squares.
BOARD_PIXEL_WIDTH = BOARDWIDTH * BOXSIZE + (BOARDWIDTH - 1) * GAPSIZE

# Calculate the total pixel height of the board, including the
# gaps between squares.
BOARD_PIXEL_HEIGHT = BOARDHEIGHT * BOXSIZE + (BOARDHEIGHT - 1) * GAPSIZE

# Calculate the left position needed to center the board
# horizontally in the window.
BOARD_LEFT = (WINDOWWIDTH - BOARD_PIXEL_WIDTH) // 2

# Calculate the top position needed to center the board vertically
# in the window.
BOARD_TOP = (WINDOWHEIGHT - BOARD_PIXEL_HEIGHT) // 2

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

    # Convert the board coordinate into a pixel x-coordinate,
    # starting from the board's centered left position.
    left = BOARD_LEFT + box_x * (BOXSIZE + GAPSIZE)

    # Convert the board coordinate into a pixel y-coordinate,
    # starting from the board's centered top position.
    top = BOARD_TOP + box_y * (BOXSIZE + GAPSIZE)

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


def get_box_at_pixel(x, y):

    # Tell the student that this function receives a mouse position
    # in pixels and needs to figure out which board position contains it.
    for box_x in range(BOARDWIDTH):

        # Explain that we search every possible box because the mouse
        # position itself is expressed in pixels, not board coordinates.
        for box_y in range(BOARDHEIGHT):

            # First convert this particular board position into pixels
            # so we know where that box actually exists on the screen.
            left, top = left_top_coords_of_box(box_x, box_y)

            # Explain that pygame.Rect is a convenient representation
            # of a rectangular area on the screen.
            boxRect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Explain that collidepoint asks a simple question:
            # "Is this pixel position inside this rectangle?"
            if boxRect.collidepoint(x, y):

                # Once we find the matching rectangle, return the
                # board coordinates rather than the pixel coordinates.
                return box_x, box_y

    # Explain that reaching this line means none of the rectangles
    # contained the mouse position, so there is no matching box.
    return None, None


while True:

    # Explain that each frame starts by clearing the previous frame.
    # Otherwise old drawings would remain on the screen.
    DISPLAYSURF.fill(BGCOLOR)

    # Explain that the function now draws all 25 boxes.
    draw_board()

    # Tell the student that Pygame gives us the mouse position in pixels,
    # such as (143, 87).
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Explain that we pass those pixel coordinates to our function,
    # which searches for the corresponding board coordinates.
    box_x, box_y = get_box_at_pixel(mouse_x, mouse_y)

    # Explain that None means "there is no box here", so we only
    # continue when the function actually found a box.
    if box_x is not None and box_y is not None:

        # Now convert the board coordinate back into a pixel position
        # because drawing requires pixel coordinates.
        left, top = left_top_coords_of_box(box_x, box_y)

        # Explain that we are drawing a slightly larger rectangle around
        # the box to make it visually obvious which box was detected.
        pygame.draw.rect(
            DISPLAYSURF,
            HIGHLIGHTCOLOR,
            (left - 3, top - 3, BOXSIZE + 6, BOXSIZE + 6),
            3
        )

    # Tell the student that Pygame applications need to process
    # events so that the operating system can communicate with them.
    for event in pygame.event.get():

        # Explain that closing the window produces a QUIT event.
        if event.type == pygame.QUIT:

            # Tell the student that pygame.quit() shuts down Pygame
            # before sys.exit() terminates the Python program.
            pygame.quit()

            sys.exit()

    # Explain that update() takes everything we drew this frame
    # and displays it on the actual window.
    pygame.display.update()