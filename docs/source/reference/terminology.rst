.. _terminology:

Terminology
===========

This page explains the main terms and concepts used in Blender and PME for newcomers and those looking to deepen their understanding.

Basic Blender Concepts
----------------------

Area
^^^^
A large workspace region within the Blender interface.  
Different editor types (such as the 3D Viewport, Outliner, etc.) each occupy an **Area**.

- PME offers a feature called **Toggle Side Area**, allowing you to show or hide side regions (like sidebars) in an Area.
- Areas may contain subregions called **Regions**, such as a toolbar or property shelf.

| **Related**: Region, Window, Workspace
| **Reference**: `Area (docs.blender.org) <https://docs.blender.org/manual/en/latest/interface/window_system/areas.html>`_

Context
^^^^^^^
Represents the **current state** of Blender, including:

- The currently selected object
- The active editing mode (e.g., Object Mode, Edit Mode)
- Cursor position
- Active tool
- Other information depending on user actions

In Python:

.. code-block:: python

    # Retrieve the active object
    active_obj = bpy.context.active_object

    # Check the current mode
    current_mode = bpy.context.mode

By leveraging the context, you can conditionally display or enable certain tools based on the current state (mode, selection, etc.).

**Reference**: `Context (docs.blender.org) <https://docs.blender.org/api/current/bpy.context.html>`_

Header
^^^^^^
A horizontal bar located at the top or bottom of an Area.
It usually contains menus, frequently used tool icons, and so forth.

- PME allows you to add custom buttons to the header using
  :ref:`Menu/Panel Extension <pme-menu-panel-extension>`.

| **Related**: Region
| **Reference**: `Header (docs.blender.org) <https://docs.blender.org/manual/en/latest/interface/window_system/regions.html#header>`_

Keymap
^^^^^^
A collection of **hotkey assignments** that change depending on the Area type or editing mode.

- Example: The **G** key is assigned to "move" in Object Mode but to "grab" in Sculpt Mode.

PME can help you tailor these keymaps further to fit your personal workflow.

**Reference**: `Keymap (docs.blender.org) <https://docs.blender.org/manual/en/latest/editors/preferences/keymap.html>`_

Mode
^^^^
Refers to the **operational state** of Blender (e.g., Object Mode, Edit Mode).  
Each mode has its own set of tools and actions.

- PME's **Poll** feature allows you to show or hide specific tools or menus based on the active mode.

**Example**: ``bpy.context.mode == 'EDIT_MESH'``


Operator
^^^^^^^^
A functional unit in Blender that performs a specific action (part of the ``bpy.ops`` module).

- Can be assigned to hotkeys
- Can appear on menus/buttons
- Callable from Python scripts
- Executable in Macros

Within PME, you can combine multiple operators using **Macro Operators** or **Modal Operators** to create custom tools.

**Example**: ``bpy.ops.mesh.subdivide()``


Panel
^^^^^
A collapsible group of UI widgets, often found in sidebars or property areas.

PME allows for:

- Creating new panels
- Extending existing panels
- Grouping panels
- Hiding unneeded panels

| **Related**: Property, Region
| **Reference**: `Panel (docs.blender.org) <https://docs.blender.org/manual/en/latest/interface/window_system/tabs_panels.html>`_


Property
^^^^^^^^
Refers to various data items in Blender (like object location, material settings, etc.) that are typically displayed as sliders, checkboxes, or fields in the UI.

In PME, you can:

- Display and edit properties on menus/panels
- Refer to them in scripts or Poll functions
- Add custom properties via the Property Editor

**Example**: ``bpy.context.object.location``


Region
^^^^^^
A subdivided area within an **Area**, containing specific UI elements (tools, properties, etc.).

- With PME's **Panel Group** feature, you can add custom content to a Region.

**Related**: Area, Panel

**Reference**: `Region (docs.blender.org) <https://docs.blender.org/manual/en/latest/interface/window_system/regions.html>`_

PME-Specific Concepts
---------------------

Menu
^^^^
A broad term in PME describing any customizable UI component you create, such as:

- Pie Menu
- Regular Menu
- Macro Operator
- Modal Operator
- etc.

