"""
Colourettu is a collection of colour related functions.

Colourettu is a small collection of colour functions in Python. These can be
used to determine the (relative) luminosity of a colour and the contrast
between two colours. There is also the palette class for dealing with a 'list'
of colours.
"""

# This is part of colourettu. See http://minchin.ca/colourettu/

from __future__ import absolute_import

from ._colour import *
from ._palette import *

from .__version__ import __version__
