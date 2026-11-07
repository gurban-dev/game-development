import pygame
# TODO 1:
# Import Path from pathlib.

# Pixel Art Awakens — 15-minute exercise
#
# The arrow keys already move a square, and the square already
# stays inside the window. That square is a placeholder. Replace
# it with a sprite, and draw the crystal sprite on top of the
# gold rectangle.
#
# Two images are already on disk, beside this file:
#   assets/adventurer.png   16 x 16, with fully transparent pixels
#   assets/crystal.png      16 x 16, with partly transparent pixels
#
# Implement all of the following:
#
# 1. Import Path from pathlib.
#
# 2. Inside Player.__init__, after the Rect is created, build a
#    path to adventurer.png from this file's own location:
#        Path(__file__).parent / "assets" / "adventurer.png"
#    Load it with pygame.image.load.
#    Call convert_alpha() on the loaded Surface.
#    Scale the result with pygame.transform.scale to (size, size).
#    Store that scaled Surface as self.sprite.
#    Leave the load after set_mode(). This file already creates
#    the player after the display exists. convert_alpha() needs
#    that display so it can match the screen's pixel format.
#    Use scale, which keeps hard pixel edges. smoothscale blends
#    pixels and will make this art look blurred.
#
# 3. In Player.draw, remove the pygame.draw.rect placeholder.
#    Copy the sprite onto the supplied Surface with blit.
#    The destination is self.rect.topleft, so the picture stays
#    aligned with the rectangle that movement already updates.
#
# 4. Before the game loop, build the same kind of path for
#    assets/crystal.png. Load it, call convert_alpha(), and scale
#    it to (64, 64). Store the result in a variable named crystal.
#    Load once, before the loop. Loading and scaling every frame
#    would repeat work that does not change.
#
# 5. In the game loop, after the gold highlight rectangle is
#    drawn, blit crystal at highlight.topleft. The crystal's
#    faint center should show the gold through it. Drawing the
#    crystal before the gold rectangle would hide that effect,
#    because the rectangle would be painted over the sprite.


class Player:
    def __init__(self, x, y, size, color, speed):
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x, y, size, size)

        # TODO 2:
        # Build the path to assets/adventurer.png with Path(__file__).
        # Load the image, call convert_alpha(), scale it to
        # (size, size) with pygame.transform.scale, and store the
        # scaled Surface as self.sprite.

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

        self.rect.topleft = (
            round(self.position.x),
            round(self.position.y),
        )

    def draw(self, surface):
        # TODO 3:
        # Remove the placeholder rectangle below.
        # Blit self.sprite onto surface at self.rect.topleft.
        pygame.draw.rect(surface, self.color, self.rect)


def main():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    PLAYER_SIZE = 64

    BACKGROUND_COLOR = (18, 20, 32)
    PLAYER_COLOR = (100, 180, 255)
    HIGHLIGHT_COLOR = (176, 132, 64)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pixel Art Exercise")

    clock = pygame.time.Clock()

    player = Player(
        x=80,
        y=80,
        size=PLAYER_SIZE,
        color=PLAYER_COLOR,
        speed=240,
    )

    highlight = pygame.Rect(300, 250, 96, 96)

    # TODO 4:
    # Build a path to assets/crystal.png with Path(__file__).
    # Load it, call convert_alpha(), scale it to (64, 64),
    # and store the scaled Surface in a variable named crystal.
    # Do this before the loop.

    running = True

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys, dt, WIDTH, HEIGHT)

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, highlight)

        # TODO 5:
        # Blit crystal at highlight.topleft.

        player.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
