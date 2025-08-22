:::{image} /_static/images/editors/pie_menu/pie_hotkey.png
:alt: Pie Menu Editor Hotkey
:width: 100%
:align: center
:::

パイメニューを呼び出すホットキーを設定します。

#### キーマップ
Blenderのキーマップは階層構造になっており、適切なキーマップを選択することで既存のホットキーを上書きできます。既存のホットキーのキーマップとアクションを調べるには、**+ボタン**を押してください。

適切なKeymapの選び方は、[Keymapの選び方](../reference/keymap_guide.md)を参照してください。

#### ホットキーモード
- **Press**: キーを押す
- **Hold**: キーを押し続ける  
- **Tweak**: キーを押しながらマウスを動かす
- **Double Click**: キーをダブルクリックする

#### モディファイア
**Any modifier**は、Ctrl、Shift、Alt、OSKeyの任意の組み合わせです。コンテキスト感応ツールの作成に使用できます。

```python
print("Ctrl is pressed" if E.ctrl else "Ctrl isn't pressed")
```

このアドオンでは**マウスボタンをホットキーモディファイアとして使用**できます。つまり、LMB+Tab、RMB+Tab、MMB+Tabなどのホットキーが使用可能です。

