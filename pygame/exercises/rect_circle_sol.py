# Import the pygame library.
import pygame

# Initialise pygame.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Draw a House")

# Define some colours.
SKY_BLUE = (135, 206, 235)
GREEN = (34, 177, 76)
BROWN = (150, 75, 0)
GRAY = (170, 170, 170)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Create a variable that controls the game loop.
running = True

# Start the game loop.
while running:

    # Check for events.
    for event in pygame.event.get():

        # Check if the user closes the window.
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with the sky colour.
    screen.fill(SKY_BLUE)

    # Draw the grass.

    # The rectangle starts at x = 0 and y = 450.
    # It stretches across the entire width of the window.
    pygame.draw.rect(
        screen,
        GREEN,
        (0, 450, 800, 150)
    )

    # Draw the main part of the house.

    # The rectangle begins at (250, 220).
    # It is 300 pixels wide and 230 pixels tall.
    pygame.draw.rect(
        screen,
        WHITE,
        (250, 220, 300, 230)
    )

    # Draw the door.

    # The door is another rectangle positioned near the
    # bottom-centre of the house.
    pygame.draw.rect(
        screen,
        BROWN,
        (360, 330, 80, 120)
    )

    # Draw the left window.

    # Since the width and height are both 60 pixels,
    # this rectangle forms a square.
    pygame.draw.rect(
        screen,
        GRAY,
        (285, 260, 60, 60)
    )

    # Draw the right window.

    # This window has the same size as the left window.
    # Only its x-coordinate changes.
    pygame.draw.rect(
        screen,
        GRAY,
        (455, 260, 60, 60)
    )

    # Draw the sun.

    # Unlike rectangles, circles are positioned using
    # their centre point instead of their top-left corner.
    pygame.draw.circle(
        screen,
        YELLOW,
        (700, 100),
        50
    )

    # Update the entire display so all drawings appear.
    pygame.display.flip()

# Exit pygame.
pygame.quit()