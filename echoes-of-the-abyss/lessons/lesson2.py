import pygame

pygame.init()

"""
Learning objective:
Detect keyboard input and use it to move a player.

Game loop sequence:
1. Process events, such as closing the window.
2. Read keyboard input.
3. Update the player's position.
4. Draw the updated frame.
5. Repeat while the game is running.

Coordinate system:
- The top-left corner of the window is (0, 0).
- Increasing X moves an object right.
- Decreasing X moves an object left.
- Increasing Y moves an object down.
- Decreasing Y moves an object up.
"""

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLUE = (50, 100, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Echoes of the Abyss")

# Define the player's position, size, and movement speed.
player_size = 50

# Movement speed in pixels per second.
player_speed = 200

player_position = pygame.Vector2(100, 100)

# A clock controls the frame rate and measures elapsed time.
clock = pygame.time.Clock()

running = True

while running:
    # Process events, including requests to close the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read the current state of the keyboard.
    # A key remains active while it is being held down.
    keys = pygame.key.get_pressed()

    # Calculate the elapsed time since the previous frame.
    elapsed_time = clock.tick(60) / 1000

    # Update the player's position based on keyboard input.

    # Multiplying speed by elapsed time makes movement
    # frame-rate independent.
    if keys[pygame.K_RIGHT]:
        print("Right key is being held.")

        player_position.x += player_speed * elapsed_time

    if keys[pygame.K_LEFT]:
        print("Left key is being held.")

        player_position.x -= player_speed * elapsed_time

    # Keep the player inside the window.
    # The maximum X coordinate is the window width minus the
    # player width.
    player_position.x = max(
        0,
        min(player_position.x, WIDTH - player_size)
    )

    player_position.y = max(
        0,
        min(player_position.y, WIDTH - player_size)
    )

    # Create a rectangle from the player's current position.
    player = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        player_size,
        player_size
    )

    # Draw the frame.
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player)

    # Update the entie screen.
    pygame.display.flip()

pygame.quit()