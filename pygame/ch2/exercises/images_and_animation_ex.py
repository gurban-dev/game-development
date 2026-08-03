# Goal:
# Practice loading one image, drawing multiple copies of it,
# and animating each one independently.

# Requirements:
# 1. Make all three pets move to the right.
# 2. Give each pet a different speed.
# 3. Draw all three pets every frame.
# 4. Place each pet on a different row.
# 5. When a pet completely leaves the right side of the window,
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

# Load the pet image.
pet = pygame.image.load("pet.png")

# Store the first pet's position.
pet1_x = 0
pet1_y = 100
pet1_speed = 3

# Store the second pet's position.
pet2_x = -200
pet2_y = 250
pet2_speed = 5

# Store the third pet's position.
pet3_x = -400
pet3_y = 400
pet3_speed = 7

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

    # Move the first pet.
    # Finish this.

    # Move the second pet.
    # Finish this.

    # Move the third pet.
    # Finish this.

    # Check if the first pet has completely left the window.
    # Finish this.

    # Check if the second pet has completely left the window.
    # Finish this.

    # Check if the third pet has completely left the window.
    # Finish this.

    # Fill the background before drawing
    # the next frame.
    screen.fill(WHITE)

    # Draw the first pet.
    # Finish this.

    # Draw the second pet.
    # Finish this.

    # Draw the third pet.
    # Finish this.

    # Show everything drawn during this frame.
    pygame.display.update()

    # Limit the game to 60 frames every second.
    clock.tick(60)