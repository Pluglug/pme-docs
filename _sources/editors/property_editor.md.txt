```{warning}
This is a simple port from the [original documentation](https://archive.blender.org/wiki/2015/index.php/User:Raa/Addons/Pie_Menu_Editor/). It will be improved in the future.
```

(property-editor)=

# Property Editor

The editor allows you to register new [Properties](https://docs.blender.org/api/current/bpy.props.html) without coding.

## Supported Property Types

* BoolProperty
* IntProperty
* FloatProperty
* StringProperty
* EnumProperty
* Vector properties

## Usage

<div class="video-container">
   <iframe src="https://www.youtube.com/embed/xQ-ETd8xacA" frameborder="0" allowfullscreen></iframe>
</div>

## Storing Values

By default PME stores property values in Add-on Preferences. If you want to store some custom data in *.blend* files you need to assign the property to some type.

For example, if you assign *MyProperty* to *Object* type, the data will be stored in *.blend* files for each object in the scene:

![Property storing example](/_static/images/original/props/pme_prop_storing.png)

Now you can use *MyProperty* like any other *Object's* property:

```python
C.object.MyProperty = True
```

## Functions

![Property functions](/_static/images/original/props/pme_prop_funcs.png)

## Scripting

To get the value of the Property by its name use *props()* function:

```python
value = props("MyProperty")
value = props().MyProperty
```

To set the value use:

```python
props("MyProperty", value)
props().MyProperty = value
```

Custom tab usage example:

```python
L.prop(props(), "MyBoolProperty", text=slot, icon='COLOR_GREEN' if props("MyBoolProperty") else 'COLOR_RED')
```

## Examples

### Slider

![Slider property example](/_static/images/original/props/pme_prop_slider.png)

### Color Widget

![Color widget example](/_static/images/original/props/pme_prop_color.png)

### Direction Widget

![Direction widget example](/_static/images/original/props/pme_prop_direction.png)

### Icon-Only Tab Bar

![Icon-only tab bar example](/_static/images/original/props/pme_prop_tabbar.png)

### Directory Path

![Directory path example](/_static/images/original/props/pme_prop_path.png)