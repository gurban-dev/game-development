import pygame
from pathlib import Path


class Player:
    def __init__(self, x, y, size, speed, image_path):
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.speed = speed
        self.rect = pygame.Rect(x, y, size, size)

        # The path is built from this file so the PNG is found
        # whichever folder the program was launched from.
        # convert_alpha() keeps the PNG transparency and matches
        # the display format. scale() returns a new Surface, so
        # the 16 x 16 file can be drawn at the body's size
        # without changing the file. An even multiple, such as
        # 64 for a 16-pixel source, keeps each pixel the same size.
        loaded = pygame.image.load(image_path).convert_alpha()
        self.sprite = pygame.transform.scale(loaded, (size, size))

    def update(self, keys, dt, screen_width, screen_height):
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_RIGHT]:
            direction.x += 1

        if keys[pygame.K_LEFT]:
            direction.x -= 1

        if keys[pygame.K_DOWN]:
            direction.y += 1

        if keys[pygame.K_UP]:
            direction.y -= 1

        if direction.length() > 0:
            direction = direction.normalize()

        self.position += direction * self.speed * dt

        self.position.x = max(
            0,
            min(screen_width - self.size, self.position.x)
        )

        self.position.y = max(
            0,
            min(screen_height - self.size, self.position.y)
        )

        # The sprite has no position of its own. blit reads the
        # rectangle, so the rectangle has to follow the float
        # position or the picture will lag behind the movement.
        self.rect.topleft = (
            round(self.position.x),
            round(self.position.y),
        )

    def draw(self, surface):
        # Transparent sprite pixels leave the background in place.
        # A filled rectangle would hide whatever is behind the
        # character's corners.
        surface.blit(self.sprite, self.rect.topleft)


def main():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    PLAYER_SIZE = 64

    BACKGROUND_COLOR = (18, 20, 32)
    HIGHLIGHT_COLOR = (176, 132, 64)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pixel Art Solution")

    clock = pygame.time.Clock()

    assets = Path(__file__).parent / "assets"

    player = Player(
        x=80,
        y=80,
        size=PLAYER_SIZE,
        speed=240,
        image_path=assets / "adventurer.png",
    )

    highlight = pygame.Rect(300, 250, 96, 96)

    # The crystal is prepared once. Its pixels do not change
    # between frames, so the loop only needs to copy them.
    crystal = pygame.image.load(
        assets / "crystal.png"
    ).convert_alpha()
    crystal = pygame.transform.scale(crystal, (64, 64))

    running = True

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys, dt, WIDTH, HEIGHT)

        screen.fill(BACKGROUND_COLOR)

        # The gold rectangle is underneath the crystal, so the
        # crystal's partial transparency has something to reveal.
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, highlight)
        screen.blit(crystal, highlight.topleft)

        player.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
