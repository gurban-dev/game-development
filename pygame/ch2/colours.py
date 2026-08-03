'''
Learning Goals
• RGB (Red, Green and Blue) colours
• Variables
• Surface methods
• fill()

Create a window that displays a:
• Red screen.
• Green screen.
• Blue screen.

Change the colour every time the program runs.
'''

# Import the pygame module.
import pygame

# Import the sys module.
import sys

import random

# Import useful pygame constants.
# The asterisk (*) indicates that everything will be imported.
from pygame.locals import *

# Initialise pygame.
pygame.init()

# Create the game window.
# The width is 600 pixels.
# The height is 400 pixels.

# set_mode() returns a Surface object representing the screen.
window = pygame.display.set_mode((600, 400))

# Create colour variables with RGB values which is how computers
# create colours.
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# The names of the above variables are written in capital letters
# because they are constants and should be modified.

# random.randint(start, stop) generates a random integer
# from start (inclusive) to stop (inclusive).

# Fill the screen with red by painting every pixel that makes up
# the Surface object red.
# window.fill(RED)

random_colour = (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
)

window.fill(random_colour)

# Main game loop.
while True:
    # Get all events from the event queue and process them.
    for event in pygame.event.get():

        # Check if the user clicked the X button located at the
        # top-right corner of the game window.
        if event.type == QUIT:

            # Shut down pygame.
            pygame.quit()

            # Exits the program by terminating pygame.
            sys.exit()
    
    # Update the screen and show any changes.
    pygame.display.update()