import pygame
import sys

'''
Objective:
Practice using pygame.draw.polygon() by drawing an outlined neon
purple decagon.

Requirements:
• Draw the provided decagon (ten-sided polygon).
• Use the NEON_PURPLE colour.
• Use the provided polygon points without modifying them.
• Set the outline width to 8 pixels.
• Leave the inside of the decagon unfilled.
'''

# Start all pygame modules.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the title shown at the top of the window.
pygame.display.set_caption("Draw Decagon")

WHITE = (255, 255, 255)

NEON_PURPLE = (139, 0, 139)

polygon_points = [
    (400, 100),
    (480, 130),
    (540, 200),
    (540, 290),
    (480, 360),
    (400, 390),
    (320, 360),
    (260, 290),
    (260, 200),
    (320, 130)
]

while True:
    screen.fill(WHITE)

    # Draw the outlined decagon here using pygame.draw.polygon().


    # Check every event that has occurred.
    for event in pygame.event.get():

        # Close the program if the user clicks the window's close button.
        if event.type == pygame.QUIT:

            # Shut down all pygame modules.
            pygame.quit()

            # Exit the Python program.
            sys.exit()

    # Update the entire display since the entire screen is
    # redrawn every frame.
    pygame.display.flip()