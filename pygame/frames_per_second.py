import pygame
import sys

# Goal:
# Learn how to control how many times the game loop runs every
# second using a pygame.time.Clock object.

# Every time the game loop runs, the game creates one frame.

# If the game loop runs:
# • 30 times every second, the game runs at 30 FPS.
# • 60 times every second, the game runs at 60 FPS.
# • 120 times every second, the game runs at 120 FPS.

# FPS stands for Frames Per Second.

# Without limiting the FPS, a game will run as fast as a computer
# allows.

# Different computers have different speeds.
# An older computer may run at 90 FPS.
# A gaming computer may run at 800 FPS.

# This means the same game could run much faster on one computer
# than another.

# To make every player's game run at approximately the same speed,
# this program will utilize a Clock object.

# Start all pygame modules.
pygame.init()

# Create a game window that is 800 pixels wide and 600 pixels tall
# which instantiates the Surface class.
screen = pygame.display.set_mode((800, 600))

# Set the text shown in the window's title bar.
pygame.display.set_caption("Frames Per Second")

# Create a Clock object that helps regulate the frame rate.
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Horizontal position.
square_x = 0

# How many pixels the square moves.
speed = 5

while True:

    # Check every event that has happened since the last frame.
    for event in pygame.event.get():

        # If the user clicks the window's close button,
        # stop the game loop.
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

    # Move the square to the right.

    # Remember that 'speed' was assigned 5.

    # If the game runs at 60 FPS, the below line executes 60 times per
    # second.

    # 5 pixels * 60 frames -> 300 pixels per second

    # With 5 FPS, it executes only 5 times per second.
    # 5 pixels * 5 frames -> 25 pixels per second
    square_x += speed

    # If the square leaves the window, move it back to the left side.
    if square_x > 800:
        square_x = -50

    # Fill the window with white before drawing anything else.
    screen.fill(WHITE)

    # 250 is the y position.
    pygame.draw.rect(screen, BLUE, (square_x, 250, 50, 50))

    # Update the display so everything drawn becomes visible.
    pygame.display.update()

    # Attempt to limit the game to 60 frames per second.

    # 60 frames are being drawn every second.

    # Notice how the fewer frames the game draws each second, the slower
    # the square appears to move.
    clock.tick(5)