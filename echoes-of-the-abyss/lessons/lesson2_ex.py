
import pygame

pygame.init()

# Set up the game window.
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("15-Minute Challenge: Move the Player")

# Define colors.
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 80, 80)

# Set up the player.
player_position = pygame.Vector2(100, 100)
player_size = 50
player_speed = 20

# Set up the target.
target = pygame.Rect(500, 300, 50, 50)

clock = pygame.time.Clock()
running = True
game_won = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # TODO 1: Detect when the player presses an arrow key.
        # Right arrow: move right.
        # Left arrow: move left.
        # Up arrow: move up.
        # Down arrow: move down.
        # Move the player by player_speed pixels per press.

        pass

    # TODO 2: Keep the player inside the window.
    # Use max() and min() to constrain the x-coordinate
    # between 0 and WIDTH - player_size.
    # Do the same for the y-coordinate

    # TODO 3: Create a rectangle representing the player.
    # Use player_position.x, player_position.y,
    # player_size, and player_size.

    # TODO 4: Check whether the player touches the target.
    # If the player touches the target, set game_won to True.

    # Draw everything.
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, target)

    # TODO 5: Draw the player as a blue rectangle.
    # Once game_won is True, display a winning message.

    pygame.display.flip()
    clock.tick(60)

pygame.quit()