(terminology)=

# 用語集

このページでは、Blenderの初心者やより深い理解を求める方に向けて、BlenderとPMEで使用される主要な用語と概念を説明します。

## Blenderの基本概念

### `bpy.context`
Blenderが入力処理・UI描画・オペレーター可用性を評価するための「評価環境」です。瞬間ごとに組み立てられる参照の束であり、直接編集する対象ではありません。

- 含まれる参照: window/screen/workspace/area/region/space_data、scene/view_layer/object（アクティブ/選択）、mode、active_tool など
- これで決まる: キーマップの解決、オペレーターの poll 可否、UIの分岐、既定の作用先
- 操作の原則: 値を変えるときは `bpy.data` を更新し、別の場所で実行したい場合は一時オーバーライドを用います。

```python
area = next(a for a in bpy.context.window.screen.areas if a.type == 'VIEW_3D')
with bpy.context.temp_override(area=area):
    bpy.ops.view3d.view_selected('INVOKE_DEFAULT')
```

**リファレンス**: [Context (docs.blender.org)](https://docs.blender.org/api/current/bpy.context.html)

### `bpy.data`
保存される「データブロック」の集合（シーン、オブジェクト、メッシュ、マテリアル等）です。`.blend`ファイルに永続化されるモデルであり、`bpy.context`（評価環境）と対になる概念です。

- 主なデータ: scenes、objects、meshes、materials、images など
- 用途: プロパティを読み書きし、変更を永続化。次のイベント/描画でコンテキストとUIに反映されます。

```python
obj = bpy.data.objects.get('Cube')
if obj: obj.location.x += 1.0
```

**リファレンス**: [Data (docs.blender.org)](https://docs.blender.org/api/current/bpy.types.BlendData.html)

::::{admonition} ポイント
:class: hint

データ（`bpy.data`）＝保存されるモデルに対し、コンテキスト（`bpy.context`）＝瞬間ごとに組み立てられる参照です。

::::


### モード（Mode）
Blenderの**動作状態**（オブジェクトモード、編集モードなど）を指します。
各モードにはそれぞれのツールとアクションのセットがあります。

- PMEの**Poll**機能により、アクティブなモードに基づいて特定のツールやメニューの表示/非表示を切り替えできます。

**例**: `bpy.context.mode == 'EDIT_MESH'`


### キーマップ（Keymap）
エリアタイプや編集モードに応じて変化する**ホットキー割り当て**のコレクションです。

- 例: **G**キーはオブジェクトモードでは「移動」に割り当てられていますが、スカルプトモードでは「つかむ」に割り当てられています。

PMEは、これらのキーマップを個人のワークフローに合わせてさらにカスタマイズするのに役立ちます。

**リファレンス**: [Keymap (docs.blender.org)](https://docs.blender.org/manual/en/latest/editors/preferences/keymap.html)


### オペレーター（Operator）
Blenderで特定のアクションを実行する機能単位（`bpy.ops`モジュールの一部）です。

- ホットキーに割り当て可能
- メニュー/ボタンに表示可能
- Pythonスクリプトから呼び出し可能
- マクロで実行可能

PME内では、**マクロオペレーター**や**モーダルオペレーター**を使用して複数のオペレーターを組み合わせ、カスタムツールを作成できます。

**例**: `bpy.ops.mesh.subdivide()`


### プロパティ（Property）
Blenderの様々なデータ項目（オブジェクトの位置、マテリアル設定など）を指し、通常UIではスライダー、チェックボックス、フィールドとして表示されます。

PMEでは以下が可能です:

- メニュー/パネルでプロパティの表示と編集
- スクリプトやPoll関数での参照
- プロパティエディターを介したカスタムプロパティの追加

**例**: `bpy.context.object.location`


## 画面構成の概念

### エリア（Area）
Blenderインターフェース内の大きなワークスペース領域です。
3Dビューポート、アウトライナーなどの異なるエディタータイプはそれぞれ**エリア**を占有します。

- PMEは**サイドエリア切り替え**機能を提供し、エリア内のサイド領域（サイドバーなど）の表示/非表示を切り替えることができます。
- エリアには、ツールバーやプロパティシェルフなどの**リージョン**と呼ばれるサブ領域が含まれる場合があります。

| **関連**: リージョン、ウィンドウ、ワークスペース
| **リファレンス**: [Area (docs.blender.org)](https://docs.blender.org/manual/en/latest/interface/window_system/areas.html)


### リージョン（Region）
**エリア**内の細分化された領域で、特定のUI要素（ツール、プロパティなど）を含みます。

- PMEの**パネルグループ**機能により、リージョンにカスタムコンテンツを追加できます。

**関連**: エリア、パネル

**リファレンス**: [Region (docs.blender.org)](https://docs.blender.org/manual/en/latest/interface/window_system/regions.html)


### ヘッダー（Header）
エリアの上部または下部にある水平バーです。
通常、メニュー、よく使用されるツールアイコンなどが含まれます。

- PMEでは{ref}`メニュー/パネル拡張 <pme-menu-panel-extension>`を使用してヘッダーにカスタムボタンを追加できます。

| **関連**: リージョン
| **リファレンス**: [Header (docs.blender.org)](https://docs.blender.org/manual/en/latest/interface/window_system/regions.html#header)


### パネル（Panel）
サイドバーやプロパティエリアによく見られる、折りたたみ可能なUIウィジェットのグループです。

PMEでは以下が可能です:

- 新しいパネルの作成
- 既存パネルの拡張
- パネルのグループ化
- 不要なパネルの非表示

| **関連**: プロパティ、リージョン
| **リファレンス**: [Panel (docs.blender.org)](https://docs.blender.org/manual/en/latest/interface/window_system/tabs_panels.html)


## PME固有の概念

### メニュー（Menu）
PMEで作成するカスタマイズ可能なUIコンポーネントを表す広義の用語で、以下を含みます:

- パイメニュー
- 通常メニュー
- マクロオペレーター
- モーダルオペレーター
- など

各メニューは複数の**スロット**で構成され、それぞれが異なる機能や要素を提供します。

### スロット（Slot）
メニュー内の個別の**要素**または**スロット**です。各スロットは以下のように設定できます:

- コマンドの実行
- プロパティの表示または編集
- サブメニューの呼び出し
- カスタムレイアウトの描画

**関連**: コマンドタブ、プロパティタブ、メニュータブ、カスタムタブ

### コマンドタブ（Command Tab）
スロットエディターのタブの一つで、Pythonコードを実行したり、オペレーターを直接呼び出したりできます。

- 1行のPythonスクリプトの実行
- カスタム関数の呼び出し
- 変数やオペレーターの操作

**例**: `C.active_object.location.x += 1.0`

### カスタムタブ（Custom Tab）
手動スクリプティングなしでより視覚的に定義されたUIレイアウトを作成するためのスロットエディターの別タブです。

**例**:

```python
L.box().label(text="Custom Layout")
```

### インタラクティブパネルモード（Interactive Panels Mode）
すべてのUI要素内に追加のPMEツールボタンを表示するPMEモードで、以下を簡単にします:

- メニューIDの識別
- パネル拡張の設定
- UIのカスタマイズ

このモードは、様々な要素やメニューがどこに配置されているかを視覚化するのに役立つため、PMEを学習する際に特に有用です。

### マクロオペレーター（Macro Operator）
**複数のオペレーターを順番に実行**することを可能にします。
PME**マクロオペレーターエディター**では以下が可能です:

- オペレーターシーケンスの記録
- オペレーターパラメーターの調整
- 実行フローの管理

複雑なワークフローを1クリックにまとめるのに非常に有用です。

### モーダルオペレーター（Modal Operator）
継続的なユーザー入力に応答するリアルタイムでインタラクティブなオペレーターです。
PMEの**モーダルオペレーターエディター**で独自のモーダルオペレーターを作成でき、以下が可能になります:

- マウス移動への反応
- キーイベントと状態変化
- リアルタイムフィードバックと更新

**カスタムインタラクティブツール**の構築に最適です。

### Poll メソッド（Poll Method）
メニューやツールが**現在使用可能かどうか**を判定するPython関数です。使用可能な場合は`True`、そうでない場合は`False`を返す必要があります。

例:

```python
ao = C.active_object; return ao and ao.type == 'MESH'
```

一般的な使用例:

- 現在のモードに基づいたUI要素の有効/無効
- 特定のオブジェクトタイプに機能を制限
- 無効なツールを非表示にしてエラーを防止

### スロットエディター（Slot Editor）
PMEメニュー/ボタンの動作を定義する**中央UI**です。以下のような複数のタブが含まれます:

- コマンド（コード実行用）
- プロパティ（プロパティ表示用）
- メニュー（他のPMEメニューの呼び出し用）
- ホットキー（ショートカット呼び出し用）
- カスタム（カスタムレイアウト用）

スクリプティングが初めての場合でも、グラフィカルインターフェースを通じてすべてを設定できるように設計されています。

## 高度な概念

### イベントシステム（Event System）
キーボードとマウスイベントを追跡するBlenderの入力処理メカニズムです。以下に不可欠です:

- モーダルオペレーター
- カスタムホットキー
- インタラクティブツール

例:

```python
E.ctrl and E.shift and message_box("Ctrl+Shift Pressed")
```

### レイアウトシステム（Layout System）
UIレイアウトを構築するBlenderのシステムです。PMEはこのシステムに依存して以下を行います:

- ラベル、ボタン、プロパティフィールドの配置
- オペレーターとカスタムウィジェットの位置決め
- UI要素の階層構造化

例:

```python
L.box().label(text=text, icon=icon, icon_value=icon_value)
```

### オペレーター実行コンテキスト（Operator Execution Context）
オペレーターの実行方法を決定します。最も一般的な2つのコンテキストは:

- **INVOKE_DEFAULT**  
  Blenderがマウス位置決めやポップアップ確認などの追加ユーザー入力を待つインタラクティブモード。

- **EXEC_DEFAULT**  
  事前設定されたパラメーターでオペレーターを即座に実行。スクリプトやマクロでよく使用される。

**例**:

```python
# マウス入力に基づいてオブジェクトをインタラクティブに移動
bpy.ops.transform.translate('INVOKE_DEFAULT')

# ユーザー入力なしでオブジェクトをX軸に沿って5.0移動
bpy.ops.transform.translate('EXEC_DEFAULT', value=(5.0, 0.0, 0.0))
```

| **関連**: オペレーター、コマンドタブ、モーダルオペレーター、マクロオペレーター
| **リファレンス**: [Execution Context (docs.blender.org)](https://docs.blender.org/api/current/bpy.ops.html#execution-context)