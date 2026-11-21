import pygame
from pathlib import Path

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Some of the Pygame Concepts Covered:

# 1. Surfaces and Sprites
#    • Load, convert, scale, and display images.

# 2. Drawing and Blitting
#    • Draw shapes, display images, and manage layering.

# 3. Transparency
#    • Create and display transparent Surfaces.


def load_scaled_image(path, size):
    # image.load() reads image data into a Surface; it does not put it
    # on screen.
    loaded_image = pygame.image.load(path)

    # convert_alpha() prepares a Surface for the display and preserves
    # any per-pixel alpha already present in the source image.
    alpha_image = loaded_image.convert_alpha()

    # transform.scale() resizes a Surface at the requested dimensions
    # and returns it.

    # Use integer multiples when possible to keep pixel-art edges crisp.

    # Integer multiples are created by multiplying the original
    # dimensions by a whole number.
    return pygame.transform.scale(alpha_image, size)


def make_alpha_example(size):
    # These assets are JPEGs, which cannot store transparent pixels.

    # When we create a Pygame Surface, we work with its color information.
    # However, with pygame.SRCALPHA we can also create a Surface that
    # stores transparency information for every individual pixel.

    # pygame.SRCALPHA is a constant makes it possible to create a
    # Surface capable of storing transparency information for its
    # pixels.
    transparent_layer = pygame.Surface(size, pygame.SRCALPHA)

    # Alpha is a value that determines the transparency or opacity of
    # a color.

    # The untouched corners have alpha 0 and reveal the scene underneath.
    # The center circle has partial alpha, so the background blends through.

    # Red: 105 Green: 225 Blue: 255 Alpha: 150
    # (105, 225, 255, 150)

    # The alpha value determines the transparency of the pixel.

    # Alpha values:
    # 0	    Completely transparent
    # 150	Partially transparent
    # 255	Completely opaque
    pygame.draw.circle(
        transparent_layer,
        (105, 225, 255, 150),
        (size[0] // 2, size[1] // 2),
        size[0] // 3,
    )

    # A smaller opaque diamond gives a fully opaque pixel region to
    # compare with both the transparent corners and the translucent
    # circle.
    center_x = size[0] // 2
    center_y = size[1] // 2

    diamond_points = [
        (center_x, center_y - 12),
        (center_x + 12, center_y),
        (center_x, center_y + 12),
        (center_x - 12, center_y),
    ]

    pygame.draw.polygon(transparent_layer, (255, 225, 120, 255), diamond_points)

    return transparent_layer


def draw_label(surface, font, text, position, color=(238, 240, 250)):
    # Text is also a Surface, so it is drawn with the same blit operation.
    rendered_text = font.render(text, True, color)

    surface.blit(rendered_text, position)


def draw_panel(surface, color, rect, border_radius=8):
    pygame.draw.rect(surface, color, rect, border_radius=border_radius)


def draw_scaled_image(surface, image, size, position):
    scaled_image = pygame.transform.scale(image, size)

    # .blit() takes a Surface that is passed to it as an argument
    # and places it on the Surface object it is being invoked on.
    surface.blit(scaled_image, position)


def move_player(player_rect, speed, dt, screen):
    keys = pygame.key.get_pressed()

    movement = pygame.Vector2(0, 0)

    if keys[pygame.K_RIGHT]:
        movement.x += 1

    if keys[pygame.K_LEFT]:
        movement.x -= 1

    if keys[pygame.K_DOWN]:
        movement.y += 1

    if keys[pygame.K_UP]:
        movement.y -= 1

    # Prevent diagonal player movement from being faster than
    # perpendicular movement.
    if movement.length_squared() > 0:
        movement = movement.normalize()

    player_rect.x += round(movement.x * speed * dt)
    player_rect.y += round(movement.y * speed * dt)

    # screen.get_rect() returns a pygame.Rect object representing
    # the entire screen.

    # Since our screen is 900 pixels wide and 600 pixels tall,
    # this rectangle has:
    # • x = 0
    # • y = 0
    # • width = 900
    # • height = 600

    # .clamp_ip() ensures that player_rect stays entirely within the
    # boundaries of the screen rectangle.

    # For example:
    # • If the player moves beyond the left edge, its x coordinate is
    #   adjusted to 0.

    # • If the player moves beyond the top edge, its y coordinate is
    #   adjusted to 0.

    # • If the player moves beyond the right edge, its right edge is
    #   aligned with the screen's right edge.

    # • If the player moves beyond the bottom edge, its bottom edge
    #   is aligned with the screen's bottom edge.
    player_rect.clamp_ip(screen.get_rect())


def draw_alpha_demo(screen, font, alpha_demo, panel_color):
    draw_label(screen, font, "Alpha in a Surface", (650, 228))

    # Create a rectangle at (650, 254) with a width and height of 100 pixels.
    panel = pygame.Rect(650, 254, 100, 100)

    draw_panel(screen, panel_color, panel)

    # The colored panel is drawn first, allowing us to see it through
    # the transparent areas of alpha_demo.
    screen.blit(alpha_demo, panel.topleft)

    draw_label(screen, font, "clear corners; blended circle", (650, 362))


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Pixel Art Awakens")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)
    small_font = pygame.font.Font(None, 21)

    # __file__ provides the path to this Python script. Path(__file__).parent
    # returns the directory that the script is located in, ensuring that the
    # assets folder is found regardless of the different path location this
    # program will be run from.
    asset_directory = Path(__file__).parent / "assets"
    adventurer_path = asset_directory / "adventurer.jpeg"

    original_image = pygame.image.load(adventurer_path)

    # Convert the original Surface for display without per-pixel alpha.
    # That is, without preserving per-pixel alpha transparency.

    # Opaque means that a pixel is completely visible and does not allow
    # the background behind it to show through it.
    opaque_converted = original_image.convert()

    # Convert the original Surface while preserving per-pixel transparency.

    # Per-pixel alpha means that every individual pixel stores its own alpha
    # value, which determines its transparency or opacity. Per-pixel
    # transparency describes the resulting effect, while per-pixel alpha
    # describes how that effect is controlled using an alpha value.
    alpha_converted = original_image.convert_alpha()

    # Load the adventurer image, convert it, and resize it to 96 × 78 pixels.
    player_sprite = load_scaled_image(adventurer_path, (96, 78))

    # In game development, a sprite is a two-dimensional or 2D
    # visual represention of a game object.
    # E.g. Player, enemy, collectible, etc.

    # Create a rectangle matching the sprite's dimensions and set its
    # initial position.
    player_rect = player_sprite.get_rect(topleft=(70, 360))

    # Create a smaller 56 × 45 pixel version for the source image preview.
    source_preview = load_scaled_image(adventurer_path, (56, 45))

    # Create a 72 × 72 pixel version for the scaled image preview.
    scaled_preview = load_scaled_image(adventurer_path, (72, 72))

    # JPEG images do not support transparency. Therefore, we create a new
    # Surface in memory to demonstrate how transparent and partially
    # transparent pixels work.

    # Consequently, both converted images look the same.
    alpha_demo = make_alpha_example((100, 100))

    # Separate panels give blit() a colored destination that remains visible
    # through transparent portions of the alpha demonstration.

    # Two separate colored background panels are being drawn before placing
    # the images on top of them. This allows us to see what happens when
    # Pygame encounters transparent pixels.

    # Create a rectangle at (650, 92) with a width and height of 108 pixels.
    opaque_panel = pygame.Rect(650, 92, 108, 108)

    alpha_panel = pygame.Rect(775, 92, 108, 108)

    background_color = (19, 23, 37)
    panel_color = (148, 44, 106)
    accent_color = (47, 70, 105)
    player_speed = 260

    running = True

    while running:
        # Delta time makes keyboard movement independent of frame rate.
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_player(player_rect, player_speed, dt, screen)

        # Draw the background and panels first; later blits appear on top.
        screen.fill(background_color)

        pygame.draw.rect(
            screen,
            accent_color,
            (34, 350, 570, 205),
            border_radius=12
        )

        draw_panel(screen, panel_color, opaque_panel)
        draw_panel(screen, panel_color, alpha_panel)

        draw_label(screen, font, "Pixel Art Awakens", (34, 24))
        draw_label(screen, small_font, "Move the sprite with the arrow keys", (34, 58))

        # Label the source-image comparison. The supplied JPEG is opaque, so
        # both conversions look alike; discuss that convert_alpha cannot add
        # transparency that the source file does not contain.
        draw_label(screen, small_font, "Source: JPEG (opaque)", (650, 55))
        draw_label(screen, small_font, "convert()", (650, 76))
        draw_label(screen, small_font, "convert_alpha()", (775, 76))

        # Blit the converted images over matching panels to compare them.
        draw_scaled_image(screen, opaque_converted, (92, 92), (658, 100))

        draw_scaled_image(screen, alpha_converted, (92, 92), (783, 100))

        # This second comparison visibly shows transparency and partial alpha.
        # Draw its magenta panel before blitting the transparent Surface.
        draw_alpha_demo(screen, small_font, alpha_demo, panel_color)

        # Show a small source preview beside a larger scaled preview.
        # transform.scale creates Surfaces and leaves the file untouched.
        draw_label(screen, small_font, "Source preview", (778, 228))
        screen.blit(source_preview, (778, 254))

        draw_label(screen, small_font, "Scaled preview", (778, 455))
        screen.blit(scaled_preview, (778, 480))

        # Draw the player last so it appears over the floor. blit uses the
        # rectangle's top-left position to keep the image aligned while moving.
        screen.blit(player_sprite, player_rect.topleft)

        draw_label(
            screen,
            small_font,
            "Pipeline: image.load  >  convert_alpha  >  transform.scale  >  blit",
            (34, 565),
        )

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()