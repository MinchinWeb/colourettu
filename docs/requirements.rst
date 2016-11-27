Requirements
============

The main *colourettu* module, has the following dependencies:

.. include:: ../requirements.txt
   :literal:

Testing
-------

Testing *colourettu* requires:

.. include:: ../colourettu/test/requirements.txt
   :literal:

For unit test, then run (from the base directory)::

    green colourettu.tests -vv

For code-style test, then run (from the base directory)::

    isort --recursive colourettu --verbose
    pydocstyle colourettu
    pycodestyle colourettu

.. note:: Code-style tests remain aspirational at this point, and so
          failures here are permitted.

Before packaging, check the manifest (``Manifest.in``) by running (from the
base directory)::

    check-manifest -v


Documentation Generation
------------------------
To generation the documentation (this) for *colourettu*,
*colourettu* itself must be installed (it is imported in
the process of building the documentation).
The following dependencies are also required:

.. include:: requirements.txt
   :literal:

Then run (on Windows) (from the ``docs`` directory)::

    make dirhtml
