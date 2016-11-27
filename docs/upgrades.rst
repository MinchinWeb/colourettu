Upgrading
=========

This page is to give hints on upgrading between version of colourettu.

1.0 -> 2.0
----------

In version 2.0.0, the *Colour* and *Palette* classes were renamed to the
CapWords-style, to better match PEP8. The suggested work-around, if needed is:

.. code:: python

    from colourettu import Colour as colour
    from colourettu import Palette as palette

0.1.1 -> 1.0
--------------

In version 0.1.1, you could access the *colour* class by using the American
spelling. In version 1.0, this has been removed. If the extra *u* is
causing problems, the suggested work-around, if needed is:

.. code:: python

	from colourettu import colour as color
