# Task: Build a 4x3 Pygame grid

# Pygame concepts:
# - Use Pygame constants to define window and grid dimensions.
# - Understand board coordinates versus pixel coordinates.
# - Write a function that converts board coordinates to pixel coordinates.
# - Use nested loops to visit every position in a 2D grid.
# - Use pygame.draw.rect() to draw squares on the screen.
# - Use a main loop to continuously redraw the Pygame window.
# - Process the pygame.QUIT event so the window can close correctly.
# - Use pygame.display.update() to display each completed frame.
# - Get the current mouse position with pygame.mouse.get_pos().
# - Convert pixel coordinates into board coordinates.

# Create a Pygame program that displays a 4-column by 3-row grid.

# Each square should be 60x60 pixels with a 10-pixel gap.

# Create a function that converts board coordinates into pixel coordinates.

# Create another function that uses nested loops to draw every square.

# Then, determine which column and row the mouse is currently hovering over.
# Print the column and row to the terminal.

# The mouse position should be checked continuously while the program runs.

# For example, if the mouse is hovering over the second column and first row,
# print:
# Column: 1, Row: 0

# Remember that board coordinates start at 0.

# Do not add mouse clicking or highlighting yet.

# Requirements:
# Window: 400 x 400 pixels
# Board: 4 columns x 3 rows
# Box size: 60 pixels
# Gap size: 10 pixels
# Background: any color
# Box: any color