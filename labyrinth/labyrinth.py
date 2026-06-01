"""
Circular Labyrinth — Playable
Player starts at the centre and must navigate to the exit on the outer ring.
Arrow keys: Up = outward, Down = inward, Left/Right = rotate around the ring.
"""

import math
import random
import tkinter as tk
from tkinter import font as tkfont

# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────
RINGS       = 9
SEED        = None
CANVAS_SIZE = 820
WALL_WIDTH  = 2
BG_COLOR    = "#0d0d0d"
WALL_COLOR  = "#e8e8e8"
PLAYER_COLOR = "#f0c040"
TRAIL_COLOR  = "rgba(240,192,64,0.15)"
EXIT_COLOR  = "#e74c3c"
VISITED_COLOR = "#1a3a1a"


# ──────────────────────────────────────────────
# Ring sizing
# ──────────────────────────────────────────────
def cells_in_ring(ring: int) -> int:
    if ring == 0:
        return 8
    base = 8
    multiplier = 2 ** (ring // 3)
    return base * multiplier


# ──────────────────────────────────────────────
# Maze generation — recursive backtracker
# ──────────────────────────────────────────────
def build_maze(num_rings: int, rng: random.Random):
    sizes = [cells_in_ring(r) for r in range(num_rings)]
    visited = set()
    passages = set()

    def dfs(ring, sector):
        visited.add((ring, sector))
        s = sizes[ring]
        adj = []

        # clockwise neighbour
        ns = (sector + 1) % s
        adj.append((('cw', ring, sector), (ring, ns)))
        # counter-clockwise neighbour
        ps = (sector - 1) % s
        adj.append((('cw', ring, ps), (ring, ps)))
        # inward
        if ring > 0:
            s_inner = sizes[ring - 1]
            ratio = s_inner / s
            inner_sec = int(sector * ratio) % s_inner
            adj.append((('out', ring - 1, inner_sec), (ring - 1, inner_sec)))
        # outward
        if ring < num_rings - 1:
            s_outer = sizes[ring + 1]
            ratio = s_outer / s
            base = int(sector * ratio)
            for k in range(int(ratio)):
                outer_sec = (base + k) % s_outer
                adj.append((('out', ring, sector), (ring + 1, outer_sec)))

        rng.shuffle(adj)
        for wall, (nr, ns2) in adj:
            if (nr, ns2) not in visited:
                passages.add(wall)
                dfs(nr, ns2)

    import sys
    sys.setrecursionlimit(100_000)
    dfs(0, 0)
    return passages, sizes


# ──────────────────────────────────────────────
# Drawing helpers
# ──────────────────────────────────────────────
def draw_arc_points(cx, cy, r, a_start, a_end):
    """Return flat list of points for a polyline arc."""
    if r <= 0:
        return []
    steps = max(4, int(abs(a_end - a_start) * r / 3))
    pts = []
    for i in range(steps + 1):
        a = a_start + (a_end - a_start) * i / steps
        pts.append(cx + r * math.cos(a))
        pts.append(cy - r * math.sin(a))
    return pts


def draw_arc(canvas, cx, cy, r, a_start, a_end, color, width=WALL_WIDTH):
    pts = draw_arc_points(cx, cy, r, a_start, a_end)
    if len(pts) >= 4:
        canvas.create_line(pts, fill=color, width=width,
                           smooth=False, capstyle=tk.ROUND)


def cell_center_xy(ring, sector, sizes, cx, cy, ring_w):
    """Return pixel centre of a cell."""
    s = sizes[ring]
    arc_span = 2 * math.pi / s
    angle = (sector + 0.5) * arc_span
    r = (ring + 0.5) * ring_w
    return cx + r * math.cos(angle), cy - r * math.sin(angle)


# ──────────────────────────────────────────────
# Draw the static maze onto a canvas layer
# ──────────────────────────────────────────────
def draw_maze_walls(canvas, passages, sizes, cx, cy, outer_r, exit_sector):
    num_rings = len(sizes)
    ring_w = outer_r / num_rings

    for ring in range(num_rings):
        s = sizes[ring]
        inner_r = ring * ring_w
        outer_r2 = (ring + 1) * ring_w
        arc_span = 2 * math.pi / s

        for sector in range(s):
            a0 = sector * arc_span
            a1 = (sector + 1) * arc_span

            # Outer arc wall
            is_outermost = (ring == num_rings - 1)
            is_exit = is_outermost and sector == exit_sector
            wall_out = ('out', ring, sector)

            if is_outermost and not is_exit:
                draw_arc(canvas, cx, cy, outer_r2, a0, a1, WALL_COLOR)
            elif not is_outermost and wall_out not in passages:
                draw_arc(canvas, cx, cy, outer_r2, a0, a1, WALL_COLOR)

            # Radial (spoke) wall at the clockwise edge
            wall_cw = ('cw', ring, sector)
            if wall_cw not in passages:
                x1 = cx + inner_r * math.cos(a1)
                y1 = cy - inner_r * math.sin(a1)
                x2 = cx + outer_r2 * math.cos(a1)
                y2 = cy - outer_r2 * math.sin(a1)
                canvas.create_line(x1, y1, x2, y2,
                                   fill=WALL_COLOR, width=WALL_WIDTH,
                                   capstyle=tk.ROUND)

    # Inner boundary circle
    canvas.create_oval(cx - ring_w, cy - ring_w,
                       cx + ring_w, cy + ring_w,
                       outline=WALL_COLOR, width=WALL_WIDTH)

    # Exit marker arrow on outer edge
    arc_span_outer = 2 * math.pi / sizes[-1]
    am = (exit_sector + 0.5) * arc_span_outer
    ex = cx + (outer_r + 14) * math.cos(am)
    ey = cy - (outer_r + 14) * math.sin(am)
    canvas.create_text(ex, ey, text="◀EXIT▶" if math.cos(am) < 0 else "▶EXIT◀",
                       fill=EXIT_COLOR, font=("Courier", 9, "bold"))


# ──────────────────────────────────────────────
# Game state + movement
# ──────────────────────────────────────────────
class Game:
    def __init__(self, canvas, passages, sizes, cx, cy, outer_r, exit_sector, root, seed):
        self.canvas    = canvas
        self.passages  = passages
        self.sizes     = sizes
        self.cx        = cx
        self.cy        = cy
        self.outer_r   = outer_r
        self.ring_w    = outer_r / len(sizes)
        self.exit_sector = exit_sector
        self.root      = root
        self.seed      = seed
        self.num_rings = len(sizes)

        # Player state (ring, sector) — start at centre
        self.ring   = 0
        self.sector = 0
        self.moves  = 0
        self.won    = False
        self.visited = {(0, 0)}

        self.player_item  = None
        self.trail_items  = []
        self.status_item  = None
        self._draw_player()
        self._update_status()

    # ── Player rendering ──────────────────────────────────────────────────
    def _player_xy(self):
        return cell_center_xy(self.ring, self.sector,
                              self.sizes, self.cx, self.cy, self.ring_w)

    def _draw_player(self):
        if self.player_item:
            self.canvas.delete(self.player_item)
        # Draw trail for visited cells
        for item in self.trail_items:
            self.canvas.delete(item)
        self.trail_items = []

        for (r, s) in self.visited:
            px, py = cell_center_xy(r, s, self.sizes, self.cx, self.cy, self.ring_w)
            item = self.canvas.create_oval(px-3, py-3, px+3, py+3,
                                           fill="#2a4a2a", outline="")
            self.trail_items.append(item)

        px, py = self._player_xy()
        r = max(5, self.ring_w * 0.32)
        self.player_item = self.canvas.create_oval(
            px - r, py - r, px + r, py + r,
            fill=PLAYER_COLOR, outline="#fff8dc", width=2)

    def _update_status(self):
        if self.status_item:
            self.canvas.delete(self.status_item)
        if self.won:
            txt = f"🎉  ESCAPED!  Moves: {self.moves}   |   Seed: {self.seed}"
            color = "#f0c040"
        else:
            txt = f"Moves: {self.moves}   |   Ring: {self.ring+1}/{self.num_rings}   |   Seed: {self.seed}   |   Arrows to move"
            color = "#888888"
        self.status_item = self.canvas.create_text(
            10, CANVAS_SIZE - 20, anchor="sw",
            text=txt, font=("Courier", 11), fill=color)

    # ── Movement logic ────────────────────────────────────────────────────
    def _can_go_outward(self):
        """Can player move from current cell to the next ring outward?"""
        ring, sector = self.ring, self.sector
        # Special: outermost ring + exit sector = win
        if ring == self.num_rings - 1:
            return sector == self.exit_sector
        wall = ('out', ring, sector)
        return wall in self.passages

    def _can_go_inward(self):
        """Can player move from current cell inward one ring?"""
        ring, sector = self.ring, self.sector
        if ring == 0:
            return False
        s_inner = self.sizes[ring - 1]
        s_cur   = self.sizes[ring]
        ratio   = s_inner / s_cur
        inner_sec = int(sector * ratio) % s_inner
        wall = ('out', ring - 1, inner_sec)
        return wall in self.passages

    def _can_go_cw(self):
        """Clockwise (increasing sector index)."""
        wall = ('cw', self.ring, self.sector)
        return wall in self.passages

    def _can_go_ccw(self):
        """Counter-clockwise."""
        s   = self.sizes[self.ring]
        prev = (self.sector - 1) % s
        wall = ('cw', self.ring, prev)
        return wall in self.passages

    def move(self, direction):
        if self.won:
            return
        ring, sector = self.ring, self.sector
        moved = False

        if direction == 'out' and self._can_go_outward():
            if ring == self.num_rings - 1 and sector == self.exit_sector:
                # WIN
                self.moves += 1
                self.won = True
                self._show_win()
                return
            # Map to outward ring — player lands in the first matching outer sector
            s_outer = self.sizes[ring + 1]
            s_cur   = self.sizes[ring]
            ratio   = s_outer / s_cur
            new_sec = int(sector * ratio) % s_outer
            self.ring   = ring + 1
            self.sector = new_sec
            moved = True

        elif direction == 'in' and self._can_go_inward():
            s_inner   = self.sizes[ring - 1]
            s_cur     = self.sizes[ring]
            ratio     = s_inner / s_cur
            new_sec   = int(sector * ratio) % s_inner
            self.ring   = ring - 1
            self.sector = new_sec
            moved = True

        elif direction == 'cw' and self._can_go_cw():
            self.sector = (sector + 1) % self.sizes[ring]
            moved = True

        elif direction == 'ccw' and self._can_go_ccw():
            self.sector = (sector - 1) % self.sizes[ring]
            moved = True

        if moved:
            self.moves += 1
            self.visited.add((self.ring, self.sector))
            self._draw_player()
            self._update_status()

    def _show_win(self):
        self._draw_player()
        self._update_status()
        # Victory overlay
        self.canvas.create_rectangle(
            self.cx - 220, self.cy - 55,
            self.cx + 220, self.cy + 55,
            fill="#0d0d0d", outline="#f0c040", width=3)
        self.canvas.create_text(
            self.cx, self.cy - 16,
            text="✦  YOU ESCAPED  ✦",
            font=("Courier", 22, "bold"), fill="#f0c040")
        self.canvas.create_text(
            self.cx, self.cy + 18,
            text=f"Solved in {self.moves} moves  ·  Press N for a new maze",
            font=("Courier", 12), fill="#aaaaaa")


# ──────────────────────────────────────────────
# App bootstrap
# ──────────────────────────────────────────────
def launch(root=None, existing_canvas=None):
    seed = SEED if SEED is not None else random.randint(0, 999_999)
    rng  = random.Random(seed)
    passages, sizes = build_maze(RINGS, rng)
    exit_sector = rng.randint(0, sizes[-1] - 1)

    if root is None:
        root = tk.Tk()
        root.configure(bg=BG_COLOR)
        root.resizable(False, False)

    root.title(f"Circular Labyrinth  ·  Escape the maze!  ·  seed {seed}")

    if existing_canvas:
        existing_canvas.destroy()

    canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE,
                       bg=BG_COLOR, highlightthickness=0)
    canvas.pack()

    cx = cy = CANVAS_SIZE / 2
    outer_r = CANVAS_SIZE / 2 - 36

    draw_maze_walls(canvas, passages, sizes, cx, cy, outer_r, exit_sector)

    game = Game(canvas, passages, sizes, cx, cy, outer_r, exit_sector, root, seed)

    # Key bindings
    # Up arrow = outward (away from centre), Down = inward
    # Right = clockwise, Left = counter-clockwise
    def on_key(event):
        k = event.keysym
        if k == 'Up':
            game.move('out')
        elif k == 'Down':
            game.move('in')
        elif k == 'Right':
            game.move('cw')
        elif k == 'Left':
            game.move('ccw')
        elif k.lower() == 'n':
            new_canvas = canvas
            launch(root, new_canvas)

    root.bind('<KeyPress>', on_key)
    canvas.focus_set()
    canvas.bind('<KeyPress>', on_key)

    # New maze button
    def new_maze():
        launch(root, canvas)

    btn = tk.Button(root, text="New Maze (N)", command=new_maze,
                    font=("Courier", 11, "bold"),
                    bg="#1a1a1a", fg="#f0c040",
                    activebackground="#333", activeforeground="#f0c040",
                    relief="flat", padx=14, pady=5, cursor="hand2",
                    bd=0, highlightthickness=0)
    btn.place(x=CANVAS_SIZE - 148, y=CANVAS_SIZE - 36)

    canvas.focus_set()
    return root, canvas


def main():
    root, _ = launch()
    root.mainloop()


if __name__ == "__main__":
    main()