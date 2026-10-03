import pygame
import sys


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

BOARD_WIDTH = 4
BOARD_HEIGHT = 3

BOX_SIZE = 60
GAP_SIZE = 10

BACKGROUND_COLOR = (255, 255, 255)
BOX_COLOR = (0, 128, 0)


def get_board_position():
    """Calculate the pixel position where the centered board begins."""
    board_width = BOARD_WIDTH * BOX_SIZE + (BOARD_WIDTH - 1) * GAP_SIZE
    board_height = BOARD_HEIGHT * BOX_SIZE + (BOARD_HEIGHT - 1) * GAP_SIZE

    start_x = (WINDOW_WIDTH - board_width) // 2
    start_y = (WINDOW_HEIGHT - board_height) // 2

    return start_x, start_y


def board_to_pixel(column, row):
    """Convert board coordinates to the pixel position of a square."""
    start_x, start_y = get_board_position()

    x = start_x + column * (BOX_SIZE + GAP_SIZE)
    y = start_y + row * (BOX_SIZE + GAP_SIZE)

    return x, y


def draw_board(screen):
    """Draw every square on the board."""
    for row in range(BOARD_HEIGHT):
        for column in range(BOARD_WIDTH):
            x, y = board_to_pixel(column, row)

            pygame.draw.rect(
                screen,
                BOX_COLOR,
                (x, y, BOX_SIZE, BOX_SIZE)
            )


def pixel_to_board(x, y):
    """Convert a pixel position to board coordinates."""
    start_x, start_y = get_board_position()

    relative_x = x - start_x
    relative_y = y - start_y

    if relative_x < 0 or relative_y < 0:
        return None

    column = relative_x // (BOX_SIZE + GAP_SIZE)
    row = relative_y // (BOX_SIZE + GAP_SIZE)

    offset_x = relative_x % (BOX_SIZE + GAP_SIZE)
    offset_y = relative_y % (BOX_SIZE + GAP_SIZE)

    if offset_x >= BOX_SIZE or offset_y >= BOX_SIZE:
        return None

    if column >= BOARD_WIDTH or row >= BOARD_HEIGHT:
        return None

    return column, row


def print_mouse_position():
    """Print the board position currently under the mouse."""
    mouse_x, mouse_y = pygame.mouse.get_pos()

    position = pixel_to_board(mouse_x, mouse_y)

    if position is not None:
        column, row = position
        print(f"Column: {column}, Row: {row}")


def main():
    """Run the Pygame application."""
    pygame.init()

    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )

    pygame.display.set_caption("4x3 Grid")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)

        draw_board(screen)
        print_mouse_position()

        pygame.display.update()


if __name__ == "__main__":
    main()