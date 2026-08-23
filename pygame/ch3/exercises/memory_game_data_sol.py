import pygame
import sys

# Main goals of this exercise:
# • Learn how to organize game data by storing related values
#   in constants and tuples.
# • Practice organizing a Pygame program by separating drawing
#   code into reusable functions.
# • Use nested loops to draw a complete game board without
#   repeating code.
# • Understand how main() controls the game loop and calls the
#   functions that draw the game.

# Initialize Pygame and prepare its modules for use.
pygame.init()

# Create an 800 x 600 game window.
screen = pygame.display.set_mode((800, 600))

# Set the title displayed at the top of the window.
pygame.display.set_caption("Memory Game Foundation")

# Create a clock to control the game's frame rate.
clock = pygame.time.Clock()

# Define the shapes that can be used in the memory game.
DONUT = "donut"
SQUARE = "square"
DIAMOND = "diamond"
LINES = "lines"
OVAL = "oval"

# Group all available shapes into one tuple.
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

# Define the colors that can be used in the memory game.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (160, 32, 240)
CYAN = (0, 255, 255)

# Group all available colors into one tuple.
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)


# Define the number of columns and rows on the board.
BOARDWIDTH = 6
BOARDHEIGHT = 4

# Calculate how many boxes will be on the board.
TOTALBOXES = BOARDWIDTH * BOARDHEIGHT

# Make sure there are enough shape and color combinations.
assert len(ALLSHAPES) * len(ALLCOLORS) >= TOTALBOXES

# Define the size of each box on the board.
BOX_SIZE = 80

# Define the space between boxes.
GAP = 10

# Define where the board starts on the screen.
START_X = 100
START_Y = 80

# Define colors used for the background and message area.
BACKGROUND = (30, 50, 100)
MESSAGE_COLOR = (230, 230, 230)

def draw_board():
    # Loop through every row of the board.
    for row in range(BOARDHEIGHT):

        # Loop through every column of the board.
        for column in range(BOARDWIDTH):

            # Calculate the horizontal position of the current box.
            x = START_X + column * (BOX_SIZE + GAP)

            # Calculate the vertical position of the current box.
            y = START_Y + row * (BOX_SIZE + GAP)

            # Alternate between red and blue based on the box position.
            if (row + column) % 2 == 0:
                box_color = RED
            else:
                box_color = BLUE

            # Draw the current box using its calculated position.
            pygame.draw.rect(
                screen,
                box_color,
                (x, y, BOX_SIZE, BOX_SIZE)
            )

def draw_message():
    # Position the message area below the game board.
    message_x = START_X
    message_y = START_Y + BOARDHEIGHT * (BOX_SIZE + GAP) + 20

    # Calculate the width of the message area.
    message_width = BOARDWIDTH * (BOX_SIZE + GAP) - GAP

    # Draw an empty rectangle that can later contain game messages.
    pygame.draw.rect(
        screen,
        MESSAGE_COLOR,
        (message_x, message_y, message_width, 50)
    )

def main():
    # Keep the game running until the player closes the window.
    running = True

    while running:

        # Check every event that has happened since the previous frame.
        for event in pygame.event.get():

            # Stop the game when the player clicks the window's X button.
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen before drawing the next frame.
        screen.fill(BACKGROUND)

        # Draw all of the boxes on the game board.
        draw_board()

        # Draw the message area below the board.
        draw_message()

        # Show everything that was drawn on the screen.
        pygame.display.update()

        # Keep the game running at a maximum of 60 frames per second.
        clock.tick(60)

# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()

# Quit Pygame after the main game loop finishes.
pygame.quit()

# Close the Python program.
sys.exit()