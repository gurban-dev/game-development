import pygame
import sys

pygame.init()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

# Instead of using the BOXSIZE variable in our code we could just
# type the integer 40 directly in the code. But there are two
# reasons to use constant variables.

# First, if we ever wanted to change the size of each box later,
# we would have to go through the entire program and find and
# replace each time we typed 40. By just using the BOXSIZE
# constant, we only have to change line 13 and the rest of
# the program is already up to date.

# Second, it makes the code more readable by allowing you to see
# what the values used in calculations actually represent as shown
# in the two commented lines below.
# XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)

# XMARGIN = int((640 - (10 * (40 + 10))) / 2)

# However, the following would be going too far:
# ZERO = 0
# ONE = 1
# TWO = 99999999
# TWOANDTHREEQUARTERS = 2.75

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


def left_top_coords_of_box(box_x, box_y):
    # Convert board coordinates into screen pixel coordinates.
    left = box_x * (BOXSIZE + GAPSIZE)
    top = box_y * (BOXSIZE + GAPSIZE)

    # Return the top-left pixel position of the box.
    return left, top


def draw_board():
    # Draw every box on the board.
    for box_x in range(BOARDWIDTH):
        for box_y in range(BOARDHEIGHT):
            left, top = left_top_coords_of_box(box_x, box_y)

            pygame.draw.rect(
                DISPLAYSURF,
                BOXCOLOR,
                (left, top, BOXSIZE, BOXSIZE)
            )


def get_box_at_pixel(x, y):
    # Check every box on the board.
    for box_x in range(BOARDWIDTH):
        for box_y in range(BOARDHEIGHT):
            left, top = left_top_coords_of_box(box_x, box_y)

            # Create a rectangle representing this box.
            boxRect = pygame.Rect(
                left,
                top,
                BOXSIZE,
                BOXSIZE
            )

            # Check whether the mouse position is inside this box.
            if boxRect.collidepoint(x, y):
                return box_x, box_y

    # Return None when the mouse is not over a box.
    return None, None


while True:
    # Clear the previous frame.
    DISPLAYSURF.fill(BGCOLOR)

    # Draw the board.
    draw_board()

    # Get the mouse's current pixel position.
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Determine which box is under the mouse.
    box_x, box_y = get_box_at_pixel(mouse_x, mouse_y)

    if box_x is not None and box_y is not None:
        # Get the pixel position of the box under the mouse.
        left, top = left_top_coords_of_box(box_x, box_y)

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