import pygame

# Starts all of the pygame modules.
pygame.init()

# Surface object where the lines will be drawn.
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Drawing Lines")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (170, 170, 170)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Image you have a pencil and a ruler. You place the pencil on
# one point of the paper, then draw a straight line until you
# reach another point.

# pygame.draw.line() works exactly the same way.

# This function needs to know:
# 1. Which surface to draw on.
# 2. Which color the line should be.
# 3. Where the line starts.
# 4. Where the line ends.
# 5. How thick the line should be.

# Syntax:
# pygame.draw.line(surface, color, start_point, end_point, width)

# surface is the screen where Pygame will draw the line.

# color determines the color of the line.

# start_point is a tuple of x, y coordinates indicating where the
# line begins.

# end_point is a tuple of x, y coordinates indicating where the
# line ends.

# width controls how thick the line is.

running = True

while running:

    screen.fill(WHITE)

    # start_point = (x, y)
    start_point = (100, 100)

    end_point = (300, 100)

    width = 5

    # Draw a horizontal line.
    pygame.draw.line(screen, BLACK, start_point, end_point, width)

    # Why doesn't this line have a slope?

    # Both points have the same y-coordinate.

    # 400 pixels to the right.
    # 100 pixels down.
    start_point = (400, 100)

    end_point = (400, 300)

    # Draw a vertical line.
    pygame.draw.line(screen, BLUE, start_point, end_point, width)

    start_point = (100, 200)

    end_point = (300, 350)

    # Diagonal line.

    # When a line moves both horizontally and vertically at the same
    # time, it is diagonal.

    # A simple rule to remember is:

    # Only X changes -> Horizontal line
    # Only Y changes -> Vertical line
    # Both X and Y change -> Diagonal line
    pygame.draw.line(screen, RED, start_point, end_point, width)

    for event in pygame.event.get():

        # Check if the user closes the window.
        if event.type == pygame.QUIT:

            running = False
    
    # Update the display.

    # pygame.display.update() updates the entire game window
    # just as pygame.display.flip() does.

    # The difference is that pygame.display.update() contains
    # an extra feature that makes it possible to have it update
    # only a certain part of the game window.
    pygame.display.update()