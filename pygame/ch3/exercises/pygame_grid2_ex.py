# TASK: Make the Grid Interactive

# You already built a 4x3 grid in the previous exercise.
# Now you are going to make the grid respond to the mouse.

# GOAL:
# When the mouse moves over a square, that square should
# become highlighted.

# You are NOT being given the implementation.
# Use the questions below to work out what code you need.

# REQUIREMENTS
# 1. Get the current mouse position.

# 2. Create a function that receives a pixel (x, y).

# 3. Inside that function, search through the entire board.

# 4. For each square, determine whether the mouse is inside it.

# 5. If the mouse is inside a square, return that square's
#    board coordinates:
#    box_x, box_y

# 6. If the mouse is not over any square, return:
#    None, None

# 7. Use the returned board coordinates to highlight the
#    square underneath the mouse.

# 8. The grid should continue working even when the mouse
#    moves from one square to another.

# ------------------------------------------------------------
# THE DATA FLOW
# ------------------------------------------------------------

# Mouse position
#       ↓
# Pixel coordinates
#       ↓
# Find the square containing those pixels
#       ↓
# Board coordinates
#       ↓
# Highlight that square

# QUESTION 1
# What information do we get from pygame.mouse.get_pos()?

# Expected:
# mouse_x, mouse_y

# QUESTION 2
# Is (mouse_x, mouse_y) a board coordinate or a pixel
# coordinate?

# Expected:
# Pixel coordinate.

# QUESTION 3
# How can we represent one square as a rectangle?

# Expected:
# pygame.Rect(...)

# QUESTION 4
# How can we ask Pygame whether the mouse is inside
# that rectangle?

# Expected:
# rect.collidepoint(x, y)

# QUESTION 5
# Once we find the rectangle containing the mouse, what
# should the function return?

# Expected:
# box_x, box_y

# QUESTION 6
# What should the function return if it doesn't find a
# square containing the mouse?

# Expected:
# None, None

# Try to solve the problem yourself before looking anything up.

# You already have most of the pieces:
# - board coordinates
# - pixel coordinates
# - nested loops
# - pygame.Rect
# - functions
# - pygame events

# Your job is to connect those pieces together.


# Your program should behave like this:
#     Mouse outside grid -> no square highlighted.
#     Mouse over a square -> that square is highlighted.
#     Mouse moves to another square -> the highlight moves.
#     Mouse leaves the grid -> the highlight disappears.

# Try to make the highlighted square use a different color
# without changing the color of the other squares.