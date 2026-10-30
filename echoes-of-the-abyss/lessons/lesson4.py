import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
SPEED = 200

BACKGROUND_COLOR = (18, 20, 32)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Collision Laboratory")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

# --------------------------------------------------
# 1. Understanding rectangles and collision detection
# --------------------------------------------------

# pygame.Rect() stores an object's position and dimensions.

# Four positional arguments:
# pygame.Rect(x, y, width, height)

player_rect = pygame.Rect(100, 100, PLAYER_SIZE, PLAYER_SIZE)

# A wall is another rectangle.
wall_rect = pygame.Rect(350, 200, 150, 200)

# A Rect also supports several useful position attributes:
# player_rect.x       -> Horizontal position.
# player_rect.y       -> Vertical position.
# player_rect.left    -> Left boundary.
# player_rect.right   -> Right boundary.
# player_rect.top     -> Top boundary.
# player_rect.bottom  -> Bottom boundary.
# player_rect.topleft -> Top-left corner as a tuple.

# Example:
# player_rect.x = 200
# player_rect.y = 150

# --------------------------------------------------
# 2. Understanding Vector2 and player movement
# --------------------------------------------------

# Vector2 stores two numerical values: X and Y.

# X represents horizontal position.
# Y represents vertical position.

# The player's position can be represented as:
player_position = pygame.Vector2(100, 100)

# Movement speed is measured in pixels per second.
SPEED = 200

# A direction vector describes the direction of movement.

# Vector2(1, 0)  -> Right.
# Vector2(-1, 0) -> Left.
# Vector2(0, -1) -> Up.
# Vector2(0, 1)  -> Down.

# Vector2(0, 0)  -> No movement.

# --------------------------------------------------
# 3. Understanding delta time (dt)
# --------------------------------------------------

# clock.tick(60) returns the elapsed time in milliseconds.

# Dividing by 1000 converts milliseconds into seconds.

# For example:
# 16 milliseconds / 1000 = 0.016 seconds.

# Multiplying SPEED by dt makes movement independent
# of the computer's frame rate.

# Distance traveled = SPEED * dt

# At 200 pixels per second:
# 0.5 seconds * 200 = 100 pixels.

# --------------------------------------------------
# 4. Understanding collision resolution
# --------------------------------------------------

# Before moving an object, save its previous position.

# If a collision occurs, restore the previous position.

# This allows the player to stop at the wall instead
# of passing through it.

# Example:
# previous_x = player_position.x
# player_position.x += SPEED * dt

# if collision:
#     player_position.x = previous_x

# Horizontal and vertical movement can be checked
# separately to allow the player to slide along walls.

# --------------------------------------------------
# 5. Understanding rectangle collision detection
# --------------------------------------------------

# colliderect() checks whether two rectangles overlap.

# Example:
# colliding = player_rect.colliderect(wall_rect)

# Returns:
# True  -> The rectangles overlap.
# False -> The rectangles do not overlap.

# Important:
# colliderect() does not move objects or prevent collisions.
# It only tells us whether an overlap exists.

# --------------------------------------------------
# 6. Understanding screen boundaries
# --------------------------------------------------

# The screen starts at coordinate (0, 0).

# Its horizontal coordinates range from 0 to WIDTH.
# Its vertical coordinates range from 0 to HEIGHT.

# To keep the player inside the screen, we must consider
# the player's dimensions, not just its position.

# Horizontal boundary example:
# player_position.x = max(
#     0, min(WIDTH - PLAYER_SIZE, player_position.x)
# )

# This ensures the player's left edge never goes below 0
# and its right edge never exceeds WIDTH.

# The same principle applies vertically.

# --------------------------------------------------
# 7. Main game loop
# --------------------------------------------------

running = True

while running:
    # Calculate the elapsed time.
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position.
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Position the player at the mouse coordinates.
    player_rect.topleft = (mouse_x, mouse_y)

    # Check whether the player overlaps the wall.
    colliding = player_rect.colliderect(wall_rect)

    # Change the wall's color when a collision occurs.
    if colliding:
        wall_color = (220, 70, 70)
    else:
        wall_color = (110, 110, 130)

    # Clear the screen.
    screen.fill(BACKGROUND_COLOR)

    # Draw the wall.
    pygame.draw.rect(screen, wall_color, wall_rect)

    # Draw the player.
    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    # Display collision status.
    status = "Collision detected!" if colliding else "No collision"

    # The .render() method creates a new Surface containing the
    # specified text.
    text_surface = font.render(status, True, (240, 240, 240))

    # The blit() method copies the contents of one Surface onto
    # another Surface.
    screen.blit(text_surface, (20, 20))

    # Update the entire screen.
    pygame.display.flip()

pygame.quit()