import pygame
# TODO 1: Import Path from pathlib. Use it to build an asset path based on
# this file's location, so the program works when launched from another folder.


# Pixel Art Awakens

# Goal: finish a small, standalone sprite demo using the existing image at
# lessons/assets/adventurer.jpeg. Do not make or save image files.
# The provided image is a JPEG and therefore has no transparent pixels.
# A separate transparent Surface will demonstrate alpha in memory.

# Complete every TODO below:
# 1. Import Path.

# 2. Finish load_scaled_image(): load the file, call convert_alpha(), and
#    return pygame.transform.scale(...) using the requested size.

# 3. Finish make_alpha_example(): make a Surface with SRCALPHA, draw a
#    partially transparent circle in its center, and return the Surface.

# 4. After the display is created, build the adventurer path from
#    Path(__file__).parent / "assets" / "adventurer.jpeg". Load and scale the
#    sprite to (96, 78), then create its Rect at (70, 360). Do this before the
#    loop; image loading and scaling do not belong in the frame loop.

# 5. Before the loop, call make_alpha_example((100, 100)) and save the result.

# 6. In the drawing section, after drawing the alpha panel, blit the alpha
#    Surface at alpha_panel.topleft. Draw the panel first so the clear corners
#    reveal its color and the semi-transparent circle blends with it.

# 7. Blit the player sprite at player_rect.topleft after drawing the floor.

# Useful details:
# - convert_alpha() preserves alpha already in an image; it cannot add alpha
#   to this JPEG. That is why the program also builds a transparent Surface.
# - The circle color should be an RGBA tuple such as (105, 225, 255, 150).
# - Use pygame.draw.circle(surface, color, center, radius).
# - Use pygame.SRCALPHA when constructing the transparent Surface.
# - blit(source_surface, destination) copies the source onto the destination.
# - Arrow-key input and direction normalization are provided; TODO 6 applies
#   that movement and clamps the Rect to the screen.


def load_scaled_image(path, size):
    # TODO 2: Load `path` with pygame.image.load(). Call convert_alpha() on
    # the loaded Surface, then return pygame.transform.scale(surface, size).
    # This helper runs once during setup, not once per frame.
    pass


def make_alpha_example(size):
    # TODO 3: Create a transparent Surface of `size` with pygame.SRCALPHA.
    # Draw a circle centered at (size[0] // 2, size[1] // 2), with radius
    # size[0] // 3 and RGBA color (105, 225, 255, 150). Return the Surface.
    pass


def draw_label(surface, font, text, position):
    # Rendered text is a Surface too, so display it with blit().
    rendered_text = font.render(text, True, (238, 240, 250))
    surface.blit(rendered_text, position)


def main():
    pygame.init()

    screen_width = 900
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pixel Art Exercise")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 26)
    small_font = pygame.font.Font(None, 21)

    # TODO 4: After set_mode(), construct the asset path with
    # Path(__file__).parent / "assets" / "adventurer.jpeg". Use
    # load_scaled_image() to prepare a (96, 78) sprite. Create a Rect for it
    # with its top-left at (70, 360). The display must exist before
    # convert_alpha() is called.

    # TODO 5: Call make_alpha_example((100, 100)) and store the result in
    # alpha_demo. Do this before the loop so the Surface is created only once.

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

        # Build the movement vector from the arrow keys.
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

        # Normalization keeps diagonal movement at the same speed.
        if movement.length_squared() > 0:
            movement = movement.normalize()

        # TODO 6: Add round(movement.x * player_speed * dt) to player_rect.x,
        # and round(movement.y * player_speed * dt) to player_rect.y. Then
        # call player_rect.clamp_ip(screen.get_rect()) to keep it visible.

        screen.fill(background_color)
        pygame.draw.rect(screen, floor_color, (34, 350, 570, 205), border_radius=12)

        draw_label(screen, font, "Pixel Art Awakens", (34, 24))
        draw_label(screen, small_font, "Move the sprite with the arrow keys", (34, 58))
        draw_label(screen, small_font, "JPEG has no built-in transparency", (650, 218))
        draw_label(screen, small_font, "Alpha Surface example", (650, 362))
        draw_label(screen, small_font, "Pipeline: load > convert_alpha > scale > blit", (34, 565))

        # Draw the colored panel first, then the transparent example on top.
        pygame.draw.rect(screen, panel_color, alpha_panel, border_radius=8)

        # TODO 7: Blit alpha_demo at alpha_panel.topleft. Its transparent
        # corners should reveal the panel, and the circle should blend with it.

        # TODO 8: Blit the prepared player sprite at player_rect.topleft after
        # drawing the floor. This replaces the old placeholder with the image.

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()