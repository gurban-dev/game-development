import random, pygame, sys

# pygame.locals is a module that contains many commonly used
# Pygame constants.

# The asterisk (*) means import all the names from the pygame.locals
# submodule.
from pygame.locals import *

# Frames per second, the general speed of the program.
FPS = 30

# Size of window's width in pixels.
WINDOW_WIDTH = 640

# Size of window's height in pixels.
WINDOW_HEIGHT = 480

# Speed boxes' sliding reveals and covers.
REVEAL_SPEED = 8

# Size of box height & width in pixels.
BOX_SIZE = 40

# Size of gap between boxes in pixels.
GAP_SIZE = 10

# Number of columns of icons.
BOARD_WIDTH = 10

# Number of rows of icons.
BOARD_HEIGHT = 7

assert (BOARD_WIDTH * BOARD_HEIGHT) % 2 == 0, (
    'Board needs to have an even number of boxes for pairs of matches.'
)

X_MARGIN = int(
    (WINDOW_WIDTH - (BOARD_WIDTH * (BOX_SIZE + GAP_SIZE))) / 2
)

Y_MARGIN = int(
    (WINDOW_HEIGHT - (BOARD_HEIGHT * (BOX_SIZE + GAP_SIZE))) / 2
)

# R G B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BG_COLOR = NAVYBLUE
LIGHT_BG_COLOR = GRAY
BOX_COLOR = WHITE
HIGHLIGHT_COLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALL_COLORS = (
    RED,
    GREEN,
    BLUE,
    YELLOW,
    ORANGE,
    PURPLE,
    CYAN
)

ALL_SHAPES = (
    DONUT,
    SQUARE,
    DIAMOND,
    LINES,
    OVAL
)

# Each unique icon is created by combining one shape with one color.
# Each unique shape-and-color combination needs to appear twice on the board.
# Multiplying by 2 accounts for the second copy needed to create a matching pair.
# This assertion checks that there are enough possible pairs to fill the board.
assert len(ALL_COLORS) * len(ALL_SHAPES) * 2 >= BOARD_WIDTH * BOARD_HEIGHT, (
    "Board is too big for the number of shapes/colors defined."
)

def main():
    # global is being used because FPS_CLOCK and DISPLAY_SURF are created
    # inside main(), but they are probably needed by other functions
    # throughout the program.

    # Without global, Python treats those assignments inside main() as creating
    # new local variables.

    # When assigning values to these names inside this function, treat them as
    # global variables, not new local variables.
    global FPS_CLOCK, DISPLAY_SURF

    pygame.init()

    # Assign a Clock object to the global FPS_CLOCK.
    FPS_CLOCK = pygame.time.Clock()

    # Assign the game's display Surface to the global DISPLAY_SURF.
    DISPLAY_SURF = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )

    # Used to store x coordinate of mouse event.
    mouse_x = 0

    # Used to store y coordinate of mouse event.
    mouse_y = 0

    pygame.display.set_caption('Memory Game')

    # Generates the randomized game board data.
    main_board = get_randomized_board()

    # Generates data describing which boxes are revealed.
    revealed_boxes = generate_revealed_boxes_data(False)

    # Stores the (x, y) of the first box clicked.
    first_selection = None

    DISPLAY_SURF.fill(BG_COLOR)

    start_game_animation(main_board)

    # Main game loop
    while True:
        mouse_clicked = False

        # Drawing the window
        DISPLAY_SURF.fill(BG_COLOR)

        draw_board(main_board, revealed_boxes)

        # Event handling loop
        for event in pygame.event.get():
            if event.type == QUIT or (
                event.type == KEYUP and event.key == K_ESCAPE
            ):
                pygame.quit()

                sys.exit()

            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos

                mouse_clicked = True

        box_x, box_y = get_box_at_pixel(mouse_x, mouse_y)

        if box_x != None and box_y != None:

            # The mouse is currently over a box.
            if not revealed_boxes[box_x][box_y]:
                draw_highlight_box(box_x, box_y)

            if not revealed_boxes[box_x][box_y] and mouse_clicked:
                reveal_boxes_animation(main_board, [(box_x, box_y)])

                # Set the box as revealed.
                revealed_boxes[box_x][box_y] = True

                if first_selection == None:
                    # The current box was the first box clicked.
                    first_selection = (box_x, box_y)

                else:
                    # The current box was the second box clicked.
                    # Check if there is a match between the two icons.

                    icon1_shape, icon1_color = get_shape_and_color(
                        main_board,
                        first_selection[0],
                        first_selection[1]
                    )

                    icon2_shape, icon2_color = get_shape_and_color(
                        main_board,
                        box_x,
                        box_y
                    )

                    if (
                        icon1_shape != icon2_shape
                        or icon1_color != icon2_color
                    ):
                        # Icons don't match. Re-cover both selections.
                        pygame.time.wait(1000)

                        cover_boxes_animation(
                            main_board,
                            [
                                (
                                    first_selection[0],
                                    first_selection[1]
                                ),
                                (box_x, box_y)
                            ]
                        )

                        revealed_boxes[first_selection[0]][first_selection[1]] = False

                        revealed_boxes[box_x][box_y] = False

                    elif has_won(revealed_boxes):

                        # Check if all pairs have been found.
                        game_won_animation(main_board)

                        pygame.time.wait(2000)

                        # Reset the board.
                        main_board = get_randomized_board()

                        revealed_boxes = generate_revealed_boxes_data(False)

                        # Show the fully unrevealed board for a second.
                        draw_board(main_board, revealed_boxes)

                        pygame.display.update()

                        pygame.time.wait(1000)

                        # Replay the start game animation.
                        start_game_animation(main_board)

                    first_selection = None

        # Redraw the screen and wait a clock tick.
        pygame.display.update()

        FPS_CLOCK.tick(FPS)

