# Scalable game archictecture allows you to expand your program
# without devolving into tightly coupled, unmaintainable systems.

# Game architecture answers questions like:
# Where does the logic live?
# Who updates what?
# How do systems communicate?
# How do you avoid tightly coupled code?
# How do you add features safely?

# Non-Scalable Architecture

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

player_x = 400
player_y = 300

enemy_x = 100
enemy_y = 100

# Problem 5: Global State Explosion
# As the game grows, more and more variables end up at
# the top level of the program. Tracking who owns and
# modifies each variable becomes difficult.

# Examples:
# player_health = 100
# player_score = 0
# enemy2_x = 300
# enemy2_y = 400

# Problem 3: No Reusability
# If you want another enemy, you end up doing:
# enemy2_x = 300
# enemy2_y = 400

bullets = []

running = True

# Problem 1: Everything is Mixed Together
# Inside one loop:
# Game state
# Input
# Movement

# Problem 6: Difficult Feature Addition
# Every new feature must be inserted into the same
# giant loop, increasing complexity and the chance
# of breaking existing functionality.

# Examples:
# Inventory
# Power-ups
# Health system
# Boss AI
# Quests
# Dialogue

# Problem 4: No encapsulation
# Player logic is scattered:
# Movement is in one place.
# Shooting is elsewhere.
# Rendering is elsewhere.
while running:
    # Input and player movement
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # The logic that handles the Player shooting.
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bullets.append([player_x, player_y])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_y -= 5

    if keys[pygame.K_s]:
        player_y += 5

    if keys[pygame.K_a]:
        player_x -= 5

    if keys[pygame.K_d]:
        player_x += 5

    # Game state

    # Problem 7: No Clear Ownership
    # The main loop controls every object directly.
    # Objects should ideally manage their own behavior.

    # Instead of the Enemy deciding how to move,
    # the main loop decides for it.
    if enemy_x < player_x:
        # Problem 2: Poor Extensibility
        # What if the speed changes?
        enemy_x += 2

    if enemy_x > player_x:
        enemy_x -= 2

    if enemy_y < player_y:
        enemy_y += 2

    if enemy_y > player_y:
        enemy_y -= 2

    for bullet in bullets:
        bullet[0] += 10

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (0, 255, 0),
                     (player_x, player_y, 50, 50))

    pygame.draw.rect(screen, (255, 0, 0),
                     (enemy_x, enemy_y, 50, 50))

    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0),
                         (bullet[0], bullet[1], 10, 10))

    pygame.display.flip()

pygame.quit()