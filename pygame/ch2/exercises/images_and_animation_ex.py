# Goal:
# Practice loading one image, drawing multiple copies of it,
# and animating each one independently.

# Requirements:
# 1. Make all three animals move to the right.
# 2. Give each animal a different speed.
# 3. Draw all three animals every frame.
# 4. Place each animal on a different row.
# 5. When a animal completely leaves the right side of the window,
#    move it just outside the left side of the window.

import pygame
import sys

# Start every pygame module.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Multiple Images and Animation")

# Create a Clock object to control the frame rate.
clock = pygame.time.Clock()

# Define some colours.
WHITE = (255, 255, 255)

# Load the cheetah image.
cheetah = pygame.image.load("cheetah.webp")

# Store the bald eagle's position.
cheetah_x = 0
cheetah_y = 100
cheetah_speed = 3

# Store the caucasian shepherd's position.
caucasian_shepherd_x = -200
caucasian_shepherd_y = 250
caucasian_shepherd_speed = 5

# Store the bald eagle's position.
bald_eagle_x = -400
bald_eagle_y = 400
bald_eagle_speed = 7

# Keep the game running.
while True:

    # Check every event.
    for event in pygame.event.get():

        # Check if the player closes the window.
        if event.type == pygame.QUIT:

            # Shut down pygame.
            pygame.quit()

            # Exit the program.
            sys.exit()

    # Move the bald eagle.
    # Finish this.

    # Move the caucasian shepherd.
    # Finish this.

    # Move the bald eagle.
    # Finish this.

    # Check if the cheetah has completely left the window.
    # Finish this.

    # Check if the caucasian shepherd has completely left the window.
    # Finish this.

    # Check if the bald eagle has completely left the window.
    # Finish this.

    # Fill the background before drawing
    # the next frame.
    screen.fill(WHITE)

    # Draw the cheetah.
    # Finish this.

    # Draw the caucasian shepherd.
    # Finish this.

    # Draw the bald eagle.
    # Finish this.

    # Update the entire display or just selected parts of the display.
    pygame.display.update()

    # Limit the game to 60 frames per second.
    clock.tick(60)