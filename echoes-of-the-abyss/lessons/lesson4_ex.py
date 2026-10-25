import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
SPEED = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Echoes of the Abyss")

clock = pygame.time.Clock()

player_position = pygame.Vector2(100, 100)

# TODO 1: Define the wall's position and dimensions.
# Hint: Use pygame.Rect() to create a wall at (350, 200)
# with a width of 150 and a height of 200.


running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    direction = pygame.Vector2(0, 0)

    # Check for horizontal movement.
    if keys[pygame.K_LEFT]:
        direction.x = -1
    if keys[pygame.K_RIGHT]:
        direction.x = 1

    # Check for vertical movement.
    if keys[pygame.K_UP]:
        direction.y = -1
    if keys[pygame.K_DOWN]:
        direction.y = 1

    # Normalize the direction vector.
    if direction.length() > 0:
        direction = direction.normalize()

    # TODO 2: Save the player's previous X coordinate.
    # Then update the player's horizontal position using
    # direction.x, SPEED, and dt.


    # TODO 3: Create the player's pygame.Rect using the
    # current position and PLAYER_SIZE.
    # Check whether it overlaps the wall using colliderect().
    # If a collision occurs, restore the previous X coordinate.


    # TODO 4: Save the player's previous Y coordinate.
    # Then update the player's vertical position using
    # direction.y, SPEED, and dt.


    # TODO 5: Create the player's pygame.Rect again using
    # the updated position.
    # Check for a collision with the wall.
    # If a collision occurs, restore the previous Y coordinate.


    # Keep the player inside the horizontal boundaries.
    player_position.x = max(
        0, min(WIDTH - PLAYER_SIZE, player_position.x)
    )

    # TODO 6: Keep the player inside the vertical boundaries.
    # Use the same approach as the horizontal boundary check.


    screen.fill((18, 20, 32))

    # TODO 7: Create the player's rectangle for drawing.


    # TODO 8: Draw the wall and the player.
    # Use different colors for the wall and the player.


    pygame.display.flip()

pygame.quit()