from __future__ import absolute_import

# from ._luminance import luminance
from ._colour import colour
from ._colour import _luminance as luminance
from ._colour import _contrast as contrast

from ._colour import _A_contrast as A_contrast
from ._colour import _AA_contrast as AA_contrast
from ._colour import _AAA_contrast as AAA_contrast

color = colour


__version__ = '0.1.1'
