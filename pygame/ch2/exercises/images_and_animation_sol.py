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

ANIMAL_WIDTH = 150
ANIMAL_HEIGHT = 100

# pygame.image.load() returns a Surface object.

# A Surface object is like a blank digital sheet of paper.

# Load the cheetah image.
cheetah = pygame.image.load("cheetah.webp")

# Load the caucasian shepherd image.
caucasian_shepherd = pygame.image.load("caucasian-shepherd.jpeg")

# Load the bald eagle image.
bald_eagle = pygame.image.load("bald-eagle.jpeg")

# pygame.transform.scale() takes a Surface object and
# returns a new Surface object with a different size.

# Resize the images so they are all the same size.
cheetah = pygame.transform.scale(
    cheetah,
    (ANIMAL_WIDTH, ANIMAL_HEIGHT)
)

caucasian_shepherd = pygame.transform.scale(
    caucasian_shepherd,
    (ANIMAL_WIDTH, ANIMAL_HEIGHT)
)

bald_eagle = pygame.transform.scale(
    bald_eagle,
    (ANIMAL_WIDTH, ANIMAL_HEIGHT)
)

# Store the animal's position.

# x controls the horizontal position.
# y controls the vertical position.

# Store the first cheetah's position.
cheetah_x = 0
cheetah_y = 100
cheetah_speed = 3

# Store the second animal's position.
caucasian_shepherd_x = -200
caucasian_shepherd_y = 250
caucasian_shepherd_speed = 5

# Store the third animal's position.
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

    # Move the first animal.
    cheetah_x += cheetah_speed

    # Move the second animal.
    caucasian_shepherd_x += caucasian_shepherd_speed

    # Move the third animal.
    bald_eagle_x += bald_eagle_speed

    # Check if the first animal has completely left
    # the window.

    if cheetah_x >= screen.get_width():

        # Move the animal just outside the left side.
        cheetah_x = -cheetah.get_width()

    # Check if the second animal has completely left
    # the window.
    if caucasian_shepherd_x >= screen.get_width():

        # Move the animal just outside the left side.
        caucasian_shepherd_x = -caucasian_shepherd.get_width()

    # Check if the third animal has completely left
    # the window.

    if bald_eagle_x >= screen.get_width():

        # Move the animal just outside the left side.
        bald_eagle_x = -bald_eagle.get_width()

    # Fill the background before drawing the next frame.
    screen.fill(WHITE)

    # .blit() pastes your image onto the screen.

    # Draw the first animal.
    screen.blit(cheetah, (cheetah_x, cheetah_y))

    # Draw the second animal.
    screen.blit(caucasian_shepherd, (caucasian_shepherd_x, caucasian_shepherd_y))

    # Draw the third animal.
    screen.blit(bald_eagle, (bald_eagle_x, bald_eagle_y))

    # Update the entire display or just selected parts of the display.
    pygame.display.update()

    # Limit the game to 60 frames per second.
    clock.tick(60)