```{warning}
This is a simple port from the [original documentation](https://archive.blender.org/wiki/2015/index.php/User:Raa/Addons/Pie_Menu_Editor/). It will be improved in the future.
```

(popup-dialog-editor)=

# Pop-up Dialog

Pop-up Dialog Editor allows you to create a layout of widgets that can be displayed in pie menus, dialogs, panels or toolbars.

## Mode

![Pop-up dialog mode settings](/_static/images/original/popup/pme_popup_mode.png)

Affects the appearance and behavior of the pop-up.

| Mode | Pie | Dialog | Popup |
|------|-----|--------|-------|
| Moving the mouse outside the pop-up closes it | ❌ | ❌ | ✓ |
| Interaction with widgets of the pop-up closes it | ✓ | ❌ | ❌ |
| OK button | ❌ | ✓ | ❌ |
| Movable | ❌ | ✓ | ✓ |
| Customizable width | ❌ | ✓ | ✓ |

## Hotkeys

### Button Hotkeys

| Hotkey | Action |
|--------|--------|
| {kbd}`LMB` | Open Menu |
| {kbd}`Ctrl+LMB` | Add Button to the Right |
| {kbd}`Ctrl+Shift+LMB` | Add Button to the Left |
| {kbd}`Ctrl+Alt+LMB` | Remove Button |
| {kbd}`Shift+LMB` | Edit Button |
| {kbd}`Alt+LMB` | Change Icon |
| {kbd}`Alt+OS+LMB` | Clear Icon |
| {kbd}`Alt+Shift+LMB` | Hide Text |
| {kbd}`OS+LMB` | Toggle Spacer |
| {kbd}`Ctrl+OS+LMB` | Copy Button |
| {kbd}`Ctrl+Shift+OS+LMB` | Paste Button |

### Row Button Hotkeys

| Hotkey | Action |
|--------|--------|
| {kbd}`LMB` | Open Menu |
| {kbd}`Ctrl+LMB` | Add Row Below |
| {kbd}`Ctrl+Shift+LMB` | Add Row Above |
| {kbd}`Shift+LMB` | Toggle Row Size |
| {kbd}`OS+LMB` | Toggle Row Spacer |

## Layout

![Layout demonstration](/_static/images/original/popup/pme_layout.gif)

<style>
.layout-colors span {
    padding: 0 4px;
    border-radius: 3px;
    color: white;
}
</style>

<div class="layout-colors">
    <p>Blender uses row/column based layout system. The editor allows you to set-up a column of <span style="background-color:rgb(213, 77, 77)">rows</span> with optional <span style="background-color:rgb(45, 100, 178)">sub-columns</span> and <span style="background-color:rgb(65, 178, 42)">sub-rows</span>.</p>
</div>

In order to add a sub-column, use {kbd}`LMB` on one of the buttons to open a menu and select *Column* separator.
To add a sub-row to the sub-column there are *Begin Subrow* and *End Subrow* entries in the menu.

If you need more options to control the layout you can write python code in Custom tab which will be used to draw custom layout of widgets instead of default button.

## Expand Layout

![Expand layout settings](/_static/images/original/popup/pme1.14.0_pd_expand.png)

To expand layout inside pie menus or another popup dialog you need to enable *Expand Popup Dialog* option in *Menu* tab.

## Fixed Columns

![Fixed columns demonstration](/_static/images/original/popup/pme_layout_fixed_columns.png)

By default Blender resizes columns depending on the number of buttons in sub-rows. You can enable *Fixed Columns* option to fix that.

## Alignment

![Alignment demonstration](/_static/images/original/popup/pme_layout_alignment.gif)

You can adjust the alignment of buttons if there are no columns in the current row.

<style>
.mode-table, .hotkey-table {
    width: 100%;
    margin: 1em 0;
}

.mode-table td, .hotkey-table td {
    padding: 0.5em;
}

.mode-table th {
    background-color: #f5f5f5;
    font-weight: bold;
}
</style>