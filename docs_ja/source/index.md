```{note}
このドキュメントは、[オリジナルのPMEドキュメント](https://archive.blender.org/wiki/2015/index.php/User:Raa/Addons/Pie_Menu_Editor/)のPMEファンによる更新版です。
```

![Pie Menu Editor Logo](/_static/images/original/pme_logo.webp)

---

# PMEドキュメントへようこそ

Pie Menu Editor (PME)は、Blenderのインターフェースを思いのままにカスタマイズできるアドオンです。パイメニューやマクロ、カスタムパネルなど、プログラミング知識がなくても手軽に作業環境を改善できます。

```{include} getting_started/feature_overview.md
```

```{admonition} プログラミングの知識は必要ですか?
:class: hint
いいえ、PMEはプログラミングなしでも十分強力です。\
もちろん、Pythonを学習すればさらに柔軟なカスタマイズが可能になります。決して難しくありません！ぜひチャレンジしてみてください！

**何か分からないことがあれば、[GitHub Discussions (日本語可)](https://github.com/Pluglug/pie-menu-editor-fork/discussions)でお気軽にご質問ください！**
```

## PMEの入手方法

PMEはroaoaoさんが有料で販売しているBlenderアドオンです。
ぜひ以下の公式販売サイトからご購入ください：

- **[SuperHive (Blender Market)](https://superhivemarket.com/products/pie-menu-editor?ref=7373)**
- **[Gumroad](https://roaoao.gumroad.com/l/pie_menu_editor)**

なお、当プロジェクトでは、コミュニティによるメンテナンス版も提供予定ですが、
まずは公式版のご購入をお願いします。


```{admonition} 開発を応援する
:class: tip

PMEは現在、オリジナル開発者のroaoaoさんに代わってPMEファンが個人的にメンテナンスしています。\
もしこの活動があなたのお役に立っているようでしたら、[GitHub Sponsors](https://github.com/sponsors/pluglug)にてご支援いただけると嬉しいです。

- 新しいBlenderバージョンへの対応
- バグ修正とパフォーマンス改善
- ドキュメントの充実
- 新機能の開発
- ユーザーサポート

小額でも大変励みになります。\
よろしくお願いします。
```

---

## コミュニティへの参加

以下の場所で情報交換や開発協力を受け付けています：

### 質問・情報交換
- [Blender Artists Forum](http://blenderartists.org/forum/showthread.php?392910): 使い方の質問、カスタマイズ例の共有
- [GitHub Discussions](https://github.com/Pluglug/pie-menu-editor-fork/discussions): 新機能のアイデア、意見交換

### バグ報告・開発協力
- [Issue Tracker](https://github.com/Pluglug/pie-menu-editor-fork/issues): バグ報告、機能リクエスト
- [Pull Requests](https://github.com/Pluglug/pie-menu-editor-fork/pulls): コード改善、新機能の実装
- {ref}`contribute-to-pme`: 開発参加について

### ドキュメント作成
{ref}`contribute-to-docs`では以下のご協力をお待ちしています：

- 内容の確認・校正
- 日本語・英語間の翻訳
- 画像・GIF・動画の提供
- 使用例やチュートリアルの追加

---

```{admonition} 関連リンク
:class: seealso

:::{hlist}
:columns: 3

* [Blender](https://www.blender.org/)
* [Blender Development Fund](https://fund.blender.org/)
* [Blender Manual](https://docs.blender.org/manual/en/latest/)
* [Blender Python API](https://docs.blender.org/api/current/)

* [PME Original Documentation](https://archive.blender.org/wiki/2015/index.php/User:Raa/Addons/Pie_Menu_Editor/)
* [PME Blender Artists Forum](http://blenderartists.org/forum/showthread.php?392910)
* [PME Fork Repository](https://github.com/Pluglug/pie-menu-editor-fork)
* [PME Docs Repository](https://github.com/Pluglug/pme-docs)
* [PME Become a Sponsor](https://github.com/sponsors/Pluglug)
:::
```

---

```{toctree}
:maxdepth: 1
:caption: はじめる

getting_started/installation
getting_started/basic_pie_menu
getting_started/popup_dialog_tutorial
getting_started/macro_tutorial
```

```{toctree}
:maxdepth: 2
:caption: エディタ
:hidden:

editors/pie_menu_editor
editors/regular_menu_editor
editors/popup_dialog_editor
editors/sticky_key_editor
editors/stack_key_editor
editors/macro_operator_editor
editors/modal_operator_editor
editors/editor_common_elements
editors/ui_customization
editors/property_editor
editors/custom_icons
editors/settings
```

```{toctree}
:maxdepth: 2
:caption: 参考資料
:hidden:

reference/terminology
reference/scripting
reference/examples
reference/keymap_guide
```

```{toctree}
:maxdepth: 2
:caption: サポート
:hidden:

support_community/faq
support_community/get_support
support_community/contribute_to_pme
support_community/changelog
```

```{toctree}
:maxdepth: 2
:caption: 開発者向け
:hidden:

reference/architecture/index
```