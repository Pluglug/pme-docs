---
description: 日本語ドキュメントを英語版に翻訳
---

# Translate Documentation to English

指定された日本語ドキュメントファイルを英語版に翻訳し、同じ構造で配置します。

## Arguments

- `file_path`: 翻訳するファイルの相対パス（例: "editors/sticky_key_editor.md", "getting_started/installation.md"）

## 実行手順

### 1. 用語辞書を読み込む

`.claude/terminology.json` を読み込んで、PME専門用語の対応表を確認

### 2. 日本語版ファイルを読み込む

`docs_ja/source/[file_path]` を読み込む

### 3. 英語に翻訳

以下の点に注意：

**PME専門用語の統一:**
- **必須**: `.claude/terminology.json` の `japanese_to_english` セクションを参照
- 特に `context_specific` セクションの用語に注意
  - **Slot types**: コマンドスロット→Command slot、プロパティスロット→Property slot など
  - **Editor types**: パイメニューエディター→Pie Menu Editor、ポップアップダイアログエディター→Popup Dialog Editor など
  - **Blender general**: 3Dビュー→3D View、ビューポート→Viewport など
- 辞書にない用語は追加候補としてレポート

**翻訳スタイル:**
- 自然な英語表現を使用
- 技術文書として正確かつ簡潔に
- 日本語特有の婉曲表現は直接的に
- ユーザー向けの親しみやすいトーンを保つ

**保持する要素:**
- MyST記法（```{note}、{admonition}など）
- 画像パス（`/_static/images/...`）
- リンク参照（`{ref}label`）
- コードブロック

### 3. 英語版ファイルを作成/更新

`docs/source/[file_path]` に翻訳を書き込む
- ディレクトリが存在しない場合は作成

### 4. 構文チェック

翻訳後、以下を確認：
- MyST記法の構文エラーがないか
- 画像パスが正しいか
- 相互参照が壊れていないか

### 5. レポート

以下を報告：
- 翻訳元: `docs_ja/source/[file_path]`
- 翻訳先: `docs/source/[file_path]`
- 翻訳時の重要な判断（意訳した箇所など）
- 不明点や要確認事項

## Example

```bash
/translate-to-en editors/sticky_key_editor.md
```

↓ 期待される動作：

1. `docs_ja/source/editors/sticky_key_editor.md` を読み込む
2. 英語に翻訳（PME用語を統一）
3. `docs/source/editors/sticky_key_editor.md` に書き込む
4. 構文エラーをチェック
5. 翻訳結果を報告

## Notes

- 既存の英語ファイルがある場合は上書き確認
- 画像やアセットは共有（`_static/` ディレクトリ）
- 日本語版で TODO になっている項目は英語版でも TODO
- スクリーンショットが日本語UI の場合は、英語版では注記を追加

## 翻訳品質チェックリスト

- [ ] PME専門用語が統一されている
- [ ] MyST記法が正しく保持されている
- [ ] 画像パスが相対パスで正しい
- [ ] 自然な英語表現になっている
- [ ] 技術的な正確さが保たれている
