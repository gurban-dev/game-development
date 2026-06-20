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
pygame.display.set_caption("Press A, B, C, or D")

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

            # Change the title for any key press.
            pygame.display.set_caption("You pressed a key!")

            # If the A key was pressed.
            if event.key == K_a:

                # Change the title to Apple.
                pygame.display.set_caption("Apple")

            # If the B key was pressed.
            elif event.key == K_b:

                # Change the title to Banana.
                pygame.display.set_caption("Banana")

            # If the C key was pressed.
            elif event.key == K_c:

                # Change the title to Cherry.
                pygame.display.set_caption("Cherry")

            # If the D key was pressed.
            elif event.key == K_d:

                # Change the title to Date.
                pygame.display.set_caption("Date")

        # Check if a key was released.
        if event.type == KEYUP:

            # Print a message to the terminal.
            print("Key was released.")

    # Update the screen.
    pygame.display.update()

'''
Questions and Answers
1. How would you make the title change to the fruit named "Date" when
   the D key is pressed?

   You would check if the event is a KEYDOWN event and whether
   the key pressed is pygame.K_d. If it is, change the window
   title to "Date".

2. How would you make the title say "You pressed a key!" for any key?

   You would check for a KEYDOWN event and set the window title
   to "You pressed a key!" without checking which specific key
   was pressed.

3. What happens if you replace KEYDOWN with KEYUP?

   Replacing KEYDOWN with KEYUP means the code will run when a
   key is released instead of when it is pressed.

4. How would you make the message "Key was released." printed in the
   terminal?

   You would check for a KEYUP event and use a print() statement:
   if event.type == pygame.KEYUP:
       print("Key was released.")
'''