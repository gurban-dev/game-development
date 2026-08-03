# Import the pygame module.
import pygame

# Import the sys module.
import sys

# Start pygame.
pygame.init()

# Create the game window by invoking set_mode() which returns
# a surface object.
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

    # The tuple (300, 100, 200, 150) specifies:
    # 300 is the x-coordinate of the top-left corner (300 pixels rightwards).
    # 100 is the y-coordinate of the top-left corner (100 pixels downwards).
    # 200 is the width of the rectangle.
    # 150 is the height of the rectangle.
    pygame.draw.rect(screen, GREY, (300, 100, 200, 150))

    # Draw the robot's body.

    # The third argument is a list of (x, y) coordinate pairs representing
    # the vertices of the polygon.
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

    # (350, 160) is the centre of the circle.
    # 15 is the radius.

    # Providing an argument for the width parameter is optional.
    # If not provided, it defaults to 0 (zero).
    pygame.draw.circle(screen, RED, (350, 160), 15, 5)
    pygame.draw.circle(screen, RED, (450, 160), 15)

    # Draw the robot's antenna.

    # (400, 100) is the start_pos.
    # (400, 40) is the end_pos.
    # 5 is the argument for the width parameter which defaults to
    # 1 if an argument is not provided.
    pygame.draw.line(screen, WHITE, (400, 100), (400, 40), 5)

    # Draw the glowing antenna tip.
    pygame.draw.circle(screen, GREEN, (400, 30), 10)

    # Draw three vertically stacked energy beams.

    # ellipse() is provided a rectangle as its third argument.
    # (330, 455) is the top-left corner of the rectangle.
    # 140 is the rectangle width.
    # 30 is the rectangle height.
    pygame.draw.ellipse(screen, GREEN, (330, 455, 140, 30))
    pygame.draw.ellipse(screen, GREEN, (350, 490, 100, 22))
    pygame.draw.ellipse(screen, GREEN, (370, 518, 60, 14))

    # Update the display so the user can see what has been draw.
    pygame.display.update()