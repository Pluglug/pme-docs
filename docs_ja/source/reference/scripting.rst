.. _pme-scripting:

===========
スクリプティング
===========

PMEは、Blenderの `Python API <https://docs.blender.org/api/current/>`_ を使用した高度なカスタマイズと自動化を可能にします。
この記事では、PMEのスクリプティング機能の概要と、組み込まれたグローバル変数と関数について説明します。


.. NOTE: RTDでのページ内目次のために必要。furo または book テーマでは不要のためコメントアウト
.. .. contents::
..    :local:
..    :depth: 2
..    :class: this-will-duplicate-information-and-it-is-still-useful-here


-----------
チュートリアル
-----------

- **動画**: `Introduction to Scripting with Python in Blender (vimeo.com) <https://vimeo.com/28203314>`_
- **動画**: `Task Automation with Python Scripting in Blender (youtube.com) <https://www.youtube.com/watch?v=ZZWSvUgR38Y>`_
- `Python for Non-Programmers (python.org) <https://wiki.python.org/moin/BeginnersGuide/NonProgrammers>`_
- `Blender Python API <https://docs.blender.org/api/current/>`_
- `Blender/Python Quickstart <https://docs.blender.org/api/current/info_quickstart.html>`_

----------------
グローバル変数
----------------

PMEの各スロットエディタ内で利用できる変数です。

.. list-table::
    :header-rows: 1
    :widths: 25 75

    * - **変数**
      - **説明**
    * - ``menu``
      - アクティブなメニューの名前
    * - ``slot``
      - アクティブなスロットの名前
    * - ``C``
      - `bpy.context <https://docs.blender.org/api/current/bpy.context.html>`_
    * - ``D``
      - `bpy.data <https://docs.blender.org/api/current/bpy.data.html>`_
    * - ``O``
      - `bpy.ops <https://docs.blender.org/api/current/bpy.ops.html>`_
    * - ``T``
      - `bpy.types <https://docs.blender.org/api/current/bpy.types.html>`_
    * - ``P``
      - `bpy.props <https://docs.blender.org/api/current/bpy.props.html>`_
    * - ``L``
      - 現在の `UILayout <https://docs.blender.org/api/current/bpy.types.UILayout.html>`_ オブジェクト
        
        .. code-block:: python

            L.box().label(text="My Label")
    * - ``E``
      - 現在の `Event <https://docs.blender.org/api/current/bpy.types.Event.html>`_ オブジェクト
        
        .. code-block:: python

            E.ctrl and E.shift and message_box("Ctrl+Shift Pressed")
    * - ``U``
      - ユーザーデータ保存用の `pme.UserData <#pme.UserData>`_ インスタンス

        .. code-block:: python

            U.foo = "value"
            U.update(foo="value1", bar="value2")  
            U.foo
            U.get("foo", "default_value")

---------------
グローバル関数
---------------

PMEのスロットエディタ内で利用できる関数です。コマンドタブとカスタムタブで利用できる関数が異なります。

.. _pme-common-functions:

共通関数
************

.. py:function:: execute_script(path, **kwargs)

    外部のPythonスクリプトを実行します。

    :param str path: スクリプトファイルパス。相対パス（``pie_menu_editor`` フォルダから、推奨）または絶対パス。
    :param kwargs: スクリプトに渡される追加のキーワード引数。
    :return: スクリプト内の ``return_value`` またはデフォルトで ``True``。

    .. warning::
       - 信頼できるソースのスクリプトのみ配置・実行してください
       - 実行前に内容を確認し、必要に応じてバックアップやテスト環境で検証してください
       - ファイル操作や設定変更など、環境に影響する処理が含まれる場合があります

    **スクリプト内で利用可能な変数**：``kwargs``、``__file__``、``return_value``、PMEのすべてのグローバル変数

    **使用例**::

        # 基本的な実行と戻り値
        execute_script("scripts/hello_world.py", msg="Hello World!")
        message_box(execute_script("scripts/get_message.py"))

        # scripts/hello_world.py
        message_box(kwargs["msg"])

        # scripts/get_message.py  
        return_value = "Hi!"

        # パラメータを使用した処理
        # scripts/process_data.py
        kwargs = locals().get("kwargs", {})
        result = my_function(kwargs.get("param1"), kwargs.get("param2", "default"))
        return_value = result
        
        # 呼び出し
        result = execute_script("scripts/process_data.py", param1=200, param2="Hello")

        # カスタムタブでのUI描画
        # scripts/custom_ui.py
        msg = kwargs.get("msg", pme.context.text or "Default Message")
        box = L.box()
        box.label(text=msg, icon=pme.context.icon, icon_value=pme.context.icon_value)
        
        # 呼び出し
        execute_script("scripts/custom_ui.py", msg="カスタムメッセージ")


