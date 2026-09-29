import pygame

# Define the size of the Pygame window in pixels.
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Define the number of columns and rows in the board.
BOARD_WIDTH = 4
BOARD_HEIGHT = 3

# Define the size of each square and the gap between squares.
BOX_SIZE = 60
GAP_SIZE = 10

# Define the colors used by the program.
BACKGROUND_COLOR = (30, 30, 30)
BOX_COLOR = (0, 200, 100)


# Convert board coordinates into pixel coordinates.
# board_x and board_y identify a square on the grid.
def get_box_pixel_position(board_x, board_y):
    pixel_x = board_x * (BOX_SIZE + GAP_SIZE)
    pixel_y = board_y * (BOX_SIZE + GAP_SIZE)

    return pixel_x, pixel_y


# Draw every square on the board.
def draw_board(screen):
    # The outer loop visits each row.
    for board_y in range(BOARD_HEIGHT):

        # The inner loop visits each column in the current row.
        for board_x in range(BOARD_WIDTH):

            # Convert the board position into a pixel position.
            pixel_x, pixel_y = get_box_pixel_position(board_x, board_y)

            # Create a rectangle at the calculated pixel position.
            box_rect = pygame.Rect(
                pixel_x,
                pixel_y,
                BOX_SIZE,
                BOX_SIZE
            )

            # Draw the square onto the screen.
            pygame.draw.rect(screen, BOX_COLOR, box_rect)


# Initialize all Pygame modules.
pygame.init()

# Create the Pygame window.
screen = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT)
)

# Give the window a title.
pygame.display.set_caption("4x3 Grid")

# Keep the main loop running until the user closes the window.
running = True

while running:

    # Check every event that has occurred since the last frame.
    for event in pygame.event.get():

        # Stop the program when the user closes the window.
        if event.type == pygame.QUIT:
            running = False

    # Fill the entire window with the background color.
    screen.fill(BACKGROUND_COLOR)

    # Draw all of the squares on the board.
    draw_board(screen)

    # Display the completed frame.
    pygame.display.update()


# Shut down Pygame after the main loop ends.
pygame.quit()