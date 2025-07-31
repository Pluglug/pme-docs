<!-- Reconsider after changing the design of the feature overview -->

```{note}
This documentation is a community-maintained update of the [original PME documentation](https://archive.blender.org/wiki/2015/index.php/User:Raa/Addons/Pie_Menu_Editor/).
```

![Pie Menu Editor Logo](/_static/images/pme_logo.webp)

---

# Welcome to PME Documentation

Pie Menu Editor (PME) empowers you to reshape Blender's interface to match your creative vision. Through intuitive menu creation and hotkey customization, PME turns your workflow ideas into reality.

```{include} getting_started/feature_overview.md
```

```{note}
Your perfect Blender setup is just a few clicks away - no coding required.
For those ready to explore Python, PME offers advanced options to extend Blender even further.
```

```{admonition} Supporting Sustainable Development
:class: important

PME's development and maintenance relies primarily on volunteer contributions.
Your support through [GitHub Sponsors](https://github.com/sponsors/pluglug) (starting from $1/month)
helps make these activities sustainable:

- Compatibility updates for new Blender versions
- Bug fixes and stability improvements
- Documentation enhancement
- New feature development
- Fast and reliable support

Your support drives PME's evolution into an even better tool.
```

```{todo}
Get Support Section
```

---

## Join the Community

PME's development and documentation thrive through community collaboration.
Here's how you can participate:

### Share and Learn
- [Blender Artists Forum](http://blenderartists.org/forum/showthread.php?392910): Ask questions and share customization examples
- [GitHub Discussions](https://github.com/Pluglug/pie-menu-editor-fork/discussions): Propose new features and exchange ideas

### Contribute to Development
- [Issue Tracker](https://github.com/Pluglug/pie-menu-editor-fork/issues): Report bugs and request features
- [Pull Requests](https://github.com/Pluglug/pie-menu-editor-fork/pulls): Improve code and add new features
- {ref}`contribute-to-pme`: Development participation guidelines

### Improve Documentation
The {ref}`contribute-to-docs` project welcomes:

- Content review and proofreading
- Documentation translation
- Contributions to Examples & Resources

```{admonition} Related Links
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
:caption: Getting Started

getting_started/installation
getting_started/basic_pie_menu
getting_started/popup_dialog_tutorial
getting_started/macro_tutorial
```

```{toctree}
:maxdepth: 2
:caption: Editors
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
:caption: Reference
:hidden:

reference/terminology
reference/scripting
reference/examples
```

```{toctree}
:maxdepth: 2
:caption: Support & Community
:hidden:

support_community/faq
support_community/get_support
support_community/contribute_to_pme
support_community/changelog
```