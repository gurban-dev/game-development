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

# Define the wall's position and dimensions.
wall_rect = pygame.Rect(350, 200, 150, 200)

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

    # Move horizontally and check for a collision.
    previous_x = player_position.x
    player_position.x += direction.x * SPEED * dt

    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    if player_rect.colliderect(wall_rect):
        player_position.x = previous_x

    # Move vertically and check for a collision.
    previous_y = player_position.y
    player_position.y += direction.y * SPEED * dt

    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    if player_rect.colliderect(wall_rect):
        player_position.y = previous_y

    # Keep the player inside the horizontal boundaries.
    player_position.x = max(
        0, min(WIDTH - PLAYER_SIZE, player_position.x)
    )

    # Keep the player inside the vertical boundaries.
    player_position.y = max(
        0, min(HEIGHT - PLAYER_SIZE, player_position.y)
    )

    screen.fill((18, 20, 32))

    # Create the player's rectangle for drawing.
    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    pygame.draw.rect(screen, (110, 110, 130), wall_rect)
    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    pygame.display.flip()

pygame.quit()