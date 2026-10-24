import pygame

pygame.init()

# What is collision?
# A wall is an object with a position and size, and that a
# collision occurs when the player overlaps it.

# pygame.Rect() makes it possible to specify an object's
# X and Y position along with its dimensions.
while True:
    # Four positional arguments.
    player_rect = pygame.Rect(100, 100, 50, 50)

    # A single sequence containing four values.
    # player_rect = pygame.Rect((100, 100, 50, 50))

    # Two sequences: position and dimensions.
    # player_rect = pygame.Rect((100, 100), (50, 50))

# wall_rect = pygame.Rect(

# )