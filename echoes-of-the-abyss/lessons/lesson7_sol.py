import pygame
from pathlib import Path


def load_scaled_image(path, size):
    loaded_image = pygame.image.load(path)

    # convert_alpha keeps source transparency and prepares the Surface for
    # this display. Scale once during setup so the frame loop only draws it.
    alpha_image = loaded_image.convert_alpha()
    return pygame.transform.scale(alpha_image, size)


def make_alpha_example(size):
    # JPEG cannot contain transparent pixels, so use an in-memory SRCALPHA
    # Surface to show clear and partly transparent areas without new files.
    transparent_layer = pygame.Surface(size, pygame.SRCALPHA)

    pygame.draw.circle(
        transparent_layer,
        (105, 225, 255, 150),
        (size[0] // 2, size[1] // 2),
        size[0] // 3,
    )
    return transparent_layer


def draw_label(surface, font, text, position):
    rendered_text = font.render(text, True, (238, 240, 250))
    surface.blit(rendered_text, position)


def main():
    pygame.init()

    screen_width = 900
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pixel Art Solution")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)
    small_font = pygame.font.Font(None, 21)

    # Anchor the asset path to this script so launching from another folder
    # still finds the existing file. The display is ready for convert_alpha.
    asset_path = Path(__file__).parent / "assets" / "adventurer.jpeg"
    player_sprite = load_scaled_image(asset_path, (96, 78))
    player_rect = player_sprite.get_rect(topleft=(70, 360))

    # Build the alpha demonstration once; loading and setup work stay outside
    # the loop because neither image changes from frame to frame.
    alpha_demo = make_alpha_example((100, 100))

    background_color = (19, 23, 37)
    panel_color = (148, 44, 106)
    floor_color = (47, 70, 105)
    player_speed = 260
    alpha_panel = pygame.Rect(650, 250, 100, 100)

    running = True

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

        # Normalize so diagonal travel covers the same distance per second.
        if movement.length_squared() > 0:
            movement = movement.normalize()

        player_rect.x += round(movement.x * player_speed * dt)
        player_rect.y += round(movement.y * player_speed * dt)
        player_rect.clamp_ip(screen.get_rect())

        screen.fill(background_color)

        pygame.draw.rect(
            screen,
            floor_color,
            (34, 350, 570, 205),
            border_radius=12
        )

        draw_label(screen, font, "Pixel Art Awakens", (34, 24))
        draw_label(screen, small_font, "Move the sprite with the arrow keys", (34, 58))
        draw_label(screen, small_font, "JPEG has no built-in transparency", (650, 218))
        draw_label(screen, small_font, "Alpha Surface example", (650, 362))
        draw_label(screen, small_font, "Pipeline: load > convert_alpha > scale > blit", (34, 565))

        # Draw the colored panel before the alpha Surface; transparent pixels
        # reveal the panel, and partial alpha blends the circle with it.
        pygame.draw.rect(screen, panel_color, alpha_panel, border_radius=8)

        screen.blit(alpha_demo, alpha_panel.topleft)

        # Draw the sprite after the floor so it appears in front of the scene.
        screen.blit(player_sprite, player_rect.topleft)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()