Changelog
=========

.. currentmodule:: colourettu

- :support:`149` swap from Travis-CI to GitHub Actions for Continuous
  Integration
- :bug:`148` proofread documentation
- :support:`148` drop official support for Python < 3.7, including
  dropping support for Python 2. I haven't changed anything in the codebase
  that I expect will break these earlier versions, but I'm no longer testing
  against them.
- :support:`148` switch to personal fork of `PSphinxTheme
  <https://github.com/MinchinWeb/PSphinxTheme/tree/colourettu>`_ and `lconf lexer
  <https://github.com/MinchinWeb/python_lconf_lexer>`_ (i.e. basically the
  documentation theme) as to provide versions that can be installed with
  current versions of *pip*. Specifically, these private version provide
  PEP440-style version numbers.
- :support:`148` black-ify codebase
- :support:`148` update *isort* to v5
- :support:`148` update minimum versions of several dependicies to remove
  support for version with known security issues.
- :support:`148` upgrade to `minchin.releaser
  <https://github.com/MinchinWeb/minchin.releaser>`_ package. Colourettu was
  previously using an early vendorized version of this.
- :release:`2.0.0 <2016-11-28>`
- :feature:`6` add *blend* functionality as both standalone functionaility as
  :py:func:`blend()` and as a method of the Palette class as
  :py:func:`Palette.blend()`
- :bug:`- major` :py:func:`Palette.to_image()` now treats ``max_width`` as a
  maximum width. This way there isn't a black bar on the bottom/left of the
  image if the number of bands do not devide evenly into ``max_width``.
- :bug:`- major` [Breaking] Update :py:class:`Colour` and :py:class:`Palette`
  class naming to CapWords-style, to match PEP8.
- :support:`40` update cloud theme to v1.8, and with it Sphinx to v1.4. Also
  added to documentation layout improvements. (also :issue:`30`, :issue:`31`)
- :support:`-` ship tests such that the command ``green colourettu`` works
  from the command-line after ``colourettu`` has been installed on the system
- :support:`-` ship tests as a subpackage of ``colourettu``
- :support:`-` re-arragne and simplify internal package metadata and
  corresponding changes in ``setup.py``
- :support:`14` add code-style tests as another part of the Travis-CI
  test suite

- :release:`1.1.0 <2015-07-20>`
- :support:`5` add project logo
- :feature:`8` allow addition of palettes, and palettes and colours
- :support:`-` manage changelog with
  `Releases <https://github.com/bitprophet/releases>`_
- :feature:`-` add :py:class:`Palette` class
- :feature:`-` allow creation of colours from normalized rgb values
- :support:`-` update to Sphinx 1.3 for documentation generation

- :release:`1.0.0 <2015-01-17>`
- :support:`1` documentation is now online at
  `minchin.ca/colourettu <http://www.minchin.ca/colourettu/>`_
- :support:`-` convert Readme and Changelog from Markdown to ReStructured Text
- :bug:`- major` *colourettu.color* (note, no *u*) no longer an alias for
  *colourettu.colour* (with the *u*)
- :release:`0.1.1 <2014-12-11>`
- :bug:`-` include extra files so module can install off of pip
- :release:`0.1.0 <2014-12-11>`
- :feature:`-` first working version!
- :feature:`-` base :py:class:`Colour` class, and (relative)
  :py:func:`luminance` and :py:func:`contrast` functions
