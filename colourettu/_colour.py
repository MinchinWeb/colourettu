# This is part of colourettu. See http://minchin.ca/colourettu/

import math


class Colour:
    """
    Base class for dealing with colours.

    Args:
        my_colour (str, list, or tuple):  string of hex representation of colour
            you are creating, or
            a 3 item list or tuple of the red, green, and blue channels of
            the colour you are creating. Default is "#FFF" (white).
        normalized_rgb (bool): whether the values for the red, green, and blue
            channels are *normalized* (i.e. values scaled from 0 to 1) or not
            (i.e. values scaled from 0 to 255). Default is *False*.

    Colours are created by calling the ``Colour`` class. Colour values can
    be provided via 3 or 6 digit hex notation, or providing a list or a
    tuple of the Red, Green, and Blue values (as integers, if
    ``normalized_rgb=False``, or as floating numbers between 0 and 1 if
    ``normalized_rgb=True``).

    .. code:: python

        import colourettu
        from colourettu import Colour

        c1 = Colour()        # defaults to #FFF
        c2 = Colour("#eee")  # equivalent to #EEEEEE
        c3 = Colour("#456bda")
        c4 = Colour([3, 56, 129])
        c5 = Colour((63, 199, 233))
        c6 = Colour([0.242, 0.434, 0.165], normalized_rgb=True)

    The value of each channel can be pulled out:

    .. code:: pycon

        >>> c4.red()
        3
        >>> c4.green()
        56
        >>> c4.blue()
        129

    You can also get the colour back as either a hex value, or a rgb tuple:

    .. code:: pycon

        >>> c2.hex()
        '#EEEEEE'
        >>> c2.rgb()
        (238, 238, 238)

    Colours are considered equal is the values of the R, G, and B channels
    match.

    .. code:: pycon

        >>> c1 == c2
        False
        >>> c2 == Color([238, 238, 238])
        True
    """

    _r = _g = _b = None

    def __init__(self, my_colour="#FFF", normalized_rgb=False):
        if type(normalized_rgb) is not bool:
            raise TypeError("normalized_rgb must be either True or False")

        if type(my_colour) is str:
            if my_colour.startswith("#"):
                my_hex = my_colour[1:]
                if len(my_hex) % 3 != 0:
                    raise ValueError("Invalid Hex Colour")
                thirds = int(len(my_hex) / 3)
                r, g, b = (
                    my_hex[0:thirds],
                    my_hex[thirds : 2 * thirds],
                    my_hex[2 * thirds : 3 * thirds],
                )
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
        elif type(my_colour) in (list, tuple):
            if len(my_colour) == 3:
                if not normalized_rgb:
                    if (
                        (type(my_colour[0]) is int)
                        and (type(my_colour[1]) is int)
                        and (type(my_colour[2]) is int)
                    ):
                        self._r, self._g, self._b = my_colour
                    else:
                        raise TypeError(
                            "Tuple and Lists must be three"
                            "integers if normalized_rgb=False."
                        )
                else:
                    if (
                        (type(my_colour[0]) in (float, int))
                        and (type(my_colour[1]) in (float, int))
                        and (type(my_colour[2]) in (float, int))
                    ):
                        if (
                            (0 <= my_colour[0] <= 1)
                            and (0 <= my_colour[1] <= 1)
                            and (0 <= my_colour[2] <= 1)
                        ):
                            self._r = int(my_colour[0] * 255)
                            self._g = int(my_colour[1] * 255)
                            self._b = int(my_colour[2] * 255)
                        else:
                            raise ValueError(
                                "Normalized RGB values must be" "between 0 and 1."
                            )
                    else:
                        raise TypeError(
                            "Tuples and Lists must be three"
                            "floating point numbers if"
                            "normalized_rgb=True"
                        )
            else:
                raise ValueError("Tuples and Lists must be three items long.")
        else:
            raise TypeError("Must supply a string, a list, or a tuple")

    def __repr__(self):
        return "<colourettu.Colour {}>".format(self.hex())

    def __str__(self):
        return "{}".format(self.hex())

    def __eq__(self, other):
        """
        Determine if Colours are 'equal'.

        Colours are considered equal if the values of the R, G, and B channels
        match.
        """
        return (
            (self._r is other.red())
            and (self._g is other.green())
            and (self._b is other.blue())
        )

    def hex(self):
        """
        Returns the HTML-style hex code for the Colour.

        Returns:
            str: the colour as a HTML-sytle hex string
        """
        return "#{:02x}{:02x}{:02x}".format(self._r, self._g, self._b).upper()

    def red(self):
        """
        Returns the value of the red channel of the Colour.

        Returns:
            int: value of the red channel of the colour
        """
        return self._r

    def green(self):
        """
        Returns the value of the green channel of the Colour.

        Returns:
            int: value of the green channel of the colour
        """
        return self._g

    def blue(self):
        """
        Returns the value of the blue channel of the Colour.

        Returns:
            int: value of the blue channel of the colour
        """
        return self._b

    def rgb(self):
        """
        Returns a tuples of the values of the red, green, and blue channels of
        the Colour.

        Returns:
            tuple: the rgb values of the colour (with values between 0 and 255)
        """
        return (self._r, self._g, self._b)

    def normalized_rgb(self):
        r"""
        Returns a tuples of the normalized values of the red, green, and blue
        channels of the Colour.

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

        `Source <http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef>`_
        """

        r1 = self._r / 255
        g1 = self._g / 255
        b1 = self._b / 255

        if r1 <= 0.03928:
            r2 = r1 / 12.92
        else:
            r2 = math.pow(((r1 + 0.055) / 1.055), 2.4)
        if g1 <= 0.03928:
            g2 = g1 / 12.92
        else:
            g2 = math.pow(((g1 + 0.055) / 1.055), 2.4)
        if b1 <= 0.03928:
            b2 = b1 / 12.92
        else:
            b2 = math.pow(((b1 + 0.055) / 1.055), 2.4)

        return (r2, g2, b2)

    def luminance(self):
        """Calls the :py:func:`luminance` on the colour defined."""
        return luminance(self)

    def contrast(self, my_other_colour):
        """Calls the :py:func:`contrast` on the colour defined."""
        return contrast(self, my_other_colour)


