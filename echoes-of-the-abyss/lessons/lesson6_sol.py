import pygame
from pathlib import Path


class Player:
    def __init__(self, x, y, size, color, speed):
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x, y, size, size)

        # The path starts at this file, not at the folder the
        # program was launched from. Launching from the project
        # root and launching from lessons/ then find the same PNG.
        # convert_alpha() keeps the transparent pixels and matches
        # the display format chosen by set_mode(). The display
        # already exists because main() constructs the player
        # after set_mode(). scale() returns a new Surface, so the
        # 16 x 16 file can be drawn at the body's size. 64 is an
        # even multiple of 16, so each source pixel stays square.
        image_path = Path(__file__).parent / "assets" / "adventurer.png"
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

        # blit has no position of its own. It copies the sprite
        # at whatever top-left the rectangle currently holds, so
        # the rectangle has to follow the floating-point position
        # or the picture will lag behind the movement.
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
    PLAYER_COLOR = (100, 180, 255)
    HIGHLIGHT_COLOR = (176, 132, 64)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pixel Art Solution")

    clock = pygame.time.Clock()

    player = Player(
        x=80,
        y=80,
        size=PLAYER_SIZE,
        color=PLAYER_COLOR,
        speed=240,
    )

    highlight = pygame.Rect(300, 250, 96, 96)

    # The crystal is prepared once. Its pixels do not change
    # between frames, so the loop only needs to copy them.
    # Partial transparency in the center is what lets the gold
    # rectangle show through after the crystal is drawn on top.
    crystal_path = Path(__file__).parent / "assets" / "crystal.png"
    crystal = pygame.image.load(crystal_path).convert_alpha()
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
