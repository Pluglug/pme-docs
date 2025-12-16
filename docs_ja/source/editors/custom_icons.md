(custom-icons)=

# カスタムアイコン

PME でカスタムアイコンを使う方法について説明します。

## 基本情報

- **対応形式**: PNG（拡張子 `.png` のみ読み込まれます）
- **配置場所**: アドオンフォルダ内の `pie_menu_editor/icons` に置く（例: `.../addons/pie_menu_editor/icons/my_icon.png`）
- **名前の扱い**: ファイル名（拡張子なし）がアイコン名になります（例: `my_icon.png` → アイコン名は `my_icon`）。大文字小文字やスペースも区別されるため、入力はファイル名と完全一致で。

## アイコンの読み込みタイミング

- アイコンは **Blender 起動時（アドオン有効化時）に一度だけ** 読み込まれます
- セッション中にアイコンを追加・変更した場合は、**Blender を再起動** する必要があります

```{note}
技術的な制約により、セッション中のアイコン再読み込みはサポートされていません。
新しいアイコンを追加したら Blender を再起動してください。
```

## カスタムアイコンの使い方

アイコン設定画面の **Custom** タブで、読み込まれたカスタムアイコンを確認・選択できます。

存在しない名前を指定すると、Blender の代替アイコンが表示されることがあります。

## スクリプトから使う（任意）

- **簡単指定（PME のラッパを利用）**: `@` を含む文字列をそのまま渡せます
  ```python
  # 例: LayoutHelper を使う場合
  lh.operator("wm.operator", text="Run", icon='@my_icon')
  ```
- **Blender 標準 UI API で使う**: `icon='NONE'` と `icon_value` を併用
  ```python
  # 例: Python から直接
  from pie_menu_editor.previews_helper import custom_icon
  layout.operator("wm.operator", text="Run", icon='NONE', icon_value=custom_icon("my_icon"))
  ```

## ネーミングと画質のヒント

- なるべく半角英数字と `_` を推奨（入力ミス防止）
- 透過背景の PNG を推奨
- 解像度は任意（一般的には 32〜64px 四方程度が見やすい）

## トラブルシューティング

- **表示されない/別アイコンになる**
  - 拡張子が `.png` か確認
  - ファイル名（拡張子なし）と指定文字列（`@name`）が完全一致か確認
  - アイコン追加後に Blender を再起動したか確認
- **一覧に出てこない**
  - `icons` 直下に置いているか確認（サブフォルダは読み込まれません）
  - 画像が壊れていないか再保存して試す
  - Blender を再起動して再確認

## 既存のサンプル

`pie_menu_editor/icons` には `p1.png`, `p2.png`, `pA.png` などのサンプルがあります。指定例: `@p1`, `@pA`

## まとめ

1. `pie_menu_editor/icons` フォルダに PNG ファイルを配置
2. Blender を再起動（アイコンが読み込まれる）
3. PME 内で `@ファイル名` の形式で指定