ボタンがクリックされた時に実行される任意のPythonコードを設定します。

```python
# オペレーターを実行する
bpy.ops.object.mode_set(mode='OBJECT')

# 条件分岐を使用する (Ctrlを押していた場合はモンキーを追加、それ以外は立方体を追加)
O.mesh.primitive_monkey_add() if E.ctrl else O.mesh.primitive_cube_add()
```

:::{admonition} コマンドの記述方法
:class: important

Blenderの文字列プロパティーは、複数行のコマンドを記述できません。
そのため、複数のコマンドを記述する場合は、セミコロン(`;`)で区切る必要があります。

参考: [Pythonコマンドの記述方法](../python/index.md)

:::

:::{admonition} グローバル変数
:class: hint

**利用可能なグローバル変数の例：**
- `C`: bpy.context（現在のBlenderコンテキスト）
- `O`: bpy.ops（Blenderのオペレーター）
- `E`: event（イベント情報）

[こちら](../reference/scripting.rst)でさらに詳細なグローバル変数の一覧を確認できます。
:::
