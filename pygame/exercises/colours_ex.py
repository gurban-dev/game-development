# Exercise: Mood Screen

# Goal
# Create a program where the user can change the mood of the screen.

# Requirements 
# 1. Press H for Happy (yellow background)
# 2. Press S for Sad (blue background)
# 3. Press A for Angry (red background)
# 4. Press R for a random mood (random colour)
# 5. Print the mood name in the terminal
# 6. The window title should change to match the mood

# Starter Code:

# Import pygame.
import pygame

# Import sys.
import sys

# Import random.
import random

# Import pygame constants.
from pygame.locals import *

# Initialise pygame.
pygame.init()

# Create the game window.
window = pygame.display.set_mode((600, 400))

# Set the starting window title.
pygame.display.set_caption("Mood Screen")

# Create colour variables.
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fill the screen with a starting colour.
window.fill(YELLOW)

# Main game loop.
while True:

    # Process all events.
    for event in pygame.event.get():

        # Check if the user clicked the close button.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Check if a key was pressed.
        if event.type == KEYDOWN:

            # Add your code here.
            pass

    # Update the display.
    pygame.display.update()

'''
Questions
1. How do we detect that a key was pressed?

2. How do we find out which key was pressed?
'''