# Import the pygame module.
import pygame

# Import the sys module.
import sys

# Start every pygame module.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Bouncing Square")

# Create a Clock object to control the frame rate.
clock = pygame.time.Clock()

# Store the square's horizontal position.
square_x = 0

# Store how many pixels the square moves every frame.

# Positive values move the square to the right.
# Negative values move the square to the left.
speed = 5

# Define some colours.
WHITE = (255, 255, 255)
GREEN = (0, 180, 0)

# Keep the game running.
while True:

    # Check every event.
    for event in pygame.event.get():

        # Check if the player closes the window.
        if event.type == pygame.QUIT:

            # Shut down pygame.
            pygame.quit()

            # Exit the program.
            sys.exit()

    # Move the square by changing its x-coordinate.

    # This line runs once every frame, creating animation.
    square_x += speed

    # ---------------------------------------
    # The game window is 800 pixels wide.
    #
    # The square is 100 pixels wide.
    #
    # Think about:
    #
    # 1. How can you tell when the square
    #    reaches the right edge?
    #
    # 2. How can you tell when the square
    #    reaches the left edge?
    #
    # 3. What should happen to the speed
    #    when the square touches either edge?
    # ---------------------------------------

    # Fill the background before drawing
    # the next frame.
    screen.fill(WHITE)

    # Draw the square at its current position.
    pygame.draw.rect(screen, GREEN, (square_x, 250, 100, 100))

    # Show everything drawn during this frame.
    pygame.display.update()

    # Limit the game to 60 frames every second.
    clock.tick(60)