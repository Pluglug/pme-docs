# Claude Code Configuration for PME Documentation

このディレクトリには、PMEドキュメント開発を効率化するClaude Code設定が含まれています。

## 設定ファイル

### commands/
カスタムSlash Commands - ドキュメント作成タスクを自動化

- **`/start-server [lang]`** - 開発サーバーを起動（sphinx-autobuild、ライブリロード対応）
- **`/investigate-feature`** - PMEソースコードから機能を調査してたたき台作成
- **`/translate-to-en`** - 日本語ドキュメントを英語に翻訳
- **`/check-source-changes`** - PMEの最近の変更を確認してドキュメント更新が必要か判断
- **`/create-draft`** - 新規ドキュメントセクションのたたき台を作成
- **`/build-preview`** - ドキュメントをビルドしてエラー・警告をチェック
- **`/sync-versions`** - PMEアドオンとドキュメントのバージョン情報を同期
- **`/merge-to-main`** - feature/ja-roughからmainへ選択的にマージ

### hooks.json
自動実行Hooks

- **user-prompt-submit**: プロンプト送信時に`git status --short`を実行して変更ファイルを把握
- **session-start**: セッション開始時にワークフロー情報を表示

### terminology.json
PME専門用語辞書

- 日本語↔英語の用語対応表（40+ 用語）
- スロットタイプ、エディタタイプ、Blender一般用語
- 翻訳コマンドで自動参照

### COMMIT_RULES.md
コミットメッセージルール

- `feature/ja-rough`: 日本語・カジュアルOK
- `main`: 英語・整理された内容（Conventional Commits準拠）
- タイプ別の粒度ガイドライン

### scripts/
自動化スクリプト

- **`merge-to-main.sh`** / **`merge-to-main.bat`** - feature/ja-roughからmainへの選択的マージ

### settings.local.json
プロジェクト固有の設定（ユーザーがカスタマイズ可能）

## 使い方

### 1. 開発サーバーの起動

```bash
# 日本語版（デフォルト）
/start-server

# または明示的に
/start-server ja

# 英語版
/start-server en
```

→ sphinx-autobuildで開発サーバーを起動します。ファイル変更時に自動リビルド・ブラウザ自動更新されます。
→ サーバーURL: http://localhost:8000

### 2. 新機能のドキュメント作成

```
/investigate-feature sticky_key
```

→ ソースコードを調査してたたき台を作成します。

### 3. 日本語から英語への翻訳

```
/translate-to-en editors/sticky_key_editor.md
```

→ 日本語版を英語版に翻訳します。

### 4. PME更新の反映

```
/check-source-changes 1 month
```

→ 最近1ヶ月のPME変更を確認し、ドキュメント更新が必要か判断します。

### 5. ビルドチェック

```
/build-preview
```

→ ドキュメントをビルドして構文エラーやリンク切れをチェックします。

### 6. バージョン同期

```
/sync-versions
```

→ PMEアドオンとドキュメントのバージョン情報を確認・同期します。

## ワークフロー例

### シナリオ1: 新規ドキュメント作成

```bash
# 1. 機能を調査してたたき台作成
/investigate-feature popup_dialog

# 2. ユーザーが内容を確認・加筆

# 3. 英語版に翻訳
/translate-to-en editors/popup_dialog_editor.md

# 4. ビルド確認
/build-preview
```

### シナリオ2: PME更新対応

```bash
# 1. 最近の変更を確認
/check-source-changes

# 2. 影響のある機能を調査
/investigate-feature [変更された機能]

# 3. ドキュメント更新

# 4. バージョン同期
/sync-versions

# 5. 翻訳と確認
/translate-to-en [更新したファイル]
/build-preview
```

## ブランチ管理

### feature/ja-rough から main へのマージ

**方針:**
- `.claude/` と `CLAUDE.md` のみをmainに公開
- `DEPLOYMENT.md`, `PLAN.md` は個人的メモとして非公開
- `docs_ja/` のWIPは含めない

**方法1: コマンド使用（推奨）**

```bash
/merge-to-main
```

**方法2: スクリプト使用**

```bash
# Windows
.claude\scripts\merge-to-main.bat

# Linux/Mac
./.claude/scripts/merge-to-main.sh
```

**方法3: 手動**

```bash
git checkout main
git checkout feature/ja-rough -- .claude/ CLAUDE.md
git commit -m "chore: update Claude Code configuration"
git push origin main
git checkout feature/ja-rough
```

詳細は `/merge-to-main` コマンドまたは `COMMIT_RULES.md` を参照。

## カスタマイズ

### 新しいコマンドの追加

`.claude/commands/` に新しい `.md` ファイルを作成：

```markdown
---
description: コマンドの説明
---

# コマンドタイトル

コマンドの詳細説明...
```

### Hooksのカスタマイズ

`.claude/hooks.json` を編集：

```json
{
  "user-prompt-submit": {
    "command": "your-command-here",
    "description": "説明"
  }
}
```

## Tips

- **並列実行**: 複数のタスクを並列実行することで効率アップ
- **Task tool**: 複雑な調査はTask toolのExploreエージェントを活用
- **CLAUDE.md**: より詳細な情報は `../CLAUDE.md` を参照

## トラブルシューティング

### コマンドが認識されない

コマンドファイルの frontmatter を確認：
```markdown
---
description: 説明が必要
---
```

### Hooksが動作しない

- `.claude/hooks.json` の構文を確認
- コマンドがシステムで実行可能か確認

## 参考

- [Claude Code Documentation](https://docs.claude.ai/code)
- [PME Documentation](https://pluglug.github.io/pme-docs)
- [PME Repository](https://github.com/Pluglug/pie-menu-editor-fork)
