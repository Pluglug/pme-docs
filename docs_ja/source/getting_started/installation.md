# PME のインストール

Pie Menu Editor (PME) をBlenderにインストールしましょう。

## 前提条件

### システム要件
- **OS**: Windows 10/11, macOS 10.15+, Linux (Ubuntu 18.04+ 推奨)
- **Blender**: バージョン 3.2 - 4.5
- **ストレージ**: 約20MB の空き容量

### 購入要件
- Gumroad または Blender Market アカウント
- PME の有効なライセンス

## インストール

::::{tab-set}
:sync-group: install-update

:::{tab-item} Blender 4.2以降
:sync: blender42

1.  購入プラットフォーム（Gumroad、Blender Market）からアドオンの`.zip`ファイルをダウンロードします。
2.  Blenderを開き、**Edit > Preferences**を選択します。

```{image} _static/getting_started/install_from_disk.png
:alt: ディスクからインストール
:width: 50%
:align: right
```

3.  **Add-ons**タブに移動し、右上の{material-regular}`keyboard_arrow_down`をクリックしてから、**Install from Disk...** をクリックします。
4.  ダウンロードした`.zip`ファイルを選択し、**Install Add-on**をクリックします。
5.  アドオンを有効にします。

:::

:::{tab-item} Blender 4.1以前
:sync: blender41

1.  購入プラットフォーム（Gumroad、Blender Market）からアドオンの`.zip`ファイルをダウンロードします。
2.  Blenderを開き、**Edit > Preferences**を選択します。
3.  **Add-ons**タブに移動し、**Install...** ボタンをクリックします。
4.  ダウンロードした`.zip`ファイルを選択し、**Install Add-on**をクリックします。
5.  アドオンを有効にします。

:::

::::

## アップデート方法

::::{tab-set}
:sync-group: install-update

:::{tab-item} Blender 4.2以降
:sync: blender42

1.  **エクスポートボタン**を使用してパイメニューをバックアップします。
2.  Blenderを開き、**Edit > Preferences**を選択します。
3.  **Add-ons**タブに移動し、右上の{material-regular}`keyboard_arrow_down`をクリックしてから、**Install from Disk...** をクリックします。
4.  ダウンロードした新しい`.zip`ファイルを選択し、**Install Add-on**をクリックします。
5.  アドオンを有効にします。
6.  Blenderを再起動します。

:::

:::{tab-item} Blender 4.1以前
:sync: blender41

1.  **エクスポートボタン**を使用してパイメニューをバックアップします。
2.  Blenderを開き、**Edit > Preferences**を選択します。
3.  **Add-ons**タブに移動し、**Install...** ボタンをクリックします。
4.  ダウンロードした新しい`.zip`ファイルを選択し、**Install Add-on**をクリックします。
5.  アドオンを有効にします。
6.  Blenderを再起動します。

:::

::::

:::{admonition} Blender 4.2で「legacy add-on」と表示されるのは問題ですか？
:class: tip
いいえ、問題ありません。これは新しいExtensionシステムとの違いを示すだけで、機能に影響はありません。
:::

## インストール後の確認

以下の画面が表示されれば、インストールは完了です。

```{image} _static/getting_started/install_success.png
:alt: Install Success
:width: 50%
:align: right
```

もし、「See System Console」と表示された場合は、なにかエラーが発生しています。\
システムコンソールを開いてください。

```{image} _static/getting_started/some_error.png
:alt: See System Console
:width: 50%
:align: right
```

:::{admonition} システムコンソールはどこにありますか？
:class: tip
Blenderのシステムコンソールを開くには、**View > Toggle System Console**を選択します。
:::

### インストールエラー
(WIP)

**エラー**: "Module not found"
- **原因**: Blenderバージョン非対応
- **解決**: サポート対象バージョンの確認

**エラー**: "Permission denied"
- **原因**: 管理者権限不足
- **解決**: Blenderを管理者として実行

### 動作エラー

**問題**: アドオンが表示されない
- **確認事項**: アドオンの有効化状態
- **解決手順**: Preferences > Add-ons > Pie Menu Editor にチェック


## インストール後の技術的詳細

PMEのインストール後、Blenderのアドオンディレクトリに以下のフォルダが作成されます：

```{code-block} text
addons/
├── pie_menu_editor/          # アドオン本体
│   ├── __init__.py
│   ├── operators.py
│   ├── ui.py
│   └── ...
└── pie_menu_editor_data/     # ユーザーデータ保存用
    ├── pie_menus.json
    ├── settings.json
    └── backups/
```

### フォルダの役割

**`pie_menu_editor/`**
- PMEアドオンの本体ファイルが格納されます
- アップデート時にこのフォルダは完全に置き換えられます

**`pie_menu_editor_data/`**
- ユーザーが作成したパイメニューの設定
- カスタマイズした設定やバックアップファイル
- アップデート時も**保持される**ため、設定が失われません

:::{admonition} データ保護の仕組み
:class: tip
この2つのフォルダに分ける設計により、アドオンをアップデートしてもユーザーのカスタマイズが失われることがありません。`pie_menu_editor_data/`フォルダは常に保護されます。
:::

### アドオンディレクトリの場所

アドオンディレクトリの場所は以下の通りです：

::::{tab-set}
:sync-group: os-paths

:::{tab-item} Windows
:sync: windows

```text
%APPDATA%\Blender Foundation\Blender\[バージョン]\scripts\addons\
```

例：`C:\Users\[ユーザー名]\AppData\Roaming\Blender Foundation\Blender\4.2\scripts\addons\`
:::

:::{tab-item} macOS
:sync: macos

```text
~/Library/Application Support/Blender/[バージョン]/scripts/addons/
```

例：`/Users/[ユーザー名]/Library/Application Support/Blender/4.2/scripts/addons/`
:::

:::{tab-item} Linux
:sync: linux

```text
~/.config/blender/[バージョン]/scripts/addons/
```

例：`/home/[ユーザー名]/.config/blender/4.2/scripts/addons/`
:::

::::

## 次のステップ

インストールが完了したら、[クイックチュートリアル](quick_tutorial.md)に進んでください。
