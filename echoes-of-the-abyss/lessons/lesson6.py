import pygame
from pathlib import Path


def load_sprite(path, size):
    # pygame.image.load reads a file from disk and returns a Surface.
    # A Surface is the image living in memory. Loading does not
    # draw anything.
    loaded = pygame.image.load(path)

    # A PNG can store a transparency amount on every pixel.
    # convert_alpha() keeps that transparency and rewrites the
    # pixels into the display's format.
    #
    # The display must already exist. set_mode() chooses the
    # pixel format, and convert_alpha() matches it.
    #
    # Do this once, at load time. A converted sprite can be
    # copied to the screen quickly on every frame.
    loaded = loaded.convert_alpha()

    # scale() builds a new Surface at the requested pixel size.
    # The file itself stays small.
    #
    # Pixel art stays blocky and readable when the new size is
    # an integer multiple of the file size. 16 x 16 scaled to
    # 64 x 64 is exactly 4 times on each side, so every source
    # pixel becomes a 4 x 4 block.
    #
    # smoothscale() would blend neighboring pixels. That is
    # useful for photographs and the wrong tool for pixel art.
    return pygame.transform.scale(loaded, (size, size))


class Player:
    def __init__(self, x, y, size, speed, image_path):
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.speed = speed

        # The Rect is still the body's position and size.
        # Movement, screen limits, and collision all use it.
        # The sprite is the picture drawn on top of that body.
        self.rect = pygame.Rect(x, y, size, size)
        self.sprite = load_sprite(image_path, size)

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

        # blit() will use this top-left corner, so the picture
        # and the rectangle stay on the same pixel.
        self.rect.topleft = (
            round(self.position.x),
            round(self.position.y),
        )

    def draw(self, surface):
        # blit copies the sprite onto the destination Surface.
        # The second argument is the top-left pixel where the
        # copy begins. Transparent pixels leave the destination
        # unchanged, which is why the colored rectangle can go.
        surface.blit(self.sprite, self.rect.topleft)


def main():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    PLAYER_SIZE = 64

    BACKGROUND_COLOR = (18, 20, 32)
    PANEL_COLOR = (186, 42, 120)
    HIGHLIGHT_COLOR = (176, 132, 64)
    LABEL_COLOR = (236, 236, 244)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pixel Art Awakens")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)

    # __file__ is the path of this script.
    # Building from the script's folder means the images are
    # found when the program is launched from this directory
    # and also when it is launched from the project root.
    # A plain relative path such as "assets/adventurer.png"
    # would only work for one of those two launch folders.
    assets = Path(__file__).parent / "assets"
    adventurer_path = assets / "adventurer.png"
    crystal_path = assets / "crystal.png"

    # The same file, prepared two ways, so the transparency
    # difference is visible.
    #
    # convert() produces an opaque Surface. Pixels that were
    # transparent in the PNG become solid black.
    # convert_alpha() keeps those pixels transparent.
    loaded = pygame.image.load(adventurer_path)
    opaque_preview = pygame.transform.scale(loaded.convert(), (64, 64))
    clear_preview = pygame.transform.scale(
        loaded.convert_alpha(),
        (64, 64),
    )

    # The file is 16 x 16. Shown at native size, it is a speck.
    # Scaling is what makes it readable in the window.
    native_sprite = loaded.convert_alpha()

    player = Player(
        x=80,
        y=80,
        size=PLAYER_SIZE,
        speed=240,
        image_path=adventurer_path,
    )

    # Any image uses the same path, load, convert_alpha, scale
    # sequence. The crystal's center pixels are only partly
    # opaque, so the gold rectangle will show through them.
    crystal = load_sprite(crystal_path, 64)
    highlight = pygame.Rect(300, 250, 96, 96)

    # Each preview sits on its own magenta panel. The panel is
    # larger than the sprite, so transparent corners reveal the
    # magenta and opaque corners cover it.
    opaque_panel = pygame.Rect(512, 56, 80, 80)
    clear_panel = pygame.Rect(512, 196, 80, 80)

    running = True

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys, dt, WIDTH, HEIGHT)

        screen.fill(BACKGROUND_COLOR)

        # Draw each panel before the sprite that sits on it.
        # The convert() copy covers its panel with a black box.
        # The convert_alpha() copy lets the panel show through.
        screen.blit(
            font.render("convert()", True, LABEL_COLOR),
            (512, 28),
        )
        pygame.draw.rect(screen, PANEL_COLOR, opaque_panel)
        screen.blit(opaque_preview, (520, 64))

        screen.blit(
            font.render("convert_alpha()", True, LABEL_COLOR),
            (512, 168),
        )
        pygame.draw.rect(screen, PANEL_COLOR, clear_panel)
        screen.blit(clear_preview, (520, 204))

        screen.blit(
            font.render("16 x 16 file", True, LABEL_COLOR),
            (512, 300),
        )
        screen.blit(native_sprite, (640, 300))

        pygame.draw.rect(screen, HIGHLIGHT_COLOR, highlight)
        screen.blit(crystal, highlight.topleft)

        player.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
