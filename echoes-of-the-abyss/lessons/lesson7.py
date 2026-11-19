import pygame
from pathlib import Path


def load_scaled_image(path, size):
    # image.load reads image data into a Surface; it does not put it on screen.
    loaded_image = pygame.image.load(path)

    # convert_alpha prepares a Surface for the display and preserves any
    # per-pixel alpha already present in the source image.
    alpha_image = loaded_image.convert_alpha()

    # scale returns a new Surface at the requested dimensions. Use integer
    # multiples when possible to keep pixel-art edges crisp.
    return pygame.transform.scale(alpha_image, size)


def make_alpha_example(size):
    # These assets are JPEGs, which cannot store transparent pixels. Build a
    # simple example Surface in memory so the lesson can still show alpha.
    transparent_layer = pygame.Surface(size, pygame.SRCALPHA)

    # The untouched corners have alpha 0 and reveal the scene underneath.
    # The center circle has partial alpha, so the background blends through.
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


def main():
    pygame.init()

    screen_width = 900
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Lesson 7: Pixel Art Awakens")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)
    small_font = pygame.font.Font(None, 21)

    # __file__ anchors this path to the lesson script, not the terminal's
    # current directory. The existing JPEG is used; no image is created.
    asset_directory = Path(__file__).parent / "assets"
    adventurer_path = asset_directory / "adventurer.jpeg"

    # The display must exist before convert_alpha() is called.
    original_image = pygame.image.load(adventurer_path)
    opaque_converted = original_image.convert()
    alpha_converted = original_image.convert_alpha()

    # Enlarge the source for the movable character while roughly keeping its
    # original aspect ratio. This JPEG has no transparent pixels even though
    # convert_alpha() is still valid.
    player_sprite = pygame.transform.scale(alpha_converted, (96, 78))
    player_rect = player_sprite.get_rect(topleft=(70, 360))

    # Fit a source preview into the panel without changing the file on disk.
    source_preview = pygame.transform.scale(alpha_converted, (56, 45))
    scaled_preview = pygame.transform.scale(alpha_converted, (72, 72))

    # This in-memory layer provides a real transparency demonstration because
    # the supplied JPEG cannot contain alpha values.
    alpha_demo = make_alpha_example((100, 100))

    # Separate panels give blit() a colored destination that remains visible
    # through transparent portions of the alpha demonstration.
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

        # The sprite replaces the placeholder rectangle and moves with arrows.
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

        # Normalize so diagonal movement is not faster than horizontal motion.
        if movement.length_squared() > 0:
            movement = movement.normalize()

        player_rect.x += round(movement.x * player_speed * dt)
        player_rect.y += round(movement.y * player_speed * dt)
        player_rect.clamp_ip(screen.get_rect())

        # Draw the background and panels first; later blits appear on top.
        screen.fill(background_color)
        pygame.draw.rect(screen, accent_color, (34, 350, 570, 205), border_radius=12)
        pygame.draw.rect(screen, panel_color, opaque_panel, border_radius=8)
        pygame.draw.rect(screen, panel_color, alpha_panel, border_radius=8)

        draw_label(screen, font, "Pixel Art Awakens", (34, 24))
        draw_label(screen, small_font, "Move the sprite with the arrow keys", (34, 58))

        # Label the source-image comparison. The supplied JPEG is opaque, so
        # both conversions look alike; discuss that convert_alpha cannot add
        # transparency that the source file does not contain.
        draw_label(screen, small_font, "Source: JPEG (opaque)", (650, 55))
        draw_label(screen, small_font, "convert()", (650, 76))
        draw_label(screen, small_font, "convert_alpha()", (775, 76))

        # Blit the converted images over matching panels to compare them.
        screen.blit(pygame.transform.scale(opaque_converted, (92, 92)), (658, 100))
        screen.blit(pygame.transform.scale(alpha_converted, (92, 92)), (783, 100))

        # This second comparison visibly shows transparency and partial alpha.
        # Draw its magenta panel before blitting the transparent Surface.
        draw_label(screen, small_font, "Alpha in a Surface", (650, 228))
        alpha_panel_small = pygame.Rect(650, 254, 100, 100)
        pygame.draw.rect(screen, panel_color, alpha_panel_small, border_radius=8)
        screen.blit(alpha_demo, alpha_panel_small.topleft)
        draw_label(screen, small_font, "clear corners; blended circle", (650, 362))

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