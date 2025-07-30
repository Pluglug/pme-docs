(changelog)=

# Change Log

## 1.18.8 (2025.01.05)

- Blender 4.2 Support
- Add `show_error_trace` option to the PME Settings
- Add `bpy.ops.pme.exec_override()` Operator
- Bug Fixes
- New documentation site (📖 you are here)

**Release Notes**: [v1.18.8](https://github.com/Pluglug/pie-menu-editor-fork/releases/tag/v1.18.8)

---

## 1.18.7 (2023.04.11)
- Blender 3.6.0 Alpha Support
- Bug Fixes

## 1.18.6 (2022.08.13)
- Fixed Click Drag and Hold hotkey modes in Blender 3.2.0+

## 1.18.5 (2022.05.02)
- Header Tools

## 1.18.4 (2021.11.11)
- Toggle side-area operator fix for recent Blender builds.

## 1.18.3 (2021.06.28)
- Support Blender 3 Alpha

## 1.18.2 (2021.04.24)
- Bug Fix for Panel Groups in Blender 2.93

## 1.18.1 (2021.03.12)
- Blender 2.93 Alpha Support

## 1.18.0 (2020.10.30)
- Key Chords
- Bug Fixes

## 1.17.5 (2020.09.23)
- Blender 2.91 Support  
- Customizable number of menu list rows  
- New global variable for scripts to store user data:

    ```python
    U.foo = "value"
    U.update(foo="value1", bar="value2")  
    U.foo
    U.get("foo", "default_value")
    ```

- Bug Fixes

## 1.17.3 (2020.07.20)
- Option to use check-boxes instead of toggle-buttons.
- Bug Fixes

## 1.17.2 (2020.05.12)
- PME Preferences in 3D View area
- Pie extra slot gap size
- Bug Fixes

## 1.17.1 (2020.04.27)
- New backup folder: `scripts/addons/pie_menu_editor_data/backups`  
- Support keymaps with commas
- Bug Fixes

## 1.17.0 (2020.03.27)
- 10 Pie Slots
- Sub-panels
- Wider Popups

## 1.16.4 (2019.10.13)
- Blender 2.81 Support
- Bug Fixes

## 1.16.2 (2019.09.21)
- Blender 2.81 Support
- Auto-backups (pie_menu_editor/data/backup folder)
- Bug Fixes

## 1.16.0 (2019.08.09)
- Remember StackKey State
- Bug Fixes

## 1.15.23 (2019.06.26)
- Bug Fixes

## 1.15.22 (2019.06.09)
- Bug Fixes

## 1.15.21 (2019.06.04)
- Toggle-able menu slots
- Add existing menus to pies, menus, or popups
- Bug Fixes

## 1.15.20 (2019.04.11)
- Bug Fixes

## 1.15.19 (2019.03.25)
Bug Fixes
- Bug Fixes

## 1.15.18 fix 1 (2019.03.24)

## 1.15.18 (2019.03.21)
- Bug Fixes

## 1.15.17 (2019.03.12)
- Blender 2.8 Beta Support
- Bug Fixes

## 1.15.16 fix 1 (2019.03.07)

## 1.15.16 (2019.02.14)
- Bug Fixes

## 1.15.15 (2019.02.13)
- Bug Fixes

## 1.15.14 (2019.01.21)
- Bug Fixes

## 1.15.13 fix 1 (2019.01.15)
- Fix for multi-column Regular Menus

- Multi-column fix

## 1.15.13 (2019.01.14)
- Blender 2.8 Beta Support

## 1.15.12 fix 2 (2019.01.11)
- Fixes for Blender 2.8 Beta
- New Python API changes.

## 1.15.12 (2019.01.07)
- Blender 2.8 Beta Support

## 1.15.11 fix 7 (2019.01.05)
- Fixes for Blender 2.8 Beta

## 1.15.11 fix 4 (2018.12.28)

## 1.15.11 fix 3 (2018.12.28)
- Fixes for PME 1.15.11

## 1.15.11 (2018.12.23)
- Blender 2.8 Beta Support
- Bug Fixes

## 1.15.10 fix 1 (2018.12.15)
- Some Fixes for Blender 2.8 builds

## 1.15.10 (2018.12.10)
- Bug Fixes

## 1.15.9 (2018.12.10)
- Bug Fixes

## 1.15.8 fix 3 (2018.12.06)

## 1.15.8 fix 3 (2018.12.04)
- Some Fixes for Blender 2.8 builds

## 1.15.8 (2018.12.03)
- Blender 2.8 Beta Support
- Bug Fixes

## 1.15.7 fix 3 (2018.11.20)
- Fix for the latest Blender 2.8 builds

## 1.15.7 (2018.11.08)
- Latest Blender 2.8 Builds Support

## 1.15.6 (2018.10.10)
- Latest Blender 2.8 Builds Support
- Bug Fixes

## 1.15.5 (2018.09.13)
- Blender 2.8 Alpha Support
- Bug Fixes

## 1.15.4 (2018.08.27)
- Blender 2.8 Alpha Support
- Python 3.7 Support

## 1.15.3 (2018.06.25)
- Show/Hide/Toggle Side Area
- Show/Hide/Toggle Sidebar
- Bug Fixes

## 1.15.2 (2018.05.16)
- [Store Property Values in `.blend` Files](../Editors/Property#Storing_Values)
- [On Property Init Function](../Editors/Property#Functions)
- Bug Fixes

## 1.15.1 (2018.05.09)
- [Context Sensitive Buttons](https://blenderartists.org/t/addon-pie-menu-editor-1-15-0/662456/1261?u=roaoao)
- Bug Fixes

## 1.15.0 (2018.05.08)
- [Property Editor](../Editors/Property)
- [Extending Panels](../Panels#Extending_Panels)
- [Tag/Untag Group of Menus](https://i.imgur.com/Hwrs49a.mp4)
- [Save/Restore Tree View State](https://i.imgur.com/jKvxCLg.mp4)
- [Select Menu by Name or Hotkey](https://i.imgur.com/bsaKFdq.mp4)
- [Auto-run Python Script Files](../Scripting#Auto-run_Scripts)
- [Custom Global Functions](../Scripting#Custom_Global_Functions)
- [New Global Variables: menu, slot](../Scripting#Global_Variables)
- [New Function: props(name)](../Scripting#Common_Functions)
- [Updated Function: open_menu(menu, slot, **kwargs)](../Scripting#Command_Tab_Functions)
- Blender 2.8 Support

## 1.14.15 (2018.04.06)
- [Move Edge Script](https://i.imgur.com/oV5lASt.mp4) (idea by [MickHanks](https://blenderartists.org/forum/showthread.php?392910&p=3299258&viewfull=1#post3299258))
- Bug Fixes

## 1.14.13 (2018.02.14)
- [Call Pie Menus from Other Add-ons](https://i.imgur.com/zpCo97J.mp4)

## 1.14.9 (2017.10.24)
- [Option to Hide Modal Sub-Hotkey](https://wiki.blender.org/uploads/7/7f/Pme1.14.9_modal_hide_hotkey.png)
- Bug Fixes

## 1.14.7 (2017.10.15)
- [New Modal Operator Options](https://wiki.blender.org/uploads/c/cd/Pme1.14.7_modal_adv_settings.png)
- [Customizable Modal Overlay Text](https://i.imgur.com/Q1nlcm5.mp4)
- `custom_icon()` Function
- `**kwargs` for [open_menu()](../Scripting#Command_Tab_Functions) Function
- Bug Fixes

## 1.14.6 (2017.10.07)
- [Macro Operator Tutorial](https://youtu.be/-RQFK1kqqVw) by [Jimmy Livefjord](https://blenderartists.org/forum/member.php?104883-jimpaw80)
- Fixed Hotkey tab

## 1.14.3 (2017.09.27)
- [Popup Area's On-Open command](http://i.imgur.com/Gu3nRSV.mp4)
- Modal Operators:
  - Angle properties support
  - [Cursor is locked in the current area](http://i.imgur.com/ekVYd6y.mp4)
  - [Panning](http://i.imgur.com/xB3H3Ll.mp4) (unlocks the cursor)
- [Stack Key Tutorial](https://youtu.be/-rknBwAPypk) by [Jimmy Livefjord](https://blenderartists.org/forum/member.php?104883-jimpaw80)
- Bug Fixes

## 1.14.2 (2017.09.22)
- [Popup Area](http://i.imgur.com/rumYTRt.gifv)
- [Modal Subsurf Modifier Example](../Examples#Modal_Subsurf_Modifier)
- Bug Fixes

## 1.14.1 (2017.09.19)
- [Copy/Paste Item hotkeys](../Editors/Popup_Dialog#Button_Hotkeys)
- Maximize Button
- Bug Fixes

## 1.14.0 (2017.09.17)
- [Modal Operator Editor](../Editors/Modal_Operator)
- [Toolbars](../Toolbars)
- [Tweak Hotkeys](../#Hotkey Mode)
- [1 Hotkey - 3 Pie Menus](../Examples#1_Hotkey_-_3_Pie_Menus)
- `'Any'` Hotkey Modifier
- [RMB Context Menu Entry](../#RMB_Context_Menu)
- Blender 2.8 Support
- [Hide Pie Menu Title](https://wiki.blender.org/uploads/e/ef/Pme1.14.0_pm_title.png)
- [Expand Item Menu](https://wiki.blender.org/uploads/b/b7/Pme1.14.0_expand_item_menu.gif)
- [Group Menus by Type/Hotkey](https://wiki.blender.org/uploads/6/60/Pme1.14.0_group_by.png)
- [New Global Functions](../Scripting#Global_Functions)
- **Pop-up Dialog Editor**:
  - ['Pop-up' Mode](../Editors/Popup_Dialog#Mode)
  - [Alignment tools](../Editors/Popup_Dialog#Alignment)
  - [Hotkeys](../Editors/Popup_Dialog#Hotkeys)
  - [New way to expand popup dialogs](../Editors/Popup_Dialog#Expand_Layout)
  - [Resize All Rows](https://wiki.blender.org/uploads/9/99/Pme1.14.0_resize_all.png)

## 1.13.6 (2017.06.10)
- [Open existing panel in a popup](https://wiki.blender.org/uploads/b/b9/Pme1.13.5_popup.png)
- Bug fixes

## 1.13.4 (2017.04.09)
- [Group and filter menus by custom tags](https://wiki.blender.org/uploads/4/4d/Pme1.13.4_tags.png)
- [Block UI](https://wiki.blender.org/uploads/b/bf/Pme1.13.4_block_ui.png) option for Sticky Keys

## 1.13.1 (2017.02.23)
- [Columns with Fixed Width](https://wiki.blender.org/uploads/e/e2/Pme1.13.1_fixed_columns.gif)
- [Dummy Modal operator](https://wiki.blender.org/uploads/0/0d/Pme1.13.1_dummy_modal.gif)  
  Can be used to pause Macro Operator (press Enter or LMB to resume)
- Removed unstable [Auto-Close Popup Dialog](https://wiki.blender.org/uploads/e/ea/Pme1.13.0_adv_options.png) option
- Bug Fixes

## 1.13.0 (2017.02.19)
- [Macro Operator Editor](https://www.youtube.com/watch?v=x4HhN4aHCxg)
- [Command Generator](https://wiki.blender.org/uploads/f/f4/Pme_item_edit.png)
- [Poll method](https://wiki.blender.org/uploads/e/ea/Pme1.13.0_adv_options.png)
- [Auto-Close Popup Dialog](https://wiki.blender.org/uploads/e/ea/Pme1.13.0_adv_options.png)
- [Updated tree view & new Show Only New Menus filter](https://wiki.blender.org/uploads/9/9d/Pme_tree.png)
- Compatibility with Blender Tabs Interface add-on

## 1.12.1 (2016.12.12)
- [Sticky Key Editor](https://youtu.be/pcFOPWnHC7U)
- [Option to disable 'Confirm on Release' feature for pie menus](https://s3.amazonaws.com/markets-rails/uploads%2F1480675508687-pme1.12.0_confirm_on_release.png)

## 1.11.4 (2016.11.13)
- [Adding command using context menu](https://static-2.gumroad.com/res/gumroad/1512858036361/asset_previews/38ea290af3476c74fd8b832e4b4351de/retina/pme1.11.3_copy.gif)
- [Side panel editor](https://youtu.be/BGs0de6ZYdw)
- [Hiding unused panels](https://youtu.be/z19c6b7XOWo)
- [Restoring mouse position for pie menus](https://cgcookiemarkets.com/app/uploads/edd/2016/10/pme1.11.0_mouse_pos.jpg)
- [Using popup dialogs inside popup dialogs](https://cgcookiemarkets.com/app/uploads/edd/2016/10/pme1.11.0_expand_pd.jpg)

## 1.10.1 (2016.07.30)
- [Stack Keys](https://youtu.be/4wZKiyKE_P4)
- [Ability to use mouse buttons as a hotkey modifier](https://youtu.be/9cGWQF6L4o4)
- [Displaying the name of the last stack key command](https://cgcookiemarkets.com/app/uploads/edd/2016/07/pme1.10.1_sk_settings.png)
- [Context sensitive menus examples](https://youtu.be/m8pCPZdK_qc)

## 1.9.2 (2016.05.17)
- [Script editor](https://youtu.be/A81jLLynssk)
- [Double click mode](https://youtu.be/8XUvscCCviA)
- [Customizable Ctrl+Shift+` hotkey](https://cgcookiemarkets.com/app/uploads/edd/2016/04/pme1.9.0_prefs_settings.png)
- Hotkeys to confirm (Enter) and cancel (Esc) item/icon editing

## 1.8.3 (2016.04.08)
- [Panel mode and Panels](https://youtu.be/-fhI2imoo4U)
- [Sticky Keys](https://youtu.be/5zDp586Uy2w?t=57)
- [Threshold and Confirm Threshold for Pie Menus](https://youtu.be/5zDp586Uy2w)
- [Tree view](https://wiki.blender.org/uploads/9/9d/Pme_tree.png)
- Customizable width of the list/tree

## 1.7.0 (2016.02.16)
- [Custom layout using python code](https://youtu.be/sF10rVDVo-k)

## 1.6.0 (2016.01.19)
- Multi-column regular menus
- Open regular menu on mouse over

## 1.5.2 (2016.01.11)
- Copy/Paste Row (Popup dialog)
- Preview of the menus
- External python scripts as a command

## 1.4.1 (2015.12.09)
- Popup dialog editor
- Pie menus with more than 8 buttons

## 1.3.0 (2015.11.28)
- Custom icons
- Hotkey as a command

## 1.2.0 (2015.10.26)
- Regular menu editor
- Multiple keymap names
- New icon selection mode

## 1.1.5 (2015.10.15)
- Pie Menu Editor