# PME Keymap選択ガイド

PMEでカスタムメニューを作成する際、適切なKeymapを選択することは重要です。
このガイドでは、Blenderのキーマップシステムの仕組みを理解し、目的に応じた最適なKeymapを選択する方法を説明します。

## Blenderキーマップの基本構造

### 実際の優先度順序

Blenderでキーが押された時、以下の順序でKeymapがチェックされます：

```
【優先度：高→低】

1. Modal Handlers（最高優先度）
   ├── Screen Editing ← 例外的に最優先！
   └── Modal Operators（Transform、Grab等）

2. Area/Region Handlers（中間優先度）
   ├── Tool固有（アクティブツール）
   ├── Mode固有（Mesh、Sculpt、Object Mode等）
   └── Editor固有（3D View、Image Editor等）

3. Window Handlers（最低優先度）
   ├── Window
   └── Screen
```

### Screen Editingの特殊性

:::{admonition} Screen Editingの注意点
:class: warning

**Screen Editing**は名前に反して「全体共通Keymap」ではありません。
実際には**最高優先度**で処理される特殊なKeymapです。

- **通常の期待**: 全体共通 → 最低優先度
- **実際の動作**: Modal Handler → **最高優先度**

PMEでScreen Editingを使用する場合は、他のすべてのKeymapより優先されることを理解した上で慎重に使用してください。
:::

### 優先度の仕組み
1. **Screen Editing** - **最高優先度**（例外的）
2. **Tool/Mode固有のKeymap** (例: `Mesh`, `Sculpt`) - 高優先度
3. **エディタ固有のKeymap** (例: `3D View`, `Image Editor`) - 中優先度  
4. **Window/Screen** - 最低優先度

## 主要なKeymap一覧

### 3D View関連

#### モード別Keymap（高優先度）

:::{list-table} 3D Viewモード別Keymap
:header-rows: 1
:widths: 25 25 50

* - Keymap名
  - 対応モード
  - 用途・説明
* - `Mesh`
  - Edit Mode (Mesh)
  - メッシュ編集時の操作。頂点・辺・面の選択や変形に最適
* - `Object Mode`
  - Object Mode
  - オブジェクトの選択・移動・追加・削除など基本操作
* - `Sculpt`
  - Sculpt Mode
  - スカルプト専用の操作。ブラシ切り替えやスカルプト設定
* - `Weight Paint`
  - Weight Paint Mode
  - ウェイトペイント時の操作。ブラシ設定やウェイト調整
* - `Vertex Paint`
  - Vertex Paint Mode
  - 頂点ペイント時の操作。色の塗り分けや設定
* - `Pose`
  - Pose Mode
  - アーマチュアのポーズ設定。ボーンの選択・回転・IK
* - `Armature`
  - Edit Mode (Armature)
  - アーマチュア編集。ボーンの追加・削除・調整
* - `Curve`
  - Edit Mode (Curve)
  - カーブ・NURBS編集。制御点やハンドル操作
* - `Font`
  - Edit Mode (Text)
  - テキストオブジェクト編集。文字入力や書式設定
:::

#### 特殊なKeymap

:::{list-table} 3D View特殊Keymap
:header-rows: 1
:widths: 25 50 25

* - Keymap名
  - 説明
  - 優先度
* - `Paint Face Mask`
  - ペイントモードでのフェースマスク操作
  - 最高
* - `Paint Vertex Selection`
  - ペイントモードでの頂点選択操作
  - 最高
* - `3D View Generic`
  - 3D View共通操作（ビュー回転、ズーム等）
  - 低
* - `3D View`
  - 3D Viewの基本操作
  - 最低
:::

### エディタ別Keymap

:::{list-table} 主要エディタのKeymap
:header-rows: 1
:widths: 25 25 50

* - エディタ
  - Keymap名
  - 用途
* - **画像エディタ**
  - `Image Editor`
  - UV展開、テクスチャペイント
