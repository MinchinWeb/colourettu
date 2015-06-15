"""This is part of colourettu. See http://minchin.ca/colourettu/ """

from math import sqrt, pow


class colour:

    '''Base class for dealing with colours.

    Args:
        mycolour (str, list, or tuple):  string of hex representation of colour
            you are creating, or
            a 3 item list or tuple of the red, green, and blue channels of
            the colour you are creating. Default is "#FFF" (white).

    Colours are created by calling the ``colour`` class. Colour values can
    be provided via 3 or 6 digit hex notation, or providing a list or a
    tuple of the Red, Green, and Blue values (as integers).

    .. code:: python

        import colourettu

        c1 = colourettu.colour()        # defaults to #FFF
        c2 = colourettu.colour("#eee")  # equivalent to #EEEEEE
        c3 = colourettu.colour("#456bda")
        c4 = colourettu.colour([3, 56, 129])
        c5 = colourettu.colour((63, 199, 233))

    The value of each channel can be pulled out:

    .. code:: python

        >>> c4.red()
        3
        >>> c4.green()
        56
        >>> c4.blue()
        129

    You can also get the colour back as either a hex value, or a rgb tuple:

    .. code:: python

        >>> c2.hex()
        '#EEEEEE'
        >>> c2.rgb()
        (238, 238, 238)
    '''

    _r = _g = _b = None

    def __init__(self, mycolour="#FFF"):
        if type(mycolour) is str:
            if mycolour.startswith("#"):
                myhex = mycolour[1:]
                if len(myhex) % 3 != 0:
                    raise ValueError("Invalid Hex Colour")
                thirds = int(len(myhex)/3)
                r, g, b = myhex[0:thirds], myhex[thirds:2*thirds], \
                    myhex[2*thirds:3*thirds]
                if len(r) == 1:
                    r = r + r
                if len(g) == 1:
                    g = g + g
                if len(b) == 1:
                    b = b + b
                self._r = int(r, 16)
                self._g = int(g, 16)
                self._b = int(b, 16)
            else:
                raise ValueError("Strings must start with '#'")
        elif type(mycolour) in(list, tuple):
            if len(mycolour) == 3:
                if (type(mycolour[0]) is int) and (type(mycolour[1]) is int) and (type(mycolour[2]) is int):
                    self._r, self._g, self._b = mycolour
                else:
                    raise TypeError('Tuple and Lists must be three integers.')
            else:
                raise ValueError('Tuples and Lists must be three items long.')
        else:
            raise TypeError('Must supply a string, a list, or a tuple')

    def __repr__(self):
        return('<colourettu.colour {}>'.format(self.hex()))

    def __str__(self):
        return('{}'.format(self.hex()))

    def hex(self):
        '''
        Returns:
            str: the colour as a HTML-sytle hex string
        '''
        return "#{:02x}{:02x}{:02x}".format(self._r, self._g, self._b).upper()

    def red(self):
        '''
        Returns:
            int: value of the red channel of the colour
        '''
        return self._r

    def green(self):
        '''
        Returns:
            int: value of the green channel of the colour
        '''
        return self._g

    def blue(self):
        '''
        Returns:
            int: value of the blue channel of the colour
        '''
        return self._b

    def rgb(self):
        '''
        Returns:
            tuple: the rgb values of the colour (with values between 0 and 255)
        '''
        return(self._r, self._g, self._b)

    def normalized_rgb(self):
        r'''
        Returns:
            tuple: the rgb values of the colour (with values normalized between
                   0.0 and 1.0)

        .. note::

            Uses the formula:

            \\[ r_{norm} = \\begin{cases}
            \\frac{r_{255}}{12.92}\\ \\qquad &\\text{if $r_{255}$ $\\le$ 0.03928}
            \\\\
            \\left(\\frac{r_{255} + 0.055}{1.055}\\right)^{2.4}
            \\quad &\\text{otherwise}
            \\end{cases} \\]

        '''
        '''Source:
        http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
        '''

        r1 = self._r / 255
        g1 = self._g / 255
        b1 = self._b / 255

        if r1 <= 0.03928:
            r2 = r1 / 12.92
        else:
            r2 = pow(((r1 + 0.055) / 1.055), 2.4)
        if g1 <= 0.03928:
            g2 = g1 / 12.92
        else:
            g2 = pow(((g1 + 0.055) / 1.055), 2.4)
        if b1 <= 0.03928:
            b2 = b1 / 12.92
        else:
            b2 = pow(((b1 + 0.055) / 1.055), 2.4)

        return (r2, g2, b2)

    def luminance(self):
        '''calls ``colourettu.luminance()`` on the colour defined'''
        return _luminance(self)

    def contrast(self, myothercolour):
        '''calls ``colourettu.contrast()`` on the colour defined'''
        return _contrast(self, myothercolour)


