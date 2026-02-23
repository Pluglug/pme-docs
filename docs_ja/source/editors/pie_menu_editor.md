(pie-menu-editor)=
# Pie Menu Editor

<div class="video-container">
   <iframe src="https://www.youtube.com/embed/COW109EjBsU" frameborder="0" allowfullscreen></iframe>
</div>

---


## エディター画面

### トップ

:::{image} /_static/images/editors/pie_menu/pie_ui_top.png
:class: img-shadow
:alt: Pie Menu Editor Top
:width: 100%
:align: center
:::

:有効性:
  このパイメニューの有効/無効を切り替えます。無効にするとホットキーが無効化されます。

:プレビュー:
  パイメニューをプレビュー表示して、レイアウトを事前に確認できます。

:アイテム選択:
  エディタに表示するPMEアイテムを切り替えます。アイコンは現在のメニュータイプを示します。

:メニュー名:
  パイメニューの名前を設定・変更します。他のメニューから参照する際の識別子としても使用されます。

:タグ:
  メニューの分類・検索用のタグを設定します。複数のタグを設定可能です。

:ドキュメント:
  Pie Menu Editorのオンラインドキュメントを開きます。

:詳細設定:
  パイメニューの高度な[設定オプション](#id5)（Poll Method、Radius等）を表示・編集します。

### Hotkey設定

```{include} common/hotkey_settings.md
```

### メニュースロット

:::{image} /_static/images/editors/pie_menu/pie_slots.png
:class: img-shadow
:alt: Pie Menu Editor Slots
:width: 30%
:align: right
:::

パイメニューは**10個のスロット**で構成されています：
- **8方向**：上下左右・斜め4方向
- **最上部・最下部**：垂直方向の追加スロット

各スロットの構成要素（左から右へ）：
1. **スロット編集ボタン**: スロットエディタを開いて機能を設定
2. **アイコン設定**: スロットに表示するアイコンを選択
3. **表示名**: スロットのラベルテキストを設定
4. **詳細設定**: スロット固有の追加オプション

::::{admonition} Expansion Tool
:class: seealso

Settings > General > Expand Slot Toolsを有効にすると、詳細設定メニューの編集ボタンが拡張されます。

:::{image} /_static/images/editors/common/slot_tools.png
:class: img-shadow
:alt: Pie Menu Slot Tools
:align: center
:width: 80%
:::
::::

### 詳細設定メニュー

:::{image} /_static/images/editors/pie_menu/pie_advanced_settings.png
:class: img-shadow
:alt: Pie Menu Editor Advanced Settings
:width: 40%
:align: right
:::

- **Poll Method**: メニューの表示条件を制御するPythonコードを設定します。条件が満たされない場合、メニューは表示されません。

- **Radius**: パイメニューの円の半径を設定します。デフォルト値（-1）で自動設定、カスタム値でアニメーションが無効化されます。

- **Threshold**: フリックモード時のマウス移動距離の閾値を設定します。この距離を超えるとスロットが選択されます。

- **Confirm Threshold**: フリックモード時の確定距離の閾値を設定します。この距離まで移動すると選択が確定されます。

- **Confirm on Threshold**: 閾値に達した時点で自動的に選択を確定するかどうかを設定します。

---

## スロットエディタ

スロット編集をクリックすると、スロットエディタが表示されます。
各スロットの機能を設定できます。Pie Menuは以下の機能タイプがあります：

:::{image} /_static/images/editors/common/slot_editor.png
:class: img-shadow
:alt: Pie Menu Slot Editor
:align: center
:width: 100%
:::

<div style="margin: 1.5rem 0;"></div>

### トップ

- **アイコン**: スロットに表示するアイコンを選択します。

- **表示名**: スロットのラベルテキストを設定します。{octicon}`arrow-left`ボタンを押すと、提案名を適用します。

- **OK / Cancel**: スロットの選択を確定・キャンセルします。Enter / Escape キーでも確定できます。

### タブ

5つの機能タイプから選択します：

::::{tab-set}

:::{tab-item} Command
:sync: command

```{include} common/slot_types/command.md
```
:::

:::{tab-item} Property
:sync: property

```{include} common/slot_types/property.md
```
:::

:::{tab-item} Menu
:sync: menu

```{include} common/slot_types/menu.md
```
:::

:::{tab-item} Hotkey
:sync: hotkey

```{include} common/slot_types/hotkey.md
```
:::

:::{tab-item} Custom
:sync: custom

```{include} common/slot_types/custom.md
```
:::
::::

### Examples

```{include} common/slot_types/examples.md
```
