---
description: ドキュメントをビルドして構文エラーやリンク切れをチェック
---

# Build and Preview Documentation

ドキュメントをビルドして、構文エラー、警告、リンク切れなどをチェックします。

## Arguments

- `lang` (optional): ビルド対象（デフォルト: "both"）
  - `ja` - 日本語版のみ
  - `en` - 英語版のみ
  - `both` - 両方

## 実行手順

### 1. ビルドコマンド実行

**両方の場合:**
```bash
python build_docs.py
```

**日本語版のみ:**
```bash
sphinx-build -b html docs_ja/source docs_ja/build
```

**英語版のみ:**
```bash
sphinx-build -b html docs/source docs/build/en
```

### 2. ビルドログを解析

以下のタイプの問題を抽出：

**優先度: 高（必ず修正）**
- エラー（ERROR）: ビルドが失敗した箇所
- 参照エラー: `undefined label`、`unknown document`
- 画像が見つからない: `image file not readable`

**優先度: 中（確認推奨）**
- 警告（WARNING）: 構文の問題、非推奨の記法
- リンク切れ: 外部URLの確認
- 重複ラベル: `duplicate label`

**優先度: 低（必要に応じて）**
- スタイル警告: インデントの問題など
- その他の通知

### 3. 問題を分類・報告

以下の形式でレポート：

```markdown
## ドキュメントビルドレポート

### ビルド結果
- 日本語版: ✅ 成功 / ❌ 失敗
- 英語版: ✅ 成功 / ❌ 失敗

### エラー（優先度: 高）

#### docs_ja/source/editors/sticky_key.md:42
```
ERROR: Unknown directive type "admontion". Did you mean "admonition"?
```
**修正案**: `admontion` → `admonition`

#### docs/source/getting_started/installation.md:15
```
WARNING: undefined label: 'installation-guide' (if the link has no caption the label must precede a section header)
```
**修正案**: ラベル定義を追加するか、参照先を確認

### 警告（優先度: 中）

[リスト...]

### その他の通知

[リスト...]

### 推奨アクション
1. [ファイル名] の行[N]を修正
2. [ファイル名] の画像パスを確認
3. 外部リンクの有効性を確認

### ビルド出力
- 日本語版: `docs_ja/build/index.html`
- 英語版: `docs/build/en/index.html`
```

### 4. 修正案の提示

可能であれば、具体的な修正案を提示：
- タイポの修正
- 正しいMyST記法
- 画像パスの修正
- 参照ラベルの追加

## Example

```bash
/build-preview
```

または言語を指定：

```bash
/build-preview ja
/build-preview en
```

## Tips

### よくあるエラーと対処法

**1. 参照エラー**
```
WARNING: undefined label: 'my-section'
```
→ ラベル定義を追加: `(my-section)=`

**2. 画像が見つからない**
```
WARNING: image file not readable: /_static/images/foo.png
```
→ ファイルパスを確認、画像ファイルの存在確認

**3. ディレクティブのタイポ**
```
ERROR: Unknown directive type "noe"
```
→ `{note}` の間違いかチェック

**4. インデントエラー**
```
WARNING: Unexpected indentation
```
→ MyST記法のインデントを確認

### ビルド後の確認

ビルド成功後、以下を手動確認することを推奨：
- ブラウザで見た目を確認
- リンクが正しく動作するか
- 画像が表示されるか
- コードブロックが正しく表示されるか

## 注意事項

- ビルドエラーがある場合、一部のページが生成されない可能性
- 警告は無視できる場合もあるが、内容を確認すること
- 外部リンクのチェックは別途手動で行うことを推奨
