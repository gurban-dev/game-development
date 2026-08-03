import pygame
import sys

# Start every pygame module.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Walking Pet")

# Create a Clock object to control the frame rate.
clock = pygame.time.Clock()

# Define some colours.
WHITE = (255, 255, 255)

# Load an image from the current folder.
pet = pygame.image.load("pet.png")

# Store the pet's horizontal position.
pet_x = 0

# Store the pet's vertical position.
pet_y = 220

# Store how many pixels the pet moves each frame.
pet_speed = 4

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

    # Move the pet to the right.
    pet_x += pet_speed

    # Check if the pet has completely left the window.
    if pet_x > 800:

        # Move the pet just outside the left edge.
        pet_x = -pet.get_width()

    # Fill the background before drawing
    # the next frame.
    screen.fill(WHITE)

    # Copy the pet image onto the display surface.
    screen.blit(pet, (pet_x, pet_y))

    # Show everything drawn during this frame.
    pygame.display.update()

    # Limit the game to 60 frames every second.
    clock.tick(60)