def generate_revealed_boxes_data(val):

    # Create a separate board that tracks whether each icon is currently
    # visible to the player (revealed) or covered so the player cannot see it
    # (hidden).
    revealed_boxes = []

    # Create one column for every column in the game board.
    # The underscore means we do not need to use the loop counter.
    for _ in range(BOARD_WIDTH):

        # Create a column containing one value for each row. For example, if
        # BOARD_HEIGHT is 4 and val is False, this creates [False, False, False, False].

        # Multiply val by BOARD_HEIGHT to create one value for every row in
        # the column, so each box in that column has a hidden or revealed state.
        revealed_boxes.append([val] * BOARD_HEIGHT)

    # Return the completed nested list representing the board's reveal state.
    return revealed_boxes

def get_randomized_board():
    # Store every possible combination of shape and color as an icon.
    icons = []

    # Loop through each available color.
    for color in ALL_COLORS:

        # Combine the current color with every available shape.
        for shape in ALL_SHAPES:
            icons.append((shape, color))

    # Randomize the order so the icons will not always appear in the same places.
    random.shuffle(icons)

    # Calculate how many different icons are needed for half of the board.
    # Each icon will appear twice so the player can find matching pairs.

    # Suppose the board is 4 columns × 4 rows.

    # Total spaces: 4 * 4 = 16
    # Every icon needs a matching pair, so divide by 2: 16 / 2 = 8

    # Therefore:
    # num_icons_used = 8

    # The board needs 8 different icons, with each one appearing twice,
    # giving us 16 total icons.
    num_icons_used = int(BOARD_WIDTH * BOARD_HEIGHT / 2)

    # Keep only the required number of unique icons and duplicate each one.

    # It is necessary because there may be more possible shape-and-color
    # combinations than the board has room for.

    # Suppose your program can create 20 different icons:
    # icons = [icon1, icon2, icon3, ..., icon20]

    # But your board is 4 × 4, which has only:
    # 4 * 4 = 16 spaces

    # Because this is a matching game, every icon needs to appear twice:
    # 16 spaces / 2 = 8 different icons needed

    # So:
    # icons[:num_icons_used]

    # keeps only 8 unique icons.

    # Then:
    # * 2

    # turns those 8 icons into 16 total icons:
    # 8 unique icons × 2 copies each = 16 board spaces
    icons = icons[:num_icons_used] * 2

    # After duplicating the icons, they are initially grouped together:
    # ["circle", "square", "star", "circle", "square", "star"]

    # Shuffle again so matching pairs are placed randomly on the board.
    random.shuffle(icons)

    # Create the board as a nested list where each column contains its rows.
    board = []

    # Create one column for each horizontal position on the board.
    for x in range(BOARD_WIDTH):
        column = []

        # Add an icon to every vertical position in the current column.
        for y in range(BOARD_HEIGHT):

            # Store the next randomized icon at this board position.
            column.append(icons[0])

            # Remove the icon after placing it so it cannot be used again.
            del icons[0]

        # Add the completed column to the board.
        board.append(column)

    # Return the completed board so the rest of the Pygame program can use it.
    return board


