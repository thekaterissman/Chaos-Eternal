import * as hz from "horizon/core";
import { Color, Vec3 } from "horizon/math";

// A component that creates a dynamic, shimmering "Stargate" effect on an object.
class StargateFloor extends hz.Component<typeof StargateFloor> {
  // --- Properties ---
  // These values can be configured in the Horizon Worlds editor.

  static propsDefinition = {
    // The speed of the color-shifting animation.
    speed: { type: hz.PropTypes.float, default: 1.0 },
    // The first color in the animation cycle.
    color1: { type: hz.PropTypes.color, default: new Color(0, 0, 1) }, // Default to Blue
    // The second color in the animation cycle.
    color2: { type: hz.PropTypes.color, default: new Color(0, 1, 1) }, // Default to Cyan
  };

  // --- State ---
  // Private variables to manage the component's state.
  private time: number = 0;

  // --- Lifecycle ---

  // The 'start' event is called once when the component is initialized.
  start() {
    // This script assumes it is attached to an object with a modifiable color.
    // In Horizon Worlds, this is typically done by setting the object's material properties.
    // We will manipulate the entity's color directly, which is a common pattern.
  }

  // The 'update' event is called every frame.
  update(deltaTime: number) {
    // Increment the internal timer by the time since the last frame, scaled by the speed property.
    this.time += deltaTime * this.props.speed;

    // Use a sine wave to create a smooth oscillation between 0 and 1.
    // The Math.sin() function returns a value between -1 and 1, so we add 1 to make it 0 to 2,
    // and then divide by 2 to normalize it to a 0 to 1 range.
    const alpha = (Math.sin(this.time) + 1) / 2;

    // Linearly interpolate between color1 and color2 using the alpha value.
    const currentColor = Color.lerp(this.props.color1, this.props.color2, alpha);

    // Apply the calculated color to the entity this component is attached to.
    // We assume the entity has a 'color' property that can be set.
    // This is a common API pattern in game engines for changing an object's base color.
    this.entity.color = currentColor;
  }
}

// Register the component with the Horizon Worlds engine.
hz.registerComponent(StargateFloor);