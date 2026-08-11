import pygame
import sys

# Learning goals:
# Learn how a Pygame program stores game data.
# Use constants to describe shapes and colors.
# Group related values into tuples.
# Use assert to check game requirements.
# Practice the basic Pygame game loop.
# Prepare data for a future memory game.

# Initialize Pygame.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Memory Game Data")

# Create a clock for controlling the frame rate.
clock = pygame.time.Clock()

# Store each possible shape as a string.
DONUT = "donut"
SQUARE = "square"
DIAMOND = "diamond"
LINES = "lines"
OVAL = "oval"

# Store each color as an RGB tuple.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

# Group all possible colors into one tuple.
ALLCOLORS = (
    RED,
    GREEN,
    BLUE,
    YELLOW,
    ORANGE,
    PURPLE,
    CYAN
)

# Group all possible shapes into one tuple.
ALLSHAPES = (
    DONUT,
    SQUARE,
    DIAMOND,
    LINES,
    OVAL
)

# Define how many boxes the board will contain.
BOARDWIDTH = 6
BOARDHEIGHT = 4

# Make sure there are enough shape and color combinations.
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT

# Keep the program running.
running = True

while running:

    # Check for events.
    for event in pygame.event.get():

        # Close the program when the player clicks the X button.
        if event.type == pygame.QUIT:
            running = False

    # Clear the window.
    screen.fill((30, 50, 100))

    # Update the entire Pygame display after drawing.
    # It can update the whole screen or selected areas.
    # With no arguments, it updates the entire display.
    # pygame.display.flip() updates the entire display only.
    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()