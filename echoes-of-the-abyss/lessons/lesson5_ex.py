import pygame


class Player:
    def __init__(self, x, y, size, color, speed):
        # TODO 1:
        # Store the player's position using pygame.Vector2.

        # TODO 2:
        # Store the player's size, color, and speed.

        # TODO 3:
        # Create a pygame.Rect representing the player.

        pass


    def update(self, keys, dt, screen_width, screen_height):
        # TODO 4:
        # Create a direction vector initialized to (0, 0).

        # TODO 5:
        # Check whether the arrow keys are pressed.
        # Update the direction vector accordingly.

        # TODO 6:
        # Normalize the direction vector if its length
        # is greater than zero.

        # TODO 7:
        # Update the player's position using:
        # direction * speed * dt

        # TODO 8:
        # Keep the player inside the screen boundaries.
        # Remember that position represents the top-left corner.

        # TODO 9:
        # Synchronize the player's Rect with its position.

        pass

    def draw(self, surface):
        # TODO 10:
        # Draw the player's rectangle onto the supplied Surface.

        pass


def main():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600

    BACKGROUND_COLOR = (18, 20, 32)
    PLAYER_COLOR = (100, 180, 255)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The Adventurer Exercise")

    clock = pygame.time.Clock()

    # TODO 11:
    # Create a Player object with these properties:
    # Position: (100, 100)
    # Size: 50
    # Color: PLAYER_COLOR
    # Speed: 200


    running = True

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # TODO 12:
        # Call the player's update method.
        # Pass keys, dt, WIDTH, and HEIGHT.

        screen.fill(BACKGROUND_COLOR)

        # TODO 13:
        # Call the player's draw method.
        # Pass screen as the argument.

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()