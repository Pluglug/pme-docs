.. _property-editor:

Property Editor
===============

The editor allows you to register new `Properties <https://docs.blender.org/api/current/bpy.props.html>`_ without coding.

Supported Property Types
-------------------------

* BoolProperty
* IntProperty
* FloatProperty
* StringProperty
* EnumProperty
* Vector properties

Usage
------

.. raw:: html

   <div class="video-container">
      <iframe src="https://www.youtube.com/embed/xQ-ETd8xacA" frameborder="0" allowfullscreen></iframe>
   </div>

|

Storing Values
---------------

By default PME stores property values in Add-on Preferences. If you want to store some custom data in *.blend* files you need to assign the property to some type.

For example, if you assign *MyProperty* to *Object* type, the data will be stored in *.blend* files for each object in the scene:

.. image:: /_static/images/original/props/pme_prop_storing.png
   :alt: Property storing example
   :align: center

|

Now you can use *MyProperty* like any other *Object's* property:

.. code-block:: python

   C.object.MyProperty = True

Functions
----------

.. image:: /_static/images/original/props/pme_prop_funcs.png
   :alt: Property functions
   :align: center

|

Scripting
----------

To get the value of the Property by its name use *props()* function:

.. code-block:: python

   value = props("MyProperty")
   value = props().MyProperty

To set the value use:

.. code-block:: python

   props("MyProperty", value)
   props().MyProperty = value

Custom tab usage example:

.. code-block:: python

   L.prop(props(), "MyBoolProperty", text=slot, icon='COLOR_GREEN' if props("MyBoolProperty") else 'COLOR_RED')


Examples
---------

Slider
^^^^^^^

.. image:: /_static/images/original/props/pme_prop_slider.png
   :alt: Slider property example
   :align: center

|

Color Widget
^^^^^^^^^^^^^^^^^

.. image:: /_static/images/original/props/pme_prop_color.png
   :alt: Color widget example
   :align: center

|

Direction Widget
^^^^^^^^^^^^^^^^^

.. image:: /_static/images/original/props/pme_prop_direction.png
   :alt: Direction widget example
   :align: center

|

Icon-Only Tab Bar
^^^^^^^^^^^^^^^^^

.. image:: /_static/images/original/props/pme_prop_tabbar.png
   :alt: Icon-only tab bar example
   :align: center

|

Directory Path
^^^^^^^^^^^^^^^^^

.. image:: /_static/images/original/props/pme_prop_path.png
   :alt: Directory path example
   :align: center

|