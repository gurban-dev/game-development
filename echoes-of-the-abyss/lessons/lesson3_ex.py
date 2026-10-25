
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
SPEED = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Echoes of the Abyss")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 28)

player_position = pygame.Vector2(100, 100)

running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    direction = pygame.Vector2(0, 0)

    # TODO: Add input checks for the left, up, and down arrow keys.
    # Update direction.x for left movement and direction.y for
    # vertical movement.
    if keys[pygame.K_RIGHT]:
        direction.x = 1

    # TODO: Normalize the direction vector when its length is greater
    # than zero.
    # This prevents the player from moving faster when moving diagonally.

    # TODO: Update the player's position using direction, SPEED, and dt.
    # Keep the movement frame-rate independent.

    # Keep the player inside the horizontal boundaries.
    player_position.x = max(
        0, min(WIDTH - PLAYER_SIZE, player_position.x)
    )

    # TODO: Keep the player inside the vertical boundaries.
    # Use HEIGHT and PLAYER_SIZE to calculate the valid Y-coordinate
    # range.

    screen.fill((18, 20, 32))

    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    vector_length = direction.length()

    message = f"Direction length: {vector_length:.2f}"

    text_surface = font.render(message, True, (240, 240, 240))

    screen.blit(text_surface, (20, 20))

    screen.blit(
        font.render("Use the arrow keys.", True, (240, 240, 240)),
        (20, 55),
    )

    pygame.display.flip()

pygame.quit()