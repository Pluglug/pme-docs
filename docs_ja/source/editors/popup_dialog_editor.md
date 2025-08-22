(popup-dialog-editor)=

# Popup Dialog Editor

<div class="video-container">
   <iframe src="https://www.youtube.com/embed/JdbmDSV9wIU" frameborder="0" allowfullscreen></iframe>
</div>

ポップアップダイアログエディタでは、パイメニュー、ダイアログ、パネル、ツールバーに表示可能なウィジェットのレイアウトを作成できます。

## レイアウト

![レイアウトのデモンストレーション](/_static/images/original/popup/pme_layout.gif)

<style>
.layout-colors span {
    padding: 0 4px;
    border-radius: 3px;
    color: white;
}
</style>

<div class="layout-colors">
    <p>Blenderは行/列ベースのレイアウトシステムを使用します。エディタでは、<span style="background-color:rgb(213, 77, 77)">行</span>の列を設定し、オプションで<span style="background-color:rgb(45, 100, 178)">サブ列</span>と<span style="background-color:rgb(65, 178, 42)">サブ行</span>を追加できます。</p>
</div>

サブ列を追加するには、ボタンの1つで{kbd}`LMB`を使ってメニューを開き、*Column*セパレータを選択します。
サブ列にサブ行を追加するには、メニューにある*Begin Subrow*と*End Subrow*のエントリを使用します。

レイアウトをより詳細に制御する必要がある場合は、Customタブでpythonコードを記述することで、デフォルトボタンの代わりにカスタムウィジェットレイアウトを描画できます。

## レイアウト展開

![レイアウト展開設定](/_static/images/original/popup/pme1.14.0_pd_expand.png)

パイメニューや他のポップアップダイアログ内でレイアウトを展開するには、*Menu*タブで*Expand Popup Dialog*オプションを有効にする必要があります。

## 固定列

![固定列のデモンストレーション](/_static/images/original/popup/pme_layout_fixed_columns.png)

デフォルトでは、Blenderはサブ行内のボタン数に応じて列サイズを調整します。*Fixed Columns*オプションを有効にすることで、これを固定できます。

## 配置

![配置のデモンストレーション](/_static/images/original/popup/pme_layout_alignment.gif)

現在の行に列がない場合、ボタンの配置を調整できます。




## モード

![ポップアップダイアログのモード設定](/_static/images/original/popup/pme_popup_mode.png)

ポップアップの見た目と動作に影響します。

:::{table} モード
:widths: 50 50 50 50
:align: left

| モード | Pie | Dialog | Popup |
|:------|:-------:|:-------:|:-------:|
| マウスをポップアップ外に移動すると閉じる | ❌ | ❌ | ✅ |
| ポップアップ内のウィジェットとの操作で閉じる | ✅ | ❌ | ❌ |
| OKボタン | ❌ | ✅ | ❌ |
| 移動可能 | ❌ | ✅ | ✅ |
| 幅のカスタマイズ可能 | ❌ | ✅ | ✅ |
:::

## 編集用ホットキー

:::{table} ボタン操作
:widths: 30 15 15 15 15 15
:align: left

| 機能 | {kbd}`LMB` | {kbd}`Ctrl` | {kbd}`Shift` | {kbd}`Alt` | {kbd}`OS` |
|------|:---:|:---:|:---:|:---:|:---:|
| メニューを開く | {kbd}`LMB` | | | | |
| ボタンを編集 | {kbd}`LMB` | | {kbd}`Shift` | | |
| 右にボタンを追加 | {kbd}`LMB` | {kbd}`Ctrl` | | | |
| 左にボタンを追加 | {kbd}`LMB` | {kbd}`Ctrl` | {kbd}`Shift` | | |
| ボタンを削除 | {kbd}`LMB` | {kbd}`Ctrl` | | {kbd}`Alt` | |
| アイコンを変更 | {kbd}`LMB` | | | {kbd}`Alt` | |
| アイコンをクリア | {kbd}`LMB` | | | {kbd}`Alt` | {kbd}`OS` |
| テキストを非表示 | {kbd}`LMB` | | {kbd}`Shift` | {kbd}`Alt` | |
| スペーサーを切り替え | {kbd}`LMB` | | | | {kbd}`OS` |
| ボタンをコピー | {kbd}`LMB` | {kbd}`Ctrl` | | | {kbd}`OS` |
| ボタンを貼り付け | {kbd}`LMB` | {kbd}`Ctrl` | {kbd}`Shift` | | {kbd}`OS` |
:::

:::{table} 行の管理操作
:widths: 30 20 20 20 10
:align: left

| 機能 | {kbd}`LMB` | {kbd}`Ctrl` | {kbd}`Shift` | {kbd}`OS` |
|------|:---:|:---:|:---:|:---:|
| メニューを開く | {kbd}`LMB` | | | |
| 下に行を追加 | {kbd}`LMB` | {kbd}`Ctrl` | | |
| 上に行を追加 | {kbd}`LMB` | {kbd}`Ctrl` | {kbd}`Shift` | |
| 行サイズを切り替え | {kbd}`LMB` | | {kbd}`Shift` | |
| 行スペーサーを切り替え | {kbd}`LMB` | | | {kbd}`OS` |
:::

<style>
.mode-table, .hotkey-table {
    width: 100%;
    margin: 1em 0;
}

.mode-table td, .hotkey-table td {
    padding: 0.5em;
}

.mode-table th {
    background-color: #f5f5f5;
    font-weight: bold;
}
</style>