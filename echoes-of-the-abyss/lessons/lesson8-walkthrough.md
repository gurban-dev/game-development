# Lesson 8: Git Checkpoint and Project Structure

## Lesson format

- **Teach:** 30 minutes
- **Project implementation:** 15 minutes
- **Main project change:** Convert `Player` into a `pygame.sprite.Sprite` and
  manage it through a `pygame.sprite.Group`.

“We’re going to use the project structure that is already here and make one
focused change: we’ll connect the Player to Pygame’s Sprite and Group system.
As we do that, we’ll look at how the files import and use one another, and
why each file has a particular job. We’ll keep the player’s movement and wall
collision working, then save the finished change as a Git checkpoint.”

“We’ll also look at functions and methods in the code that is already here.
We won’t move the whole game loop into a new `main()` function today. That
could be a useful separate refactor, but our project time is for the Sprite
and Group change.”

## What the learner should understand

By the end of the teaching portion, the learner should be able to explain:

- A Python file is a module, and imports let one module use names defined in
  another.
- A function names a task; a method is a function that belongs to a class.
- Each project module has a clear job: `main.py` creates the display and
  game objects, handles the frame loop, and chooses the drawing order;
  `player.py` defines the player's image, movement, and collision behavior;
  `world.py` stores the wall rectangles and draws them.
- A `pygame.sprite.Sprite` exposes an `image` and a `rect` for a
  `pygame.sprite.Group` to draw.
- A sprite group does not automatically handle wall collision.
- Git status, diff, staging, and committing help make a reviewable checkpoint.

## Teach: 30 minutes

### 0–5 minutes: Map the project

Let’s start with the project files. A module is a Python file that contains
code the rest of the program can use. We already have separate modules for
the game loop, the player, and the world.

`main.py` creates the display, creates the Player and World objects, handles
keyboard and window events, tells the player when to update, and decides what
to draw and in what order. `player.py` defines the Player: its image, its
movement, and the rectangle used to keep it inside the screen and check it
against walls. `world.py` stores the wall rectangles and draws those walls.
That is why we’ll make the Sprite changes in `player.py` and `main.py`; the
wall setup in `world.py` already has its own clear place.

Here in `main.py`, these imports bring the Player and World class names into
this file:

```python
from player import Player
from world import World
```

The definitions stay in `player.py` and `world.py`. The imports let `main.py`
create those objects and call their methods without putting all their code
in one file. A function is a named set of instructions. When a function
belongs to a class, we call it a method. For example, `Player.update()` moves
the player, `Player.draw()` draws the player image, and `World.draw()` draws
the walls. The main loop calls these methods at the right time in each frame.

### 5–10 minutes: Explain responsibility and refactoring

Let’s follow one frame in `main.py`:

```python
player.update(keys, dt, WIDTH, HEIGHT, world.walls)
screen.fill(BACKGROUND_COLOR)
world.draw(screen)
player.draw(screen)
pygame.display.flip()
```

`main.py` reads the keyboard and measures how much time has passed. It passes
the keys and time to `Player.update()`, which changes the player's location
and checks the wall rectangles supplied by `World`. Then `main.py` clears
the screen, asks `World.draw()` to draw the walls, asks `Player.draw()` to
draw the player, and updates the display.

This is an example of each file doing a particular job. Refactoring means
reorganizing code to make those jobs clearer or to support a new feature. We
already have the Player and World in their own files. Today we’ll keep that
structure and change how Pygame can manage and draw the Player.

In Lesson 7, we also saw named functions such as `load_scaled_image()`.
That function groups the image-loading steps under one name. Here,
`Player.update()` and `Player.draw()` are methods that give the player's
movement and drawing their own named places.

### 10–18 minutes: Teach `pygame.sprite.Sprite` and `Group`

A Pygame Sprite is a game object that can be managed by sprite groups. For
a group to draw a sprite, it looks for two standard attributes: `image`, the
picture to draw, and `rect`, the rectangle that gives its position. Our
Player already has an image stored as `self.sprite` and a collision
rectangle stored as `self.rect`. We will rename the image attribute to
`self.image` so the group can find it.

