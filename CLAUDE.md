# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the documentation repository for Pie Menu Editor (PME), a Blender addon that allows users to customize Blender's interface through pie menus, popup dialogs, macros, and custom panels.

**Two separate documentation builds:**
- `docs/` - English documentation
- `docs_ja/` - Japanese documentation

Each has its own Sphinx configuration and build directory. The Japanese documentation is the primary development language, with English translations following.

## Repository Structure

```
pme-docs/                      # Documentation repository (this repo)
├── docs/                      # English documentation
│   ├── source/                # English source files (.md)
│   │   ├── conf.py            # English Sphinx config
│   │   ├── index.md
│   │   ├── getting_started/
│   │   ├── editors/
│   │   ├── reference/
│   │   ├── support_community/
│   │   └── _static/           # Static assets (CSS, JS, images)
│   ├── build/en/              # English build output
│   ├── Makefile
│   └── make.bat
├── docs_ja/                   # Japanese documentation
│   ├── source/                # Japanese source files (.md)
│   │   ├── conf.py            # Japanese Sphinx config
│   │   └── (same structure as English)
│   └── build/                 # Japanese build output
├── build_docs.py              # Build script for both languages
├── start_autobuild.sh         # Dev server startup script
└── requirements.txt           # Python dependencies

MyScriptDir/addons/pie_menu_editor/  # Actual addon code (separate workspace)
├── __init__.py                # Blender addon entry point
├── ed_*.py                    # Editor modules (ed_pie_menu, ed_popup, etc.)
├── operators.py               # PME operators
├── preferences.py             # Addon preferences UI
├── keymap_helper.py           # Keymap management
└── (many other utility modules)
```

## Common Commands

### Development Server (Live Preview)

```bash
# Japanese documentation (primary development)
cd docs_ja
make livehtml
# or: sphinx-autobuild source build --host 0.0.0.0 --port 8000 --open-browser

# English documentation
cd docs
make livehtml
```

The dev server auto-rebuilds on file changes and serves at http://localhost:8000.

### Building Documentation

```bash
# Build both English and Japanese versions
python build_docs.py

# Build only English version
cd docs
make html
# Windows: make.bat html

# Build only Japanese version
cd docs_ja
sphinx-build source build
```

Output locations:
- English: `docs/build/en/index.html`
- Japanese: `docs_ja/build/index.html`

### Installing Dependencies

```bash
pip install -r requirements.txt
```

Dependencies: sphinx, sphinx_rtd_theme, myst-parser, sphinx-design, sphinx-autobuild, furo, sphinxcontrib-mermaid

## Documentation Architecture

### Source Format

- **Markup**: MyST (Markdown for Sphinx) with `.md` extension
- **Theme**: Furo (both languages)
- **Extensions**: myst_parser, sphinx_design, sphinx.ext.intersphinx

### Key Sphinx Configuration

Both `docs/source/conf.py` and `docs_ja/source/conf.py` share similar settings:
- Project name: "Pie Menu Editor"
- Release version: Check conf.py for current version
- MyST extensions: colon_fence, deflist, html_admonition, html_image, replacements, smartquotes, substitution, tasklist
- Custom CSS: `_static/css/custom.css`
- Custom JS: `_static/js/force-light.js`

### Content Organization

Documentation follows this structure:
- `getting_started/` - Installation, tutorials, feature overview
- `editors/` - Individual editor documentation (pie menu, popup dialog, etc.)
- `reference/` - Advanced topics (scripting, examples, terminology)
- `support_community/` - FAQ, changelog, contribution guide

## PME Addon Architecture

The actual addon code is in a separate workspace directory: `E:\0187_Pie-Menu-Editor\MyScriptDir\addons\pie_menu_editor`

PME is a complex Blender addon with 60+ modules. Key editor modules:
- `ed_base.py` - Base editor class with common functionality
- `ed_pie_menu.py`, `ed_popup.py`, `ed_menu.py` - Menu editors
- `ed_panel_group.py` - Side panel editor
- `ed_stack_key.py`, `ed_sticky_key.py` - Key behavior editors
- `ed_macro.py`, `ed_modal.py`, `ed_property.py` - Operator/property editors

Key utility modules: `keymap_helper.py`, `layout_helper.py`, `operator_utils.py`, `bl_utils.py`

**For detailed architecture investigation, use `/investigate-feature [feature_name]` slash command.**

### Key PME Concepts

When documenting PME features:
1. **Slots**: Menu/dialog items (Commands, Hotkeys, Menus, Properties, Custom code)
2. **Editors**: Different UI customization types (pie menu, popup, panel, etc.)
3. **Hotkey Settings**: Keymap configuration for triggering custom UIs
4. **Custom Icons**: Icon assignment for menu items
5. **Scripting**: Python code execution in Custom slots

