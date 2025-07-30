# PME Documentation Development Plan

## Background

The PME documentation project was stalled due to the overhead of writing in English.
This new structure enables:

1. **Efficient Development**: Write in Japanese first, then improve English version
2. **Clear Separation**: No file conflicts between languages
3. **Easy Preview**: Use sphinx-autobuild for real-time preview
4. **Gradual Migration**: Focus on important sections first

## Technical Changes

- Created `docs_ja/` directory with Japanese-specific Sphinx config
- Updated `build_docs.py` for directory-based builds
- Simplified configuration by removing environment variable complexity
- Maintained existing English documentation structure

## Development Workflow

- **Japanese Development**: `sphinx-autobuild docs_ja/source docs_ja/build`
- **English Development**: `sphinx-autobuild docs/source docs/build/en`
- **Full Build**: `python build_docs.py`

## Next Steps

1. Complete Japanese version of getting_started/ section
2. Polish content quality
3. Reflect improvements to English version
4. Deploy both versions 


# PME ドキュメント開発

## プロジェクト概要

**ブランチ**: `feature/ja-rough`  
**目的**: PMEドキュメントを作業しやすい日本語で完成させ、その後英語版に反映する

## アプローチ

### ディレクトリ構造
```
pme-docs/
├── docs/                    # 英語版
│   ├── source/
│   │   ├── conf.py         # 英語版設定
│   │   ├── index.md        # 英語版
│   │   └── getting_started/
│   │       └── installation.md
│   └── build/
│       └── en/
└── docs_ja/                # 日本語版
    ├── source/
    │   ├── conf.py         # 日本語版設定
    │   ├── index.md        # 日本語版
    │   └── getting_started/
    │       └── installation.md
    └── build/
```

### メリット
1. **完全に分離**: 英語版と日本語版が混在しない
2. **シンプルな設定**: 各言語専用の設定ファイル
3. **作業しやすい**: `sphinx-autobuild`で確認しやすい
4. **段階的に移行可能**: 重要な部分から順番に

## 開発計画

### Phase 1: 基盤整備 (Week 1) - `feature/ja-rough`
- [x] ビルドシステムの設定
- [x] ディレクトリ分離の実装
- [ ] 重要なファイルの日本語版作成
  - [ ] `docs_ja/source/getting_started/installation.md`
  - [ ] `docs_ja/source/getting_started/quick_tutorial.md`
  - [ ] `docs_ja/source/getting_started/feature_overview.md`

### Phase 2: 基本セクション完成 (Week 2-3) - `feature/ja-rough`
- [ ] `docs_ja/source/editors/`セクションの基本部分
  - [ ] `docs_ja/source/editors/pie_menu_editor.md`
  - [ ] `docs_ja/source/editors/regular_menu_editor.md`
  - [ ] `docs_ja/source/editors/popup_dialog_editor.md`
- [ ] 日本語版の内容を完成させる

### Phase 3: 高度なセクション (Week 4) - `feature/ja-polish`
- [ ] `docs_ja/source/reference/`セクション
- [ ] `docs_ja/source/support_community/`セクション
- [ ] 全体の調整と統一

### Phase 4: 英語版反映 (Week 5) - `feature/en-update`
- [ ] 日本語版を参考に英語版を更新
- [ ] 両言語版の最終調整
- [ ] デプロイ準備

## 開発指針

### コミットメッセージ
- 日本語でOK
- 気負わずに適当で良い
- 例: `feat: インストールガイドを日本語で完成`

### 品質基準
- **Phase 1-2**: ラフでも良い、内容を完成させることを優先
- **Phase 3**: 日本語版の品質向上
- **Phase 4**: 英語版の品質を向上

### ファイル管理
- 日本語版は`docs_ja/source/`に配置
- 英語版は`docs/source/`に配置

## ビルドとデプロイ

### 個別ビルド
```bash
# 日本語版のみ
sphinx-autobuild docs_ja/source docs_ja/build

# 英語版のみ
sphinx-autobuild docs/source docs/build/en
```

### 一括ビルド
```bash
# 両方のバージョンをビルド
python build_docs.py
```

### デプロイ先
- **英語版**: `docs/build/en/` → メインサイト
- **日本語版**: `docs_ja/build/` → 日本語版サイト

## 技術仕様

### 使用技術
- **Sphinx**: ドキュメント生成
- **MyST**: Markdownパーサー
- **Furo**: テーマ
- **Python**: ビルドスクリプト

### 設定ファイル
- `docs/source/conf.py`: 英語版Sphinx設定
- `docs_ja/source/conf.py`: 日本語版Sphinx設定
- `build_docs.py`: ビルドスクリプト
- `requirements.txt`: 依存関係

## 成功指標

### 短期目標 (~25/09)
- [ ] PMEドキュメントの完成
- [ ] 基本的な機能の説明が利用可能

### 中期目標 (~25/10)
- [ ] 英語版の品質向上
- [ ] 両言語版のデプロイ完了

### 長期目標 (~25/11)
- [ ] コミュニティからのフィードバック収集
- [ ] 継続的な改善体制の確立
