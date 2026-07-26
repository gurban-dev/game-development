"""
Exercise: Build A Moving Player Box

Goal:
Create a blue square that:
- Moves with arrow keys.
- Cannot leave the screen.
- Updates smoothly.

Concepts Reinforced:
- Coordinates
- Velocity
- Game loop
- Input handling
- Rendering
- Input -> update -> draw structure

Instructions:
1. Run the starter code.
2. Make the player move:
    - Left
    - Right
    - Up
    - Down
3. Prevent the player from leaving the screen boundaries.
4. Test your movement in all directions.

Hints:
- Moving left means decreasing x.
- Moving right means increasing x.
- Moving up means decreasing y.
- Moving down means increasing y.

Example movement logic:
    x -= speed
    x += speed
    y -= speed
    y += speed

Boundary Logic:
- The player should never move outside the window.
- Keep x and y within valid screen coordinates.

Optional Bonus Challenges:
1. Change the square color while moving.
2. Add sprinting with Shift.
3. Allow smooth diagonal movement.

Main Learning Goal:
The objective is not memorising pygame method names.
The objective is understanding how game state changes
over time inside a game loop.
"""