# Import the pygame library so we can use its
# game development tools.
import pygame

# Initialize all pygame systems such as:
# - Graphics
# - Keyboard input
# - Timing systems
pygame.init()

# Store the width of the game window in pixels.
WINDOW_WIDTH = 800

# Store the height of the game window in pixels.
WINDOW_HEIGHT = 600

# Create the main game window using the width
# and height values defined above.
screen = pygame.display.set_mode(
    (
        WINDOW_WIDTH,
        WINDOW_HEIGHT
    )
)

# Set the title shown at the top of the window.
pygame.display.set_caption("Moving Player Box")

# Create a clock object used to control FPS.
clock = pygame.time.Clock()

# Store the player's width in pixels.
player_width = 50

# Store the player's height in pixels.
player_height = 50

# Store the player's starting horizontal position.
x = 375

# Store the player's starting vertical position.
y = 275

# Store how many pixels the player moves
# every frame while a key is held down.
speed = 5

# Store the player's default color using RGB.
player_color = (0, 150, 255)

# Control whether the main game loop continues running.
running = True

# Start the main game loop.
#
# This loop continuously:
# - Handles events
# - Reads keyboard input
# - Updates game state
# - Draws graphics
while running:

    # Process every event currently waiting
    # in pygame's event queue.
    for event in pygame.event.get():

        # Detect whether the player clicked
        # the window close button.
        if event.type == pygame.QUIT:

            # Stop the game loop.
            running = False

    # Read the current keyboard state.
    #
    # This allows us to check whether keys
    # are actively being held down.
    keys = pygame.key.get_pressed()

    # Reset the player color back to blue
    # at the beginning of every frame.
    player_color = (0, 150, 255)

    # Check whether the left arrow key is held.
    if keys[pygame.K_LEFT]:

        # Move the player left by decreasing x.
        x -= speed

        # Change player color while moving.
        player_color = (255, 100, 100)

    # Check whether the right arrow key is held.
    if keys[pygame.K_RIGHT]:

        # Move the player right by increasing x.
        x += speed

        # Change player color while moving.
        player_color = (255, 100, 100)

    # Check whether the up arrow key is held.
    if keys[pygame.K_UP]:

        # Move the player upward by decreasing y.
        y -= speed

        # Change player color while moving.
        player_color = (255, 100, 100)

    # Check whether the down arrow key is held.
    if keys[pygame.K_DOWN]:

        # Move the player downward by increasing y.
        y += speed

        # Change player color while moving.
        player_color = (255, 100, 100)

    # Prevent the player from moving past
    # the left edge of the screen.
    if x < 0:
        x = 0

    # Prevent the player from moving past
    # the right edge of the screen.
    if x > WINDOW_WIDTH - player_width:
        x = WINDOW_WIDTH - player_width

    # Prevent the player from moving above
    # the top edge of the screen.
    if y < 0:
        y = 0

    # Prevent the player from moving below
    # the bottom edge of the screen.
    if y > WINDOW_HEIGHT - player_height:
        y = WINDOW_HEIGHT - player_height

    # Fill the entire screen with a dark color.
    #
    # This clears the previous frame so old
    # drawings do not remain visible.
    screen.fill((30, 30, 30))

    # Draw the player rectangle using:
    # - The screen surface
    # - The player's color
    # - The player's position and size
    pygame.draw.rect(
        screen,
        player_color,
        (
            x,
            y,
            player_width,
            player_height
        )
    )

    # Update the display so all newly drawn
    # graphics become visible on the screen.
    pygame.display.update()

    # Limit the game to 60 frames per second.
    #
    # This keeps gameplay smooth and prevents
    # the program from running too fast.
    clock.tick(60)

# Shut down pygame systems cleanly.
pygame.quit()