* - **ノードエディタ**
  - `Node Editor`
  - マテリアル・ジオメトリノード編集
* - **アウトライナー**
  - `Outliner`
  - オブジェクト階層の管理
* - **プロパティパネル**
  - `Property Editor`
  - オブジェクト・マテリアルプロパティ
* - **ドープシート**
  - `Dopesheet`
  - アニメーションキーフレーム編集
* - **タイムライン**
  - `Timeline`
  - アニメーション再生・時間制御
:::

### 全体共通Keymap

全体共通Keymapは、Blenderのどのエディタ・どのモードでも使用できるKeymapです。
ただし、それぞれ**処理される優先度**が異なるため、理解して使い分ける必要があります。

#### 階層システムにおける位置づけ

全体共通Keymapは、階層システムの中で以下の位置にあります：

```
【Blenderキーマップ階層】

モード固有Keymap (最高優先度)
├── Mesh, Sculpt, Object Mode等
│
エディタ固有Keymap (中間優先度) 
├── 3D View, Image Editor, Node Editor等
│
全体共通Keymap (最低優先度)
├── Screen Editing ← モード固有よりも優先度が高い
├── Window      ← 中間  
└── Screen      ← 最低
```

:::{list-table} 全体共通Keymap概要
:header-rows: 1
:widths: 25 25 50

* - Keymap名
  - 優先度
  - 特徴
* - `Screen Editing`
  - **最高**
  - 全体共通の中で最優先。重要な編集操作
* - `Window`
  - **中間**
  - アプリケーション全体のファイル・設定操作
* - `Screen`
  - **最低**
  - 画面レイアウト・ワークスペース管理
:::

#### Screen系Keymapの詳細な仕組み

BlenderのScreen系Keymapは似た名前で混乱しやすいですが、実際には**処理される順番**が異なります。この仕組みを理解することで、PMEで意図した通りの動作を実現できます。

#### キーが押された時の処理の流れ

キーボードやマウスが押された時、Blenderは以下の順番でKeymapをチェックします：

```{mermaid}
flowchart LR
    A[キーが押される] --> B[1. Screen Editing をチェック]
    B --> C{該当するキーがある？}
    C -->|Yes| D[実行して終了]
    C -->|No| E[2. 各エディタのKeymap をチェック]
    E --> F{該当するキーがある？}
    F -->|Yes| G[実行して終了]  
    F -->|No| H[3. Window / Screen をチェック]
    H --> I{該当するキーがある？}
    I -->|Yes| J[実行して終了]
    I -->|No| K[何も実行されない]
```

#### 3つのScreen系Keymapの特徴

**🥇 Screen Editing（最優先）**
- **いつ実行される**: 他のすべてより**先に**チェックされる
- **どこで使える**: Blenderのどの場所でも
- **既存の例**: `Tab`（編集モード切り替え）、`G`（移動）、`R`（回転）
- **PMEで使うべき場面**: 「**絶対に実行したい**」重要な機能

**🥈 Window（後で実行）**  
- **いつ実行される**: Screen Editingやエディタ固有のKeymapで処理されなかった場合
- **どこで使える**: Blenderのどの場所でも
- **既存の例**: `Ctrl+S`（保存）、`Ctrl+O`（開く）、`Ctrl+N`（新規作成）
- **PMEで使うべき場面**: ファイル操作や全体的な設定

**🥉 Screen（最後に実行）**
- **いつ実行される**: WindowやScreen Editingで処理されなかった場合
- **どこで使える**: Blenderのどの場所でも
- **既存の例**: ワークスペース切り替え、画面レイアウト操作
- **PMEで使うべき場面**: レイアウトやワークスペース関連

#### 実際の使い分け例

**🎯 良い使い分けの例**

