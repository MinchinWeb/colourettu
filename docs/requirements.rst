Requirements
============

The main *colourettu* module, has the following dependencies:

.. include:: ../requirements.txt
   :literal:

Testing
-------

Testing *colourettu* requires:

.. include:: ../tests/requirements.txt
   :literal:

Then run (from the base directory)::

	green test -vv


Documentation Generation
------------------------
To generation the documentation (this) for *colourettu*,
*colourettu* itself must be installed (it is imported in
the process of building the documentation).
The following dependencies are also required:

.. include:: requirements.txt
   :literal:

Then run (on Windows) (from the ``docs`` directory)::

	make html
