'''
Learning goals:
• Understand CLI (command-line input) vs GUI
  (Graphical user interface).

  A UI (user interface) can simply be a CLI.
  A GUI is made up of windows, icons, buttons, etc.
• Grasp what Pygame is.
• Create a game window.
• Comprehend the game loop.
• Close a window properly.

This program creates a simple Pygame window and introduces the
basic structure used by most games.

It uses a game loop to continuously check for events, update the
screen, and close the window properly when the user clicks the
X button.
'''

# Import the pygame module.
import pygame

# Import the sys module.
import sys

# Import useful pygame constants.
# The asterisk (*) indicates that everything will be imported.
from pygame.locals import *

# Initialise pygame.
pygame.init()

# Create the game window.
# The width is 500 pixels.
# The height is 400 pixels.

# set_mode() returns a Surface object representing the screen.
window = pygame.display.set_mode((500, 400))

# Set the title bar text.
pygame.display.set_caption("Practice Game")

# Main game loop.
while True:

    # Process all events.

    # The event object stores information about a user event
    # that has occurred, such as a key press, mouse click,
    # or window close event.

    # pygame.event.get() gets all events that have occurred since
    # the previous frame.

    # A frame refers to a single image drawn to the screen during
    # one of the iterations in the game loop.
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