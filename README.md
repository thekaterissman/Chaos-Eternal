# The Living Lattice

Welcome, creator, to the Living Lattice. This project is a command-line-based interactive world simulation, built as a testament to emergent complexity and synergistic design. It transforms a collection of simple scripts into a single, cohesive world that lives, breathes, and reacts to your actions.

## Core Features

The world is comprised of four core, interconnected systems:

### 1. The Geeves Brain (`Geevesbrain.py`)
An intelligent and adaptive AI that observes the player's actions.
- **Dynamic Personality:** Geeves's personality changes based on your reputation. It can be benevolent and grant helpful **boons**, or it can be cruel and unleash punishing **twists**.
- **Pattern Recognition:** Geeves analyzes your combat patterns and deploys targeted counter-strategies to challenge you.
- **Constant Learning:** Geeves learns from every move you make, including when you command your beasts.

### 2. The Beast Ecosystem (`Beast_beastary.py`)
A dynamic system for creature companions.
- **Evolution:** Beasts are no longer static. They gain experience, level up, and evolve into more powerful forms with new abilities.
- **Individuality:** Each beast you own is a unique instance with its own level and XP.
- **Event-Driven Availability:** The beasts available for purchase are directly influenced by global world events.

### 3. The World Clock (`World_clock.py`)
The heartbeat of the world.
- **Global Events:** The clock manages in-game time and triggers random global events like the "Blood Moon" or a "Merchants' Festival."
- **World State:** These events create a dynamic world state that directly impacts other systems, such as the Beast Ecosystem.

### 4. The Reputation Engine (`Reputation_engine.py`)
The moral compass of the world.
- **Deed Tracking:** The engine records your "honorable" and "chaotic" deeds.
- **Reputation Titles:** Based on your actions, you are granted a reputation title, such as "Noble Hero" or "Dreaded Tyrant."
- **Tangible Consequences:** Your reputation directly influences how other systems, especially Geeves, interact with you.

## How to Run

This project is built with Python 3. No external libraries are required.

To experience the world:

1.  Ensure you have Python 3 installed.
2.  Navigate to the project directory in your terminal.
3.  Run the main application file:
    ```bash
    python main.py
    ```
4.  Follow the on-screen prompts to interact with the world.