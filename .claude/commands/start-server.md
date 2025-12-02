---
description: sphinx-autobuildで開発サーバーを起動（日本語版/英語版）
---

# Start Development Server

sphinx-autobuildを使って開発サーバーを起動します。ファイル変更時に自動的にリビルドされ、ブラウザが自動更新されます。

## Arguments

- `lang`: 起動する言語バージョン（デフォルト: `ja`）
  - `ja` - 日本語ドキュメント
  - `en` - 英語ドキュメント

## 実行内容

### 日本語版（`ja`）

```bash
cd docs_ja
sphinx-autobuild source build --host 0.0.0.0 --port 8000
```

- ソース: `docs_ja/source/`
- ビルド先: `docs_ja/build/`
- URL: http://localhost:8000

### 英語版（`en`）

```bash
cd docs
sphinx-autobuild source build/en --host 0.0.0.0 --port 8000
```

- ソース: `docs/source/`
- ビルド先: `docs/build/en/`
- URL: http://localhost:8000

## 使用例

### 日本語版を起動（デフォルト）

```bash
/start-server
```

または明示的に：

```bash
/start-server ja
```

### 英語版を起動

```bash
/start-server en
```

## サーバーの動作

起動後、以下の動作をします：

1. **初回ビルド**: ドキュメント全体をビルド
2. **ファイル監視**: `source/` ディレクトリ内のファイル変更を監視
3. **自動リビルド**: ファイル保存時に自動的にリビルド
4. **自動更新**: ブラウザが自動的にリロード

**ブラウザでアクセス**: http://localhost:8000 を手動で開いてください

## サーバーの停止

開発サーバーを停止するには：
- `Ctrl+C` を押す（ターミナルで）

## トラブルシューティング

### ポート8000が既に使用されている

```bash
# 既存のサーバーを停止するか、別のポートを使用
sphinx-autobuild source build --port 8001
```

### sphinx-autobuildがインストールされていない

```bash
pip install sphinx-autobuild
```

または：

```bash
pip install -r requirements.txt
```

### 変更が反映されない

1. サーバーを再起動（`Ctrl+C` して再度 `/start-server`）
2. ブラウザのキャッシュをクリア（`Ctrl+Shift+R` または `Cmd+Shift+R`）
3. `build/` ディレクトリを削除して再ビルド

```bash
# 日本語版
rm -rf docs_ja/build/

# 英語版
rm -rf docs/build/
```

## Notes

- **並列実行不可**: 日本語版と英語版を同時に起動する場合は、どちらかのポートを変更する必要があります
- **初回ビルドは時間がかかる**: 大量のページがある場合、初回ビルドに数秒かかります
- **自動リロード**: LiveReloadが有効なので、ブラウザが自動的に更新されます
- **エラー表示**: ビルドエラーがある場合、ターミナルに表示されます

## 実装例

コマンドを実行すると以下のメッセージが表示されます：

```
=== Starting Development Server ===

Language: 日本語 (ja)
Source: docs_ja/source/
Build: docs_ja/build/
Port: 8000

Server starting...
[sphinx-autobuild] > sphinx-build source build
Running Sphinx v7.x.x
...
Build finished.

✓ Server is running at http://localhost:8000
✓ Watching for changes...

Open http://localhost:8000 in your browser.
Press Ctrl+C to stop the server.
```
