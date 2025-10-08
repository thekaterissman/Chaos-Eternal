// This script needs to be compiled in the Meta Horizon Worlds environment.
// The environment provides the 'horizon/core' module and the necessary types.

import * as hz from "horizon/core";

// A component that displays "Hello World!" on a text object.
class HelloWorld extends hz.Component<typeof HelloWorld> {
  // A property to hold a reference to the text object in the world.
  // This needs to be linked in the Horizon Worlds editor.
  static propsDefinition = {
    textObject: { type: hz.PropTypes.Entity },
  };

  // The 'start' event is called once when the component is initialized.
  start() {
    // Get the TextGizmo from the textObject entity.
    const textGizmo = this.props.textObject.as(hz.TextGizmo);
    if (textGizmo) {
      // Set the text of the TextGizmo.
      textGizmo.text = "Hello World!";
    }
  }
}

// This line is important to register the component with the Horizon Worlds engine.
hz.registerComponent(HelloWorld);
