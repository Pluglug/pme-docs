# デプロイ設定

## 言語切り替え機能

デプロイ後、ユーザーは右上の言語切り替えボタンで言語を切り替えられます。

### デプロイ構造

```
example.com/
├── index.html          # 英語版ホーム
├── getting_started/    # 英語版セクション
├── editors/           # 英語版セクション
├── reference/         # 英語版セクション
├── support_community/ # 英語版セクション
└── ja/               # 日本語版ディレクトリ
    ├── index.html    # 日本語版ホーム
    ├── getting_started/
    ├── editors/
    ├── reference/
    └── support_community/
```

### 言語切り替えの動作

1. **英語版から日本語版へ**:
   - `example.com/editors/pie_menu_editor.html`
   - → `example.com/ja/editors/pie_menu_editor.html`

2. **日本語版から英語版へ**:
   - `example.com/ja/editors/pie_menu_editor.html`
   - → `example.com/editors/pie_menu_editor.html`

### 実装内容

- **言語切り替えボタン**: 右上に固定表示
- **現在の言語ハイライト**: アクティブな言語が強調表示
- **URL保持**: 同じページの別言語版に移動
- **ダークモード対応**: テーマに合わせてスタイル調整

### デプロイ手順

1. **英語版をデプロイ**:
   ```bash
   cp -r docs/build/en/* /path/to/website/
   ```

2. **日本語版をデプロイ**:
   ```bash
   cp -r docs_ja/build/* /path/to/website/ja/
   ```

3. **静的ファイルをコピー**:
   ```bash
   cp -r docs/source/_static /path/to/website/
   cp -r docs_ja/source/_static /path/to/website/ja/
   ```

### 注意事項

- 両言語版で同じファイル構造を維持
- 静的ファイル（CSS、JS、画像）は両方にコピー
- 言語切り替えボタンは両方のバージョンに含まれる 