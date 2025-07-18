(pme-scripting)=

# Scripting

PME allows for advanced customization and automation using Blender's [Python API](https://docs.blender.org/api/current/).
This article provides an overview of PME's scripting capabilities and explains the built-in global variables and functions.

## Tutorials

- **Video**: [Introduction to Scripting with Python in Blender (vimeo.com)](https://vimeo.com/28203314)
- **Video**: [Task Automation with Python Scripting in Blender (youtube.com)](https://www.youtube.com/watch?v=ZZWSvUgR38Y)
- [Python for Non-Programmers (python.org)](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
- [Blender Python API](https://docs.blender.org/api/current/)
- [Blender/Python Quickstart](https://docs.blender.org/api/current/info_quickstart.html)

## Global Variables

| Variables | Description |
|-----------|-------------|
| `menu` | Name of the active menu |
| `slot` | Name of the active slot |
| `C` | [bpy.context](https://docs.blender.org/api/current/bpy.context.html) |
| `D` | [bpy.data](https://docs.blender.org/api/current/bpy.data.html) |
| `O` | [bpy.ops](https://docs.blender.org/api/current/bpy.ops.html) |
| `T` | [bpy.types](https://docs.blender.org/api/current/bpy.types.html) |
| `P` | [bpy.props](https://docs.blender.org/api/current/bpy.props.html) |
| `L` | Current [UILayout](https://docs.blender.org/api/current/bpy.types.UILayout.html) object<br><br>```python<br>L.box().label(text="My Label")<br>``` |
| `E` | Current [Event](https://docs.blender.org/api/current/bpy.types.Event.html) object<br><br>```python<br>E.ctrl and E.shift and message_box("Ctrl+Shift Pressed")<br>``` |
| `U` | [pme.UserData](#pme.UserData) instance for user data storage<br><br>```python<br>U.foo = "value"<br>U.update(foo="value1", bar="value2")<br>U.foo<br>U.get("foo", "default_value")<br>``` |

## Global Functions

Below is a list of global functions provided by PME.

(pme-common-functions)=

### Common Functions

````{py:function} execute_script(path, **kwargs)
:noindex:

Execute an external Python script.

:param str path: Path to the `.py` file.
:param kwargs: Additional keyword arguments passed to the script.
:return: Value of local variable `return_value` if it exists, otherwise `True`.

**Example**:

```python
# Display 'Hello World!' message:
execute_script("scripts/hello_world.py", msg="Hello World!")

# scripts/hello_world.py:
# message_box(kwargs["msg"])

# Display 'Hi!' message:
message_box(execute_script("scripts/hi.py"))

# scripts/hi.py:
# return_value = "Hi!"
```
````

````{py:function} props(name=None, value=None)
:noindex:

Get or set the value of a PME Property.

:param str name: Name of the property.
:param value: New value of the property.
:return: PME property container if `name` is `None`, property value if only `name` is given, `True` if setting a value.

**Example**:

```python
# Get property value using string notation
value = props("MyProperty")

# Alternative: get property using attribute notation
value = props().MyProperty  # props() returns property container

# Set property value using string notation
props("MyProperty", value)

# Alternative: set property using attribute notation
props().MyProperty = value  # props() returns property container
```
````

````{py:function} paint_settings()
:noindex:

Retrieve the context-sensitive paint settings.

:return: The current paint settings or `None` if not in a paint mode.

**Example**:

```python
ps = paint_settings(); ps and L.template_ID_preview(ps, 'brush')
```
````

````{py:function} find_by(collection, key, value)
:noindex:

Find the first item in `collection` where `key` equals `value`.

:return: Collection item if found, otherwise `None`.

**Example**:

```python
m = find_by(C.active_object.modifiers, "type", 'SUBSURF')
```
````

````{py:function} setattr(object, name, value)
:noindex:

Same as Python's built-in `setattr`, but returns `True` after setting.

:return: `True`
````

(pme-command-tab-functions)=

### Command Tab Functions

````{py:function} open_menu(name, slot=None, **kwargs)
:noindex:

Open menu, pie menu, popup dialog or execute a stack key, sticky key, modal operator, or macro operator by name.

:param str name: Name of the menu.
:param slot: Index or name of the slot for Stack Key execution.
:param kwargs: Arguments for Modal / Macro Operators used as local variables.
:return: `True` if the menu exists, `False` otherwise.

**Example**:

```python
# Open the menu depending on the active object's type:
open_menu("Lamp Pie Menu" if C.active_object.type == 'LAMP' else "Object Pie Menu")

# Call "My Stack Key" slot depending on Ctrl modifier:
open_menu("My Stack Key", "Ctrl slot" if E.ctrl else "Shift slot")
```
````

````{py:function} toggle_menu(name, value=None)
:noindex:

Enable or disable a menu.

:param str name: Name of the menu.
:param bool value: `True` to enable, `False` to disable, `None` to toggle.
:return: `True` if the menu exists, `False` otherwise.
````

````{py:function} tag_redraw(area=None, region=None)
:noindex:

Redraw UI areas or regions.

:param str area: The Area.type to redraw. Redraw all areas if `None`.
:param str region: The Region.type to redraw. Redraw all regions if `None`.
:return: `True`
````

````{py:function} close_popups()
:noindex:

Close all popup dialogs.

:return: `True`
````

````{py:function} overlay(text, **kwargs)
:noindex:

Draw an overlay message.

:param str text: Message to display.
:param kwargs: 
    - `alignment`: One of `['TOP', 'TOP_LEFT', 'TOP_RIGHT', 'BOTTOM', 'BOTTOM_LEFT', 'BOTTOM_RIGHT']`. Default is `'TOP'`.
    - `duration`: Duration in seconds. Default is `2.0`.
    - `offset_x`: Horizontal offset. Default is `10` px.
    - `offset_y`: Vertical offset. Default is `10` px.
:return: `True`

**Example**:

```python
overlay('Hello PME!', offset_y=100, duration=1.0)
```
````

````{py:function} message_box(text, icon='INFO', title="Pie Menu Editor")
:noindex:

Show a message box.

:param str text: Message to display.
:param str icon: Icon name (e.g. 'INFO', 'ERROR', 'QUESTION', etc.).
:param str title: Window title.
:return: `True`
````

````{py:function} input_box(func=None, prop=None)
:noindex:

Show an input box.

:param func: Function to call with the input value.
:param str prop: Path to the property to edit.
:return: `True`

**Example**:

```python
# Rename object:
input_box(prop="C.active_object.name")

# Display input value:
input_box(func=lambda value: overlay(value))
```
````

(pme-custom-tab-functions)=

### Custom Tab Functions

````{py:function} draw_menu(name, frame=True, dx=0, dy=0)
:noindex:

Draw a popup dialog inside another popup dialog or a pie menu.

:param str name: Name of the menu (popup dialog).
:param bool frame: Whether to draw a frame.
:param int dx: Horizontal offset.
:param int dy: Vertical offset.
:return: `True` if the popup dialog exists, otherwise `False`.
````

````{py:function} operator(layout, operator, text="", icon='NONE', emboss=True, icon_value=0, **kwargs)
:noindex:

Similar to UILayout.operator(), but allows filling operator properties.

:param layout: A UILayout instance.
:param str operator: Identifier of the operator.
:return: OperatorProperties object.

**Example**:

```python
operator(L, "wm.context_set_int", "Material Slot 1",
        data_path="active_object.active_material_index", value=0)

# Same as:
# op = L.operator("wm.context_set_int", text="Material Slot 1")
# op.data_path = "active_object.active_material_index"
# op.value = 0
```
````

````{py:function} custom_icon(filename)
:noindex:

Get the integer value associated with a custom icon.

:param str filename: Icon filename without extension, located in `pie_menu_editor/icons/`.
:return: The integer value of the custom icon.

**Example**:

```python
L.label(text="My Custom Icon", icon_value=custom_icon("p1"))
```
````

````{py:function} panel(id, frame=True, header=True, expand=None)
:noindex:

Draws a panel by its ID.

:param str id: ID of the panel.
:param bool frame: Draw a framed panel.
:param bool header: Draw the panel header.
:param expand: `True` to expand, `False` to collapse, `None` to use the current state.
:return: `True`

**Example**:

```python
panel("MATERIAL_PT_context_material", True, True, True)
```
````

---

## Auto-run Scripts

PME allows you to create Python scripts that automatically execute when Blender starts.
To use this feature, place files in the `pie_menu_editor/scripts/autorun` folder using any of these methods:

- Direct `.py` files
- Folders containing scripts
- Symbolic links

```{warning}
Scripts in the `autorun` folder are executed directly in PME's context.
Only use scripts from trusted sources.
```

## Add Custom Global Functions

To use custom functions in PME:

1. Place your script in `pie_menu_editor/scripts/autorun` folder 
2. Register functions using `pme.context.add_global()`

Example:

```python
def hello_world():
    print("Hello World")

pme.context.add_global("hello", hello_world)
```

The registered function `hello()` becomes available in:

- Command tab
- Custom tab  
- External scripts

## PME Components

PME maintains a global context that provides access to commonly used functions, variables, and user-defined additions.
This context is accessible through two main interfaces:

````{py:class} pme.context

```{py:attribute} globals
:type: dict

Access PME's global context dictionary. Contains:

- Built-in shortcuts (`C`, `D`, `O`, `L`, etc.)
- Registered custom functions and values
- User data storage (`U`)

```python
from pie_menu_editor import pme

# Access globals from external scripts
g = pme.context.globals
props = g.get('props')
user_data = g.get('U')
```
```

```{py:method} add_global(key, value)

Register a custom function or value in the global context.

:param str key: Name for accessing the item
:param value: Function or value to register
:rtype: None

```python
# Register a function
def my_tool():
    bpy.ops.mesh.select_all(action='TOGGLE')

pme.context.add_global("toggle_select", my_tool)

# Register a constant
pme.context.add_global("MAX_ITEMS", 10)

# Access from PME menus via Command tab:
# toggle_select()
# MAX_ITEMS
```
```
````

````{py:class} pme.UserData

Flexible storage for user-defined data that persists during the Blender session.

```{py:method} get(name, default=None)

Get a stored value.

:param str name: Data key
:param default: Value to return if key doesn't exist
:return: Stored value or default
```

```{py:method} update(**kwargs)

Update multiple values at once.

```python
U = pme.context.globals['U']  # Get UserData instance
U.update(tool_state="active", count=5)
print(U.tool_state)  # "active"
```
```
````