## Available Slash Commands

Use these custom commands to streamline documentation workflows:

- **`/investigate-feature [feature_name]`** - Investigate PME source code and create documentation draft
- **`/translate-to-en [file_path]`** - Translate Japanese docs to English (e.g., `editors/sticky_key_editor.md`)
- **`/check-source-changes [period]`** - Check recent PME source changes and identify doc updates needed
- **`/create-draft [section] [topic] [file_name]`** - Create new documentation draft with source investigation
- **`/build-preview [lang]`** - Build docs and check for errors/warnings (lang: `ja`, `en`, or `both`)
- **`/sync-versions`** - Check and sync version info between PME addon and documentation
- **`/merge-to-main`** - Selectively merge `.claude/` and `CLAUDE.md` from feature/ja-rough to main

## Development Workflow

### Typical Documentation Task Flow

1. Edit Japanese source in `docs_ja/source/` (primary development language)
2. Use `make livehtml` in `docs_ja/` for live preview
3. Commit changes when content is complete
4. Later, use `/translate-to-en` to reflect improvements to English version
5. Build both versions with `python build_docs.py` or `/build-preview`

### Workflow Examples

**Creating new feature documentation:**
1. `/investigate-feature sticky_key` - Investigate and create draft
2. User reviews and enhances the draft
3. `/translate-to-en editors/sticky_key_editor.md` - Translate to English
4. `/build-preview` - Verify build

**Syncing with PME updates:**
1. `/check-source-changes` - Check recent changes
2. `/investigate-feature [changed_feature]` - Investigate specific changes
3. Update relevant documentation files
4. `/sync-versions` - Ensure version consistency

### File Editing

- Use MyST (Markdown) syntax with Sphinx directives
- Common directives: `{note}`, `{warning}`, `{admonition}`, `{include}`, `{ref}`
- Images: Place in `_static/images/` and reference with `/_static/images/filename.ext`
- Cross-references: Use `{ref}label` syntax (define labels with `(label-name)=`)

## Branch Strategy

### feature/ja-rough (Personal Experimental Branch)

**Purpose**: Personal workflow experiments and Japanese draft writing

**Commit Style**: Casual, Japanese OK
```bash
git commit -m "パイメニューのドキュメント追加"
git commit -m "WIP: スティッキーキー調査中"
```

**Files to keep private**:
- `DEPLOYMENT.md` - Personal deployment notes
- `PLAN.md` - Personal planning notes
- Work-in-progress files in `docs_ja/`

### main (Public Branch)

**Purpose**: Public release branch

**Commit Style**: English, organized, follows [Conventional Commits](https://www.conventionalcommits.org/)
```bash
git commit -m "docs: add Sticky Key editor documentation

- Add basic usage guide
- Include hotkey configuration examples
- Add troubleshooting section"
```

**Merge Strategy**: Selective merge of `.claude/` and `CLAUDE.md` only
- Use `/merge-to-main` command for automated merging
- See `.claude/COMMIT_RULES.md` for detailed guidelines

## Commit Message Rules

### For main branch (REQUIRED)

**Format**: `<type>: <subject>`

**Types**:
- `docs`: Documentation additions/updates
- `feat`: New feature documentation
- `fix`: Typo fixes, broken link fixes
- `refactor`: Structural changes
- `chore`: Build config, meta files, settings

**Examples**:
```bash
# Good
git commit -m "docs: add Sticky Key editor documentation"
git commit -m "chore: update Claude Code configuration"
git commit -m "fix: correct broken links in getting started guide"

# Bad (don't use on main)
git commit -m "ドキュメント追加"  # Japanese
git commit -m "update files"      # Too vague
```

### For feature/ja-rough (FLEXIBLE)

Any style is acceptable - Japanese, casual, WIP commits are fine.

## Language Switching Feature

The deployed documentation includes a language switcher in the top-right:
- English version: `example.com/editors/pie_menu_editor.html`
- Japanese version: `example.com/ja/editors/pie_menu_editor.html`

The switcher preserves the current page path when switching languages.

## Important Notes

- **Two separate Sphinx projects**: English and Japanese are built independently
- **Japanese-first development**: Write content in Japanese, then improve English version
- **Addon code is separate**: The actual PME addon code is in a different workspace directory
- **Community-maintained**: This documentation is a community effort to update the original PME documentation
- **Version correspondence**: Documentation version should match the PME addon version (currently 1.18.8 in docs, 1.19.2-beta in addon)
