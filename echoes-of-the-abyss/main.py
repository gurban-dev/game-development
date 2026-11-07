import pygame

from world import World

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
SPEED = 200

BACKGROUND_COLOR = (18, 20, 32)
PLAYER_COLOR = (100, 180, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Echoes of the Abyss")

# Create a clock to control the game's frame rate.
clock = pygame.time.Clock()

# Store the player's position as a vector.
player_position = pygame.Vector2(100, 100)

player_rect = pygame.Rect(
    round(player_position.x),
    round(player_position.y),
    PLAYER_SIZE,
    PLAYER_SIZE,
)

world = World()

running = True

while running:
    # Calculate the time elapsed since the previous frame
    # and convert it from milliseconds to second.
    dt = clock.tick(60) / 1000

    # Handle events such as closing the game window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read the current keyboard state to determine which arrow
    # keys are being pressed.
    keys = pygame.key.get_pressed()

    # Build the movement direction from keyboard input.
    direction = pygame.Vector2(0, 0)

    if keys[pygame.K_RIGHT]:
        direction.x += 1

    if keys[pygame.K_LEFT]:
        direction.x -= 1

    if keys[pygame.K_DOWN]:
        direction.y += 1

    if keys[pygame.K_UP]:
        direction.y -= 1

    # Normalize the direction to prevent faster diagonal movement.
    if direction.length() > 0:
        direction = direction.normalize()

    # Attempt horizontal movement.

    # If the player collides with a wall, the program should
    # restore their previous X-coordinate.
    previous_x = player_position.x

    # Update the player's position.
    player_position.x += direction.x * SPEED * dt

    # Update the position of the player's rectangle so that it
    # matches the player's current position.
    player_rect.topleft = (

        # player_rect is an instance of the pygame.Rect class.
        # pygame.Rect expects integers which is why the x and y
        # coordinates must be rounded.
        round(player_position.x),
        round(player_position.y),
    )

    # Check whether the player has collided with any walls.
    for wall in world.walls:
        if player_rect.colliderect(wall):
            # Restore the player's previous X-coordinate.
            player_position.x = previous_x

            player_rect.topleft = (
                round(player_position.x),
                round(player_position.y),
            )

            break

    # Attempt vertical movement.
    previous_y = player_position.y

    player_position.y += direction.y * SPEED * dt

    player_rect.topleft = (
        round(player_position.x),
        round(player_position.y),
    )

    # Resolve vertical collisions.
    for wall in world.walls:
        if player_rect.colliderect(wall):
            player_position.y = previous_y

            player_rect.topleft = (
                round(player_position.x),
                round(player_position.y),
            )

            break

    # Keep the player inside the game window.
    player_position.x = max(
        0, min(WIDTH - PLAYER_SIZE, player_position.x)
    )

    player_position.y = max(
        0, min(HEIGHT - PLAYER_SIZE, player_position.y)
    )

    # Synchronize the player's rectangle.
    player_rect.topleft = (
        round(player_position.x),
        round(player_position.y),
    )

    # Draw the game.
    screen.fill(BACKGROUND_COLOR)

    # Draw all the walls belonging to the game world onto the
    # game screen.
    world.draw(screen)

    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        player_rect
    )

    # Update the entire screen.
    pygame.display.flip()

pygame.quit()