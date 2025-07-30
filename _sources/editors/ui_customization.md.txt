```{warning}
This is a simple port from the [original documentation](https://archive.blender.org/wiki/2015/index.php/User:Raa/Addons/Pie_Menu_Editor/). It will be improved in the future.
```

(ui-customization)=

```{include} side_panel_editor.md
```

---

```{include} hiding_unused_panels.md
```

---

(pme-menu-panel-extension)=

# Menu/Panel Extension

<div class="video-container">
   <iframe src="https://www.youtube.com/embed/iO9PzLX6EDQ" frameborder="0" allowfullscreen></iframe>
</div>

---

(pme-toolbar)=

# PME Toolbar

```{admonition} Note
:class: warning

It stopped working after 4.3. I am in the process of fixing this.
Your support through [GitHub Sponsors](https://github.com/sponsors/pluglug) helps me to work on this and other features.
```

PME allows you to use the *User Preferences* area as a toolbar when its width or height is minimal:

![PME Toolbar](/_static/images/original/toolbars/pme_toolbars.gif)

<div class="video-container">
   <iframe src="https://www.youtube.com/embed/PB3wtlZ6AaM" frameborder="0" allowfullscreen></iframe>
</div>

## Naming

Toolbars display popup dialog's layout depending on its name:

```text
Toolbar <Screen Name> <Position>
```

Where *Screen Name* and *Position* are optional and *Position* takes one of these values: *Left*, *Right*, *Top*, *Bottom*.

## Examples

| Example | Description |
|---------|-------------|
| `Toolbar Top` | Top toolbar, all screens |
| `Toolbar UV Editing Right` | Right toolbar, *UV Editing* screen |
| `Toolbar 3D View Full` | Any toolbar, *3D View Full* screen |

## Saving

Toolbar widgets are stored in *User Preferences*. The position and size of the toolbars are stored in *.blend* files. So in order to save your toolbars, you need to use both {menuselection}`File --> User Preferences --> Save User Settings` and {menuselection}`File --> Save Startup File` commands.

By default Blender loads UI stored in *.blend* files. To keep the current UI (including toolbars) you need to uncheck *Load UI* option:

![PME Load UI option](/_static/images/original/toolbars/pme_load_ui.png)