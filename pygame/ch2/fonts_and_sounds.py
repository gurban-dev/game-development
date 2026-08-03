import pygame
import sys

# Start every pygame module.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Fonts and Sounds")

# Store some commonly used colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (40, 120, 255)

# Create a Font object.

# The first argument is the font file.
# Passing None tells pygame to use the default font.

# The second argument is the font size.
font = pygame.font.Font(None, 48)

# Load the sound effect.

# Make sure beep.wav is in the same folder as this program.
beep_sound = pygame.mixer.Sound("beep.wav")

# Store the player's score.
score = 0

# Start the main game loop.
while True:

    # Fill the entire window with white.
    screen.fill(WHITE)

    # Create a Surface object containing the score text.

    # The first argument is the text.
    # The second argument turns anti-aliasing on.
    # The third argument is the text color.
    score_text = font.render(
        f"Score: {score}",
        True,
        BLACK
    )

    # Create another Surface object containing instructions.
    instruction_text = font.render(
        "Press SPACE to earn points!",
        True,
        BLUE
    )

    # Copy the score Surface onto the game window.
    screen.blit(score_text, (50, 50))

    # Copy the instructions onto the game window.
    screen.blit(instruction_text, (50, 130))

    # Check every event that happened.
    for event in pygame.event.get():

        # Check if the player closed the window.
        if event.type == pygame.QUIT:

            # Shut down pygame.
            pygame.quit()

            # End the program.
            sys.exit()

        # Check if a keyboard key was pressed.
        if event.type == pygame.KEYDOWN:

            # Check if the SPACE key was pressed.
            if event.key == pygame.K_SPACE:

                # Increase the score.
                score += 1

                # Play the sound effect.
                beep_sound.play()

    # Update the display.
    pygame.display.update()