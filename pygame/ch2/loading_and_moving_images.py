import pygame
import sys

# Learning goal:
# Understand how to load an image into a Pygame Surface,
# display it on the screen using blit(), control its position
# with X and Y coordinates, and update those coordinates under
# each frame to create a simple animation.

# Start every pygame module.
pygame.init()

# Create the game window (Surface object).
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Walking Cat")

# Create a Clock object to control the frame rate.
clock = pygame.time.Clock()

# Define some colours.
WHITE = (255, 255, 255)

# pygame.image.load() loads an image file and returns a
# Surface object.
cat = pygame.image.load("cat.jpeg")

# Store the cat's horizontal position.
cat_x = 0

# Store the cat's vertical position (220 pixels downwards).
cat_y = 220

# Store how many pixels the cat moves each frame.
cat_speed = 4

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

    # Move the cat to the right.
    cat_x += cat_speed

    # Check if the cat has completely left the window.
    if cat_x > 800:

        # The .get_width() method reveals how wide a Pygame Surface
        # is, measured in pixels.

        # -cat.get_with() will move the cat entirely to the left of
        # the left side of the window.
        cat_x = -cat.get_width()

    # Fill the background before drawing
    # the next frame.
    screen.fill(WHITE)

    # While pygame.image.load() will load an image into the
    # computer's memory, it doesn't automatically put that
    # image inside the game window.

    # blit() is an instruction that says take this image and
    # copy it onto the Surface object that 'screen' references
    # at position (cat_x, cat_y).
    screen.blit(cat, (cat_x, cat_y))

    # Update the entire display or just selected parts of the display.
    pygame.display.update()

    # Limit the game to 60 frames per second.
    clock.tick(60)