"""Five-minute opening talk track for explaining the lesson 6 game changes.

Open this file to read the presentation script, or run it to print the script.
It is documentation only and does not edit main.py, player.py, or world.py.
"""

TALK_TRACK = r'''
FIRST FIVE MINUTES: WHY WE UPDATED THE GAME
===========================================

This is a spoken script. The timing is approximate; pause briefly to point at
the named files and code. The goal is to connect lesson 6's image concepts to
the way this project is organized, and explain the reason for each change.


0:00–0:45 | Connect the previous exercise to today's lesson
-----------------------------------------------------------
“In our previous exercise, we made the player an object. The object kept its
own position and size, updated its movement, stayed within the screen, and
drew itself. Today we keep that same idea, but replace its simple colored
rectangle with a real image. That means we need to prepare an image Surface,
preserve any transparent pixels, resize it for the game window, and draw it
in the correct place.”

“The important design idea is that the player's rules and appearance belong
with the Player, while the game loop coordinates the whole game. The world
continues to own the walls.”


0:45–1:50 | Explain player.py
-----------------------------
“Open player.py. Player now receives an image_path when it is created. It
still stores position as a Vector2, plus its size and speed. It also keeps a
pygame.Rect. That rectangle is the player's body for collision checks and
screen boundaries; it is not the picture itself.”

“The image is loaded in __init__, once when we create the player. Loading it
once avoids repeating disk work every frame. We call convert_alpha() because
the character image has transparent pixels. That keeps those pixels
transparent and prepares the Surface for the display's pixel format. Then
transform.scale() creates the display-sized version. Scaling is also done
once. We use scale for this pixel art so its hard edges stay crisp.”

“The update method still builds a direction from the arrow keys, normalizes
it so diagonal movement is not faster, and multiplies by speed and delta
time. It now receives the world's wall rectangles as well. It tries movement
on the X axis and then the Y axis, reverting an axis if the Rect overlaps a
wall. That separate-axis approach preserves the game's ability to slide
along a wall. At the end it clamps the position to the screen and syncs the
Rect, which keeps collision and drawing aligned.”

“Finally, draw uses surface.blit(self.sprite, self.rect.topleft). blit copies
the prepared Surface onto the game screen. The Rect supplies the sprite's
top-left position, so the sprite follows the same position used for
collisions. Its transparent pixels let the already-drawn background show
through.”


1:50–2:25 | Explain world.py
---------------------------
“world.py does not need a lesson 6 code change. It already has a clear job:
store the wall Rects and draw them. Those Rects are useful for collision, and
their draw method is useful for rendering. Keeping this responsibility in
World means Player can ask about walls without taking over how the level is
stored or drawn.”

“The draw order matters: main draws the world first, then the player. That
way the sprite appears over the scene, and transparent parts reveal the
background or whatever was drawn beneath them.”


2:25–3:40 | Explain main.py
--------------------------
“main.py imports Player and World. It creates the display before creating
the Player because convert_alpha() needs an established display format. It
builds the image path from Path(__file__).parent, then adds the lessons/assets
folder and the adventurer filename. This makes the path relative to main.py,
instead of depending on which working directory was used to launch Python.”

“The Player is created with its starting position, size, speed, and image
path. World is created separately. In the loop, main still handles events,
gets the pressed keys, calculates delta time, clears the screen, and flips
the display. It delegates player movement and collision to player.update(),
then delegates player rendering to player.draw(). It asks World to draw its
walls.”

“This keeps main focused on coordinating the frame, instead of repeating
player movement and collision details there. It also makes the player code
reusable and easier to change in one place.”


3:40–4:35 | Tie the project to lesson 6's four image steps
---------------------------------------------------------
“Here is the full image pipeline from the lesson. First, image.load reads
the file and returns a Surface in memory; it does not display it by itself.
Second, convert_alpha preserves alpha transparency and prepares the image
for the display. Third, transform.scale makes a new Surface at the intended
size while preserving pixel-art edges. Fourth, blit copies that prepared
Surface to the display at the player's Rect position.”

“We prepare the image once during Player creation, after the display exists.
During each frame we only update the position and blit the already-prepared
image. This separates setup work from repeated frame work.”


4:35–5:00 | Summary and transition
----------------------------------
“So each file has one clear role: Player owns player state, movement,
collision, and sprite drawing; World owns walls; main creates the display,
connects those objects, and runs the loop. The visible change is a sprite
instead of a rectangle. The underlying movement and collision behavior is
still supported by the Rect. Next, we can look at the loading, conversion,
scaling, and blitting calls in the code and see what each one changes.”


PRESENTER CHECK
===============
- Point out that the actual asset path in main.py is
  `lessons/assets/adventurer.jpeg` relative to the script's directory.
- Point out that player.py loads and scales the image once, not in update()
  or inside the main game loop.
- Point out that world.py is intentionally unchanged: it already provides
  both collision Rects and a draw method.
- Avoid saying that the sprite itself performs collision. The Rect handles
  collision; the sprite is the visual image drawn at the Rect's position.
'''


if __name__ == "__main__":
    print(TALK_TRACK)
