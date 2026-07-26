# Import the modules we need.
import pygame
import sys

# Start all of Pygame's modules.
pygame.init()

# Create a window that is 800 pixels wide and 600 pixels tall.
screen = pygame.display.set_mode((800, 600))

# Set the text shown in the window's title bar.
pygame.display.set_caption("Static Square")

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# This variable controls whether the game loop keeps running.
running = True

# The game loop runs many times every second.
# Each time through the loop, we clear the screen and
# draw the same square in exactly the same position.
# Because its position never changes, the square appears
# to be perfectly still.
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paint the entire background white before drawing anything else.
    screen.fill(WHITE)

    # Draw a blue square.
    # (100, 250) is the top-left corner.
    # 100 is the width.
    # 100 is the height.
    pygame.draw.rect(screen, "blue", (100, 250, 100, 100))

    # Show everything we've drawn during this frame.
    pygame.display.flip()

pygame.quit()
sys.exit()