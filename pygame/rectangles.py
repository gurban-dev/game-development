import pygame
import sys
from pygame.locals import *

pygame.init()

# set_mode() returns a Surface object representing the screen.
screen = pygame.display.set_mode((500, 400))

# Set the title bar text.
pygame.display.set_caption("Rectangles")

# Goal:
# Create rectangles using the pygame.Rect() constructor.

# Almost every game uses rectangles for:
# • Buttons
# • Walls
# • Collision detection

# Creating a Rect requires the following:

# Position of the rectangle
x_pos = 100
y_pos = 50

width = 200
height = 100

# A rectangle could be drawn like this:

# pygame.draw.rect(screen, "blue", (100, 50, 200, 100))

# However, creating a Rect object gives us many useful attributes
# and methods, making it much easier to work with rectangles.

# The Rect class does not draw anything. It simply stores
# information about a rectangle, such as its position and size.

# To actually display the rectangle, we pass the Rect object
# to pygame.draw.rect().

# Create a Rect object using the rectangle's position and size.
blue_rect = pygame.Rect(x_pos, y_pos, width, height)

# Note that the Rect constructor does not accept keyword arguments.

# pygame.draw.rect() accepts either:
# • A tuple containing (x, y, width, height)
# • A Rect object
pygame.draw.rect(screen, "blue", blue_rect)

# The left attribute represents the x-coordinate of the rectangle's
# left edge.

# left is always equal to the rectangle's x-coordinate position.

# The right attribute represents the x-coordinate of the rectangle's
# right edge.

# right = left + width

# right = 100 + 200

# right = 300

# A Rect object provides many useful attributes.

# Position:
# left
# top
# right
# bottom

# Size:
# width
# height
# size

# Center:
# centerx
# centery
# center

# Corners:
# topleft
# topright
# bottomleft
# bottomright

# Notice that we never assigned values to left, right, centerx,
# centery or bottomright.

# The Rect object calculates these values automatically from the
# rectangle's position and size.
print("\nblue_rect.left:", blue_rect.left)
print("blue_rect.right:", blue_rect.right)

print("\nblue_rect.width:", blue_rect.width)
print("blue_rect.height:", blue_rect.height)

# The centerx attribute is the x-coordinate of the rectangle's
# center.

# centerx = left + (width / 2)

# centerx = 100 + (200 / 2)

# centerx = 100 + 100

# centerx = 200

# The centery attribute is the y-coordinate of the rectangle's
# center.

# centery = y_pos + (height / 2)

# centery = 50 + (100 / 2)

# centery = 50 + 50

# centery = 100

print("\nblue_rect.centerx:", blue_rect.centerx)
print("blue_rect.centery:", blue_rect.centery)

# The topleft attribute returns both the x and y coordinates of
# the rectangle's top-left corner as a tuple.
print("\nblue_rect.topleft:", blue_rect.topleft)

print("blue_rect.bottomright:", blue_rect.bottomright)

# Recap

# A Rect object stores information about a rectangle.

# It remembers:
# • Position
# • Size
# • Center
# • Corners

# The Rect object can be passed directly to pygame.draw.rect()
# whenever we want to draw it.

while True:
    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()
    
    pygame.display.update()