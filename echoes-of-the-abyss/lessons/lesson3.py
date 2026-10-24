
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
position = pygame.Vector2(375, 275)

running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    direction = pygame.Vector2(0, 0)

    if keys[pygame.K_RIGHT]:
        direction.x += 1

    if keys[pygame.K_LEFT]:
        direction.x -= 1

    if keys[pygame.K_DOWN]:
        direction.y += 1

    if keys[pygame.K_UP]:
        direction.y -= 1

    # Deliberately skip normalization to show the problem.
    position += direction * SPEED * dt

    player_rect = pygame.Rect(
        round(position.x),
        round(position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    screen.fill((18, 20, 32))

    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    # Display the direction vector's length.
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