
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

running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Existing Lesson 2 movement.
    direction = pygame.Vector2(0, 0)

    if keys[pygame.K_RIGHT]:
        direction.x = 1

    player_position += direction * SPEED * dt

    # Keep the player inside the horizontal boundaries.
    player_position.x = max(
        0, min(WIDTH - PLAYER_SIZE, player_position.x)
    )

    screen.fill((18, 20, 32))

    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    pygame.display.flip()

pygame.quit()