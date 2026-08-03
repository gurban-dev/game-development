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

            # Shut down pygame.
            pygame.quit()

            # Exit the program.
            sys.exit()

        # Check if a key was pressed.
        if event.type == KEYDOWN:

            # Check if the H key was pressed.
            if event.key == K_h:

                # Change the background colour to yellow.
                window.fill(YELLOW)

                # Change the window title.
                pygame.display.set_caption("Happy")

                # Print the mood name.
                print("Happy")

            # Check if the S key was pressed.
            elif event.key == K_s:

                # Change the background colour to blue.
                window.fill(BLUE)

                # Change the window title.
                pygame.display.set_caption("Sad")

                # Print the mood name.
                print("Sad")

            # Check if the A key was pressed.
            elif event.key == K_a:

                # Change the background colour to red.
                window.fill(RED)

                # Change the window title.
                pygame.display.set_caption("Angry")

                # Print the mood name.
                print("Angry")

            # Check if the R key was pressed.
            elif event.key == K_r:

                # Create a random colour.
                random_colour = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )

                # Fill the screen with the random colour.
                window.fill(random_colour)

                # Change the window title.
                pygame.display.set_caption("Random Mood")

                # Print the mood name.
                print("Random Mood")

    # Update the display.
    pygame.display.update()

'''
Questions and Answers
1. How do we detect that a key was pressed?

   We check whether the event type is pygame.KEYDOWN. If it is,
   Pygame is telling us that a key has been pressed.

2. How do we find out which key was pressed?

   We use event.key, which stores the specific key that was pressed.
   For example, pygame.K_SPACE represents the Space key and pygame.K_a
   represents the A key.
'''