import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
SPEED = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Echoes of the Abyss")

clock = pygame.time.Clock()

# Store the player's top-left position as an (x, y) vector.
player_position = pygame.Vector2(100, 100)

running = True

while running:
    # Measure the time since the previous frame in seconds.
    # This keeps movement consistent across different frame rates.
    dt = clock.tick(60) / 1000

    # Process events such as closing the game window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of all keyboard keys.
    keys = pygame.key.get_pressed()

    # Start with zero movement in both directions.
    direction = pygame.Vector2(0, 0)

    # Decrease x to move left and increase x to move right.
    if keys[pygame.K_LEFT]:
        direction.x -= 1

    if keys[pygame.K_RIGHT]:
        direction.x += 1

    # Decrease y to move up and increase y to move down.
    if keys[pygame.K_UP]:
        direction.y -= 1

    if keys[pygame.K_DOWN]:
        direction.y += 1

    # Normalize the direction to prevent faster diagonal movement.
    # A nonzero vector is scaled to a length of exactly 1.
    if direction.length() > 0:
        direction = direction.normalize()

    # Calculate how far to move using direction, speed, and elapsed time.
    # SPEED is measured in pixels per second, and dt is measured in seconds.
    player_position += direction * SPEED * dt

    # Keep the player's left edge between 0 and the rightmost valid x-coordinate.
    # Subtract PLAYER_SIZE because the position represents the left edge,
    # and we want the entire player to remain inside the window.
    player_position.x = max(
        0, min(WIDTH - PLAYER_SIZE, player_position.x)
    )

    # Keep the player's top edge between 0 and the bottommost valid y-coordinate.
    # Subtract PLAYER_SIZE because the position represents the top edge,
    # and we want the entire player to remain inside the window.
    player_position.y = max(
        0, min(HEIGHT - PLAYER_SIZE, player_position.y)
    )

    # Clear the screen before drawing the next frame.
    screen.fill((18, 20, 32))

    # Create a rectangle using the player's current position and size.
    # Round the coordinates because pygame.Rect uses integer positions.
    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    # Draw the player as a light-blue rectangle.
    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    # Update the entire screen.
    pygame.display.flip()

pygame.quit()