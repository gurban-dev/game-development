
import pygame

pygame.init()

# Set up the game window.
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Player")

# Define colors.
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 80, 80)
BLACK = (0, 0, 0)

# Set up the player.
player_position = pygame.Vector2(100, 100)
player_size = 50
player_speed = 5

# Set up the target.
target = pygame.Rect(500, 300, 50, 50)

# Set up the font.
font = pygame.font.Font(None, 48)

clock = pygame.time.Clock()
running = True
game_won = False

while running:
    # Handle events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current keyboard state.
    keys = pygame.key.get_pressed()

    # TODO 1: Detect arrow keys and move the player.
    # Move the player while an arrow key is held down.
    if not game_won:
        if keys[pygame.K_RIGHT]:
            player_position.x += player_speed

        if keys[pygame.K_LEFT]:
            player_position.x -= player_speed

        if keys[pygame.K_UP]:
            player_position.y -= player_speed

        if keys[pygame.K_DOWN]:
            player_position.y += player_speed

    # TODO 2: Keep the player inside the window.
    # Constrain the x-coordinate between 0 and WIDTH - player_size.
    player_position.x = max(
        0, min(player_position.x, WIDTH - player_size)
    )

    # Constrain the y-coordinate between 0 and HEIGHT - player_size.
    player_position.y = max(
        0, min(player_position.y, HEIGHT - player_size)
    )

    # TODO 3: Create a rectangle representing the player.
    # Method 1:
    # pygame.Rect(x_pos, y_pos, width, height)

    # Method 2:
    # pygame.Rect((x_pos, y_pos), (width, height))
    player = pygame.Rect(
        player_position.x,
        player_position.y,
        player_size,
        player_size
    )

    # TODO 4: Check whether the player touches the target.
    # colliderect() returns True when the rectangles overlap.
    if player.colliderect(target):
        game_won = True

    # Draw everything.
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, target)

    # TODO 5: Draw the player as a blue rectangle.
    pygame.draw.rect(screen, BLUE, player)

    # TODO 5: Display a winning message once game_won is True.
    if game_won:
        message = font.render("You Win!", True, BLACK)

        message_rect = message.get_rect(
            center=(WIDTH // 2, 50)
        )

        screen.blit(message, message_rect)

    # Update the display.
    pygame.display.flip()

    # Limit the game to 60 frames per second.
    clock.tick(60)

pygame.quit()