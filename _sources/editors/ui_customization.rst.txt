.. _ui-customization:

.. include:: side_panel_editor.rst

----

.. include:: hiding_unused_panels.rst

----

.. _pme-menu-panel-extension:

Menu/Panel Extension
====================

.. raw:: html

   <div class="video-container">
      <iframe src="https://www.youtube.com/embed/iO9PzLX6EDQ" frameborder="0" allowfullscreen></iframe>
   </div>

----

.. _pme-toolbar:

PME Toolbar
===========

.. admonition:: Note
   :class: warning

   It stopped working after 4.3. I am in the process of fixing this.
   Your support through `GitHub Sponsors <https://github.com/sponsors/pluglug>`_ helps me to work on this and other features.

PME allows you to use the *User Preferences* area as a toolbar when its width or height is minimal:

.. image:: /_static/images/original/toolbars/pme_toolbars.gif
   :alt: PME Toolbar
   :align: center

|

.. raw:: html

   <div class="video-container">
      <iframe src="https://www.youtube.com/embed/PB3wtlZ6AaM" frameborder="0" allowfullscreen></iframe>
   </div>


Naming
------

Toolbars display popup dialog's layout depending on its name:

.. code-block:: text

   Toolbar <Screen Name> <Position>

Where *Screen Name* and *Position* are optional and *Position* takes one of these values: *Left*, *Right*, *Top*, *Bottom*.

Examples
--------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - ``Toolbar Top``
     - Top toolbar, all screens
   * - ``Toolbar UV Editing Right``
     - Right toolbar, *UV Editing* screen
   * - ``Toolbar 3D View Full``
     - Any toolbar, *3D View Full* screen

Saving
------

Toolbar widgets are stored in *User Preferences*. The position and size of the toolbars are stored in *.blend* files. So in order to save your toolbars, you need to use both :menuselection:`File --> User Preferences --> Save User Settings` and :menuselection:`File --> Save Startup File` commands.

By default Blender loads UI stored in *.blend* files. To keep the current UI (including toolbars) you need to uncheck *Load UI* option:

.. image:: /_static/images/original/toolbars/pme_load_ui.png
   :alt: PME Load UI option

|