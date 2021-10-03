"""
Colourettu is a collection of colour related functions.

Colourettu is a small collection of colour functions in Python. These can be
used to determine the (relative) luminosity of a colour and the contrast
between two colours. There is also the palette class for dealing with a 'list'
of colours.
"""

# This is part of colourettu. See http://minchin.ca/colourettu/

from __future__ import absolute_import

# METADATA

__title__ = "Colourettu"
__description__ = "Colourettu is a collection of colour related functions."
__url__ = "http://minchin.ca/colourettu/"
__author__ = "William Minchin"
__email__ = "w_minchin@hotmail.com"
__license__ = "MIT License"
__copyright_years__ = '2014-16'
__copyright__ = "Copyright (c) {} {}".format(__copyright_years__, __author__)

"""
This project uses the Semantic Versioning scheme in conjunction with PEP 0440:

    <http://semver.org/>
    <https://www.python.org/dev/peps/pep-0440>

Major versions introduce significant changes to the API, and backwards
compatibility is not guaranteed. Minor versions are for new features and other
backwards-compatible changes to the API. Patch versions are for bug fixes and
internal code changes that do not affect the API.

Version 0.x should be considered a development version with an unstable API,
and backwards compatibility is not guaranteed for minor versions.
"""
__version__ = "2.0.0"

# Package Implementation

from ._colour import *
from ._palette import *
