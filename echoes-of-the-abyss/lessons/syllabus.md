# Echoes of the Abyss: 36-Lesson Development Roadmap

## Syllabus

[View the complete 36-lesson syllabus on GitHub](https://github.com/gurban-dev/game-development/blob/main/echoes-of-the-abyss/lessons/syllabus.md)

## Phase 1: Python Foundations and the First Playable Room

**Lessons 1-4:** Establish the development environment and core game loop.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 1. Enter the Abyss | Install Pygame; understand coordinates, variables, loops, and program execution | `pygame.init`, `display.set_mode`, `event.get`, `display.flip`, `draw.rect`, `Clock.tick` | Open a window, draw the player, and close the game properly | Beginner | Python basics |
| 2. The First Movement | Keyboard input, position, velocity, and frame rate | `key.get_pressed`, `time.Clock`, `Vector2` | Move the player in four directions | Beginner | Lesson 1 |
| 3. Eight Directions | Functions, vectors, diagonal normalization, and delta time | `Vector2.normalize`, `Vector2.length`, `Clock.tick` | Implement responsive eight-direction movement | Beginner | Lesson 2 |
| 4. The First Walls | Rectangles, boundaries, collision basics, and debugging | `Rect`, `Rect.colliderect`, `draw.rect` | Build a room with solid walls that block the player | Beginner | Lesson 3 |

**Milestone 1:** A playable room with responsive movement and walls. The student understands the main loop, events, drawing, coordinates, and basic collision.

## Phase 2: Game Architecture and Visual Identity

**Lessons 5-8:** Turn the prototype into a maintainable game.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 5. The Adventurer | Classes, attributes, methods, and object state | `Surface`, `Rect` | Create a `Player` class and move rendering out of the main loop | Beginner+ | Lesson 4 |
| 6. Pixel Art Awakens | Image loading, transparency, scaling, and asset paths | `image.load`, `Surface.convert_alpha`, `transform.scale`, `blit` | Replace the placeholder with a sprite | Beginner+ | Lesson 5 |
| 7. Bringing Sprites to Life | Animation frames, timing, facing direction, and state | `image.load`, `transform.flip`, `Surface.subsurface` | Animate walking and idling using a sprite sheet | Intermediate | Lesson 6 |
| 8. Git Checkpoint and Project Structure | Modules, imports, functions, version control, and refactoring | Introduction to `pygame.sprite.Sprite` | Split the growing program into logical modules and commit the milestone | Intermediate | Lessons 5-7 |

**Milestone 2:** A character with visual identity and animation, supported by a growing codebase that can be extended without putting everything in one file.

## Phase 3: Dungeon Exploration and Camera

**Lessons 9-12:** Build a navigable world.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 9. The Dungeon Tiles | Two-dimensional lists, tile IDs, and data-driven maps | `Surface`, `blit`, `draw.rect` | Build a tile-based dungeon from a grid | Intermediate | Lesson 8 |
| 10. Collision Without Cheating | Collision resolution, wall sliding, and movement axes | `Rect`, `colliderect` | Prevent wall penetration and implement reliable movement around obstacles | Intermediate | Lesson 9 |
| 11. Beyond the Screen | World versus screen coordinates and camera offsets | `Vector2`, `Surface.blit` | Implement a scrolling camera that follows the player | Intermediate | Lesson 10 |
| 12. Rooms and Exits | Map boundaries, room transitions, and triggers | `Rect.colliderect`, event handling | Connect two rooms and transition when the player reaches an exit | Intermediate | Lesson 11 |

**Milestone 3:** The player can explore a connected dungeon with tile-based walls, collision handling, and a scrolling camera.

## Phase 4: Combat and Enemy AI

**Lessons 13-16:** Introduce the core action gameplay.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 13. Health and Damage | State, methods, health limits, and invulnerability timers | `Rect`, `time.get_ticks` or delta time | Add player health and damage handling | Intermediate | Lesson 12 |
| 14. The First Strike | Input events, attack hitboxes, and cooldowns | `event.get`, `Rect.colliderect` | Implement a melee attack that damages an enemy | Intermediate | Lesson 13 |
| 15. Enemies That Fight Back | Enemy classes, composition, and behavior states | `pygame.sprite.Sprite`, `Group` | Create a pursuing enemy with contact damage | Intermediate | Lesson 14 |
| 16. Projectiles and Knockback | Vectors, projectile lifecycle, and entity collisions | `Vector2`, `Rect`, `Group` | Implement a ranged attack, projectile cleanup, and knockback | Intermediate+ | Lesson 15 |

**Milestone 4:** A combat prototype with health, melee attacks, ranged attacks, and a functioning enemy.

## Phase 5: Roguelike Systems and Progression

**Lessons 17-20:** Make dungeon runs varied and rewarding.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 17. Enemy Personalities | State machines, chasing, attacking, and retreating | `Vector2`, `Group`, timing | Add a second enemy type with distinct behavior | Intermediate+ | Lesson 16 |
| 18. Treasure and Equipment | Dictionaries, lists, item data, and inventory modeling | `Rect`, `draw.rect`, `font.Font` | Add chests, collectibles, and a basic inventory | Intermediate | Lesson 17 |
| 19. Procedural Dungeons | Randomness, grids, graph connectivity, and seeded runs | `random`, `Rect` | Generate connected rooms and corridors | Advanced | Lesson 18 |
| 20. Finding the Player | Grid search, breadth-first search, and pathfinding | `Vector2`, `Rect` | Improve enemy navigation around obstacles | Advanced | Lesson 19 |

**Milestone 5:** Dungeon runs offer different layouts, collectible rewards, equipment, and enemies that can navigate around obstacles.

## Phase 6: Interface, Audio, and Game Feel

**Lessons 21-24:** Make the game understandable and satisfying to play.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 21. The Game HUD | Text rendering, health bars, and information hierarchy | `font.Font`, `Surface.blit`, `draw.rect` | Display health, equipment, and dungeon progress | Intermediate | Lesson 20 |
| 22. Menus and Game States | State transitions, input handling, and separation of concerns | `event.get`, `mouse.get_pos`, `mouse.get_pressed` | Add main menu, pause menu, and game-over screen | Intermediate | Lesson 21 |
| 23. Sound of the Abyss | Music, sound effects, and volume settings | `mixer.Sound`, `mixer.music` | Add attack, damage, pickup, and ambient audio | Intermediate | Lesson 22 |
| 24. Impact and Atmosphere | Particles, damage numbers, screen shake, and visual feedback | `draw`, `Surface`, `transform` | Add particles and feedback to attacks and damage | Intermediate+ | Lesson 23 |

**Milestone 6:** A game with readable UI, menus, sound, and feedback that makes combat feel more responsive.

## Phase 7: Boss Encounters and Complete Game Loop

**Lessons 25-28:** Give the game a meaningful beginning and ending.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 25. The Abyssal Guardian | Boss state machines, attack patterns, and phases | `Vector2`, timing, collision | Implement a boss with at least two distinct attacks | Advanced | Lesson 24 |
| 26. Balance and Replayability | Data-driven configuration, difficulty tuning, and randomness | Existing gameplay APIs | Tune enemy health, damage, loot, and encounter difficulty | Intermediate+ | Lesson 25 |
| 27. Save Your Progress | Serialization, JSON, validation, and error handling | Python `json`, file operations | Save and load settings and selected persistent progression | Intermediate | Lesson 26 |
| 28. Escape the Abyss | Victory conditions, transitions, and run lifecycle | Existing game-state and UI systems | Implement the final objective, victory screen, and restart flow | Intermediate+ | Lesson 27 |

**Milestone 7:** The game has a full run lifecycle: start, explore, fight, collect, defeat the boss, win or lose, and play again.

## Phase 8: Reliability, Testing, and Polish

**Lessons 29-32:** Turn a working game into a reliable release candidate.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 29. Finding Hidden Bugs | Reproduction steps, breakpoints, logging, and assertions | Python debugging tools, `pygame.event` | Diagnose and fix deliberately introduced gameplay bugs | Intermediate | Lesson 28 |
| 30. Automated Testing | Pure functions, unit tests, and deterministic behavior | Python `unittest` or `pytest` | Test damage, inventory, generation, and save/load logic | Intermediate+ | Lesson 29 |
| 31. Performance and Display Options | Profiling, object cleanup, fullscreen, and resizing | `display.set_mode`, `display.flip`, `Clock.get_fps` | Add display options and fix one measured performance issue | Intermediate+ | Lesson 30 |
| 32. Accessibility and Final Polish | Readability, remappable controls where practical, and visual options | `font`, `display`, `mixer` | Add selected accessibility options and fix usability problems | Intermediate+ | Lesson 31 |

**Milestone 8:** A tested release candidate with improved stability, settings, accessibility, and performance.

## Phase 9: Publishing and Independent Assessment

**Lessons 33-36:** Prepare a portfolio-quality release.

| Lesson | Main learning objectives | Pygame APIs | Student implementation | Difficulty | Dependencies |
|---|---|---|---|---|---|
| 33. Clean Up the Codebase | Responsibility boundaries, composition, and refactoring | Existing project modules | Refactor one problematic subsystem and document the architecture | Intermediate+ | Lesson 32 |
| 34. Package the Game | Dependencies, asset bundling, and clean-environment testing | `pygame` runtime and packaging tools | Build a distributable version and verify its startup | Intermediate+ | Lesson 33 |
| 35. The Portfolio Release | README writing, screenshots, gameplay capture, and licensing | Existing game APIs | Prepare documentation, controls, credits, and release materials | Intermediate | Lesson 34 |
| 36. Independent Developer Challenge | Transfer of knowledge, debugging, and implementation planning | APIs relevant to the chosen challenge | Independently add a small feature or enemy type and explain the design | Advanced | Lesson 35 |

**Final milestone:** A portfolio-quality game release, followed by an independent development challenge that demonstrates the student's ability to plan, implement, debug, and explain a new feature.