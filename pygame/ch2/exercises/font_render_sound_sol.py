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
# The Font object stores information about how the text should look.
font = pygame.font.Font(None, 48)

# Load the sound effect.
# Make sure piano-note.wav is in the same folder as this program.
beep_sound = pygame.mixer.Sound("piano-note.wav")

# Store the number of times the sound has been played.
# The counter starts at 0 because the sound has not been played yet.
play_count = 0

SCREEN_WIDTH = screen.get_width()

def calculate_centered_x(surface_obj):
    centered_x = (SCREEN_WIDTH - surface_obj.get_width()) // 2

    return centered_x

# Start the main game loop.
# The loop repeatedly draws the current game state,
# checks for events, and updates the display.
while True:

    # Fill the entire window with white.
    screen.fill(WHITE)

    # Create a Surface object containing the title text "Animal Soundboard".
    # render() converts the string into a Surface object that Pygame can draw.
    # True enables anti-aliasing, which smooths the edges of the text.
    # The third argument sets the text color.
    title_text = font.render(
        "Animal Soundboard",
        True,
        BLACK
    )

    # Create a Surface containing the instruction text.
    instruction_text = font.render(
        "Press SPACE to play a sound.",
        True,
        BLUE
    )

    # Create a Surface containing the current play count.
    # The f-string inserts the current value of play_count into the text.
    counter_text = font.render(
        f"Times played: {play_count}",
        True,
        BLACK
    )

    # The .blit() method places Surface objects onto the game window.

    # Draw the title near the top of the window.
    screen.blit(title_text, (calculate_centered_x(title_text), 50))

    # Draw the instructions below the title.
    screen.blit(instruction_text, (calculate_centered_x(instruction_text), 130))

    # Draw the play counter below the instructions.
    screen.blit(counter_text, (calculate_centered_x(counter_text), 210))

    # Check whether the sound has been played at least 10 times.
    if play_count >= 10:

        # Create a Surface containing the congratulation message.
        master_text = font.render(
            "You are a Sound Master!",
            True,
            GREEN
        )

        # Draw the congratulation message on the screen.
        screen.blit(master_text, (calculate_centered_x(master_text), 290))

    # Check every event that happened since the previous loop iteration.
    for event in pygame.event.get():

        # Check if the player closed the window.
        if event.type == pygame.QUIT:

            # Shut down Pygame before ending the program.
            pygame.quit()

            # End the Python program.
            sys.exit()

        # Check if a keyboard key was pressed.
        if event.type == pygame.KEYDOWN:

            # Check if the pressed key was the SPACE key.
            if event.key == pygame.K_SPACE:

                # Increase the number of times the sound has been played.
                # The += operator adds 1 to the current value.
                play_count += 1

                # Play the sound effect.
                beep_sound.play()

    # Update the entire display or certain parts of the display so that
    # changes become visible in the window.
    pygame.display.update()