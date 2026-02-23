---
description: feature/ja-roughから.claudeとCLAUDE.mdのみをmainに選択的にマージ
---

# Merge to Main Branch

`feature/ja-rough`（個人的な実験ブランチ）から、公開すべきファイルのみを`main`ブランチに選択的にマージします。

## 方針

### マージするもの
- `.claude/` ディレクトリ全体（コマンド、用語辞書、設定）
- `CLAUDE.md`（プロジェクト指示書）
- `docs/` の変更（英語ドキュメント）

### マージしないもの
- `DEPLOYMENT.md`（デプロイ手順：個人的メモ）
- `PLAN.md`（開発計画：個人的メモ）
- `docs_ja/` の作業途中ファイル（完成したものは選択的にマージ）
- その他の個人的な実験ファイル

## 実行手順

### 1. 現在の状態を確認

```bash
# 現在のブランチを確認
git branch

# 変更ファイルを確認
git status

# mainとの差分を確認
git diff main --name-only
```

### 2. mainブランチに切り替え

```bash
git checkout main

# 念のためmainを最新に
git pull origin main
```

### 3. 選択的にマージ

**オプションA: Cherry-pick方式（推奨）**

```bash
# feature/ja-roughから.claudeとCLAUDE.mdのみをマージ
git checkout feature/ja-rough -- .claude/
git checkout feature/ja-rough -- CLAUDE.md

# docs/の変更も必要に応じてマージ
git checkout feature/ja-rough -- docs/

# ステージングエリアの内容を確認
git status

# コミット（英語で簡潔に）
git commit -m "docs: update Claude Code configuration and commands

- Add custom slash commands for documentation workflow
- Add terminology dictionary for consistent translation
- Update CLAUDE.md with workflow examples and best practices"
```

**オプションB: パッチ方式**

```bash
# 特定ファイルのパッチを作成
git diff main feature/ja-rough -- .claude/ CLAUDE.md > selective-merge.patch

# パッチを確認
cat selective-merge.patch

# パッチを適用
git apply selective-merge.patch

# コミット
git commit -m "docs: update Claude Code configuration"

# パッチファイルを削除
rm selective-merge.patch
```

### 4. 確認してプッシュ

```bash
# コミット内容を確認
git log -1 --stat

# mainにプッシュ
git push origin main
```

### 5. feature/ja-roughに戻る

```bash
git checkout feature/ja-rough
```

## コミットメッセージルール

### docs/ (英語ドキュメント) - 厳格

**形式:**
```
<type>: <subject>

[optional body]
```

**Type:**
- `docs`: ドキュメント追加・更新
- `feat`: 新機能ドキュメント
- `fix`: 誤記修正、リンク切れ修正
- `refactor`: 構造変更
- `chore`: ビルド設定、メタファイル

**例:**
```bash
# Good
git commit -m "docs: add Sticky Key editor documentation

- Add basic usage guide
- Include hotkey configuration examples
- Add troubleshooting section"

# Bad
git commit -m "sticky keyのドキュメント追加した"
```

### docs_ja/ (日本語ドキュメント) - カジュアルOK

**形式:** 自由（日本語OK）

**例:**
```bash
git commit -m "Sticky Keyのドキュメント追加"
git commit -m "画像追加、誤字修正"
git commit -m "WIP: ポップアップダイアログの説明途中"
```

## 使用例

### シナリオ1: Claude Code設定をmainに反映

```bash
# 現在: feature/ja-rough
# やったこと: .claude/commands/ にコマンド追加、terminology.json作成

/merge-to-main

# → 以下を自動実行:
# 1. git checkout main
# 2. git checkout feature/ja-rough -- .claude/ CLAUDE.md
# 3. git commit -m "docs: add custom slash commands and terminology dictionary"
# 4. git push origin main
# 5. git checkout feature/ja-rough
```

### シナリオ2: 英語ドキュメント完成版をmainに反映

```bash
# 現在: feature/ja-rough
# やったこと: docs/editors/sticky_key_editor.md を完成

/merge-to-main docs/editors/sticky_key_editor.md

# → 選択的にマージ
```

## 自動化スクリプト（オプション）

以下のスクリプトを `.claude/scripts/merge-to-main.sh` として保存：

```bash
#!/bin/bash

echo "=== Selective Merge to Main ==="

# 現在のブランチを保存
CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" != "feature/ja-rough" ]; then
    echo "Error: Must be on feature/ja-rough branch"
    exit 1
fi

# mainに切り替え
echo "Switching to main..."
git checkout main

# 最新化
echo "Pulling latest main..."
git pull origin main

# 選択的にマージ
echo "Merging .claude/ and CLAUDE.md..."
git checkout feature/ja-rough -- .claude/
git checkout feature/ja-rough -- CLAUDE.md

# ステータス表示
git status

echo ""
echo "Files staged for commit. Please review and commit with:"
echo "  git commit -m \"docs: <your message>\""
echo ""
echo "After committing, run:"
echo "  git push origin main"
echo "  git checkout feature/ja-rough"
```

**使い方:**
```bash
chmod +x .claude/scripts/merge-to-main.sh
./.claude/scripts/merge-to-main.sh
```

## 注意事項

- **個人的なファイルは絶対にマージしない**: DEPLOYMENT.md, PLAN.md
- **docs_ja/ は慎重に**: 完成したページのみマージ、WIPは含めない
- **コミットメッセージは英語**: mainへのコミットは必ず英語で
- **レビュー**: マージ前に `git diff --cached` で内容確認

## トラブルシューティング

### コンフリクトが発生した場合

```bash
# マージを中断
git merge --abort

# または手動で解決
git checkout main
git checkout feature/ja-rough -- <conflicted-file>
# 内容を確認・編集
git add <conflicted-file>
git commit
```

### 間違ってマージしてしまった場合

```bash
# 最後のコミットを取り消し（コミット前の状態に戻る）
git reset --soft HEAD~1

# または完全に取り消し（変更も破棄）
git reset --hard HEAD~1
```
