(pie-menu-editor)=
# Pie Menu Editor

<div class="video-container">
   <iframe src="https://www.youtube.com/embed/COW109EjBsU" frameborder="0" allowfullscreen></iframe>
</div>

---


## エディター画面

### トップ

:::{image} /_static/images/editors/pie_menu/pie_ui_top.png
:alt: Pie Menu Editor Top
:width: 100%
:align: center
:::

- **有効性**: 有効/無効を切り替えます。

- **プレビュー**: プレビューを表示します。

- **アイテム選択**: エディタに表示するアイテムを切り替えます。

- **メニュー名**: 名前を変更します。

- **タグ**: タグを設定します。

- **ドキュメント**: ドキュメントを表示します。

- **詳細設定**: 詳細設定を表示します。

### Hotkey設定

:::{image} /_static/images/editors/pie_menu/pie_hotkey.png
:alt: Pie Menu Editor Hotkey
:width: 100%
:align: center
:::

Pie Menuを呼び出すHotkeyを設定します。
→ [Hotkeyの設定方法](../hotkeys/index.md)

### メニュースロット

:::{image} /_static/images/editors/pie_menu/pie_slots.png
:alt: Pie Menu Editor Slots
:width: 30%
:align: right
:::

8方向 + 最上部 + 最下部の10のメニュースロットを設定できます。
左から、スロット編集・アイコン設定・スロット表示名・詳細設定です。

::::{admonition} Expansion Tool
:class: seealso

Settings > General > Expand Slot Toolsを有効にすると、詳細設定メニューの編集ボタンが拡張されます。

:::{image} /_static/images/editors/pie_menu/pie_slot_tools.png
:alt: Pie Menu Slot Tools
:align: center
:::
::::

### 詳細設定メニュー

:::{image} /_static/images/editors/pie_menu/pie_advanced_settings.png
:alt: Pie Menu Editor Advanced Settings
:width: 40%
:align: right
:::

- **Pollメソッド**

- **Radius**

- **Threshold**

- **Confirm Threshold**

- **Confirm on Threshold**

---

## スロットエディタ

スロット編集をクリックすると、スロットエディタが表示されます。
各スロットの機能を設定できます。Pie Menuは5つの機能タイプがあります。

:::{image} /_static/images/editors/pie_menu/pie_slot_editor.png
:alt: Pie Menu Slot Editor
:align: center
:::

### Command

任意のPythonコマンドを実行します。
Python code that will be executed when the user clicks the button.

```python
# オペレーターを実行する
bpy.ops.object.mode_set(mode='OBJECT')

# 条件分岐を使用する
ao = C.active_object; ao and message_box("Mesh" if ao.type == 'MESH' else "Not a mesh")
```

:::{admonition} コマンドの記述方法

Blenderの文字列プロパティーは、複数行のコマンドを記述できません。
そのため、コマンドを記述する場合は、セミコロン(`;`)で区切る必要があります。

参考: [Pythonコマンドの記述方法](../python/index.md)

また、利用可能なグローバルは[Scripting](../reference/scripting.rst)を参照してください。

:::

### Property

Path to the object's property which will be displayed as a widget.

### Menu

Open/execute the menu, popup or operator when the user clicks the button. Or draw a popup dialog inside the current popup dialog or pie menu.

### Hotkey

Blender's hotkey that will be used to find and execute an operator assigned to it when the user clicks the button.

### Custom

Python code that will be used to draw custom layout of widgets.

```python
L.box().label(text, icon=icon, icon_value=icon_value)
```
