Requirements
============

If you are just using the main *colourettu* module, it
has no other dependencies.

Testing
-------

Testing *colourettu* requires:

 - green

Then run (from the base directory)::

	green tests


Documentation Generation
------------------------
To geneation the documentation (this) for *colourettu*,
*colourettu* itself must be installed (it is imported in
the process of building the docuemtation).
The following depencies are also required:

 - sphinx 1.2
 - sphinxcontrib-napoleon

Then run (on Windows) (from the ``docs`` directory)::

	make html
