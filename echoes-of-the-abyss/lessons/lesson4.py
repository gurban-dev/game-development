import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Laboratory")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

# What is collision?
# A wall is an object with a position and size, and that a
# collision occurs when the player overlaps it.

# pygame.Rect() makes it possible to specify an object's
# X and Y position along with its dimensions.

# Four positional arguments.
player_rect = pygame.Rect(100, 100, 50, 50)

# A single sequence containing four values.
# player_rect = pygame.Rect((100, 100, 50, 50))

# Two sequences: position and dimensions.
# player_rect = pygame.Rect((100, 100), (50, 50))

# Define the wall's position and dimensions.
wall_rect = pygame.Rect(350, 200, 150, 200)

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player rectangle to the mouse position.
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player_rect.topleft = (mouse_x, mouse_y)

    # Check whether the rectangles overlap.
    colliding = player_rect.colliderect(wall_rect)

    screen.fill((18, 20, 32))

    # Draw the wall differently when a collision occurs.
    if colliding:
        wall_color = (220, 70, 70)
    else:
        wall_color = (110, 110, 130)

    pygame.draw.rect(screen, wall_color, wall_rect)
    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    status = "Collision detected!" if colliding else "No collision"
    text_surface = font.render(status, True, (240, 240, 240))
    screen.blit(text_surface, (20, 20))

    pygame.display.flip()

pygame.quit()