```
Screen Editing: Shift+A → 「追加メニュー」
↳ どのエディタでも必ず実行したい重要なメニュー

Window: Ctrl+Alt+S → 「設定メニュー」  
↳ アプリケーション全体の設定を変更するメニュー

Screen: Alt+W → 「ワークスペース切り替えメニュー」
↳ レイアウト変更に関するメニュー
```

**❌ 問題が起こる例**

```
同じShift+Aキーを複数のKeymapに登録した場合：

Screen Editing: Shift+A → 「重要メニュー」 ← これが実行される
3D View: Shift+A → 「3D用メニュー」      ← 実行されない  
Window: Shift+A → 「ファイルメニュー」   ← 実行されない
```

#### わかりやすい選択方法

:::{list-table} どのKeymapを選ぶべきか
:header-rows: 1
:widths: 30 35 35

* - あなたの用途
  - 推奨Keymap
  - 理由
* - **絶対に実行したい重要機能**
  - `Screen Editing`
  - 最優先で処理される
* - **ファイル・設定系の操作**
  - `Window`
  - アプリ全体に関わる操作に適している
* - **画面レイアウト・ワークスペース**
  - `Screen`
  - レイアウト関連の操作に適している
* - **特定のエディタでのみ使いたい**
  - `3D View`、`Mesh`等
  - そのエディタ・モードでのみ動作
:::

#### 初心者向けの推奨事項

1. **最初は`Screen Editing`を試す**
   - 最優先で実行されるので動作が確実
   - 問題があれば他のKeymapに変更

2. **既存のキーと重複しないか確認**
   - PMEのホットキー設定で`+`ボタンを押す
   - 既存のキー割り当てをチェック

3. **段階的にテスト**
   - まずは使用頻度の低いキーでテスト
   - 動作確認後に本格運用

:::{admonition} 簡単な覚え方
:class: tip

**Screen Editing**: 「重要な編集操作」→ 最優先
**Window**: 「ファイル・アプリ操作」→ 中間
**Screen**: 「画面・レイアウト操作」→ 最後

迷った時は**Screen Editing**から始めて、必要に応じて他に変更しましょう。
:::

この仕組みを理解することで、PMEメニューが「動かない」「意図した通りに動作しない」といった問題を避けることができます。

## 実用的な選択指針

### 1. 特定モードでの専用メニュー

**目的**: 特定の作業モードでのみ使用したい機能

**推奨Keymap**: モード固有のKeymap（`Mesh`, `Sculpt`等）

**例**:
- メッシュモデリング用パイメニュー → `Mesh`
- スカルプト用ブラシ切り替えメニュー → `Sculpt`
- ポーズ設定用メニュー → `Pose`

**メリット**: 
- そのモードでのみ動作し、他のモードに影響しない
- モード固有の機能に集中できる

### 2. 3D View全般で使用するメニュー

**目的**: 3D Viewのどのモードでも使いたい汎用機能

**推奨Keymap**: `3D View`

**例**:
- ビューポート表示切り替えメニュー
- よく使うオブジェクト追加メニュー
- 汎用的な変形操作メニュー

**メリット**:
- 3D Viewのすべてのモードで一貫して使用可能
- ビュー操作と相性が良い

### 3. 全エディタで使用するメニュー

**目的**: どのエディタでも使いたいグローバル機能

**推奨Keymap**: `Screen Editing`

**例**:
- ファイル操作メニュー
- レンダリング関連メニュー
- アドオン管理メニュー

**注意事項**:
- 既存の重要な機能（LMB、RMB等）を上書きしないよう注意
- 全エディタに影響するため、慎重に設計する

### 4. 特定エディタでの専用メニュー

**目的**: 特定のエディタでの専門的な作業

**推奨Keymap**: エディタ固有のKeymap

**例**:
- UV編集用メニュー → `Image Editor`
- ノード作成メニュー → `Node Editor`
- アニメーション制御メニュー → `Dopesheet`

## 実際の選択フローチャート