def split_into_groups_of(group_size, the_list):
    # Split a list into lists containing at most group_size items.
    result = []

    # Example: the_list = [A, B, C, D, E, F, G, H]
    #          group_size = 3

    # The loop moves through the list by 3 positions at a time:
    # i = 0  -> [A, B, C]
    # i = 3  ->          [D, E, F]
    # i = 6  ->                   [G, H]

    # Each slice is added as a separate group to result.
    for i in range(0, len(the_list), group_size):

        # Take the items starting at i and ending before i + group_size.
        result.append(the_list[i:i + group_size])

    # Final result:
    # [[A, B, C], [D, E, F], [G, H]]
    return result

def left_top_coords_of_box(box_x, box_y):
    # Think of the board as a grid of boxes:
    #                    box_x ->
    #                 0        1        2
    #              +--------+--------+--------+
    # box_y = 0    | (0, 0) | (1, 0) | (2, 0) |
    #              +--------+--------+--------+
    # box_y = 1    | (0, 1) | (1, 1) | (2, 1) |
    #              +--------+--------+--------+
    # box_y = 2    | (0, 2) | (1, 2) | (2, 2) |
    #              +--------+--------+--------+

    # Each board coordinate must be converted into a pixel position
    # before Pygame knows where to draw the box on the screen.

    # Example:
    # X_MARGIN
    #    |
    #    v
    #    +--------+ GAP +--------+ GAP +--------+
    #    | Box 0  |     | Box 1  |     | Box 2  |
    #    +--------+     +--------+     +--------+
    #    <------->
    #     BOX_SIZE
    #
    # Moving one box to the right requires moving:
    # BOX_SIZE + GAP_SIZE pixels.

    # Calculate the x pixel coordinate of the box's left edge.
    left = box_x * (BOX_SIZE + GAP_SIZE) + X_MARGIN

    # Calculate the y pixel coordinate of the box's top edge.
    # Moving down one box also requires BOX_SIZE + GAP_SIZE pixels.
    top = box_y * (BOX_SIZE + GAP_SIZE) + Y_MARGIN

    # Return the pixel coordinates of the box's top-left corner.
    return (left, top)

def get_box_at_pixel(x, y):

    for box_x in range(BOARD_WIDTH):

        for box_y in range(BOARD_HEIGHT):
            left, top = left_top_coords_of_box(box_x, box_y)

            boxRect = pygame.Rect(
                left,
                top,
                BOX_SIZE,
                BOX_SIZE
            )

            if boxRect.collide_point(x, y):
                return (box_x, box_y)

    return (None, None)


def draw_icon(shape, color, box_x, box_y):
    quarter = int(BOX_SIZE * 0.25)
    half = int(BOX_SIZE * 0.5)

    # Get pixel coordinates from board coordinates.
    left, top = left_top_coords_of_box(box_x, box_y)

    # Draw the shapes.
    if shape == DONUT:
        pygame.draw.circle(
            DISPLAY_SURF,
            color,
            (left + half, top + half),
            half - 5
        )

        pygame.draw.circle(
            DISPLAY_SURF,
            BG_COLOR,
            (left + half, top + half),
            quarter - 5
        )

    elif shape == SQUARE:
        pygame.draw.rect(
            DISPLAY_SURF,
            color,
            (
                left + quarter,
                top + quarter,
                BOX_SIZE - half,
                BOX_SIZE - half
            )
        )

    elif shape == DIAMOND:
        pygame.draw.polygon(
            DISPLAY_SURF,
            color,
            (
                (left + half, top),
                (left + BOX_SIZE - 1, top + half),
                (left + half, top + BOX_SIZE - 1),
                (left, top + half)
            )
        )

    elif shape == LINES:
        for i in range(0, BOX_SIZE, 4):
            pygame.draw.line(
                DISPLAY_SURF,
                color,
                (left, top + i),
                (left + i, top)
            )

            pygame.draw.line(
                DISPLAY_SURF,
                color,
                (left + i, top + BOX_SIZE - 1),
                (left + BOX_SIZE - 1, top + i)
            )

    elif shape == OVAL:
        pygame.draw.ellipse(
            DISPLAY_SURF,
            color,
            (
                left,
                top + quarter,
                BOX_SIZE,
                half
            )
        )


def get_shape_and_color(board, box_x, box_y):
    # The shape value is stored in board[x][y][0].
    # The color value is stored in board[x][y][1].
    return board[box_x][box_y][0], board[box_x][box_y][1]


