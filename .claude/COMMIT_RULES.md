# Commit Message Rules

PMEドキュメントプロジェクトのコミットメッセージルール

## ブランチ別ルール

### `feature/ja-rough` - 個人的実験ブランチ

**ルール: 自由（日本語OK）**

このブランチは個人的なワークフロー実験場です。コミットメッセージは自由に：

✅ **OK例:**
```bash
git commit -m "パイメニューのドキュメント追加"
git commit -m "WIP: スティッキーキー調査中"
git commit -m "画像追加"
git commit -m "typo修正"
git commit -m "ちょっと試した"
```

- 日本語でOK
- 適当な粒度でOK
- WIP（Work In Progress）もOK
- 短文でOK

---

### `main` - 公開ブランチ

**ルール: 英語・整理された内容**

公開されるブランチなので、整理されたコミットメッセージを使用：

#### 基本形式

```
<type>: <subject>

[optional body]

[optional footer]
```

#### Type（種類）

- **docs**: ドキュメント追加・更新
- **feat**: 新機能ドキュメント
- **fix**: 誤記修正、リンク切れ修正
- **refactor**: 構造変更、リネーム
- **chore**: ビルド設定、メタファイル、設定変更
- **style**: フォーマット変更（内容に影響なし）

#### Subject（件名）

- 英語で簡潔に（50文字以内）
- 命令形を使用（"Add" not "Added"）
- 最初の文字は小文字
- 末尾にピリオドなし

#### Body（本文・オプション）

- 変更の詳細を箇条書きで
- 各行は72文字以内
- "Why"（なぜ変更したか）を説明

#### Examples

**✅ Good:**
```bash
# 基本
git commit -m "docs: add Sticky Key editor documentation"

# 詳細版
git commit -m "docs: add Sticky Key editor documentation

- Add basic usage guide with step-by-step instructions
- Include hotkey configuration examples
- Add troubleshooting section for common issues
- Include screenshots for UI elements"

# 修正
git commit -m "fix: correct broken links in getting started guide"

# Claude Code設定
git commit -m "chore: add custom slash commands for documentation workflow

- Add /investigate-feature command for source code analysis
- Add /translate-to-en command with terminology dictionary
- Add /build-preview command for build verification"
```

**❌ Bad:**
```bash
# 日本語を使っている
git commit -m "ドキュメント追加"

# 不明瞭
git commit -m "update files"

# 詳細すぎる内容を1行に詰め込み
git commit -m "docs: add sticky key documentation and fix typos and add images and update links"

# 過去形を使用
git commit -m "docs: added sticky key documentation"
```

---

## ファイル別の推奨粒度

### `.claude/` - Claude Code設定

**粒度: 機能単位**

```bash
# 新しいコマンド追加
git commit -m "chore: add /investigate-feature command"

# 用語辞書更新
git commit -m "chore: update terminology dictionary with PME-specific terms"

# 複数の関連する変更
git commit -m "chore: enhance translation workflow

- Add terminology dictionary
- Update /translate-to-en command to use dictionary
- Add usage examples to README"
```

### `CLAUDE.md`

**粒度: セクション単位**

```bash
git commit -m "docs: update PME architecture documentation in CLAUDE.md"

git commit -m "docs: add workflow examples to CLAUDE.md"
```

### `docs/` - 英語ドキュメント

**粒度: ページまたはセクション単位**

```bash
# 新しいページ
git commit -m "docs: add Sticky Key editor documentation"

# セクション追加
git commit -m "docs: add troubleshooting section to pie menu editor"

# 複数ページの一貫した更新
git commit -m "docs: standardize terminology across all editor pages

- Replace 'menu item' with 'slot' consistently
- Update examples to use current PME version
- Fix broken cross-references"
```

### `docs_ja/` - 日本語ドキュメント

**粒度: 自由（feature/ja-roughの場合）**

```bash
# なんでもOK
git commit -m "パイメニュー編集中"
git commit -m "WIP"
git commit -m "いったん保存"
```

---

## Conventional Commits準拠

このプロジェクトは[Conventional Commits](https://www.conventionalcommits.org/)に準拠します。

### Structure

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Examples with Scope

```bash
git commit -m "docs(editors): add popup dialog editor documentation"

git commit -m "fix(getting-started): correct installation steps for Blender 4.0"

git commit -m "chore(build): update Sphinx configuration for better PDF output"
```

---

## コミット時のチェックリスト

### mainブランチにコミットする前

- [ ] コミットメッセージは英語
- [ ] Type（docs, feat, fix, chore等）を使用
- [ ] 件名は50文字以内で簡潔
- [ ] 複数の変更は箇条書きで説明
- [ ] DEPLOYMENT.md, PLAN.mdは含まれていない
- [ ] docs_jaのWIPファイルは含まれていない

### feature/ja-roughにコミットする場合

- [ ] 好きにやる！

---

## 参考資料

- [Conventional Commits](https://www.conventionalcommits.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
- [Angular Commit Message Guidelines](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit)

---

## このファイルについて

- **場所**: `.claude/COMMIT_RULES.md`
- **目的**: コミットメッセージの一貫性を保つ
- **適用**: mainブランチへのマージ時に厳格に適用
- **更新**: プロジェクトの成長に応じて随時更新