def luminance(my_colour):
    r"""Determine (relative) luminance of a colour.

    Args:
        my_colour(colourettu.Colour): a colour

    Luminance is a measure of how 'bright' a colour is. Values are
    normalized so that the Luminance of White is 1 and the Luminance of
    Black is 0. That is to say:

    .. code:: pycon

        >>> colourettu.luminance("#FFF")    # white
        0.9999999999999999
        >>> colourettu.luminance("#000")    # black
        0.0

    ``luminance()`` can also be called on an already existing colour:

    .. code:: pycon

        >>> c3.luminance()
        0.2641668488934239
        >>> colourettu.luminance(c4)
        0.08007571268096524

    .. note::

        Uses the formula:

        \\[ lum = \\sqrt{0.299 r^2 + 0.587 g^2 + 0.114 b^2} \\]
    """

    colour_for_type = Colour()
    if type(my_colour) is type(colour_for_type):
        my_colour_2 = my_colour
    else:
        try:
            my_colour_2 = Colour(my_colour)
        except (TypeError, ValueError):
            raise TypeError("Must supply a colourettu.Colour")

    (r1, g1, b1) = my_colour_2.normalized_rgb()

    return math.sqrt(
        0.299 * math.pow(r1, 2) + 0.587 * math.pow(g1, 2) + 0.114 * math.pow(b1, 2)
    )


def contrast(colour_1, colour_2):
    r"""Determines the contrast between two colours.

    Args:
        colour_1 (colourettu.Colour): a colour
        colour_2 (colourettu.Colour): a second colour

    Contrast the difference in (perceived) brightness between colours.
    Values vary between 1:1 (a given colour on itself) and 21:1 (white on
    black).

    To compute contrast, two colours are required.

    .. code:: pycon

        >>> colourettu.contrast("#FFF", "#FFF") # white on white
        1.0
        >>> colourettu.contrast(c1, "#000") # black on white
        20.999999999999996
        >>> colourettu.contrast(c4, c5)
        4.363552233203198

    ``contrast`` can also be called on an already existing colour, but a
    second colour needs to be provided:

    .. code:: pycon

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

    .. code:: pycon

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
    """

    colour_for_type = Colour()
    if type(colour_1) is type(colour_for_type):
        my_colour_1 = colour_1
    else:
        try:
            my_colour_1 = Colour(colour_1)
        except (TypeError, ValueError):
            raise TypeError("colour_1 must be a colourettu.colour")

    if type(colour_2) is type(colour_for_type):
        my_colour_2 = colour_2
    else:
        try:
            my_colour_2 = Colour(colour_2)
        except (TypeError, ValueError):
            raise TypeError("colour_2 must be a colourettu.colour")

    lum1 = my_colour_1.luminance()
    lum2 = my_colour_2.luminance()

    min_lum = min(lum1, lum2)
    max_lum = max(lum1, lum2)

    return (max_lum + 0.05) / (min_lum + 0.05)


def blend(colour_1, colour_2):
    r"""Takes two :py:class:`Colour` s and returns the 'average' Colour.

    Args:
        colour_1 (colourettu.Colour): a colour
        colour_2 (colourettu.Colour): a second colour

    .. note::

        Uses the formula:

        \\[ r_{blended} = \\sqrt \\frac{r_1^2 + r_2^2}{2} \\]


        It is shown here for the red channel, but applied independently to each
        of the red, green, and blue channels. The reason for doing it this way
        (rather than using a simple average) is that the brightness of the
        colours is stored in a logarithmic scale, rather than a linear one.

        For a fuller explanation, Minute Physics has released a great
        `YouTube video <https://youtu.be/LKnqECcg6Gw>`_.

    .. seealso:: :py:func:`Palette.blend`
    """
    # raw docstring is needed so that MathJax will render in generated
    # documentation

    # gamma is the power we're going to use to do this conversion
    gamma = 2.0

    # start by normalizing values
    r_1 = colour_1.red() / 255.0
    g_1 = colour_1.green() / 255.0
    b_1 = colour_1.blue() / 255.0
    r_2 = colour_2.red() / 255.0
    g_2 = colour_2.green() / 255.0
    b_2 = colour_2.blue() / 255.0

    r_m = math.pow(((math.pow(r_1, gamma) + math.pow(r_2, gamma)) / 2), 1 / gamma)
    g_m = math.pow(((math.pow(g_1, gamma) + math.pow(g_2, gamma)) / 2), 1 / gamma)
    b_m = math.pow(((math.pow(b_1, gamma) + math.pow(b_2, gamma)) / 2), 1 / gamma)

    c_m = Colour([r_m, g_m, b_m], normalized_rgb=True)

    return c_m


A_contrast = 3.0
AA_contrast = 4.5
AAA_contrast = 7.0