def draw_box_covers(board, boxes, coverage):
    # Draw boxes being covered or revealed.
    for box in boxes:
        left, top = left_top_coords_of_box(box[0], box[1])

        pygame.draw.rect(
            DISPLAY_SURF,
            BG_COLOR,
            (left, top, BOX_SIZE, BOX_SIZE)
        )

        shape, color = get_shape_and_color(
            board,
            box[0],
            box[1]
        )

        draw_icon(shape, color, box[0], box[1])

        if coverage > 0:
            pygame.draw.rect(
                DISPLAY_SURF,
                BOX_COLOR,
                (left, top, coverage, BOX_SIZE)
            )

        pygame.display.update()

        FPS_CLOCK.tick(FPS)


def reveal_boxes_animation(board, boxesToReveal):
    # Do the box reveal animation.
    for coverage in range(BOX_SIZE, (-REVEAL_SPEED) - 1, -REVEAL_SPEED):
        draw_box_covers(board, boxesToReveal, coverage)


def cover_boxes_animation(board, boxesToCover):
    # Do the box cover animation.
    for coverage in range(0, BOX_SIZE + REVEAL_SPEED, REVEAL_SPEED):
        draw_box_covers(board, boxesToCover, coverage)


def draw_board(board, revealed):
    # Draw all boxes in their covered or revealed state.
    for box_x in range(BOARD_WIDTH):
        for box_y in range(BOARD_HEIGHT):
            left, top = left_top_coords_of_box(box_x, box_y)

            if not revealed[box_x][box_y]:
                # Draw a covered box.
                pygame.draw.rect(
                    DISPLAY_SURF,
                    BOX_COLOR,
                    (left, top, BOX_SIZE, BOX_SIZE)
                )

            else:
                # Draw the revealed icon.
                shape, color = get_shape_and_color(
                    board,
                    box_x,
                    box_y
                )

                draw_icon(shape, color, box_x, box_y)


def draw_highlight_box(box_x, box_y):
    left, top = left_top_coords_of_box(box_x, box_y)

    pygame.draw.rect(
        DISPLAY_SURF,
        HIGHLIGHT_COLOR,
        (
            left - 5,
            top - 5,
            BOX_SIZE + 10,
            BOX_SIZE + 10
        ),
        4
    )


def start_game_animation(board):
    # Store data describing which board boxes are currently covered.
    # This state is used by the drawing functions to control what the
    # player sees on the screen.

    # 10 rows and 7 columns
    # [False, False, False, False, False, False, False]
    # [False, False, False, False, False, False, False]
    # ...
    # [False, False, False, False, False, False, False]
    covered_boxes = generate_revealed_boxes_data(False)

    # Create a list containing the coordinates of every box on the board.
    # Pygame programs commonly represent positions as (x, y) tuples.
    boxes = []

    # Visit every column and row to generate coordinates for the entire
    # game board.

    # BOARD_WIDTH = 10
    # BOARD_HEIGHT = 7
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            # boxes.append((0, 0))
            # ...
            # boxes.append((9, 6))

            # boxes = [(0, 0), (0, 1), ... (9, 5), (9, 6)]
            boxes.append((x, y))

    # Shuffle the coordinates so the animation reveals boxes in a random
    # order instead of moving predictably across the board.
    random.shuffle(boxes)

    # Divide the boxes into small groups so the animation can update only
    # a few boxes during each animation step.
    box_groups = split_into_groups_of(8, boxes)

    # Draw the initial board state before the animation begins.
    # Pygame animations work by repeatedly drawing updated game states.
    draw_board(board, covered_boxes)

    # Process one small group at a time to create a sequence of visual
    # changes that the player perceives as an animation.
    for box_group in box_groups:
        # Reveal the current group of boxes by repeatedly updating and
        # redrawing the display during the reveal animation.
        reveal_boxes_animation(board, box_group)

        # Cover the same boxes again, creating the flashing effect used
        # during the game's starting animation.
        cover_boxes_animation(board, box_group)


def game_won_animation(board):
    # Flash the background color when the player has won.
    covered_boxes = generate_revealed_boxes_data(True)

    color1 = LIGHT_BG_COLOR
    color2 = BG_COLOR

    for i in range(13):
        color1, color2 = color2, color1

        DISPLAY_SURF.fill(color1)

        draw_board(board, covered_boxes)

        pygame.display.update()

        pygame.time.wait(300)


def has_won(revealed_boxes):
    # Return True if all boxes have been revealed.
    for i in revealed_boxes:
        if False in i:
            return False

    return True


if __name__ == '__main__':
    main()