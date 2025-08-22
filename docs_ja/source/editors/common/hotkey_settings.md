:::{image} /_static/images/editors/common/hotkey.png
:class: img-shadow
:alt: Hotkey Settings
:width: 100%
:align: center
:::

<div style="margin: 1.5rem 0;"></div>

```{grid} 1 1 2 3
:gutter: 2

::::{grid-item-card} キーマップ
:class-card: ex-card ex-card--keymap

Blenderのキーマップは階層構造です。適切なキーマップを選ぶことで既存のホットキーを安全に上書きできます。既存のホットキーのキーマップやアクションを調べるには、エディタの`+`ボタンを使用してください。

- 参考: [Keymapの選び方](../reference/keymap_guide.md)
::::

::::{grid-item-card} ホットキーモード
:class-card: ex-card ex-card--hotkey

- **Press**: キーを押す
- **Hold**: キーを押し続ける  
- **Tweak**: キーを押しながらマウスを動かす
- **Double Click**: キーをダブルクリックする
::::

::::{grid-item-card} モディファイア
:class-card: ex-card ex-card--modifier

**Any modifier** は Ctrl / Shift / Alt / OSKey の任意の組み合わせです。コンテキスト感応ツールの作成に使えます。

このアドオンではマウスボタンをモディファイアとして使えます（例: LMB+Tab / RMB+Tab / MMB+Tab）。

```python
print("Ctrl is pressed" if E.ctrl else "Ctrl isn't pressed")
```

::::

