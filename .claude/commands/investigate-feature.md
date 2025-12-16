---
description: PMEソースコードから指定機能を調査し、ドキュメントのたたき台を作成
---

# Investigate PME Feature

PMEソースコード（CLAUDE.mdの`PME_SOURCE_PATH`で指定されたパス）から指定された機能を調査し、ドキュメント用のたたき台を作成してください。

## Arguments

- `feature_name`: 調査する機能名（例: "sticky_key", "pie_menu", "popup_dialog"）

## 実行手順

### 1. ソースコード調査（Task toolのExploreエージェントを推奨）

関連ファイルを特定：
- エディタ機能なら `ed_*.py` ファイル
- オペレータなら `operators.py` や `extra_operators.py`
- ヘルパー機能なら `*_utils.py` や `*_helper.py`

以下を理解：
- 主要なクラスと関数
- ユーザーに露出するUI要素
- 設定項目とパラメータ
- 他機能との連携

### 2. たたき台作成

`docs_ja/source/` の適切な場所に日本語でたたき台を作成：
- `editors/` - エディタ機能
- `reference/` - 高度な機能やスクリプティング
- `getting_started/` - 基本的な使い方

### たたき台の構成例

```markdown
# [機能名]

## 概要
この機能の目的と基本的な用途を説明

## 使い方

### 基本的な使い方
1. 手順1
2. 手順2
3. 手順3

### 設定項目
- **項目1**: 説明
- **項目2**: 説明

## 使用例
具体的な使用シーン

## TODO
- [ ] スクリーンショット: [説明]
- [ ] 動画/GIF: [説明]
- [ ] 補足説明が必要: [箇所]
```

### 3. レポート

以下を含むレポートを作成：
- 調査したファイルと主要コード箇所（ファイルパス:行番号）
- 作成したたたき台のパス
- スクリーンショットが必要な箇所
- 追加で調査が必要な項目

## 注意事項

- ユーザー向けの説明レベルに調整（実装詳細すぎない）
- 日本語で作成（英語翻訳は後で `/translate-to-en` を使用）
- 既存のドキュメントと用語・スタイルを統一
- 不明点はTODOとして明記

## Example

```bash
/investigate-feature sticky_key
```

↓ 期待される出力：

1. `ed_sticky_key.py` を調査
2. `docs_ja/source/editors/sticky_key_editor.md` にたたき台作成
3. スクリーンショット必要箇所をリスト
4. 関連する `keymap_helper.py` の機能を説明
