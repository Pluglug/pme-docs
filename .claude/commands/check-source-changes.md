---
description: PMEソースコードの最近の変更を確認し、ドキュメント反映が必要か判断
---

# Check PME Source Changes

PMEソースコード（`E:\0187_Pie-Menu-Editor\MyScriptDir\addons\pie_menu_editor`）の最近の変更を確認し、ドキュメントに反映が必要か判断します。

## Arguments

- `period` (optional): 確認期間（デフォルト: "1 month"）
  - 例: "1 week", "2 months", "10 days"

## 実行手順

### 1. Git履歴を確認

PMEアドオンディレクトリで以下を実行：

```bash
cd "E:\0187_Pie-Menu-Editor\MyScriptDir\addons\pie_menu_editor"
git log --since="[period] ago" --oneline --no-merges
```

### 2. 重要な変更を抽出

以下のタイプの変更に注目：
- **新機能**: 新しいエディタ、オペレータ、UI要素
- **仕様変更**: 既存機能の動作変更、パラメータ変更
- **Deprecation**: 非推奨になった機能
- **バグ修正（重要なもの）**: ユーザーが知るべき修正
- **互換性**: Blenderバージョン対応の変更

無視してよい変更：
- 内部リファクタリング（動作変更なし）
- 細かいバグ修正（ドキュメントに影響なし）
- コメント・ドキュメンテーションのみの変更

### 3. 影響を受けるドキュメントを特定

変更ごとに、影響を受けるドキュメントファイルをリスト：

**マッピング例:**
- `ed_sticky_key.py` → `docs_ja/source/editors/sticky_key_editor.md`
- `ed_popup.py` → `docs_ja/source/editors/popup_dialog_editor.md`
- `keymap_helper.py` → `docs_ja/source/editors/common/hotkey_settings.md`
- `__init__.py` (bl_info) → `docs_ja/source/getting_started/installation.md`

### 4. 更新箇所を詳細化

各ファイルについて：
- どのセクションを更新すべきか
- 新しいスクリーンショット/GIFが必要か
- 新規セクション追加が必要か
- 削除すべき古い情報はあるか

### 5. 優先度付けレポート

以下の形式でレポート：

```markdown
## PMEソースコード変更レポート

### 期間
[開始日] ～ [終了日] ([N]コミット)

### 優先度: 高
**[機能名]** ([コミットハッシュ])
- 変更内容: [説明]
- 影響ファイル: `docs_ja/source/...`
- 必要な作業: [具体的な更新内容]
- 調査コマンド: `/investigate-feature [feature]`

### 優先度: 中
...

### 優先度: 低
...

### ドキュメント更新不要
- [コミット]: 内部リファクタリング
...

### 推奨アクション
1. まず [ファイル名] を更新
2. [機能名] の新規ドキュメント作成
3. スクリーンショット更新: [箇所]
```

## Example

```bash
/check-source-changes
```

または期間指定：

```bash
/check-source-changes 2 weeks
```

## Tips

- 大きな変更がある場合は、Task toolで並列調査を提案
- バージョン番号の変更があれば `/sync-versions` を推奨
- 新機能があれば `/investigate-feature` と `/create-draft` を提案

## 注意事項

- コミットメッセージだけでなく、必要に応じて diff も確認
- ユーザーに影響がない変更は過剰に報告しない
- 不明な変更は「要調査」として報告
