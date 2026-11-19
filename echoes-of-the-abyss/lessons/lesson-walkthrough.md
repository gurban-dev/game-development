# Lesson 7: Pixel Art Awakens — 20-minute teaching walkthrough

This guide follows [`lesson7.py`](lesson7.py), a small Pygame program that
loads and displays an image, compares image conversion, demonstrates alpha
transparency, scales an image, and blits images onto the screen. It runs on its
own; it does not launch the game.

## Before the lesson

Open a terminal in the project folder and run:

```bash
python lessons/lesson7.py
```

The lesson uses `lessons/assets/adventurer.jpeg`, which is already in the
project. It does not create or save any image files. The asset is a JPEG, so it
has no transparency. The program makes a separate transparent Surface in
memory to demonstrate alpha.

Keep these four ideas in view throughout the lesson:

1. `pygame.image.load(path)` reads an image into a Surface.
2. `.convert_alpha()` prepares a Surface for display while retaining alpha
   transparency that the original image has.
3. `pygame.transform.scale(surface, size)` makes a resized Surface.
4. `surface.blit(image, position)` draws one Surface onto another.

## 0–3 minutes: Introduce Surfaces and image loading

Start the program and point to the character and the two comparison panels.
Ask: “Does loading an image make it appear on screen?” Let them observe that
the answer is no: loading creates image data in memory, but the program must
still draw that data.

Explain that a Pygame `Surface` is a rectangular area of pixels. The display
is a Surface, a loaded image is a Surface, and rendered text is also a Surface.
Pygame can draw one Surface onto another, which is why images and text both use
`blit()` later.

In `main()`, point to:

```python
screen = pygame.display.set_mode((screen_width, screen_height))
```

This creates the display Surface and chooses its pixel format. The image is
loaded later, after the display exists, because `convert_alpha()` uses the
display format.

## 3–6 minutes: Explain the asset path

Point to the `Path` import and these lines:

```python
asset_directory = Path(__file__).parent / "assets"
adventurer_path = asset_directory / "adventurer.jpeg"
```

Explain each part in plain language:

- `__file__` means “the path to this Python file.”
- `.parent` means “the folder containing this Python file.”
- `/ "assets" / "adventurer.jpeg"` joins folder and file names into a path.

So the program looks for the image beside the lesson file, in its `assets`
folder. A plain path such as `"assets/adventurer.jpeg"` is interpreted from
the terminal's current folder. It may work from one launch location and fail
from another. The `__file__` path avoids that dependency.

Ask: “If we move the terminal to a different folder before launching this
script, where will this path still begin?” Answer: in the folder containing
`lesson7.py`.

## 6–10 minutes: Compare `convert()` and `convert_alpha()`

Point to:

```python
original_image = pygame.image.load(adventurer_path)
opaque_converted = original_image.convert()
alpha_converted = original_image.convert_alpha()
```

Explain that both methods create display-ready Surfaces. `convert()` is for
images that do not need per-pixel transparency. `convert_alpha()` preserves
per-pixel alpha when the source contains it. A pixel's alpha controls how
transparent that pixel is: fully clear pixels reveal what is underneath,
partly clear pixels blend with it, and opaque pixels cover it.

Point out that the two image panels look alike in this program. This is
intentional: the source is JPEG, and JPEG cannot store alpha transparency.
Calling `convert_alpha()` cannot invent transparency that the file did not
contain. For a character image with a transparent background, the source
asset must itself use a format that supports alpha, such as PNG.

This distinction prevents a common misunderstanding: `convert_alpha()` keeps
the source image's alpha; it is not a background-removal tool.

## 10–13 minutes: Demonstrate alpha on an in-memory Surface

Point to `make_alpha_example()`:

```python
transparent_layer = pygame.Surface(size, pygame.SRCALPHA)
```

Explain that `pygame.SRCALPHA` creates a Surface with per-pixel alpha. The
circle is drawn using four color values: red, green, blue, and alpha. The
circle uses alpha `150`, so it is partly transparent. The untouched corners
have alpha `0`, so they are completely transparent.

