import pygame


class Player:
    def __init__(self, x, y, size, color, speed):
        # Each object maintains its own position and properties.
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.color = color
        self.speed = speed

        # The Rect provides a representation for drawing and collision.
        self.rect = pygame.Rect(x, y, size, size)

    def update(self, keys, dt, screen_width, screen_height):
        # Build a movement vector from the currently pressed keys.
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_RIGHT]:
            direction.x += 1

        if keys[pygame.K_LEFT]:
            direction.x -= 1

        if keys[pygame.K_DOWN]:
            direction.y += 1

        if keys[pygame.K_UP]:
            direction.y -= 1

        # Normalization prevents diagonal movement from being faster.
        if direction.length() > 0:
            direction = direction.normalize()

        # Delta time keeps movement consistent across frame rates.
        self.position += direction * self.speed * dt

        # The top-left coordinate must leave room for the full rectangle.
        self.position.x = max(
            0,
            min(screen_width - self.size, self.position.x)
        )

        self.position.y = max(
            0,
            min(screen_height - self.size, self.position.y)
        )

        # Keep the Rect synchronized with the floating-point position.
        self.rect.topleft = (
            round(self.position.x),
            round(self.position.y),
        )

    def draw(self, surface):
        # The object handles rendering without exposing it to main().
        pygame.draw.rect(
            surface,
            self.color,
            self.rect
        )


def main():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600

    BACKGROUND_COLOR = (18, 20, 32)
    PLAYER_COLOR = (100, 180, 255)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("The Adventurer Exercise")

    clock = pygame.time.Clock()

    # Create an independent Player object.
    player = Player(
        x=100,
        y=100,
        size=50,
        color=PLAYER_COLOR,
        speed=200
    )

    running = True

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Update the player's position based on keyboard input,
        # elapsed time and the screen boundaries.
        player.update(keys, dt, WIDTH, HEIGHT)

        screen.fill(BACKGROUND_COLOR)

        # Delegate rendering to the Player.
        player.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()