Upgrading
=========

This page is to give hints on upgrade between version of colourettu.

0.1.1 -> 1.0
--------------

In version 0.1.1, you could access the *colour* class by using the American
spelling. In version 1.0, this has been removed. If the extra *u* is
causing problems, the suggested work-around is:

.. code:: python

	from colourettu import colour as color
