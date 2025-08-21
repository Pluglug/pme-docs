# Keymapの選び方

:::{figure} /_static/images/reference/keymap_selection.png
:width: 100%
:align: center

PMEのHotkey設定画面。
:::

## そもそもKeymapって何？

:::{image} /_static/images/reference/keymap_prefs.png
:alt: PreferencesのKeymap設定
:width: 40%
:align: right
:::

**Keymap**は、Blenderの入力イベントを[コンテキスト](terminology.md#bpy-context)階層（モード → エディタ → 全体共通）で解決する仕組みです。

たとえば、`G`キーはオブジェクトの移動ですが、スカルプトモードではグラブツールになります。`F`キーはメッシュ編集では面の作成（Fill）、スカルプトではブラシ半径の変更になります。

このように、状況に応じてショートカットキーと機能を結びつけるのがKeymapです。


## どうやって判断しているの？

BlenderのKeymapは**階層構造**をもっており、エディタータイプや編集モードごとにHotkey設定が格納されています。

```
Window / Screen
├── 3D View (3D Viewエリア全体)
│   ├── Mesh (メッシュ編集モード)
│   ├── Object Mode (オブジェクトモード)
│   ├── Sculpt (スカルプトモード)
│   └── その他のモード...
├── Image Editor (画像エディタ)
├── Outliner (アウトライナー)
└── その他のエディタ...
```

実際にキーイベントが発生したときには[コンテキスト](terminology.md#bpy-context)をチェックして、**より具体的な**（*= 対象コンテキストの範囲が狭い*）Keymapを優先してHotkeyを走査します。

:::{mermaid}
flowchart TD
    A(キーが押される) --> B[1. Screen Editing をチェック]
    B --> C[/該当するキーがある？\]
    C -->|Yes| D[実行して終了]
    C -->|No| E[2. 各エディタのKeymap をチェック]
    E --> F[/モード固有/エディタ固有に該当する？\]
    F -->|Yes| G[モード固有/エディタ固有を実行して終了]
    F -->|No| H[3. Window / Screen をチェック]
    H --> I[/該当するキーがある？\]
    I -->|Yes| J[実行して終了]
    I -->|No| K[何も実行されない]
:::

<!-- 縦スペースを削減するため、{条件分岐}ではなく[/ループ\]を使用した -->

::::{list-table} キーマップ処理の優先度
:header-rows: 1
:widths: 24 16 60

* - レイヤー
  - 優先度
  - 主な対象・例
* - Modal Handlers
  - 最高
  - Screen Editing／モーダルオペレータ（Transform, Grab など）
* - Area/Region Handlers
  - 中
  - Tool固有（アクティブツール）／Mode固有（Mesh, Sculpt, Object Mode）／Editor固有（3D View, Image Editor など）
* - Window Handlers
  - 最低
  - Window／Screen
::::

:::{admonition} Screen Editing
:class: warning
Screen Editingは、**最高優先度**で処理される特殊なKeymapです。最優先で実行されるので動作が確実ですが、競合が起きやすく意図しない場面で発火してしまう可能性があります。

- まずはエディタ/モード固有で定義し、必要最小限のみScreen Editingに置く
- Poll条件を併用して発火条件を限定する
- 重要な既存キー(Tab, Space, LMB/RMBなど)は避ける。
:::


## Poll関数の併用

特定の条件でのみメニューを表示したい場合は、Poll Methodを組み合わせて使用します：

```python
# メッシュオブジェクトが選択されている場合のみ
ao = C.active_object; return ao and ao.type == 'MESH'

# 編集モードかつ面選択モードの場合のみ
return C.mode == 'EDIT_MESH' and C.tool_settings.mesh_select_mode[2]

# スカルプトモードかつDyntopoが有効な場合のみ
return C.mode == 'SCULPT' and C.active_object.use_dynamic_topology_sculpting
```

:::{hint}
Poll関数がFalseを返した場合、実行されずに次のKeymapアイテムのチェックに進みます。
:::


## よくあるケース

メッシュ編集モードでPie Menuを表示したい
: `Mesh`（モード専用）

スカルプト中のブラシ切り替えメニュー
: `Sculpt`（モード専用）

オブジェクトモードでメッシュオブジェクトが選択されている場合のみ
: `Object Mode` + Poll関数を使用

キーフレームに関する操作
: `Frames`（全エディタで共通）

どのエディタでも共通の作成メニュー
: `Window` or `Screen`（全体共通）

いつでもどこでも絶対に表示したい場合
: `Screen Editing`（競合注意）


<!-- 避けるべきケース -->
<!-- 既存のキーマップを探索してみると気付きがある。 -->
<!-- PMEのKeymapを直接編集するのはやめよう -->
<!-- コラム：キーマップの重複問題 -->
