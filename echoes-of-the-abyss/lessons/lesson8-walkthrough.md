# Lesson 8: Git Checkpoint and Project Structure

## Lesson format

- **Teach:** 30 minutes
- **Project implementation:** 15 minutes
- **Main project change:** Convert `Player` into a `pygame.sprite.Sprite` and
  manage it through a `pygame.sprite.Group`.

This lesson focuses the project work on one refactor that demonstrates
modules, imports, methods, responsibilities, and the Pygame sprite system.
The project already has separate `main.py`, `player.py`, and `world.py`
modules, so do not split it into more files just to practice file creation.
The learner will preserve movement and wall collision, then commit the
working milestone.

The 15-minute implementation does **not** move all of `main.py` into a new
`main()` function. Explain what functions and methods do using the existing
code. Making startup import-safe is a useful later refactor, but combining it
with the Sprite conversion would make this project task too large for the
allotted time.

## What the learner should understand

By the end of the teaching portion, the learner should be able to explain:

- A Python file is a module, and imports let one module use names defined in
  another.
- A function names a task; a method is a function that belongs to a class.
- Each project module has a responsibility: `main.py` coordinates,
  `player.py` owns the player, and `world.py` owns walls.
- A `pygame.sprite.Sprite` exposes an `image` and a `rect` for a
  `pygame.sprite.Group` to draw.
- A sprite group does not automatically handle wall collision.
- Git status, diff, staging, and committing help make a reviewable checkpoint.

## Teach: 30 minutes

### 0–5 minutes: Map the project

Open the project tree and say:

“We already have a useful module structure. A module is a Python file that
contains code we can define and use. `main.py` starts and coordinates the
game. `player.py` defines the player. `world.py` defines the walls and draws
them. `update.py` contains presenter notes; the game does not import it, so
it is not part of the running game.”

Point to these lines in `main.py`:

```python
from player import Player
from world import World
```

Say:

“These imports make the `Player` and `World` names available here. Their
class definitions stay in their own files, so `main.py` can create and
coordinate the objects without containing every detail of their behavior.”

Ask the learner to find `Player.__init__()`, `Player.update()`,
`Player.draw()`, `World.__init__()`, and `World.draw()`. Explain that these
are methods: functions attached to a class. The main loop calls methods on
the objects it created.

### 5–10 minutes: Explain responsibility and refactoring

Trace the current frame in `main.py`:

```python
player.update(keys, dt, WIDTH, HEIGHT, world.walls)
screen.fill(BACKGROUND_COLOR)
world.draw(screen)
player.draw(screen)
pygame.display.flip()
```

Say:

“`main.py` gathers input and time, then delegates player behavior to the
Player and wall drawing to the World. Refactoring means changing the
organization of code to make responsibilities clearer or to support the
next feature. We are not moving code into extra files today. We are changing
how the existing Player connects to Pygame's sprite system.”

Point out that `lesson7.py` also uses functions such as
`load_scaled_image()` and `draw_alpha_demo()` to give a named piece of work a
clear place. In this project, `Player.update()` and `Player.draw()` already
separate player behavior from the main loop.

### 10–18 minutes: Teach `pygame.sprite.Sprite` and `Group`

Say:

“A Pygame Sprite is a game object that can be managed by sprite groups. For
a group to draw a sprite, it looks for two standard attributes: `image`, the
picture to draw, and `rect`, the rectangle that gives its position. Our
Player already has an image stored as `self.sprite` and a collision
rectangle stored as `self.rect`. We will rename the image attribute to
`self.image` so the group can find it.”

Show this target shape for `player.py`:

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

Explain `super().__init__()` as the setup call for the Sprite base class.
The `get_rect()` call creates a rectangle matching the image dimensions and
places it at the starting position. Keeping the rectangle is important:
the current `Player.update()` uses it for screen limits and
`colliderect()` wall checks. The sprite group will also use it to position
the image.

Say:

“Making Player inherit from Sprite does not give it wall collision. The
collision behavior stays in our existing `Player.update()` method. Sprite
gives us a standard way to group and draw game objects.”

### 18–23 minutes: Trace the group in main.py

Explain that after creating `player`, `main.py` will create a group:

```python
all_sprites = pygame.sprite.Group(player)
```

Say:

“A Group is a container for sprites. `all_sprites.update(...)` calls each
member's `update()` method with the arguments we provide. Our Player update
method already takes these arguments, so the group can forward the keyboard
state, elapsed time, screen size, and wall rectangles.”

Show the update call:

```python
all_sprites.update(keys, dt, WIDTH, HEIGHT, world.walls)
```

Then show the drawing calls:

```python
screen.fill(BACKGROUND_COLOR)
world.draw(screen)
all_sprites.draw(screen)
```

Explain that `Group.draw()` uses each sprite's `image` and `rect`. The World
remains separate and is drawn first, so the player is drawn over the world.
For this lesson there is only one sprite, but the same calls can manage more
sprites later.

### 23–26 minutes: Explain the Git checkpoint

Say:

“Git keeps named checkpoints of changes. We will inspect the current state,
make one focused refactor, review exactly what is staged, and commit the
working result. A commit records staged changes; it does not automatically
include every file in the folder.”

Show the commands, but do not commit before the learner has made and reviewed
the changes:

```bash
git status --short
git diff -- main.py player.py world.py
```

Explain that `status` shows changed and untracked files, while `diff` shows
changes to tracked files. If the project already has unrelated changes,
identify them before choosing what belongs in this checkpoint.

### 26–30 minutes: Preview the implementation

Say:

“In the implementation time, we will make a small set of connected edits.
In `player.py`, Player will inherit from Sprite, the image will be named
`self.image`, and the existing rectangle will keep handling collision. In
`main.py`, we will put the player in a Group, update it through the Group,
and use the Group to draw it. We will leave `world.py` alone. Then we will
run the game, review the diff, stage only these project files, and commit.”

Ask the learner to repeat the roles: Which file owns the player? Which file
owns walls? Which file coordinates a frame? Answer together if needed:
`player.py`, `world.py`, and `main.py` respectively.

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