.. py:function:: props(name=None, value=None)

    PMEプロパティの値を取得または設定します。

    :param str name: プロパティの名前。
    :param value: プロパティの新しい値。
    :return: ``name`` が ``None`` の場合はPMEプロパティコンテナ、``name`` のみが指定された場合はプロパティ値、値を設定する場合は ``True``。

    **例**::

        # 文字列記法を使用してプロパティ値を取得
        value = props("MyProperty")
        
        # 代替: 属性記法を使用してプロパティを取得
        value = props().MyProperty  # props()はプロパティコンテナを返す
        
        # 文字列記法を使用してプロパティ値を設定
        props("MyProperty", value)
        
        # 代替: 属性記法を使用してプロパティを設定
        props().MyProperty = value  # props()はプロパティコンテナを返す


.. py:function:: paint_settings()

    コンテキストに応じたペイント設定を取得します。

    :return: 現在のペイント設定、またはペイントモードでない場合は ``None``。

    **例**::

        ps = paint_settings(); ps and L.template_ID_preview(ps, 'brush')



.. py:function:: find_by(collection, key, value)

    ``collection`` 内で ``key`` が ``value`` と等しい最初のアイテムを検索します。

    :return: 見つかった場合はコレクションアイテム、そうでなければ ``None``。

    **例**::

        m = find_by(C.active_object.modifiers, "type", 'SUBSURF')


.. py:function:: setattr(object, name, value)

    Pythonの組み込み :func:`setattr` と同じですが、設定後に ``True`` を返します。

    :return: ``True``


.. _pme-command-tab-functions:
コマンドタブ関数
*******************

.. py:function:: open_menu(name, slot=None, **kwargs)

    名前を指定してメニュー、パイメニュー、ポップアップダイアログを開くか、スタックキー、スティッキーキー、モーダルオペレーター、またはマクロオペレーターを実行します。

    :param str name: メニューの名前。
    :param slot: スタックキー実行のためのスロットのインデックスまたは名前。
    :param kwargs: ローカル変数として使用されるモーダル/マクロオペレーターの引数。
    :return: メニューが存在する場合は ``True``、そうでなければ ``False``。

    **例**::

        # アクティブオブジェクトのタイプに応じてメニューを開く:
        open_menu("Lamp Pie Menu" if C.active_object.type == 'LAMP' else "Object Pie Menu")

        # Ctrl修飾キーに応じて"My Stack Key"スロットを呼び出す:
        open_menu("My Stack Key", "Ctrl slot" if E.ctrl else "Shift slot")


.. py:function:: toggle_menu(name, value=None)

    メニューを有効または無効にします。

    :param str name: メニューの名前。
    :param bool value: 有効にする場合は ``True``、無効にする場合は ``False``、トグルする場合は ``None``。
    :return: メニューが存在する場合は ``True``、そうでなければ ``False``。


.. py:function:: tag_redraw(area=None, region=None)

    UIエリアまたはリージョンを再描画します。

    :param str area: 再描画する :attr:`Area.type <bpy.types.Area.type>`。``None`` の場合はすべてのエリアを再描画。
    :param str region: 再描画する :attr:`Region.type <bpy.types.Region.type>`。``None`` の場合はすべてのリージョンを再描画。
    :return: ``True``


.. py:function:: close_popups()

    すべてのポップアップダイアログを閉じます。

    :return: ``True``


.. py:function:: overlay(text, **kwargs)

    オーバーレイメッセージを描画します。

    :param str text: 表示するメッセージ。
    :param kwargs: 
        - ``alignment``: ``['TOP', 'TOP_LEFT', 'TOP_RIGHT', 'BOTTOM', 'BOTTOM_LEFT', 'BOTTOM_RIGHT']`` のいずれか。デフォルトは ``'TOP'``。
        - ``duration``: 表示時間（秒）。デフォルトは ``2.0``。
        - ``offset_x``: 水平オフセット。デフォルトは ``10`` ピクセル。
        - ``offset_y``: 垂直オフセット。デフォルトは ``10`` ピクセル。
    :return: ``True``

    **例**::

        overlay('Hello PME!', offset_y=100, duration=1.0)


.. py:function:: message_box(text, icon='INFO', title="Pie Menu Editor")

    メッセージボックスを表示します。

    :param str text: 表示するメッセージ。
    :param str icon: アイコン名（例: 'INFO', 'ERROR', 'QUESTION' など）。
    :param str title: ウィンドウタイトル。
    :return: ``True``


.. py:function:: input_box(func=None, prop=None)

    入力ボックスを表示します。

    :param func: 入力値で呼び出す関数。
    :param str prop: 編集するプロパティへのパス。
    :return: ``True``

    **例**::

        # オブジェクトの名前を変更:
        input_box(prop="C.active_object.name")

        # 入力値を表示:
        input_box(func=lambda value: overlay(value))

.. _pme-custom-tab-functions:
カスタムタブ関数
*********************

.. py:function:: draw_menu(name, frame=True, dx=0, dy=0)

   別のポップアップダイアログまたはパイメニュー内にポップアップダイアログを描画します。

   :param str name: メニュー（ポップアップダイアログ）の名前。
   :param bool frame: フレームを描画するかどうか。
   :param int dx: 水平オフセット。
   :param int dy: 垂直オフセット。
   :return: ポップアップダイアログが存在する場合は ``True``、そうでなければ ``False``。


