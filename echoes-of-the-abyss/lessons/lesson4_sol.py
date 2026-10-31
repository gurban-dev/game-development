import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
SPEED = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Echoes of the Abyss")

clock = pygame.time.Clock()

player_position = pygame.Vector2(100, 100)

# Define the wall's position and dimensions.
wall_rect = pygame.Rect(350, 200, 150, 200)

running = True

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    direction = pygame.Vector2(0, 0)

    # Check for horizontal movement.
    if keys[pygame.K_LEFT]:
        direction.x = -1
    if keys[pygame.K_RIGHT]:
        direction.x = 1

    # Check for vertical movement.
    if keys[pygame.K_UP]:
        direction.y = -1
    if keys[pygame.K_DOWN]:
        direction.y = 1

    # Normalize the direction vector.
    if direction.length() > 0:
        direction = direction.normalize()

    # Move horizontally and check for a collision.
    previous_x = player_position.x
    player_position.x += direction.x * SPEED * dt

    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    if player_rect.colliderect(wall_rect):
        player_position.x = previous_x

    # Move vertically and check for a collision.
    previous_y = player_position.y
    player_position.y += direction.y * SPEED * dt

    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    if player_rect.colliderect(wall_rect):
        player_position.y = previous_y

    # Keep the player inside the horizontal boundaries.
    player_position.x = max(
        0, min(WIDTH - PLAYER_SIZE, player_position.x)
    )

    # Keep the player inside the vertical boundaries.
    player_position.y = max(
        0, min(HEIGHT - PLAYER_SIZE, player_position.y)
    )

    screen.fill((18, 20, 32))

    # Create the player's rectangle for drawing.
    player_rect = pygame.Rect(
        round(player_position.x),
        round(player_position.y),
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    pygame.draw.rect(screen, (110, 110, 130), wall_rect)
    pygame.draw.rect(screen, (100, 180, 255), player_rect)

    pygame.display.flip()

pygame.quit()


# Question 1:
# Why do we save previous_x before updating
# the player's position?

# Answer:
# We save the previous X coordinate so that we
# can restore the player's original position if
# a collision occurs after horizontal movement.


# Question 2:
# What does colliderect() return?

# Answer:
# It returns True if two rectangles overlap
# and False if they do not overlap.


# Question 3:
# Why do we create a new player rectangle after
# updating its position?

# Answer:
# Because the player's position has changed.
# We need an updated rectangle to accurately
# detect collisions at the new position.


# Question 4:
# Why do we check horizontal and vertical
# collisions separately?

# Answer:
# This allows us to determine which direction
# caused the collision. We can undo movement
# along the blocked axis while allowing movement
# along the other axis.

# This also allows the player to slide along walls.


# Question 5:
# Why do we multiply movement by dt?

# Answer:
# dt represents the time elapsed since the
# previous frame. Multiplying movement by dt
# makes the player's movement independent of
# the frame rate.


# Question 6:
# Why do we subtract PLAYER_SIZE from WIDTH
# and HEIGHT when checking screen boundaries?

# Answer:
# Because player_position represents the
# top-left corner of the player.

# We subtract PLAYER_SIZE to ensure that the
# player's entire rectangle remains inside
# the screen rather than just its top-left corner.


# Question 7:
# Why do we draw the wall and player after
# filling the screen with the background color?

# Answer:
# screen.fill() clears the previous frame.
# We then draw the wall and player on top of
# the background so they remain visible.


# Question 8:
# What would happen if we removed direction
# normalization?

# Answer:
# The player would move faster diagonally than
# horizontally or vertically.

# Normalizing the direction vector ensures
# that its length is 1, keeping movement speed
# consistent in every direction.