def _luminance(mycolour):
    r'''Determine (relative) luminance of a colour.

    Args:
        mycolour (colourettu.colour):

    Luminance is a measure of how 'bright' a colour is. Values are
    normalized so that the Luminance of White is 1 and the Luminance of
    Black is 0. That is to say:

    .. code:: python

        >>> colourettu.luminance("#FFF")    # white
        0.9999999999999999
        >>> colourettu.luminance("#000")    # black
        0.0

    ``luminance()`` can also be called on an already existing colour:

    .. code:: python

        >>> c3.luminance()
        0.2641668488934239
        >>> colourettu.luminance(c4)
        0.08007571268096524

    .. note::

        Uses the formula:

        \\[ lum = \\sqrt{0.299 r^2 + 0.587 g^2 + 0.114 b^2} \\]
    '''

    if type(mycolour) is colour:
        mycolour2 = mycolour
    else:
        try:
            mycolour2 = colour(mycolour)
        except:
            raise TypeError("Must supply a colourettu.colour")

    (r1, g1, b1) = mycolour2.normalized_rgb()

    return sqrt(0.299*pow(r1, 2) + 0.587*pow(g1, 2) + 0.114*pow(b1, 2))


def _contrast(colour1, colour2):
    r'''Determines the contrast between two colours.

    Args:
        colour1 (colourettu.colour):
        colour2 (colourettu.colour):

    Contrast the difference in (perceived) brightness between colours.
    Values vary between 1:1 (a given colour on itself) and 21:1 (white on
    black).

    To compute contrast, two colours are required.

    .. code:: python

        >>> colourettu.contrast("#FFF", "#FFF") # white on white
        1.0
        >>> colourettu.contrast(c1, "#000") # black on white
        20.999999999999996
        >>> colourettu.contrast(c4, c5)
        4.363552233203198

    ``contrast`` can also be called on an already existing colour, but a
    second colour needs to be provided:

    .. code:: python

        >>> c4.contrast(c5)
        4.363552233203198

    .. note::

        Uses the formula:

        \\[ contrast = \\frac{lum_1 + 0.05}{lum_2 + 0.05} \\]

    **Use of Contrast**

    For Basic readability, the ANSI standard is a contrast of 3:1 between
    the text and it's background. The W3C proposes this as a minimum
    accessibility standard for regular text under 18pt and bold text under
    14pt. This is referred to as the *A* standard. The W3C defines a higher
    *AA* standard with a minimum contrast of 4.5:1. This is approximately
    equivalent to 20/40 vision, and is common for those over 80. The W3C
    define an even higher *AAA* standard with a 7:1 minimum contrast. This
    would be equivalent to 20/80 vision. Generally, it is assumed that those
    with vision beyond this would access the web with the use of assistive
    technologies.

    If needed, these constants are stored in the library.

    .. code:: python

        >>> colourettu.A_contrast
        3.0
        >>> colourettu.AA_contrast
        4.5
        >>> colourettu.AAA_contrast
        7.0

    I've also found mention that if the contrast is *too* great, this can
    also cause readability problems when reading longer passages. This is
    confirmed by personal experience, but I have been (yet) unable to find
    any quantitative research to this effect.
    '''

    if type(colour1) is colour:
        mycolour1 = colour1
    else:
        try:
            mycolour1 = colour(colour1)
        except:
            raise TypeError("colour1 must be a colourettu.colour")

    if type(colour2) is colour:
        mycolour2 = colour2
    else:
        try:
            mycolour2 = colour(colour2)
        except:
            raise TypeError("colour2 must be a colourettu.colour")

    lum1 = mycolour1.luminance()
    lum2 = mycolour2.luminance()

    minlum = min(lum1, lum2)
    maxlum = max(lum1, lum2)

    return (maxlum + 0.05) / (minlum + 0.05)

_A_contrast = 3.0
_AA_contrast = 4.5
_AAA_contrast = 7.0
