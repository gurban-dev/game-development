# Import the pygame module.
import pygame

# Import the sys module.
import sys

# Start pygame.
pygame.init()

# Create the game window.
screen = pygame.display.set_mode((800, 600))

# Set the window title.
pygame.display.set_caption("Robot Exercise")

# Define some colours.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (170, 170, 170)
BLUE = (50, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Start the game loop.
while True:

    # Look for events.
    for event in pygame.event.get():

        # Close the window if needed.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background.
    screen.fill(BLACK)

    # Draw the robot's head.
    pygame.draw.rect(screen, GREY, (300, 100, 200, 150))

    # Draw the robot's body.
    pygame.draw.polygon(
        screen,
        BLUE,
        [
            (275, 250),
            (525, 250),
            (475, 450),
            (325, 450),
        ],
    )

    # Draw the robot's eyes.
    pygame.draw.circle(screen, RED, (350, 160), 15)
    pygame.draw.circle(screen, RED, (450, 160), 15)

    # Draw the robot's antenna.
    pygame.draw.line(screen, WHITE, (400, 100), (400, 40), 5)

    # Draw the glowing antenna tip.
    pygame.draw.circle(screen, GREEN, (400, 30), 10)

    # Draw three vertically stacked energy beams.
    pygame.draw.ellipse(screen, GREEN, (330, 455, 140, 30))
    pygame.draw.ellipse(screen, GREEN, (350, 490, 100, 22))
    pygame.draw.ellipse(screen, GREEN, (370, 518, 60, 14))

    # Show everything on the screen.
    pygame.display.update()