In `player.py`, the class declaration and setup will look like this:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed, image_path):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.speed = speed

        loaded_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(loaded_image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
```

`super().__init__()` runs the setup for the Pygame Sprite class that Player
is building on. `get_rect()` makes a rectangle the same size as the image
and places it at the starting location. We keep that rectangle because
`Player.update()` uses it to stay inside the screen and to check whether the
player overlaps a wall. The Group will use that same rectangle to position
the image.

Making Player inherit from Sprite does not give it wall collision. The
collision behavior stays in our existing `Player.update()` method. Sprite
gives us a standard way to group and draw game objects.

### 18–23 minutes: Trace the group in main.py

After `main.py` creates the player, we’ll put it in a group like this:

```python
all_sprites = pygame.sprite.Group(player)
```

A Group is a container for sprites. `all_sprites.update(...)` calls each
member's `update()` method with the arguments we provide. Our Player update
method already takes these arguments, so the group can forward the keyboard
state, elapsed time, screen size, and wall rectangles. In each frame, the
group passes the same keys, elapsed time, screen dimensions, and wall
rectangles that `Player.update()` already uses:

```python
all_sprites.update(keys, dt, WIDTH, HEIGHT, world.walls)
```

For drawing, we keep the world first, then draw the group:

```python
screen.fill(BACKGROUND_COLOR)
world.draw(screen)
all_sprites.draw(screen)
```

`Group.draw()` looks at each Sprite's `image` and `rect` to draw it in the
right place. We draw the World first, then the Group, so the player appears
over the walls and floor. There is only one sprite in the group right now,
but this same group can hold more characters or objects later.

### 23–26 minutes: Explain the Git checkpoint

Git keeps named checkpoints of changes. We will inspect the current state,
make one focused refactor, review exactly what is staged, and commit the
working result. A commit records staged changes; it does not automatically
include every file in the folder.

Before we make changes, these commands show the current state:

```bash
git status --short
git diff -- main.py player.py world.py
```

`git status` tells us which files have changed and which are new.
`git diff` shows edits to tracked files. If there are other changes in the
project, we’ll look at them before deciding what belongs in this checkpoint.

### 26–30 minutes: Preview the implementation

In the implementation time, we will make a small set of connected edits.
In `player.py`, Player will inherit from Sprite, the image will be named
`self.image`, and the existing rectangle will keep handling collision. In
`main.py`, we will put the player in a Group, update it through the Group,
and use the Group to draw it. We will leave `world.py` alone. Then we will
run the game, review the diff, stage only these project files, and commit.

Before we start, tell me which file defines the player's movement and
collision behavior, which file stores and draws the walls, and which file
handles input and decides the order of updates and drawing. The answers are
`player.py`, `world.py`, and `main.py`.

## Project implementation: 15 minutes

Keep this work limited to `player.py` and `main.py`. `world.py` should not
need an edit for this refactor.

### Minutes 0–2: Inspect the starting state

Have the learner open `player.py` and `main.py`, then run:

```bash
git status --short
```

Point out existing changes before editing. Explain that the new checkpoint
should contain the Sprite and Group refactor, not unrelated work.

### Minutes 2–7: Make Player a Sprite in player.py

Have the learner:

1. Change the class declaration to inherit from `pygame.sprite.Sprite`.
2. Call `super().__init__()` at the start of `Player.__init__()`.
3. Keep `position`, `size`, and `speed` because movement still uses them.
4. Store the loaded and scaled image in `self.image` instead of
   `self.sprite`.
5. Create `self.rect` from the image with its starting top-left location.
6. Keep `Player.update()` and its wall collision checks.
7. Remove `Player.draw()` because the Group will draw the image.

Use this target for the setup portion:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed, image_path):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.size = size
        self.speed = speed
        loaded_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(loaded_image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
```

Explain that the existing update method must continue syncing `self.rect`
after movement and collision resolution. Without that, the group would draw
the image at an out-of-date location and wall checks would use an out-of-date
box.

### Minutes 7–11: Add and use a Group in main.py

Immediately after `player` is created, add:

```python
all_sprites = pygame.sprite.Group(player)
```

Replace the direct update call with:

```python
all_sprites.update(keys, dt, WIDTH, HEIGHT, world.walls)
```

In the drawing section, keep the world first and replace
`player.draw(screen)` with:

```python
world.draw(screen)
all_sprites.draw(screen)
```

The group calls the Player's update method and draws its image using
`image` and `rect`. The World still draws walls; the Player still checks
collisions with those wall rectangles.

### Minutes 11–13: Review the behavior

Have the learner run `python main.py` and check that:

- the player image appears;
- arrow-key movement still works;
- the player stays inside the screen;
- the player cannot pass through the wall;
- the world is drawn before the player.

If a check fails, inspect the names first: the group needs `self.image` and
`self.rect`, and the update call needs to pass the same arguments that
`Player.update()` expects.

### Minutes 13–15: Review and commit

Run:

```bash
git status --short
git diff -- main.py player.py world.py
```

Review the diff together. Confirm that the change is limited to the Player
Sprite conversion and Group use, and that `world.py` did not need editing.
Then stage and commit the intended files:

```bash
git add main.py player.py
git diff --cached
git commit -m "use a sprite group for the player"
```

If Git reports there is nothing to commit or shows unexpected files, stop
and inspect `git status --short` before continuing.

## End-of-lesson check

Ask the learner to explain these in their own words, using the open files as
reference:

1. Why do `main.py`, `player.py`, and `world.py` have separate jobs?
2. What does importing `Player` let `main.py` do?
3. Why does a Group need `image` and `rect` on each sprite?
4. Where does wall collision still happen, and why is that unchanged?
5. What does the Git commit record?

The learner does not need to memorize the API names. The goal is to connect
the names to their role in this project and to explain where the next change
belongs.

## Optional extension for a later session

The current `main.py` starts the game at the module's top level. A separate
refactor could move startup and the loop into `main()` and add an
`if __name__ == "__main__":` guard. That makes importing the module safer,
but it is intentionally outside this 15-minute Sprite and Group exercise.

## References

- [Pygame Sprite and Group reference](https://www.pygame.org/docs/ref/sprite.html)
- [Pygame Sprite module introduction](https://www.pygame.org/docs/tut/SpriteIntro.html)
