Requirements
============

The main *colourettu* module, has the following dependencies:

.. include:: ../setup.py
   :start-line: 68
   :end-line: 69
   :literal:

Testing
-------

Testing *colourettu* requires:

.. include:: ../.requirements/test.in
   :literal:

For unit test, then run (from the base directory)::

    green colourettu.tests -vv

For code-style test, then run (from the base directory)::

    isort colourettu setup.py tasks.py --verbose
    black colourettu
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

.. include:: ../.requirements/docs.in
   :literal:

Then run (on Windows) (from the ``docs`` directory)::

    make dirhtml

To upload the documention, then run (still from the ``docs`` directory)::

    ghp-import -p _build/dirhtml
