# Import the pygame module so we can create games.
import pygame

# Import the sys module so we can safely exit the program.
import sys

# Start all of Pygame's modules.
pygame.init()

# Create a game window that is 800 pixels wide and 600 pixels tall.
screen = pygame.display.set_mode((800, 600))

# Set the text shown in the window's title bar.
pygame.display.set_caption("Moving Square")

# Store the square's horizontal (x) position.
# It starts at the left side of the window.
square_x_pos = 0

# Define some colours using RGB values.
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# This variable controls whether the game loop keeps running.
running = True

# The game loop runs over and over again until the user
# closes the window.
while running:

    # Check every event that has happened since the last frame.
    for event in pygame.event.get():

        # If the user clicks the window's close button,
        # stop the game loop.
        if event.type == pygame.QUIT:
            running = False

    # Paint the entire background white before drawing anything else.
    screen.fill(WHITE)

    # Draw a blue square on the screen.

    # square_x_pos is the square's x-coordinate.
    # 250 is the square's y-coordinate.
    # 100 is the square's width.
    # 100 is the square's height.
    pygame.draw.rect(screen, BLUE, (square_x_pos, 250, 100, 100))

    # Increase the x-coordinate by 1 pixel.
    # On the next frame, the square will be drawn
    # slightly farther to the right.
    square_x_pos += 1

    # Update the entire display window by copying every pixel from
    # the display surface to the screen.
    pygame.display.flip()

# Shut down all of Pygame's modules.
pygame.quit()

# Exit the Python program.
sys.exit()