Each menu is composed of multiple **Slots**, each providing a distinct functionality or element.


Slot
^^^^
An individual **element** or **slot** within a menu. Each slot can be configured to:

- Run a command
- Display or edit a property
- Invoke a sub-menu
- Draw a custom layout

**Related**: Command Tab, Property Tab, Menu Tab, Custom Tab


Command Tab
^^^^^^^^^^^
One of the tabs in the Slot Editor that lets you run Python code or invoke operators directly.

- Execute single-line Python scripts
- Call custom functions
- Manipulate variables or operators

**Example**: ``C.active_object.location.x += 1.0``


Custom Tab
^^^^^^^^^^
Another tab in the Slot Editor for creating more visually defined UI layouts without manual scripting.

**Example**:

.. code-block:: python

    L.box().label(text="Custom Layout")


Interactive Panels Mode
^^^^^^^^^^^^^^^^^^^^^^^
A PME mode that displays additional PME Tools buttons within every UI element, making it easier to:

- Identify menu IDs
- Configure panel extensions
- Customize your UI

This mode is especially useful when learning PME, as it helps you visualize where various elements and menus are located.


Macro Operator
^^^^^^^^^^^^^^
Allows you to **execute multiple operators in sequence**.  
In the PME **Macro Operator Editor**, you can:

- Record operator sequences
- Adjust operator parameters
- Manage execution flow

It is invaluable for bundling complex workflows into a single click.


Modal Operator
^^^^^^^^^^^^^^
A real-time, interactive operator that responds to continuous user input.
You can create your own Modal Operators with PME's **Modal Operator Editor**, enabling:

- Reactions to mouse movements
- Key events and state changes
- Real-time feedback and updates

Perfect for building **custom interactive tools**.


Poll Method
^^^^^^^^^^^
A Python function used to determine whether a menu or tool is **currently usable**. It must return ``True`` if available, or ``False`` otherwise.

For example:

.. code-block:: python

    ao = C.active_object; return ao and ao.type == 'MESH'

Common use cases include:

- Enabling/disabling UI elements based on the current mode
- Restricting features to certain object types
- Preventing errors by hiding invalid tools


Slot Editor
^^^^^^^^^^^
The **central UI** for defining how PME menus/buttons behave. It includes multiple tabs such as:

- Command (for code execution)
- Property (for property display)
- Menu (for calling other PME's menus)
- Hotkey (for invoking shortcuts)
- Custom (for custom layouts)

It's designed so you can set up everything through a graphical interface, even if you're new to scripting.


Advanced Concepts
-----------------

Event System
^^^^^^^^^^^^
Blender's input handling mechanism, which tracks keyboard and mouse events. It is essential for:

- Modal Operators
- Custom hotkeys
- Interactive tools

For example:

.. code-block:: python

    E.ctrl and E.shift and message_box("Ctrl+Shift Pressed")


Layout System
^^^^^^^^^^^^^
Blender's system for constructing UI layouts. PME relies on this system to:

- Place labels, buttons, and property fields
- Position operators and custom widgets
- Structure UI elements hierarchically

For example:

.. code-block:: python

    L.box().label(text=text, icon=icon, icon_value=icon_value)


Operator Execution Context
^^^^^^^^^^^^^^^^^^^^^^^^^^
Determines how an operator is executed. The two most common contexts are:

- **INVOKE_DEFAULT**  
  An interactive mode in which Blender waits for additional user input, such as mouse positioning or pop-up confirmation.

- **EXEC_DEFAULT**  
  Runs the operator immediately with preset parameters, often used in scripts or macros.

**Example**:

.. code-block:: python

    # Move an object interactively based on mouse input
    bpy.ops.transform.translate('INVOKE_DEFAULT')

    # Move an object 5.0 along the X axis without user input
    bpy.ops.transform.translate('EXEC_DEFAULT', value=(5.0, 0.0, 0.0))

| **Related**: Operator, Command Tab, Modal Operator, Macro Operator
| **Reference**: `Execution Context (docs.blender.org) <https://docs.blender.org/api/current/bpy.ops.html#execution-context>`_
