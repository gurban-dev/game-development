import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
SPEED = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Diagonal Movement Demonstration")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

# A 2D vector bundles an (X, Y) coordinate into a single object.
# Think of it as a container for tracking where things are on
# the screen.

# 1. Position Vector (Where you are):
#    Points to a specific coordinate on the screen relative to (0,0).
#    Above, 'position' tells us exactly where the player is located.

# 2. Direction Vector (Where you are going):
#    Represents a movement intent or offset, not a fixed place.
#    It answers "which way and how much?" (e.g., [1, -1] means moving
#    right and up). Its length represents the magnitude of intent.

# In Pygame, the screen origin (0, 0) is the top-left corner.
# X increases to the right. Y increases downward.

# The object's X position is 375.
# The object's Y position is 275.
position = pygame.Vector2(375, 275)

running = True

while running:
    # Each repetition of this loop is called a frame.

    # During each frame, the program:
    # 1. Measures the time that has passed.
    # 2. Checks for events, such as closing the window.
    # 3. Checks which keys are being pressed.
    # 4. Calculates the player's movement.
    # 5. Draws the updated scene.

    # clock.tick(60) limits the game to about 60 frames per second.
    # It returns the number of milliseconds that have passed since
    # the previous call to clock.tick().

    # Dividing by 1000 converts the value from milliseconds to seconds.

    # dt is short for delta time. This stores the elapsed time in
    # seconds between frames.
    dt = clock.tick(60) / 1000

    # Check for events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keys are being pressed.
    keys = pygame.key.get_pressed()

    # At the beginning of every frame, the program resets the
    # direction vector to (0, 0).
    direction = pygame.Vector2(0, 0)

    if keys[pygame.K_RIGHT]:
        direction.x += 1

    if keys[pygame.K_LEFT]:
        direction.x -= 1

    if keys[pygame.K_DOWN]:
        direction.y += 1

    if keys[pygame.K_UP]:
        direction.y -= 1

    # Normalize the direction vector to a length of 1 so that
    # diagonal movement is not faster than horizontal or vertical
    # movement while preserving the direction in which the player
    # is moving.
    if direction.length() > 0:
        # .normalize() creates a new vector with a length of 1
        # and assign it to direction.
        direction.normalize()

    # Update the player's position.
    position += direction * SPEED * dt

    # Create the player at the position specified in the position
    # vector.
    player_rect = pygame.Rect(
        # round() will return an integer if the number of digits
        # to round to is not specified.
        round(position.x),
        round(position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    screen.fill((18, 20, 32))

    # Draw the player on the screen.
    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    # Compute the length of the direction vector.

    # This is included to demonstrate that diagonal movement
    # is faster.

    # Diagonal movement causes the player to move along both
    # the X-axis and the Y-axis at the same time, each at
    # 200 pixels per second.

    # Moving only vertically or only horizontally means that
    # either the X component or the Y component is 1 in the
    # vector, but not both.

    # square_root(1**2 + 0**2) -> 1

    # square_root(0**2 + 1**2) -> 1

    # Moving diagonally:
    # square_root(1**2 + 1**2) -> square_root(2) -> 1.41

    # E.g. The user presses the up and right arrows simultaneously.
    vector_length = direction.length()

    message = f"Direction length: {vector_length:.2f}"

    text_surface = font.render(message, True, (240, 240, 240))

    # 'screen' is the game window.
    # 'text_surface' is the rendered text.
    # (20, 20) is the location where the text should be drawn.
    screen.blit(text_surface, (20, 20))

    screen.blit(
        font.render("Use the arrow keys.", True, (240, 240, 240)),
        (20, 55),
    )

    # Update the entire screen.
    pygame.display.flip()

pygame.quit()