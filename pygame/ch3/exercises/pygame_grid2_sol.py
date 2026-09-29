import pygame
import sys

# Define the size of each square in pixels.
BOXSIZE = 60

# Define the gap between neighboring squares.
GAPSIZE = 10

# Define how many columns the grid has.
BOARDWIDTH = 4

# Define how many rows the grid has.
BOARDHEIGHT = 3

# Define the size of the window.
WINDOWWIDTH = 4 * BOXSIZE + 5 * GAPSIZE
WINDOWHEIGHT = 3 * BOXSIZE + 4 * GAPSIZE

# Define the colors used by the program.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)


def getBoxAtPixel(mouse_x, mouse_y):
    # Loop through every column on the board.
    for box_x in range(BOARDWIDTH):

        # Loop through every row on the board.
        for box_y in range(BOARDHEIGHT):

            # Convert the board coordinates into pixel coordinates.
            left = GAPSIZE + box_x * (BOXSIZE + GAPSIZE)
            top = GAPSIZE + box_y * (BOXSIZE + GAPSIZE)

            # Create a rectangle representing the current square.
            rect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)

            # Check whether the mouse position is inside this square.
            if rect.collidepoint(mouse_x, mouse_y):

                # Return the board coordinates of the square.
                return box_x, box_y

    # Return None, None when the mouse is not over any square.
    return None, None


pygame.init()

# Create the game window.
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# Create a clock to control the frame rate.
clock = pygame.time.Clock()

# Store the board coordinates of the currently highlighted square.
highlighted_x = None
highlighted_y = None

# Continue running the program until the user quits.
while True:

    # Check each event that has occurred since the previous frame.
    for event in pygame.event.get():

        # Close the program when the user closes the window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current mouse position in pixel coordinates.
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Find which square contains the mouse.
    highlighted_x, highlighted_y = getBoxAtPixel(mouse_x, mouse_y)

    # Fill the background with white.
    screen.fill(WHITE)

    # Draw every square in the grid.
    for box_x in range(BOARDWIDTH):

        # Loop through every row of the current column.
        for box_y in range(BOARDHEIGHT):

            # Convert the square's board coordinates into pixel coordinates.
            left = GAPSIZE + box_x * (BOXSIZE + GAPSIZE)
            top = GAPSIZE + box_y * (BOXSIZE + GAPSIZE)

            # Create a rectangle for the current square.
            rect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)

            # Use the highlight color if this is the square under the mouse.
            if box_x == highlighted_x and box_y == highlighted_y:
                color = YELLOW

            # Use the normal color for every other square.
            else:
                color = GREEN

            # Draw the square using the selected color.
            pygame.draw.rect(screen, color, rect)

    # Update the window so the new frame becomes visible.
    pygame.display.update()

    # Limit the program to approximately 60 frames per second.
    clock.tick(60)