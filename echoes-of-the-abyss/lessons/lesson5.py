import pygame


class Player:
    # __init__() is a dunder method because it has two leading
    # and two trailing underscores.
    def __init__(self, x, y, size, color, speed):
        # Store the player's attributes inside the object.

        # pygame.Vector2 creates a 2D vector that stores two numerical
        # values: an X-coordinate and a Y-coordinate.
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.color = color
        self.speed = speed

        # The rectangle represents the player's position and size.
        self.rect = pygame.Rect(x, y, size, size)

    def update(self, keys, dt, screen_width, screen_height):
        # Calculate the movement direction from keyboard input.
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_RIGHT]:
            direction.x += 1

        if keys[pygame.K_LEFT]:
            direction.x -= 1

        if keys[pygame.K_DOWN]:
            direction.y += 1

        if keys[pygame.K_UP]:
            direction.y -= 1

        # Normalize diagonal movement to maintain consistent speed.
        if direction.length() > 0:
            direction = direction.normalize()

        # Update the player's position using elapsed time.
        self.position += direction * self.speed * dt

        # Keep the player inside the screen boundaries.
        self.position.x = max(
            0,
            min(screen_width - self.size, self.position.x)
        )

        self.position.y = max(
            0,
            min(screen_height - self.size, self.position.y)
        )

        # Synchronize the rectangle with the player's position.

        # Update the position of the player's rectangle so that it
        # matches the player's current position.
        self.rect.topleft = (
            # self.rect is an instance of the pygame.Rect class.
            # pygame.Rect expects integers which is why the x and y
            # coordinates must be rounded.
            round(self.position.x),
            round(self.position.y),
        )

    def draw(self, surface):
        # Draw the player onto the supplied Pygame Surface.
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

    pygame.display.set_caption("The Adventurer")

    clock = pygame.time.Clock()

    # Create a Player object using the Player class.
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

        # Handle events such as closing the game window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Read the current keyboard state.
        keys = pygame.key.get_pressed()

        # Update the player's position based on keyboard input,
        # elapsed time and the screen boundaries.
        player.update(keys, dt, WIDTH, HEIGHT)

        # Draw the game.
        screen.fill(BACKGROUND_COLOR)

        # Let the Player object handle its own rendering.
        player.draw(screen)

        # Update the entire screen.
        pygame.display.flip()

    pygame.quit()

# __name__ is a built-in Python dunder variable that reveals how
# a Python program is being executed.

# It has two possible values:
# • "__main__": If you run the file directly (with python lesson5.py).
# • "lesson5" (the filename): If the file is being imported as a module
#                             into another script.
print("__name__:", __name__)

if __name__ == "__main__":
    main()