The program first draws a magenta panel and then blits this Surface onto it.
The clear corners leave the panel visible; the circle blends with the panel.
The opaque diamond in the same Surface has alpha `255`, so it covers what is
under it. This example is drawn in memory and is not saved as an image file.

Ask: “Why can we see magenta at the corners? Why does the circle look mixed
with magenta?” Connect both answers to the alpha value of those pixels.

## 13–16 minutes: Explain scaling

Point to the sprite preparation:

```python
player_sprite = pygame.transform.scale(alpha_converted, (96, 78))
```

`transform.scale()` returns a new Surface at the requested width and height.
It changes the in-memory version used by the game; it does not change the
file on disk. The program also makes small and large previews so the size
difference is easy to see.

For pixel art, ordinary `scale()` keeps hard pixel edges rather than blending
neighboring pixels. Scaling by whole-number multiples usually gives the most
even-looking enlarged pixels. The example asset is not square, so the player
image is scaled to a roughly matching aspect ratio instead of forced into a
square.

Mention that resizing is setup work. The player sprite and the two preview
Surfaces are prepared before the game loop, rather than loading or scaling
those versions again on every frame. There is one useful optimization to
notice: the two conversion-comparison panels call `transform.scale()` inside
the draw loop. Since their size never changes, those two scaled copies could
also be prepared once before the loop. Use that as an example of spotting
repeat work; it does not change what the demo teaches about scaling.

## 16–18 minutes: Explain `blit()` and draw order

Point to a call such as:

```python
screen.blit(player_sprite, player_rect.topleft)
```

The first argument is the Surface being copied. The second is the destination
position on the screen. `player_rect.topleft` gives the image's current
top-left coordinates. The rectangle tracks movement; the sprite supplies the
picture.

Explain drawing order as layers: the program fills the background, draws
panels and the floor, and then blits the character. Later drawing appears on
top of earlier drawing. For the alpha example, drawing the magenta panel
before the transparent Surface gives its clear pixels something to reveal.
If the panel were drawn after the alpha Surface, it would cover the example.

## 18–20 minutes: Let them try it and recap

Have them move the character with the arrow keys. Ask them to identify the
four image steps in order and describe what each does:

```text
image.load → convert_alpha → transform.scale → blit
```

Finish with these checks:

- Does `image.load()` draw the image? No; it creates a Surface in memory.
- Can `convert_alpha()` make a JPEG transparent? No; the source needs alpha.
- Does `transform.scale()` edit the image file? No; it creates a new Surface.
- What decides which image appears in front? The order of drawing and blitting.

## Code landmarks for questions

| Concept | Find it in `lesson7.py` | Beginner explanation |
| --- | --- | --- |
| Reliable asset path | `Path(__file__).parent / "assets"` | Start looking beside this script. |
| Load image | `pygame.image.load(adventurer_path)` | Read pixels into a Surface. |
| Keep source alpha | `original_image.convert_alpha()` | Preserve existing transparency for display. |
| Opaque conversion | `original_image.convert()` | Prepare an image that does not need alpha. |
| Make a transparent layer | `pygame.Surface(size, pygame.SRCALPHA)` | Create an in-memory Surface with alpha. |
| Draw resized image | `pygame.transform.scale(...)` | Return a Surface at the chosen dimensions. |
| Draw a Surface | `screen.blit(...)` | Copy its pixels to a destination Surface. |
| Show the finished frame | `pygame.display.flip()` | Present the newly drawn screen. |

## One small code detail to point out

`load_scaled_image()` at the top of the lesson file packages image loading,
alpha conversion, and scaling into one helper. The demonstration also shows
those calls separately in `main()` to compare `convert()` with
`convert_alpha()`. The helper is available as a reusable pattern even though
the comparison needs the individual steps written out. The two scaled copies
used for that comparison are currently created inside the loop; they could
be moved to setup to avoid repeating the work each frame.
