# Exercise: Build the Memory Game Foundation.
#
# This exercise tests two Pygame concepts:
# 1. Organizing game data.
# 2. Organizing code with functions.

# Instructions:

# Create a new Pygame program based on the two programs you just studied:
# - memory_game_data.py
# - memory_game_functions.py

# Your goal is to combine the ideas from both programs.

# ------------------------------------------------------------
# PART 1: SET UP PYGAME
# ------------------------------------------------------------

# Your program should:
# 1. Initialize Pygame.
# 2. Create an 800 x 600 window.
# 3. Set a window title.
# 4. Create a clock.
# 5. Run the game at 60 FPS.
# 6. Close when the player clicks the X button.

# ------------------------------------------------------------
# PART 2: CREATE GAME DATA
# ------------------------------------------------------------

# Create constants for these shapes:
# DONUT
# SQUARE
# DIAMOND
# LINES
# OVAL

# Create constants for these colors:
# RED
# GREEN
# BLUE
# YELLOW
# ORANGE
# PURPLE
# CYAN

# Group all colors into:
# ALLCOLORS

# Group all shapes into:
# ALLSHAPES

# Use tuples to store these groups of related values.

# ------------------------------------------------------------
# PART 3: CHECK THE BOARD REQUIREMENTS
# ------------------------------------------------------------

# Create these constants:
# BOARDWIDTH = 6
# BOARDHEIGHT = 4

# Use assert to make sure there are enough possible
# shape and color combinations for the board.

# The board will contain 24 boxes.

# ------------------------------------------------------------
# PART 4: CREATE draw_board()
# ------------------------------------------------------------

# Create a function named:
# draw_board()

# Inside this function:
# 1. Use a nested for loop.
# 2. Loop through the rows.
# 3. Loop through the columns.
# 4. Calculate each box's x position.
# 5. Calculate each box's y position.
# 6. Draw each box with pygame.draw.rect().

# Your board should contain:
# 6 columns
# 4 rows
# 24 boxes total

# Do not write 24 separate drawing commands.

# ------------------------------------------------------------
# PART 5: CREATE draw_message()
# ------------------------------------------------------------

# Create a function named:
# draw_message()

# Use this function to draw a rectangle above or below
# the game board.

# This rectangle will eventually become a message area.

# You do not need to display text yet.

# ------------------------------------------------------------
# PART 6: CREATE main()
# ------------------------------------------------------------

# Create a function named:
# main()

# Put the main game loop inside this function.

# Inside the game loop:
# 1. Check for Pygame events.
# 2. Handle pygame.QUIT.
# 3. Clear the screen.
# 4. Call draw_board().
# 5. Call draw_message().
# 6. Update the display.
# 7. Limit the frame rate to 60 FPS.

# ------------------------------------------------------------
# PART 7: USE THE MAIN GUARD
# ------------------------------------------------------------

# End your program with:

# if __name__ == "__main__":
#     main()

# Make the board display different colors based on position.

# For example:
# RED    BLUE   RED    BLUE   RED    BLUE
# BLUE   RED    BLUE   RED    BLUE   RED
# RED    BLUE   RED    BLUE   RED    BLUE
# BLUE   RED    BLUE   RED    BLUE   RED

# Use your row and column numbers to determine the color.

# Do not write 24 separate pygame.draw.rect() calls.

# ------------------------------------------------------------
# WHAT YOU SHOULD BE ABLE TO EXPLAIN
# ------------------------------------------------------------

# After completing the exercise, explain:

# 1. Why game data can be stored in constants.
# 2. Why related values can be grouped into tuples.
# 3. What assert checks in this program.
# 4. Why drawing code belongs inside functions.
# 5. Why nested loops are useful for game boards.
# 6. Why main() contains the game loop.
# 7. How main() calls the drawing functions.
# 8. Why pygame.display.update() is needed after drawing.

# The main lesson:

# Combine organized game data with organized functions.

# This is the foundation for building a real memory game.