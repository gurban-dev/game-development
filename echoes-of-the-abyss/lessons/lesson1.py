import pygame

# Initializes all the import Pygame modules (sound, graphics
# and fonts).
pygame.init()

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (25, 20, 35)
RECT_COLOR = (90, 180, 230)

# Create the game window while specifying the width and height.

# If the width and height are not specified, the window will
# occupy the entire screen.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window so it doesn't just default to
# "pygame window".
pygame.display.set_caption("Echoes of the Abyss")

# Without a clock object, the game loop could run at different
# speeds on a high-end gaming PC compared to an old laptop,
# because each computer may execute the game loop at a
# different rate.

# Different computers shuld be forced to run the game loop at exactly
# the same time because the game should feel identical for everyone.

# E.g. 60 times per second.
clock = pygame.time.Clock()

rect_width = 40
rect_height = 40

rect_x = 380
rect_y = 380

running = True

# This main game loop is responsible for the program repeatedly
# updating and redrawing the game.
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Filling the game window with a background color.

    # Clear the screen before drawing the next frame so the
    # previous frame's drawings do not remain visible.
    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(
        screen,
        RECT_COLOR,
        (rect_x, rect_y, rect_width, rect_height),
    )

    # .update() can update the entire or just specific parts
    # of the screen.

    # In chess, .update() is more appropriate since the only time
    # anything moves is when you physically drag a piece from one
    # square to another. In this case, redrawing all 32 pieces would
    # be unnecessary in this case.

    # .flip() updates the entire screen.

    # In a game like Super Mario, .flip() is appropriate because
    # every pixel on the screen has to shift its position since
    # the player moves from left to right.
    pygame.display.flip()

    # Limit the game loop to 60 iterations per second.
    # This must be inside the loop so that each frame,
    # which represents one cycle of updating and drawing
    # the game, is regulated to keep the game running
    # at a consistent speed.
    clock.tick(60)

# Shut down all Pygame processes.
pygame.quit()