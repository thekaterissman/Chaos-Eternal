import * as hz from "horizon/core";

// A simple component that prints a message when the world starts.
class HelloWorld extends hz.Component<typeof HelloWorld> {
  // Components can have properties that are configurable in the editor.
  // We don't need any for this simple example.
  static propsDefinition = {};

  // The 'start' event is called once when the component is initialized.
  start() {
    console.log("Hello, Meta Horizon World!");
  }
}

// This line is important to register the component with the Horizon Worlds engine.
hz.registerComponent(HelloWorld);
