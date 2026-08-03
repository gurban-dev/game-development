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

# Initialise all imported Pygame modules.
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

# 'screen' can be thought of as a canvas.

# WIDTH and HEIGHT are passed to the set_mode() function
# in a tuple because Pygame expects width and height as a pair.
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

# Remember that the expression written in a while clause should
# be descriptive in the sense that it makes it clear what
# condition must be True for the block of code to run.
while running:
    # Event processing.
    
    # Check for all incoming events.
    for event in pygame.event.get():

        # Check if the user has closed their window.
        if event.type == pygame.QUIT:
            running = False

    # Fill the entire screen with black.
    screen.fill((0, 0, 0))

    # Rect is a class provided by Pygame.

    # It represents a rectangle using:
    # (x, y, width, height)

    rectangle_width = WIDTH - 50
    recetangle_height = HEIGHT - 50

    # Horizontally and vertically center the rectangle.

    # rectangle_x = 25
    rectangle_x = (WIDTH - rectangle_width) // 2

    # rectangle_y = 25
    rectangle_y = (HEIGHT - recetangle_height) // 2

    wall_rect = pygame.Rect(rectangle_x, rectangle_y, rectangle_width, recetangle_height)

    # Since 'screen' was passed as the first argument, this means
    # that the rectangle will be drawn on the screen surface.
    pygame.draw.rect(screen, (255, 255, 255), wall_rect)

    # Update the display by refreshing the screen so the user can
    # see any changes made during the current frame.

    # In a game, a frame is a single cycle of a game loop.
    # The current frame is the current cycle of the game loop.
    pygame.display.update()

# Shut down pygame cleanly.

# The word "cleanly" in this context means properly closing
# and releasing all of the resources that Pygame was using.

# The game window.
# Internal pygame modules.
# Keyboard/mouse handling.
pygame.quit()

# Exit the Python process itself.
sys.exit()