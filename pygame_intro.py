# A namespace is a place where names are stored for your program.

# Some examples:

# Variable names
# E.g. num = 10
# The variable 'num' is now in your namespace.

# Import the Pygame module, which provides functionality
# for graphics, input handling, sound, and game timing.
import pygame

# Import Python's sys module so the interpreter can
# terminate the program cleanly using sys.exit().
import sys

# Initialiases all imported Pygame modules.
pygame.init()

# Establish the window dimensions in pixels.
WIDTH = 800
HEIGHT = 600

# It is noticeable that WIDTH and HEIGHT are constants because
# they are written in uppercase letters.

# WIDTH and HEIGHT are constants because they define the
# size of the game window in pixels.

# Pygame creates a window and returns a Surface object.
# A Surface is an area of memory that represents pixels.
# Everything is drawn onto this surface.

# WIDTH and HEIGHT are are passed to the set_mode() function
# in a tuple because Pygame expts width and height as a pair.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title shown in the window's title bar.
pygame.display.set_caption("Pygame Fundamentals")

# The Clock object makes it possible to control the timing
# of the game.
clock = pygame.time.Clock()

# Define the coordinates of the player since Pygame uses
# screen coordinates.

# (0, 0) is the top-left corner of the screen.
# Increasing x moves the position rightward.
# Increasing y moves the position downward.
player_x = 375
player_y = 275

# Define the dimensions for the player's rectangle.
player_width = 50
player_height = 50

# Define the speed of the player's rectangle.

# Pressing the keyboard's left arrow subtracts 5 pixels from
# the x coordinate.

# Pressing the keyboard's right arrow would add 5 pixels to
# the x coordinate.
player_speed = 5

# Create the main game loop.
running = True

while running:
    # Event processing.
    pass