```{mermaid}
flowchart TD
    A[PMEメニューを作成したい] --> B{どこで使用する？}
    
    B -->|特定のモードのみ| C[モード固有Keymap]
    C --> C1[Mesh, Sculpt, Object Mode等]
    
    B -->|3D View全般| D[3D View Keymap]
    D --> D1[3D View]
    
    B -->|特定エディタ| E[エディタ固有Keymap]
    E --> E1[Image Editor, Node Editor等]
    
    B -->|全エディタ共通| F{既存機能との競合は？}
    F -->|競合の可能性あり| G[慎重に検討]
    F -->|競合なし| H[Screen Editing]
    
    G --> I[キー組み合わせを変更]
    I --> H
```

## よくある間違いと対策

### ❌ 間違った選択例

1. **Screen Editingで基本操作を上書き**
   - `Space`キーでScreen Editingに登録 → 検索機能が無効化
   - `Tab`キーでScreen Editingに登録 → モード切り替えが無効化

2. **適用範囲が広すぎるKeymap選択**
   - スカルプト専用機能を`3D View`に登録 → 他のモードで不要なメニュー表示

3. **適用範囲が狭すぎるKeymap選択**
   - 汎用的な機能を`Mesh`だけに登録 → 他のモードで使用不可

### ✅ 正しい対策

1. **既存機能の確認**
   ```python
   # PMEのHotkey設定で+ボタンを使用して既存キーを調査
   # 競合しない組み合わせを選択
   ```

2. **段階的なテスト**
   ```
   1. 狭い範囲（特定モード）でテスト
   2. 問題なければ徐々に範囲を拡大
   3. 最終的に適切なKeymapを選択
   ```

3. **バックアップの作成**
   ```
   - PME設定をエクスポート
   - 変更前の状態を保存
   - 問題があれば即座に復元可能な状態を維持
   ```

## 高度なテクニック

### Poll関数の活用

特定の条件でのみメニューを表示したい場合は、Poll Methodを組み合わせて使用します：

```python
# メッシュオブジェクトが選択されている場合のみ表示
return C.active_object and C.active_object.type == 'MESH'

# 編集モードかつ面選択モードの場合のみ表示
return C.mode == 'EDIT_MESH' and C.tool_settings.mesh_select_mode[2]

# スカルプトモードかつDyntopoが有効な場合のみ表示
return C.mode == 'SCULPT' and C.active_object.use_dynamic_topology_sculpting
```

### キーマップの組み合わせ戦略

複数のKeymapを組み合わせて、階層的なメニューシステムを構築：

```
Screen Editing: Shift+A → メイン作成メニュー
├─ 3D View: Shift+Alt+A → 3D View専用作成メニュー
├─ Mesh: Shift+Ctrl+A → メッシュ編集専用メニュー
└─ Sculpt: Shift+S → スカルプトブラシメニュー
```

## デバッグとトラブルシューティング

### メニューが表示されない場合

1. **Keymapの優先度を確認**
   ```python
   # より具体的なKeymapで同じキーが使用されていないか確認
   # Blender Preferences > Keymap で検索
   ```

2. **Poll関数の動作確認**
   ```python
   # Poll Method欄で条件を簡素化してテスト
   return True  # 常に表示（デバッグ用）
   ```

3. **PMEログの確認**
   ```python
   # System Console (Window > Toggle System Console) でエラー確認
   ```

### 既存機能が動作しなくなった場合

1. **競合するキーマップアイテムを特定**
2. **キー組み合わせを変更**
3. **必要に応じてKeymapを変更**

## まとめ

適切なKeymap選択により、PMEメニューを効率的に配置できます：

- **特定モード専用** → モード固有Keymap
- **エディタ内汎用** → エディタ固有Keymap  
- **グローバル機能** → Screen Editing（注意深く）

常に既存機能との競合を避け、段階的にテストしながら実装することが重要です。