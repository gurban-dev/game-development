'''
For a scalable Pygame project, one common structure is designed to
solve several problems early on:

1. Keeping files small.
2. Separating responsibilities.
3. Avoiding circular dependencies.
4. Making features easier to add.
5. Keeping update and render flow predictable.

Recommended Project Structure:

game/
│
├── main.py
├── config.py
│
├── core/
│   ├── game.py
│   ├── state_machine.py
│   ├── asset_manager.py
│   ├── input_manager.py
│   └── constants.py
│
├── states/
│   ├── main_menu.py
│   ├── gameplay.py
│   ├── pause_menu.py
│   └── game_over.py
│
├── entities/
│   ├── player.py
│   ├── enemy.py
│   ├── bullet.py
│   └── npc.py
│
├── systems/
│   ├── collision_system.py
│   ├── combat_system.py
│   ├── animation_system.py
│   └── particle_system.py
│
├── ui/
│   ├── button.py
│   ├── health_bar.py
│   └── inventory_ui.py
│
├── levels/
│   ├── level_loader.py
│   └── maps/
│
├── assets/
│   ├── images/
│   ├── audio/
│   ├── fonts/
│   └── data/
│
├── save/
│
└── utils/
├── math_utils.py
├── helpers.py
└── timer.py

## Root Level

main.py is the application entry point.

Typically:

• Pygame is initialized in this file.
• A game window is created.
• A Game object is created.
• The main game loop is launched.
• The application shuts down cleanly when the game exits.

config.py stores configuration values such as screen dimensions,
frame rate settings and other values that may need to be changed
without modifying game logic.

## The Core Folder

The core folder contains the foundation that drives the application.

This includes:

• The Game class.
• State management.
• Asset loading.
• Input handling.
• Shared constants.

These components are commonly used throughout the entire project.

## The States Folder

The states folder contains components that represent major modes of
the game.

Examples include:

• Main Menu
• Gameplay
• Pause Menu
• Game Over Screen

Only one state is typically active at a time.

State management allows the game to switch between these modes
cleanly without filling a giant update loop with conditional
statements.

## The Entities Folder

The entities folder contains objects that exist inside the game
world.

Examples include:

• Player
• Enemy
• Bullet
• NPC (Non-Player Character)

NPC is any character in a game that is not directly controlled
by the player.

Each entity owns its own data and behavior.

For example, a Player class may be responsible for movement,
shooting, health and rendering.

## The Systems Folder

The systems folder contains logic that operates on multiple
entities.

Examples include:

• Collision detection
• Combat calculations
• Animation updates
• Particle effects

Systems help keep shared functionality separate from entity code.

## The UI Folder

The ui folder contains user interface elements.

Examples include:

• Buttons
• Health bars
• Inventory windows
• Menus

Keeping UI separate from gameplay code makes the project easier to
maintain.

## The Levels Folder

The levels folder contains level-loading logic and map data.

This allows game content to be managed separately from gameplay
systems and entity logic.

## The Assets Folder

The assets folder stores game resources.

Examples include:

• Images
• Audio files
• Fonts
• Data files

Organizing assets into dedicated folders makes them easier to find
and manage as the project grows.

## The Save Folder

The save folder stores save-game data and player progress.

This might include:

• Completed levels
• Player statistics
• Inventory data
• Settings

## The Utils Folder

The utils folder contains reusable helper functions and utility
classes.

Examples include:

• Math helpers
• Timers
• Utility functions
• General-purpose tools

These utilities can be used throughout the project without
belonging to a specific gameplay system.

## Key Idea

A scalable architecture is based on separation of responsibilities.

Each folder has a specific purpose.

• main.py starts the application.
• States manage screens and game modes.
• Entities represent objects in the game world.
• Systems handle shared game logic.
• UI manages user interface elements.
• Assets store game resources.
• Utils provide reusable helper code.

As projects grow larger, this organization helps keep the codebase
maintainable, reusable and easier to expand.
'''