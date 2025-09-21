# How to Create a "Hello World" Script in Meta Horizon Worlds

This document outlines the steps to create a basic "Hello World" script in Meta Horizon Worlds, as described by the user. This process uses the visual scripting tools available within the Horizon Worlds environment.

## Steps

1.  **Place a Script Block:**
    *   Open your build menu.
    *   Find the "Script Block" object.
    *   Place it in your world.

2.  **Add a Text Object:**
    *   Open your build menu.
    *   Find the "Text" object.
    *   Place it in your world, preferably near the Script Block for easy reference.

3.  **Create the Script:**
    *   Open the Script Block's editor by selecting the Script Block.
    *   Inside the script editor, find the `When world is started` event node. This is the entry point for the script.
    *   Drag a wire from the `When world is started` node's output to the input of a `say` action node. If you don't have a `say` node, you can create one from the node menu.
    *   Connect the `say` action node to your Text object. This tells the script which object will display the text.
    *   In the `say` action node's text field, type the message: `Hello World!`

## Result

When the world loads, the script will execute. The `say` action will be triggered, causing the connected Text object to display the "Hello World!" message.
