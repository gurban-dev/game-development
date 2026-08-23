import pygame
import sys

# Learning goals:
# Learn how functions organize a Pygame program.
# Learn to create functions for drawing game elements.
# Learn how functions make code easier to understand.
# Learn how main() controls the game loop.
# Learn how one function can call other functions.

# Initialize Pygame.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Memory Game Functions")

# Create a clock for controlling the frame rate.
clock = pygame.time.Clock()

# Store the colors used by the program.
NAVY = (30, 50, 100)
WHITE = (255, 255, 255)
BLUE = (100, 180, 255)

def draw_message():
    # Draw a rectangle that represents a message area.
    pygame.draw.rect(screen, BLUE, (250, 200, 300, 100))

def draw_board():
    # Draw a simple three-by-three board.
    for row in range(3):
        for column in range(3):
            x = 250 + column * 70
            y = 100 + row * 70

            pygame.draw.rect(
                screen,
                WHITE,
                (x, y, 60, 60)
            )

def main():
    # Keep the program running.
    running = True

    while running:

        # Check for events.
        for event in pygame.event.get():

            # Close the program when the player clicks the X button.
            if event.type == pygame.QUIT:
                running = False

        # Clear the window.
        screen.fill(NAVY)

        # Call the functions that draw the game.
        draw_board()
        draw_message()

        # Update the entire Pygame display after drawing.
        # It can update the whole screen or selected areas.
        # With no arguments, it updates the entire display.
        # pygame.display.flip() updates the entire display only.
        pygame.display.update()

        # Limit the FPS to 60.
        clock.tick(60)

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()