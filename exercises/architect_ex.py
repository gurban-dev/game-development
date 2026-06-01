# =========================================================
# EXERCISE:
# Refactoring a Small Pygame Prototype Into a More
# Scalable Architecture.
# =========================================================

# GOAL:
# Learn why large games become difficult to maintain when
# everything is placed inside one file and one game loop.
#
# In this exercise, you will reorganize this prototype into
# multiple files and folders based on responsibility.

# =========================================================
# YOUR TASKS:
# =========================================================

# 1. Run the game first.

#    Controls:
#    - W/A/S/D -> Move player.
#    - SPACE   -> Shoot bullets.

# 2. Read every above-line comment carefully.

#    Each section tells you where that code SHOULD live in
#    a scalable architecture.

# 3. Create the following folder structure:

#    game/
#    │
#    ├── main.py
#    ├── config.py
#    │
#    ├── core/
#    ├── entities/
#    ├── systems/

# 4. Move code into the correct files.

#    Example:

#    - Player variables:
#      -> entities/player.py

#    - Enemy update logic:
#      -> systems/enemy_system.py

#    - Input handling:
#      -> core/input_manager.py

# 5. Import the code back into main.py.

#    The final main loop should become much smaller and
#    cleaner.

# =========================================================
# WHAT YOU SHOULD NOTICE:
# =========================================================

# BAD ARCHITECTURE:

# - One giant file.
# - Global variables everywhere.
# - Logic mixed together.
# - Hard to expand safely.
# - Features become tightly coupled.

# BETTER ARCHITECTURE:

# - Responsibilities are separated.
# - Systems become modular.
# - Easier debugging.
# - Easier collaboration.
# - Easier feature expansion.
# - Cleaner mental model.

# =========================================================
# FINAL CHALLENGE:
# =========================================================

# After refactoring:

# Try adding:
# - Multiple enemies.
# - Bullet collision.
# - Health system.
# - Score system.

# You will immediately notice that scalable architecture
# makes new features dramatically easier to implement.
# =========================================================

import pygame

pygame.init()

# ============================================
# Main window configuration.
# This should eventually move to:
# -> config.py
# ============================================

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

clock = pygame.time.Clock()

# ============================================
# Player data.
# This should eventually move to:
# -> entities/player.py
# ============================================

player_x = 400
player_y = 300
player_speed = 5

# ============================================
# Enemy data.
# This should eventually move to:
# -> entities/enemy.py
# ============================================

enemy_x = 100
enemy_y = 100
enemy_speed = 2

# ============================================
# Bullet data.
# This should eventually move to:
# -> entities/bullet.py
# ============================================

bullets = []

# ============================================
# Input handling logic.
# This should eventually move to:
# -> core/input_manager.py
# ============================================

def handle_input():

    global player_x
    global player_y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_y -= player_speed

    if keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_a]:
        player_x -= player_speed

    if keys[pygame.K_d]:
        player_x += player_speed

# ============================================
# Enemy movement system.
# This should eventually move to:
# -> systems/enemy_system.py
# ============================================

def update_enemy():

    global enemy_x
    global enemy_y

    if enemy_x < player_x:
        enemy_x += enemy_speed

    if enemy_x > player_x:
        enemy_x -= enemy_speed

    if enemy_y < player_y:
        enemy_y += enemy_speed

    if enemy_y > player_y:
        enemy_y -= enemy_speed

# ============================================
# Bullet update system.
# This should eventually move to:
# -> systems/projectile_system.py
# ============================================

def update_bullets():

    for bullet in bullets:
        bullet[0] += 10

# ============================================
# Rendering system.
# This should eventually move to:
# -> core/render_system.py
# ============================================

def render():

    screen.fill((30, 30, 30))

    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (player_x, player_y, 50, 50)
    )

    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (enemy_x, enemy_y, 50, 50)
    )

    for bullet in bullets:

        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (bullet[0], bullet[1], 10, 10)
        )

    pygame.display.flip()

# ============================================
# Main game loop.
# This should eventually stay inside:
# -> core/game.py
# ============================================

running = True

while running:

    # ========================================
    # Window event handling.
    # This should remain near the main loop.
    # ========================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # ====================================
        # Bullet spawning logic.
        # This should eventually move to:
        # -> systems/projectile_system.py
        # ====================================

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bullets.append(
                    [player_x, player_y]
                )

    # ========================================
    # System updates.
    # ========================================

    handle_input()

    update_enemy()

    update_bullets()

    # ========================================
    # Render everything.
    # ========================================

    render()

    clock.tick(60)

pygame.quit()