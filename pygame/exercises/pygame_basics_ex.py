'''
Exercise: Secret Title Changer

Goal
Create a window that changes its title when certain keys are pressed.

Requirements
When the user presses:
A -> title becomes "Apple"
B -> title becomes "Banana"
C -> title becomes "Cherry"

The window should still close properly when the X button is clicked.
'''

# Import the pygame module.
import pygame

# Import the sys module.
import sys

# Import useful pygame constants.
from pygame.locals import *

# Initialize pygame.
pygame.init()

# Create the game window.
window = pygame.display.set_mode((500, 400))

# Set the starting title.
pygame.display.set_caption("Press A, B, or C")

# Main game loop.
while True:

    # Process all events.
    for event in pygame.event.get():

        # Check if the user clicked the close button.
        if event.type == QUIT:

            # Shut down pygame.
            pygame.quit()

            # Exit the program.
            sys.exit()

        # Check if a key was pressed.
        if event.type == KEYDOWN:

            # If the A key was pressed.
            if event.key == K_a:
                pygame.display.set_caption("Apple")

            # If the B key was pressed.
            elif event.key == K_b:
                pygame.display.set_caption("Banana")

            # If the C key was pressed.
            elif event.key == K_c:
                pygame.display.set_caption("Cherry")

    # Update the screen.
    pygame.display.update()

'''
Questions
1. How would you make the title change to the fruit named "Date" when
   the D key is pressed?

2. How would you make the title say "You pressed a key!" for any key?

3. What happens if you replace KEYDOWN with KEYUP?

4. How would you make the message "Key was released." printed in the
   terminal?
'''