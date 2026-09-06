import pygame
import sys

pygame.init()

WINDOWWIDTH = 500
WINDOWHEIGHT = 500

BOXSIZE = 60
GAPSIZE = 10

BOARDWIDTH = 5
BOARDHEIGHT = 5

BGCOLOR = (60, 60, 100)
BOXCOLOR = (255, 255, 255)
HIGHLIGHTCOLOR = (0, 0, 255)

DISPLAYSURF = pygame.display.set_mode(
    (WINDOWWIDTH, WINDOWHEIGHT)
)

pygame.display.set_caption('Mouse Tracker')