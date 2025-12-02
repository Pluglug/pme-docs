---
description: PMEアドオンとドキュメントのバージョン情報を確認・同期
---

# Sync Version Information

PMEアドオンとドキュメントのバージョン情報を確認し、不一致があれば更新方法を提案します。

## Arguments

なし

## 実行手順

### 1. バージョン情報を収集

以下のファイルからバージョン情報を読み取る：

**PMEアドオン:**
```python
# E:\0187_Pie-Menu-Editor\MyScriptDir\addons\pie_menu_editor\__init__.py
bl_info = {
    "version": (1, 19, 2, "beta", 0),  # 例
    ...
}
```

**ドキュメント（日本語版）:**
```python
# docs_ja/source/conf.py
release = "1.18.8"  # 例
```

**ドキュメント（英語版）:**
```python
# docs/source/conf.py
release = "1.18.8"  # 例
```

### 2. バージョンを比較

バージョン形式の変換：
- PME: `(1, 19, 2, "beta", 0)` → `1.19.2-beta`
- PME: `(1, 18, 8)` → `1.18.8`
- Docs: `"1.18.8"` → `1.18.8`

不一致のパターン：
- PMEとドキュメントのメジャー/マイナーバージョンが異なる
- 日本語版と英語版のバージョンが異なる
- Beta/RC情報の不一致

### 3. レポート作成

```markdown
## バージョン同期レポート

### 現在のバージョン

| 項目 | バージョン | ファイル |
|------|-----------|---------|
| PMEアドオン | 1.19.2-beta | `__init__.py:4` |
| 日本語ドキュメント | 1.18.8 | `docs_ja/source/conf.py:12` |
| 英語ドキュメント | 1.18.8 | `docs/source/conf.py:12` |

### 不一致の検出

#### PME vs ドキュメント
- PME: `1.19.2-beta`
- Docs: `1.18.8`
- **差分**: ドキュメントが1マイナーバージョン古い

#### 日本語版 vs 英語版
- ✅ 一致

### 推奨アクション

#### 1. ドキュメントバージョンを更新
PMEのバージョンアップに合わせて、ドキュメントバージョンを更新してください。

**日本語版（`docs_ja/source/conf.py`）:**
```python
release = "1.19.2"  # beta情報は通常省略
```

**英語版（`docs/source/conf.py`）:**
```python
release = "1.19.2"
```

#### 2. 変更履歴の確認
`/check-source-changes` コマンドで1.18.8以降の変更を確認し、ドキュメント更新が必要か判断してください。

#### 3. インストールガイドの更新
バージョン情報が含まれる可能性のあるページ：
- `docs_ja/source/getting_started/installation.md`
- `docs/source/getting_started/installation.md`

これらのページにバージョン番号の記載がある場合、更新してください。
```

### 4. 自動修正の提案（オプション）

ユーザーが承認した場合、以下を実行：
1. `docs_ja/source/conf.py` の `release` を更新
2. `docs/source/conf.py` の `release` を更新
3. 関連ドキュメントファイルのバージョン記載を更新

## Example

```bash
/sync-versions
```

## バージョン管理のベストプラクティス

### ドキュメントのバージョン表記

- **stable版**: `"1.18.8"` のように完全なバージョン
- **beta版**: `"1.19.0"` としてbeta表記は省略（注記で説明）
- **開発版**: `"1.19.0-dev"` または注記で明記

### バージョンアップ時のチェックリスト

- [ ] PMEアドオンの `bl_info["version"]` 確認
- [ ] 両方のドキュメント `conf.py` の `release` 更新
- [ ] インストールガイドのバージョン記載更新
- [ ] 変更履歴（Changelog）に追記
- [ ] `/check-source-changes` で機能変更を確認

## 注意事項

- ドキュメントバージョンは必ずしもPMEと完全一致させる必要はない
- 大きなバージョン差（2つ以上のマイナーバージョン）がある場合は警告
- Beta/RC情報はドキュメントでは省略し、注記で説明することが一般的
