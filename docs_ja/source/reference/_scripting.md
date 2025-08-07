(pme-scripting)=

# スクリプティング

PMEはBlenderの[Python API](https://docs.blender.org/api/current/)を使用した高度なカスタマイズと自動化を可能にします。
この記事では、PMEのスクリプティング機能の概要と、組み込みのグローバル変数と関数について説明します。

## チュートリアル

- **動画**: [Introduction to Scripting with Python in Blender (vimeo.com)](https://vimeo.com/28203314)
- **動画**: [Task Automation with Python Scripting in Blender (youtube.com)](https://www.youtube.com/watch?v=ZZWSvUgR38Y)
- [Python for Non-Programmers (python.org)](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
- [Blender Python API](https://docs.blender.org/api/current/)
- [Blender/Python Quickstart](https://docs.blender.org/api/current/info_quickstart.html)

## グローバル変数

PMEでは以下のグローバル変数が利用できます:

### `menu`
アクティブなメニューの名前を取得します。

### `slot`
アクティブなスロットの名前を取得します。

### `C`
[bpy.context](https://docs.blender.org/api/current/bpy.context.html)のショートカットです。
Blenderの現在のコンテキスト（選択オブジェクト、モードなど）にアクセスできます。

```python
ao = C.active_object; ao and ao.type == 'MESH' and message_box("Mesh Selected")
```

### `D`
[bpy.data](https://docs.blender.org/api/current/bpy.data.html)のショートカットです。
Blenderのデータブロック（メッシュ、マテリアル、テクスチャなど）にアクセスできます。

```python
m = [m for m in D.meshes if m.name == 'My Mesh']; m and setattr(m, 'name', 'New Name')
```

### `O`
[bpy.ops](https://docs.blender.org/api/current/bpy.ops.html)のショートカットです。
Blenderのオペレーター（コマンド）を実行できます。

```python
O.mesh.select_all(action='TOGGLE')
```

### `T`
[bpy.types](https://docs.blender.org/api/current/bpy.types.html)のショートカットです。
Blenderのデータタイプとクラス定義にアクセスできます。

### `P`
[bpy.props](https://docs.blender.org/api/current/bpy.props.html)のショートカットです。
Blenderのプロパティタイプ（IntProperty、StringPropertyなど）にアクセスできます。

### `L`
現在の[UILayout](https://docs.blender.org/api/current/bpy.types.UILayout.html)オブジェクトです。
UI要素（ボタン、ラベル、プロパティフィールドなど）を描画するために使用します。

```python
L.box().label(text="My Label")
```

### `E`
現在の[Event](https://docs.blender.org/api/current/bpy.types.Event.html)オブジェクトです。
マウスやキーボードの入力状態を取得できます。

```python
E.ctrl and E.shift and message_box("Ctrl+Shift Pressed")
```

### `U`
ユーザーデータ保存用の[pme.UserData](#pme.UserData)インスタンスです。
Blenderセッション中にカスタムデータを保存・取得できます。

```python
U.foo = "value"
U.update(foo="value1", bar="value2")
U.foo
U.get("foo", "default_value")
```

## グローバル関数

以下はPMEが提供するグローバル関数のリストです。

(pme-common-functions)=

### 共通関数

````{py:function} execute_script(path, **kwargs)
:noindex:

外部のPythonスクリプトを実行します。

**Parameters:**
- **path** (`str`) -- `.py`ファイルへのパス。
- **kwargs** -- スクリプトに渡される追加のキーワード引数。

**Returns:**
  ローカル変数`return_value`が存在する場合はその値、存在しない場合は`True`。

**例**:

```python
# 'Hello World!'メッセージを表示:
execute_script("scripts/hello_world.py", msg="Hello World!")

# scripts/hello_world.py:
# message_box(kwargs["msg"])

# 'Hi!'メッセージを表示:
message_box(execute_script("scripts/hi.py"))

# scripts/hi.py:
# return_value = "Hi!"
```
````

````{py:function} props(name=None, value=None)
:noindex:

PMEプロパティの値を取得または設定します。

**Parameters:**
- **name** (`str`, optional) -- プロパティの名前。
- **value** (optional) -- プロパティの新しい値。

**Returns:**
  `name`が`None`の場合はPMEプロパティコンテナ、`name`のみ指定された場合はプロパティの値、値を設定する場合は`True`。

**例**:

```python
# 文字列記法を使ってプロパティ値を取得
value = props("MyProperty")

# 代替: 属性記法を使ってプロパティを取得
value = props().MyProperty  # props()はプロパティコンテナを返す

# 文字列記法を使ってプロパティ値を設定
props("MyProperty", value)

# 代替: 属性記法を使ってプロパティを設定
props().MyProperty = value  # props()はプロパティコンテナを返す
```
````

````{py:function} paint_settings()
:noindex:

コンテキストに依存するペイント設定を取得します。

**Returns:**
  現在のペイント設定、またはペイントモードでない場合は`None`。

**例**:

```python
ps = paint_settings(); ps and L.template_ID_preview(ps, 'brush')
```
````

````{py:function} find_by(collection, key, value)
:noindex:

`collection`内で`key`が`value`と等しい最初のアイテムを検索します。

**Parameters:**
- **collection** -- 検索対象のコレクション。
- **key** (`str`) -- 検索するキー。
- **value** -- 検索する値。

**Returns:**
  見つかった場合はコレクションアイテム、見つからない場合は`None`。

**例**:

```python
m = find_by(C.active_object.modifiers, "type", 'SUBSURF')
```
````

````{py:function} setattr(object, name, value)
:noindex:

Pythonの組み込み`setattr`と同じですが、設定後に`True`を返します。

**Parameters:**
- **object** -- 属性を設定するオブジェクト。
- **name** (`str`) -- 属性名。
- **value** -- 設定する値。

**Returns:**
  `True`
````

(pme-command-tab-functions)=

### コマンドタブ関数

````{py:function} open_menu(name, slot=None, **kwargs)
:noindex:

名前でメニュー、パイメニュー、ポップアップダイアログを開くか、スタックキー、スティッキーキー、モーダルオペレーター、またはマクロオペレーターを実行します。

**Parameters:**
- **name** (`str`) -- メニューの名前。
- **slot** (optional) -- スタックキー実行のためのスロットのインデックスまたは名前。
- **kwargs** -- ローカル変数として使用されるモーダル/マクロオペレーターの引数。

**Returns:**
  メニューが存在する場合は`True`、存在しない場合は`False`。

**例**:

```python
# アクティブなオブジェクトのタイプに応じてメニューを開く:
open_menu("Lamp Pie Menu" if C.active_object.type == 'LAMP' else "Object Pie Menu")

# Ctrlモディファイアに応じて"My Stack Key"スロットを呼び出す:
open_menu("My Stack Key", "Ctrl slot" if E.ctrl else "Shift slot")
```
````

````{py:function} toggle_menu(name, value=None)
:noindex:

メニューを有効または無効にします。

**Parameters:**
- **name** (`str`) -- メニューの名前。
- **value** (`bool`, optional) -- 有効にする場合は`True`、無効にする場合は`False`、切り替える場合は`None`。

**Returns:**
  メニューが存在する場合は`True`、存在しない場合は`False`。
````

````{py:function} tag_redraw(area=None, region=None)
:noindex:

UIエリアまたはリージョンを再描画します。

**Parameters:**
- **area** (`str`, optional) -- 再描画するArea.type。`None`の場合は全エリアを再描画。
- **region** (`str`, optional) -- 再描画するRegion.type。`None`の場合は全リージョンを再描画。

**Returns:**
  `True`
````

````{py:function} close_popups()
:noindex:

すべてのポップアップダイアログを閉じます。

**Returns:**
  `True`
````

````{py:function} overlay(text, **kwargs)
:noindex:

オーバーレイメッセージを描画します。

**Parameters:**
- **text** (`str`) -- 表示するメッセージ。
- **kwargs** -- オプションパラメータ:
  - `alignment`: `['TOP', 'TOP_LEFT', 'TOP_RIGHT', 'BOTTOM', 'BOTTOM_LEFT', 'BOTTOM_RIGHT']`のいずれか。デフォルトは`'TOP'`。
  - `duration`: 秒単位の表示時間。デフォルトは`2.0`。
  - `offset_x`: 水平オフセット。デフォルトは`10`px。
  - `offset_y`: 垂直オフセット。デフォルトは`10`px。

**Returns:**
  `True`

**例**:

```python
overlay('Hello PME!', offset_y=100, duration=1.0)
```
````

````{py:function} message_box(text, icon='INFO', title="Pie Menu Editor")
:noindex:

メッセージボックスを表示します。

**Parameters:**
- **text** (`str`) -- 表示するメッセージ。
- **icon** (`str`, optional) -- アイコン名（例: 'INFO', 'ERROR', 'QUESTION'など）。
- **title** (`str`, optional) -- ウィンドウタイトル。

**Returns:**
  `True`
````

````{py:function} input_box(func=None, prop=None)
:noindex:

入力ボックスを表示します。

**Parameters:**
- **func** (optional) -- 入力値で呼び出す関数。
- **prop** (`str`, optional) -- 編集するプロパティへのパス。

**Returns:**
  `True`

**例**:

```python
# オブジェクト名を変更:
input_box(prop="C.active_object.name")

# 入力値を表示:
input_box(func=lambda value: overlay(value))
```
````

(pme-custom-tab-functions)=

### カスタムタブ関数

````{py:function} draw_menu(name, frame=True, dx=0, dy=0)
:noindex:

別のポップアップダイアログまたはパイメニュー内にポップアップダイアログを描画します。

**Parameters:**
- **name** (`str`) -- メニューの名前（ポップアップダイアログ）。
- **frame** (`bool`, optional) -- フレームを描画するかどうか。
- **dx** (`int`, optional) -- 水平オフセット。
- **dy** (`int`, optional) -- 垂直オフセット。

**Returns:**
  ポップアップダイアログが存在する場合は`True`、存在しない場合は`False`。
````

````{py:function} operator(layout, operator, text="", icon='NONE', emboss=True, icon_value=0, **kwargs)
:noindex:

UILayout.operator()と似ていますが、オペレータープロパティの設定が可能です。

**Parameters:**
- **layout** -- UILayoutインスタンス。
- **operator** (`str`) -- オペレーターの識別子。
- **text** (`str`, optional) -- ボタンのテキスト。
- **icon** (`str`, optional) -- アイコン名。
- **emboss** (`bool`, optional) -- ボタンのエンボス。
- **icon_value** (`int`, optional) -- アイコンの値。
- **kwargs** -- オペレータープロパティ。

**Returns:**
  OperatorPropertiesオブジェクト。

**例**:

```python
operator(L, "wm.context_set_int", "Material Slot 1",
        data_path="active_object.active_material_index", value=0)

# 以下と同じ:
# op = L.operator("wm.context_set_int", text="Material Slot 1")
# op.data_path = "active_object.active_material_index"
# op.value = 0
```
````

````{py:function} custom_icon(filename)
:noindex:

カスタムアイコンに関連付けられた整数値を取得します。

**Parameters:**
- **filename** (`str`) -- `pie_menu_editor/icons/`にある拡張子なしのアイコンファイル名。

**Returns:**
  カスタムアイコンの整数値。

**例**:

```python
L.label(text="My Custom Icon", icon_value=custom_icon("p1"))
```
````

````{py:function} panel(id, frame=True, header=True, expand=None)
:noindex:

IDでパネルを描画します。

**Parameters:**
- **id** (`str`) -- パネルのID。
- **frame** (`bool`, optional) -- フレーム付きパネルを描画。
- **header** (`bool`, optional) -- パネルヘッダーを描画。
- **expand** (optional) -- 展開する場合は`True`、折りたたむ場合は`False`、現在の状態を使用する場合は`None`。

**Returns:**
  `True`

**例**:

```python
panel("MATERIAL_PT_context_material", True, True, True)
```
````

---

## 自動実行スクリプト

PMEでは、Blender起動時に自動実行されるPythonスクリプトを作成できます。
この機能を使用するには、以下のいずれかの方法で`pie_menu_editor/scripts/autorun`フォルダにファイルを配置します:

- 直接の`.py`ファイル
- スクリプトを含むフォルダ
- シンボリックリンク

```{warning}
`autorun`フォルダ内のスクリプトはPMEのコンテキストで直接実行されます。
信頼できるソースからのスクリプトのみを使用してください。
```

## カスタムグローバル関数の追加

PMEでカスタム関数を使用するには:

1. `pie_menu_editor/scripts/autorun`フォルダにスクリプトを配置
2. `pme.context.add_global()`を使用して関数を登録

例:

```python
def hello_world():
    print("Hello World")

pme.context.add_global("hello", hello_world)
```

登録された関数`hello()`は以下で利用可能になります:

- コマンドタブ
- カスタムタブ
- 外部スクリプト

## PMEコンポーネント

PMEは、よく使用される関数、変数、ユーザー定義の追加機能へのアクセスを提供するグローバルコンテキストを維持します。
このコンテキストは2つの主要なインターフェースを通じてアクセス可能です:

````{py:class} pme.context

```{py:attribute} globals
:type: dict

PMEのグローバルコンテキスト辞書にアクセスします。以下を含みます:

- 組み込みショートカット（`C`, `D`, `O`, `L`など）
- 登録されたカスタム関数と値
- ユーザーデータストレージ（`U`）

```

```python
from pie_menu_editor import pme

# 外部スクリプトからグローバルにアクセス
g = pme.context.globals
props = g.get('props')
user_data = g.get('U')
```


```{py:method} add_global(key, value)

グローバルコンテキストにカスタム関数または値を登録します。

:param str key: アイテムにアクセスするための名前
:param value: 登録する関数または値
:rtype: None

```

```python
# 関数を登録
def my_tool():
    bpy.ops.mesh.select_all(action='TOGGLE')

pme.context.add_global("toggle_select", my_tool)

# 定数を登録
pme.context.add_global("MAX_ITEMS", 10)

# PMEメニューからコマンドタブ経由でアクセス:
# toggle_select()
# MAX_ITEMS
```
````

````{py:class} pme.UserData

Blenderセッション中に持続するユーザー定義データの柔軟なストレージ。

```{py:method} get(name, default=None)

保存された値を取得します。

:param str name: データキー
:param default: キーが存在しない場合に返す値
:return: 保存された値またはデフォルト値
```

```{py:method} update(**kwargs)

複数の値を一度に更新します。

```
```python
U = pme.context.globals['U']  # UserDataインスタンスを取得
U.update(tool_state="active", count=5)
print(U.tool_state)  # "active"
```
````