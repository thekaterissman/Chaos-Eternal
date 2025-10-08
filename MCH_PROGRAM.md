# MCH Program Documentation

This document provides a comprehensive overview of the "MCH Program," the core Python-based game logic for "The Coliseum: Chaos Eternal."

## Overview

The MCH Program is a text-based simulation of a dynamic, futuristic gladiator game. It is built around a collection of interconnected Python scripts that manage different aspects of the game, from character abilities to AI behavior. The central hub of this system is `kate.py`, which orchestrates the various components to create a cohesive gameplay experience.

## Core Components

The program is divided into several key files, each responsible for a specific domain of the game's logic:

### 1. `kate.py` - The Game Engine

This is the heart of the game.

- **`Game` Class**: The main class that initializes all other systems and contains the primary game loop.
- **State Management**: Tracks player score, level, power-ups, and the currently selected character.
- **Action Processing**: Takes player input (as a string) and simulates a turn, updating the game state accordingly.
- **Orchestration**: Ensures all the other modules (AI, Bestiary, Modes, etc.) work together seamlessly.

### 2. `characters.py` - The Chaos Queens

This file defines the playable characters.

- **Base `Character` Class**: A template for all characters, defining common attributes like name and trait.
- **Specific Characters (`Kate`, `Amya`, `Holly`)**: Each queen has a unique `special_ability()` method that provides a distinct gameplay advantage.

### 3. `Aichaosbrain.py` - The AI System

This module gives the game its unpredictable nature.

- **`AIChaosBrain` Class**: Simulates a learning AI.
- **`learn_move()`**: The AI "remembers" player actions to build a memory of their playstyle.
- **`throw_twist()`**: Randomly introduces surprising events into the game, like sandstorms or "Dance or Die" challenges, making each turn unique.
- **Persistence**: The AI's memory can be saved to and loaded from a `chaos_memory.json` file, allowing it to "evolve" across sessions.

### 4. `Beast_bestiary.py` - Beast and Mount System

Manages the creatures that players can own and ride.

- **`BeastBestiary` Class**: Handles the logic for buying and using beasts.
- **`buy_beast()`**: Allows players to spend in-game coins to acquire a new beast.
- **`ride_beast()`**: Allows players to ride a beast they own, providing a score bonus.

### 5. `Modes_manager.py` - Game Mode System

Controls the different ways the game can be played.

- **`ModesManager` Class**: Manages the current game mode.
- **`switch_mode()`**: Changes the active mode (e.g., from "Hunter" to "Therapy"). The mode affects how player actions are interpreted.
- **`earn_xp()`**: Tracks player experience points, which are used for leveling up.

### 6. `Gotcha_fails_system.py` - The Fails System

A fun system for highlighting player mistakes.

- **`GotchaFailsSystem` Class**: Manages a list of "fails."
- **`add_fail()`**: Adds a new embarrassing moment to the list and displays it in a "Total Fails Reel."

## How to Run the Simulation

The game logic can be run directly from the command line:

```bash
python game.py
```

This will execute the `if __name__ == '__main__':` block in `game.py`, which runs a pre-defined sequence of actions to demonstrate how the various systems interact.

## Extending the Game ("Forking")

The codebase is designed to be extensible. To "fork" the game, you can:

1.  **Create New Characters**: Add a new character class in `characters.py`.
2.  **Add New Game Modes**: Add a new mode to the `ModesManager`.
3.  **Create New AI Twists**: Add more unpredictable events to `AIChaosBrain`.
4.  **Modify the Game Loop**: Create a copy of `game.py` (e.g., `game_fork.py`) and alter the `game_loop_turn()` method to add new actions or change how existing ones are handled.