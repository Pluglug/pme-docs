.. _popup-dialog-editor:

Pop-up Dialog
==============

Pop-up Dialog Editor allows you to create a layout of widgets that can be displayed in pie menus, dialogs, panels or toolbars.

Mode
-----

.. image:: /_static/images/original/popup/pme_popup_mode.png
   :alt: Pop-up dialog mode settings
   :align: center

|

Affects the appearance and behavior of the pop-up.

.. list-table::
   :header-rows: 1
   :widths: 40 20 20 20
   :class: mode-table

   * - Mode
     - Pie
     - Dialog
     - Popup
   * - Moving the mouse outside the pop-up closes it
     - ❌
     - ❌
     - ✓
   * - Interaction with widgets of the pop-up closes it
     - ✓
     - ❌
     - ❌
   * - OK button
     - ❌
     - ✓
     - ❌
   * - Movable
     - ❌
     - ✓
     - ✓
   * - Customizable width
     - ❌
     - ✓
     - ✓

|

Hotkeys
---------------

Button Hotkeys
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 0
   :class: hotkey-table

   * - :kbd:`LMB`
     - Open Menu
   * - :kbd:`Ctrl+LMB`
     - Add Button to the Right
   * - :kbd:`Ctrl+Shift+LMB`
     - Add Button to the Left
   * - :kbd:`Ctrl+Alt+LMB`
     - Remove Button
   * - :kbd:`Shift+LMB`
     - Edit Button
   * - :kbd:`Alt+LMB`
     - Change Icon
   * - :kbd:`Alt+OS+LMB`
     - Clear Icon
   * - :kbd:`Alt+Shift+LMB`
     - Hide Text
   * - :kbd:`OS+LMB`
     - Toggle Spacer
   * - :kbd:`Ctrl+OS+LMB`
     - Copy Button
   * - :kbd:`Ctrl+Shift+OS+LMB`
     - Paste Button

|

Row Button Hotkeys
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 0
   :class: hotkey-table

   * - :kbd:`LMB`
     - Open Menu
   * - :kbd:`Ctrl+LMB`
     - Add Row Below
   * - :kbd:`Ctrl+Shift+LMB`
     - Add Row Above
   * - :kbd:`Shift+LMB`
     - Toggle Row Size
   * - :kbd:`OS+LMB`
     - Toggle Row Spacer


Layout
---------------

.. image:: /_static/images/original/popup/pme_layout.gif
   :alt: Layout demonstration
   :align: center

|

.. raw:: html

    <style>
    .layout-colors span {
        padding: 0 4px;
        border-radius: 3px;
        color: white;
    }
    </style>
    
    <div class="layout-colors">
        <p>Blender uses row/column based layout system. The editor allows you to set-up a column of <span style="background-color:rgb(213, 77, 77)">rows</span> with optional <span style="background-color:rgb(45, 100, 178)">sub-columns</span> and <span style="background-color:rgb(65, 178, 42)">sub-rows</span>.</p>
    </div>

.. Blender uses row/column based layout system. The editor allows you to set-up a column of :guilabel:`rows` with optional :guilabel:`sub-columns` and :guilabel:`sub-rows`.



|

In order to add a sub-column, use :kbd:`LMB` on one of the buttons to open a menu and select *Column* separator.
To add a sub-row to the sub-column there are *Begin Subrow* and *End Subrow* entries in the menu.

If you need more options to control the layout you can write python code in Custom tab which will be used to draw custom layout of widgets instead of default button.

Expand Layout
---------------

.. image:: /_static/images/original/popup/pme1.14.0_pd_expand.png
   :alt: Expand layout settings
   :align: center

|

To expand layout inside pie menus or another popup dialog you need to enable *Expand Popup Dialog* option in *Menu* tab.

Fixed Columns
---------------

.. image:: /_static/images/original/popup/pme_layout_fixed_columns.png
   :alt: Fixed columns demonstration
   :align: center

|

By default Blender resizes columns depending on the number of buttons in sub-rows. You can enable *Fixed Columns* option to fix that.

Alignment
---------------

.. image:: /_static/images/original/popup/pme_layout_alignment.gif
   :alt: Alignment demonstration
   :align: center

|

You can adjust the alignment of buttons if there are no columns in the current row.

.. raw:: html

    <style>
    .mode-table, .hotkey-table {
        width: 100%;
        margin: 1em 0;
    }

    .mode-table td, .hotkey-table td {
        padding: 0.5em;
    }

    .mode-table th {
        background-color: #f5f5f5;
        font-weight: bold;
    }

    </style>
