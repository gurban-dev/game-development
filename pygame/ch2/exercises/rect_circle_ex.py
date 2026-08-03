# Import the pygame library.
import pygame

# Initialize pygame.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Draw a House")

# Define some colors.
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

    # Fill the background with the sky color.
    screen.fill(SKY_BLUE)

    # Exercise

    # Draw the grass.

    # Use pygame.draw.rect().

    # Color:
    # GREEN

    # Position:
    # x = 0
    # y = 450

    # Size:
    # width = 800
    # height = 150

    # Your code here


    # Draw the house.

    # Use pygame.draw.rect().

    # Color:
    # WHITE

    # Position:
    # x = 250
    # y = 220

    # Size:
    # width = 300
    # height = 230

    # Your code here


    # Draw the door.

    # Use pygame.draw.rect().

    # Color:
    # BROWN

    # Position:
    # x = 360
    # y = 330

    # Size:
    # width = 80
    # height = 120

    # Your code here

    # Draw the left window.

    # Use pygame.draw.rect().

    # The window should be:
    # • Gray
    # • 60 pixels wide
    # • 60 pixels tall
    # • Located at (285, 260)

    # Your code here


    # Draw the right window.

    # Use pygame.draw.rect().

    # The window should be:
    # • Gray
    # • 60 pixels wide
    # • 60 pixels tall
    # • Located at (455, 260)

    # Your code here


    # Draw the sun.

    # Draw a yellow circle centered at (700, 100)
    # with a radius of 50 pixels.

    # Your code here


    # Updates the entire window whereas pygame.display.update()
    # updates only specific portions of the screen.
    pygame.display.flip()

# Exit pygame.
pygame.quit()