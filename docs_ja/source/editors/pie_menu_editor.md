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

- **有効性**: このパイメニューの有効/無効を切り替えます。無効にするとホットキーが無効化されます。

- **プレビュー**: パイメニューをプレビュー表示して、レイアウトを事前に確認できます。

- **アイテム選択**: エディタに表示するPMEアイテムを切り替えます。アイコンは現在のメニュータイプを示します。

- **メニュー名**: パイメニューの名前を設定・変更します。他のメニューから参照する際の識別子としても使用されます。

- **タグ**: メニューの分類・検索用のタグを設定します。複数のタグを設定可能です。

- **ドキュメント**: Pie Menu Editorのオンラインドキュメントを開きます。

- **詳細設定**: パイメニューの高度な[設定オプション](#id5)（Poll Method、Radius等）を表示・編集します。

### Hotkey設定

:::{image} /_static/images/editors/pie_menu/pie_hotkey.png
:alt: Pie Menu Editor Hotkey
:width: 100%
:align: center
:::

パイメニューを呼び出すホットキーを設定します。

#### キーマップ
Blenderのキーマップは階層構造になっており、適切なキーマップを選択することで既存のホットキーを上書きできます。既存のホットキーのキーマップとアクションを調べるには、**+ボタン**を押してください。

:::{admonition} 全てのホットキーを上書きする場合
:class: tip

すべての既存ホットキーを上書きしたい場合は**Screen Editing**キーマップを使用できます。ただし、**LMBホットキー**の場合は基本的なクリック機能を無効化しないよう注意が必要です。

詳細なキーマップの説明は[こちら](../hotkeys/index.md)を参照してください。
:::

**Keymap選択について：**
適切なKeymapの選択方法について詳しくは、[PME Keymap選択ガイド](../reference/keymap_selection_guide.md)を参照してください。

詳細なキーマップの説明は[こちら](../hotkeys/index.md)を参照してください。
:::

#### ホットキーモード
- **Press**: キーを押す
- **Hold**: キーを押し続ける  
- **Tweak**: キーを押しながらマウスを動かす
- **Double Click**: キーをダブルクリックする

#### モディファイア
**Any modifier**は、Ctrl、Shift、Alt、OSKeyの任意の組み合わせです。コンテキスト感応ツールの作成に使用できます。

```python
print("Ctrl is pressed" if E.ctrl else "Ctrl isn't pressed")
```

このアドオンでは**マウスボタンをホットキーモディファイアとして使用**できます。つまり、LMB+Tab、RMB+Tab、MMB+Tabなどのホットキーが使用可能です。

→ [詳細なホットキー設定方法](../hotkeys/index.md)

### メニュースロット

:::{image} /_static/images/editors/pie_menu/pie_slots.png
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

- **Poll Method**: メニューの表示条件を制御するPythonコードを設定します。条件が満たされない場合、メニューは表示されません。

- **Radius**: パイメニューの円の半径を設定します。デフォルト値（-1）で自動設定、カスタム値でアニメーションが無効化されます。

- **Threshold**: フリックモード時のマウス移動距離の閾値を設定します。この距離を超えるとスロットが選択されます。

- **Confirm Threshold**: フリックモード時の確定距離の閾値を設定します。この距離まで移動すると選択が確定されます。

- **Confirm on Threshold**: 閾値に達した時点で自動的に選択を確定するかどうかを設定します。

---

## スロットエディタ

スロット編集をクリックすると、スロットエディタが表示されます。
各スロットの機能を設定できます。Pie Menuは以下の機能タイプがあります：

:::{image} /_static/images/editors/pie_menu/pie_slot_editor.png
:alt: Pie Menu Slot Editor
:align: center
:::

### Command（コマンド）

ボタンがクリックされた時に実行される任意のPythonコードを設定します。

```python
# オペレーターを実行する
bpy.ops.object.mode_set(mode='OBJECT')

# 条件分岐を使用する (Ctrlを押していた場合はモンキーを追加、それ以外は立方体を追加)
O.mesh.primitive_monkey_add() if E.ctrl else O.mesh.primitive_cube_add()
```

:::{admonition} コマンドの記述方法
:class: important

Blenderの文字列プロパティーは、複数行のコマンドを記述できません。
そのため、複数のコマンドを記述する場合は、セミコロン(`;`)で区切る必要があります。

参考: [Pythonコマンドの記述方法](../python/index.md)

:::

:::{admonition} グローバル変数
:class: hint

**利用可能なグローバル変数の例：**
- `C`: bpy.context（現在のBlenderコンテキスト）
- `O`: bpy.ops（Blenderのオペレーター）
- `E`: event（イベント情報）

[こちら](../reference/scripting.rst)でさらに詳細なグローバル変数の一覧を確認できます。
:::


### Property（プロパティ）

オブジェクトのプロパティへのパスを指定し、ウィジェットとして表示します。
例：`bpy.context.object.location`でオブジェクトの位置を表示・編集できます。

:::{admonition} 高度なプロパティ操作
:class: tip

インデックス指定やより複雑なプロパティ操作が必要な場合は、[Property Editor](../editors/property_editor.md)を利用してください。
:::

### Menu（メニュー）

ボタンがクリックされた時にPME内で作成した他のメニューアイテムを呼び出します。
例：
- **Popup Dialog**を`Expand Popup Dialog`で表示
- **Regular Menu**を`Open on Mouse Over`で表示
- **Macro Operator**を実行

### Hotkey（ホットキー）

ボタンがクリックされた時に、指定されたBlenderのホットキーに割り当てられているオペレーターを検索して実行します。
例：`G`でGrab（移動）、`R`でRotate（回転）など、Blenderの標準ホットキーを利用できます。

### Custom（カスタム）

カスタムなウィジェットレイアウトを描画するためのPythonコードを設定します。
`L`はレイアウトオブジェクトを表し、Blenderのレイアウトシステムを使用してUIを構築できます。

```python
# ボックス内にラベルを表示
L.box().label(text=text, icon=icon, icon_value=icon_value)

# 複数のボタンを縦に配置
col = L.column(); operator(col, "mesh.primitive_cube_add", text="立方体"); operator(col, "mesh.primitive_uv_sphere_add", text="球")
```
