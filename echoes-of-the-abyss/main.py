import pygame
from player import Player
from pathlib import Path

from world import World

pygame.init()

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 64
SPEED = 200

BACKGROUND_COLOR = (18, 20, 32)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Echoes of the Abyss")

# Create a clock to control the game's frame rate.
clock = pygame.time.Clock()

# Resolve the asset beside this script, independent of the launch directory.
assets_directory = Path(__file__).parent / "lessons" / "assets"
adventurer_path = assets_directory / "adventurer.jpeg"

# The display already exists, which convert_alpha() requires.
player = Player(100, 100, PLAYER_SIZE, SPEED, adventurer_path)

world = World()

running = True

while running:
    # Calculate the time elapsed since the previous frame
    # and convert it from milliseconds to second.
    dt = clock.tick(60) / 1000

    # Handle events such as closing the game window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read the current keyboard state to determine which arrow
    # keys are being pressed.
    keys = pygame.key.get_pressed()

    player.update(keys, dt, WIDTH, HEIGHT, world.walls)

    # Draw the game.
    screen.fill(BACKGROUND_COLOR)

    # Draw all the walls belonging to the game world onto the
    # game screen.
    world.draw(screen)

    player.draw(screen)

    # Update the entire screen.
    pygame.display.flip()

pygame.quit()