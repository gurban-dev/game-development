# Goal:
# Create a simple soundboard.

# Requirements:
# 1. Display the title "Animal Soundboard" near the top of the window.
# 2. Display the message "Press SPACE to play a sound."
# 3. Display the number of times the sound has been played.
# 4. Every time the SPACE key is pressed:
#    - Increase the play counter by 1.
#    - Play the beep sound.
# 5. When the sound has been played 10 times,
#    display the message "You are a Sound Master!".

import pygame
import sys

# Start every pygame module.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Animal Soundboard")

# Store some colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (40, 120, 255)
GREEN = (0, 170, 0)

# Create a Font object.
font = pygame.font.Font(None, 48)

# Load the sound effect.
beep_sound = pygame.mixer.Sound("beep.wav")

# Store the number of times the sound has been played.
play_count = 0

# Start the main game loop.
while True:

    # Fill the window with white.
    screen.fill(WHITE)

    # Create the title text.
    # Finish this.

    # Create the instruction text.
    # Finish this.

    # Create the play counter text.
    # Finish this.

    # Draw the title.
    # Finish this.

    # Draw the instructions.
    # Finish this.

    # Draw the play counter.
    # Finish this.

    # Display a congratulation message after
    # the sound has been played 10 times.
    # Finish this.

    # Check every event.
    for event in pygame.event.get():

        # Check if the player closed the window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check if a keyboard key was pressed.
        if event.type == pygame.KEYDOWN:

            # Check if the SPACE key was pressed.
            if event.key == pygame.K_SPACE:

                # Increase the play counter.
                # Finish this.

                # Play the sound effect.
                # Finish this.

                pass

    # Updates the entire display or just selected parts of the display.
    pygame.display.update()