import pygame
import sys

# Learning goal:
# Know how to use pygame.font.Font() and render() to create
# text, blit() to display it, KEYDOWN events to detect keyboard
# input, and pygame.mixer.Sound() with play() to trigger sound
# effects.

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

# Pygame needs a way of turning text into something that can
# actually be drawn to a Surface. A Font object is what tells
# Pygame how the text should look, including which font and
# what size to use.

# A Font object knows how to render text.

# The first argument is the font file path.
# A font file path is the location of a font file on your computer.
# It tells Pygame which font file to load and use for the text.
# Passing None tells Pygame to use its default font.

# The second argument is the font size.
font = pygame.font.Font(None, 48)

# Load the sound effect.

# To provide pygame with a way of loading sound, pygame.mixer.Sound()
# loads a sound file into a Sound object so that pygame can play it.

# Make sure piano_note.wav is in the same folder as this program.
beep_sound = pygame.mixer.Sound("piano-note.wav")

# Store the player's score.
score = 0

# Start the main game loop.
while True:

    # Fill the entire window with white.
    screen.fill(WHITE)

    # Create a Surface object containing the rendered text which is the
    # score text in this case.

    # The Font object stores the font configuration (font style and font size).

    # The render() method belongs to a Font object and takes a
    # string and rendering parameters, then creates and returns
    # a new pygame.Surface object containing the rendered text.

    # The first argument is the text.
    # True being the second argument enables anti-aliasing.

    # Anti-aliasing smooths the edges of the text so they look less
    # rough or uneven.

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
    # The second argument specifies where to place the Surface.
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

    # Update the entire display or just selected parts of the display.
    pygame.display.update()