.. py:function:: operator(layout, operator, text="", icon='NONE', emboss=True, icon_value=0, **kwargs)

    :meth:`UILayout.operator() <bpy.types.UILayout.operator>` と似ていますが、オペレータープロパティの設定が可能です。

    :param layout: :class:`UILayout <bpy.types.UILayout>` インスタンス。
    :param str operator: オペレーターの識別子。
    :return: :class:`OperatorProperties <bpy.types.OperatorProperties>` オブジェクト。

    **例**::

        operator(L, "wm.context_set_int", "Material Slot 1",
                data_path="active_object.active_material_index", value=0)

        # 以下と同じ:
        # op = L.operator("wm.context_set_int", text="Material Slot 1")
        # op.data_path = "active_object.active_material_index"
        # op.value = 0


.. py:function:: custom_icon(filename)

    カスタムアイコンに関連付けられた整数値を取得します。

    :param str filename: ``pie_menu_editor/icons/`` にある拡張子なしのアイコンファイル名。
    :return: カスタムアイコンの整数値。

    **例**::

        L.label(text="My Custom Icon", icon_value=custom_icon("p1"))


.. py:function:: panel(id, frame=True, header=True, expand=None)

    IDによってパネルを描画します。

    :param str id: パネルのID。
    :param bool frame: フレーム付きパネルを描画するかどうか。
    :param bool header: パネルヘッダーを描画するかどうか。
    :param expand: 展開する場合は ``True``、折りたたむ場合は ``False``、現在の状態を使用する場合は ``None``。
    :return: ``True``

    **例**::

        panel("MATERIAL_PT_context_material", True, True, True)

----

-----------------
自動実行スクリプト
-----------------

PMEでは、Blender起動時に自動的に実行されるPythonスクリプトを作成できます。
この機能を使用するには、以下のいずれかの方法で ``pie_menu_editor/scripts/autorun`` フォルダにファイルを配置します：

- 直接 ``.py`` ファイル
- スクリプトを含むフォルダ
- シンボリックリンク

.. warning::
   - 信頼できるソースのスクリプトのみ配置・実行してください
   - 実行前に内容を確認し、必要に応じてバックアップやテスト環境で検証してください
   - ファイル操作や設定変更など、環境に影響する処理が含まれる場合があります

---------------------------------
カスタムグローバル関数の追加
---------------------------------

PMEでカスタム関数を使用するには：

1. ``pie_menu_editor/scripts/autorun`` フォルダにスクリプトを配置
2. ``pme.context.add_global()`` を使用して関数を登録

例：

.. code-block:: python

    def hello_world():
        print("Hello World")

    pme.context.add_global("hello", hello_world)

登録された関数 ``hello()`` は以下で利用可能になります：

- コマンドタブ
- カスタムタブ
- 外部スクリプト


-----------------
PMEコンポーネント
-----------------

PMEは、よく使用される関数、変数、およびユーザー定義の追加項目へのアクセスを提供するグローバルコンテキストを維持します。
このコンテキストは、2つの主要なインターフェースからアクセス可能です：

.. py:class:: pme.context

    .. py:attribute:: globals
        :type: dict

        PMEのグローバルコンテキスト辞書へのアクセス。以下を含みます：
        
        - 組み込みショートカット（``C``, ``D``, ``O``, ``L`` など）
        - 登録されたカスタム関数と値
        - ユーザーデータストレージ（``U``）
        
        .. code-block:: python
            
            from pie_menu_editor import pme
            
            # 外部スクリプトからグローバルにアクセス
            g = pme.context.globals
            props = g.get('props')
            user_data = g.get('U')

    .. py:method:: add_global(key, value)
        
        グローバルコンテキストにカスタム関数または値を登録します。

        :param str key: アイテムにアクセスするための名前
        :param value: 登録する関数または値
        :rtype: None

        .. code-block:: python

            # 関数を登録
            def my_tool():
                bpy.ops.mesh.select_all(action='TOGGLE')
            
            pme.context.add_global("toggle_select", my_tool)

            # 定数を登録
            pme.context.add_global("MAX_ITEMS", 10)

            # コマンドタブ経由でPMEメニューからアクセス:
            # toggle_select()
            # MAX_ITEMS


.. py:class:: pme.UserData

    Blenderセッション中に持続するユーザー定義データのための柔軟なストレージ。

    .. py:method:: get(name, default=None)

        保存された値を取得します。

        :param str name: データキー
        :param default: キーが存在しない場合に返す値
        :return: 保存された値またはデフォルト値

    .. py:method:: update(**kwargs)

        複数の値を一度に更新します。

        .. code-block:: python

            U = pme.context.globals['U']  # UserDataインスタンスを取得
            U.update(tool_state="active", count=5)
            print(U.tool_state)  # "active"
