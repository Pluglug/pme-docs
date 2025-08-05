<!-- 機能概要のデザイン変更後に再検討 -->

```{note}
このドキュメントは、[オリジナルのPMEドキュメント](https://archive.blender.org/wiki/2015/index.php/User:Raa/Addons/Pie_Menu_Editor/)のコミュニティによる更新版です。
```

![Pie Menu Editor Logo](/_static/images/pme_logo.webp)

---

# PMEドキュメントへようこそ

Pie Menu Editor (PME)は、Blenderのインターフェースを自由にカスタマイズできるアドオンです。コーディング無しで気軽にカスタマイズできるため、あらゆるBlenderユーザーにとって
<!-- Pie Menu Editor (PME)は、Blenderのインターフェースをあなたの創造的なビジョンに合わせて再構築する力を与えます。直感的なメニュー作成とホットキーカスタマイズを通じて、PMEはあなたのワークフローのアイデアを現実に変えます。 -->

```{include} getting_started/feature_overview.md
```

```{note}
完璧なBlender設定は、わずか数クリックで実現できます - コーディングは不要です。
Pythonを探索する準備ができている方には、PMEはBlenderをさらに拡張する高度なオプションを提供します。
```

```{admonition} 持続可能な開発のサポート
:class: important

PMEの開発とメンテナンスは主にボランティアの貢献に依存しています。
[GitHub Sponsors](https://github.com/sponsors/pluglug)（月額$1から）を通じたあなたのサポートが、
これらの活動を持続可能にするのに役立ちます：

- 新しいBlenderバージョンとの互換性アップデート
- バグ修正と安定性の向上
- ドキュメントの強化
- 新機能の開発
- 迅速で信頼性の高いサポート

あなたのサポートがPMEをさらに良いツールへと進化させます。
```

```{todo}
サポートセクション
```

---

## コミュニティに参加

PMEの開発とドキュメントは、コミュニティの協力によって発展しています。
以下の方法で参加できます：

### 共有と学習
- [Blender Artists Forum](http://blenderartists.org/forum/showthread.php?392910): 質問をしたり、カスタマイズ例を共有したり
- [GitHub Discussions](https://github.com/Pluglug/pie-menu-editor-fork/discussions): 新機能を提案したり、アイデアを交換したり

### 開発への貢献
- [Issue Tracker](https://github.com/Pluglug/pie-menu-editor-fork/issues): バグの報告や機能のリクエスト
- [Pull Requests](https://github.com/Pluglug/pie-menu-editor-fork/pulls): コードの改善や新機能の追加
- {ref}`contribute-to-pme`: 開発参加ガイドライン

### ドキュメントの改善
{ref}`contribute-to-docs`プロジェクトは以下を歓迎します：

- コンテンツのレビューと校正
- ドキュメントの翻訳
- 例とリソースへの貢献

```{admonition} 関連リンク
:class: hint

:::{hlist}
:columns: 2

* [Blender](https://www.blender.org/)
* [Blender Development Fund](https://fund.blender.org/)
* [Blender Manual](https://docs.blender.org/manual/en/latest/)
* [Blender Python API](https://docs.blender.org/api/current/)

* [PME Original Documentation](https://archive.blender.org/wiki/2015/index.php/User:Raa/Addons/Pie_Menu_Editor/)
* [PME Blender Artists Forum](http://blenderartists.org/forum/showthread.php?392910)
* [PME Fork Repository](https://github.com/pluglug/pie-menu-editor-fork)
* [PME Docs Repository](https://github.com/pluglug/pme-docs)
* [PME Become a Sponsor](https://github.com/sponsors/pluglug)
:::
```

---

```{toctree}
:maxdepth: 1
:caption: はじめに

getting_started/installation
getting_started/basic_pie_menu
getting_started/popup_dialog_tutorial
getting_started/macro_tutorial
```

```{toctree}
:maxdepth: 2
:caption: エディター
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
:caption: リファレンス
:hidden:

reference/terminology
reference/scripting
reference/examples
```

```{toctree}
:maxdepth: 2
:caption: サポート & コミュニティ
:hidden:

support_community/faq
support_community/get_support
support_community/contribute_to_pme
support_community/changelog
```