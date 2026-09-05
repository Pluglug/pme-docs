カスタムなウィジェットレイアウトを描画するためのPythonコードを設定します。
`L`はレイアウトオブジェクトを表し、Blenderのレイアウトシステムを使用してUIを構築できます。

```python
# ボックス内にラベルを表示
L.box().label(text=text, icon=icon, icon_value=icon_value)

# 複数のボタンを縦に配置
col = L.column(); operator(col, "mesh.primitive_cube_add", text="立方体"); operator(col, "mesh.primitive_uv_sphere_add", text="球")
```
