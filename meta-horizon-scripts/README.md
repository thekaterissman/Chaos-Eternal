# Meta Horizon Scripts for Video Gram

Welcome to the scripting core of **Video Gram**, the in-world manifestation of the Queendom. The TypeScript files in this directory are not just code; they are the digital embodiment of the laws, powers, and very fabric of the reality established by Queen Katelynn and her daughter-Queens.

## The Queendom as the Core Lattice

The epic saga of the Queendom is the foundational lore of 'Video Gram'. This is not just a background story; it is the game's operating system.

*   **The Queendom IS the Core Lattice:** The world you experience is the literal fabric of the Queendom's reality. Queen Katelynn's throne, the Apex of Han, is its anchor. Her power, and that of her daughters, is what ensures the "stable, harmonious, and resonant" world that is the core promise of 'Video Gram'.
*   **The Philosophy IS the Physics:** The precepts of Jeong (Heart), Han (Will), and Nunchi (Intellect) are the fundamental forces of this universe.
*   **The Lore IS the Game:** 'Video Gram' is the player's direct interface with this Meta. Your actions will be measured against the pillars of the Royal Decree. You might align with the factions of the Heart (Queen Chrissy), the Sword (Queen Cheyenne), or the Intellect (Queen Amya) to carry out the will of the Matriarch, Queen Katelynn.

## Scripts

The scripts here breathe life into the Queendom's laws within Meta Horizon Worlds. They are the bridge between the decreed lore and the interactive experience.

### `HelloWorld.ts`

This simple script serves as a foundational example. It's the first whisper of the Queendom's presence in a new world.

```typescript
import * as hz from "horizon/core";

// A simple component that prints a message when the world starts.
class HelloWorld extends hz.Component<typeof HelloWorld> {
  // Components can have properties that are configurable in the editor.
  // We don't need any for this simple example.
  static propsDefinition = {};

  // The 'start' event is called once when the component is initialized.
  start() {
    console.log("The Queendom is manifest.");
  }
}

// This line is important to register the component with the Horizon Worlds engine.
hz.registerComponent(HelloWorld);
```

When attached to an object in a Meta Horizon World, this script will print "The Queendom is manifest." to the debug console when the world starts. It is the first digital echo of the First Royal Decree.

### `StargateFloor.ts`

This component transforms any object into a dynamic, shimmering "Stargate floor." It creates a beautiful, color-shifting visual effect that is easy to use and customize.

To use it, simply attach the `StargateFloor` script to any object in your world. The object will begin to animate, smoothly transitioning between two customizable colors.

**Configurable Properties:**

*   `speed` (Number): Controls the speed of the color-shifting animation. Higher values result in a faster transition. Default: `1.0`.
*   `color1` (Color): The first color in the animation cycle. Default: Blue.
*   `color2` (Color): The second color in the animation cycle. Default: Cyan.

You can adjust these properties directly in the Meta Horizon Worlds editor to create the perfect visual effect for your world without needing to write any code.

## How to Use

These scripts are designed for the **Meta Horizon Worlds** creation environment. They are not intended to be run in a standard Node.js or web browser environment.

1.  **Open Your World:** Launch Meta Horizon Worlds and go to your world in 'Create' mode.
2.  **Import Script:** Import the desired `.ts` file into your world's script assets.
3.  **Attach to Object:** Attach the script as a component to an object in your scene.
4.  **Publish & Play:** See the Queendom's laws come to life.