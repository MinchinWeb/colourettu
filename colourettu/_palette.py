# This is part of colourettu. See http://minchin.ca/colourettu/

from __future__ import absolute_import

from PIL import Image

from ._colour import Colour


class Palette:
    """Class for creating a palette of colours.

    A palette here is a list of colours.

    Args:
        start_colour (colourettu.colour): the colour you want your palette to
            start with.
        end_colour (colourettu.colour): the colour you want your palette to
            end with.

    .. note::

        If a *string*, *tuple*, or *list* is provided for `start_colour` or
        `end_colour`, a conversion to a :py:class:`colourettu.Colour` object
        will be attempted.

    .. code:: python

        p1 = colourettu.Palette()
        p1.to_image('p1.png', 60)

    .. image:: p1.png

    .. code:: python

        all_colours = [c1, c2, c3, c4, c5, c6]
        p2 = colourettu.Palette()
        p2.from_list(all_colours)
        p2.to_image('p2.png', max_width=360, vertical=False)

    .. image:: p2.png

    """

    # TODO: Convert these code examples to an external file, so we can
    # auto-generate the .png files!
    #
    # see http://sphinx-doc.org/markup/code.html#includes

    _start = None
    _end = None
    _colours = []

    def __init__(self, start_colour=Colour("#FFF"), end_colour=Colour("#000")):
        # testing to see if the type is colourettu.colour throws an error.
        # This is an ugly hack.
        # TODO: Fix this!
        colour_for_type = Colour()
        if type(start_colour) is type(colour_for_type):
            self._start = start_colour
        else:
            try:
                self._start = Colour(start_colour)
            except:
                raise ValueError("Invalid start_colour given.")
        if type(end_colour) is type(colour_for_type):
            self._end = end_colour
        else:
            try:
                self._end = Colour(end_colour)
            except:
                raise ValueError("Invalid end_colour given.")

        self._colours = [self._start, self._end]

    def __repr__(self):
        return('<colourettu.Palette {} to {}, {} colours>'.format(
               self._start, self._end, len(self._colours)))

    def __str__(self):
        return('{}'.format(", ".join([c.hex() for c in self._colours])))

    def __len__(self):
        return(len(self._colours))

    def __add__(self, other):
        """
        Combine two Palettes.

        - adding two `colourettu.Palette`s will concatenate the two together
        - if two `colourettu.Palette`s are added, and the last colour of the
        first palette is the same as the first colour of the second palette,
        that colour will only appear once in the new palette
        - `colourettu.Palette`s and `colourettu.Colour`s can be added to
        create new `colourettu.Palette`s
        """
        colour_for_type = Colour()
        palette_for_type = Palette()
        if type(other) is type(colour_for_type):
            self._colours.append(other)
            self._end = other
            return self
        elif type(other) is type(palette_for_type):
            if (self._end == other._start):
                self._colours.extend(other._colours[1:])
            else:
                self._colours.extend(other._colours)
            self._end = other._end
            return self
        else:
            raise TypeError('unsupported opperand type(s) for +: {} and'
                            '{}'.format(type(self), type(other)))

    def __radd__(self, other):
        # used for `Colour + Palette`
        colour_for_type = Colour()
        if type(other) is type(colour_for_type):
            self._colours.insert(0, other)
            self._start = other
            return self
        else:
            raise TypeError('unsupported opperand type(s) for +: {} and'
                            '{}'.format(type(self), type(other)))

    # TO-DO     def __init__(self)   #this allows :  for colour in palette:

    def from_list(self, list_of_colours, normalized_rgb=False):
        """
        Given an interable (usually a list or a tuple) containing
        :py:class:`Colour` s,
        this then becomes the Colours contained by the Palette.

        Args:
            list_of_colours(list, tuple, or other interable): a collection of
                :py:class:`Colour` s to be loaded into the palette. If these
                are :py:class:`colourettu.Colour` 's, they will be loaded
                directly. Otherwise, an attempt to convert each item to a
                :py:class:`colourettu.Colour` will take place.
            normalized_rgb(bool): assuming the list is to be converted to
                :py:class:`colourettu.Colour` s, this parameter is passed on
                as part of
                that conversion process.

        .. note:

            This will overwrite the colours already defined by the palette.

        """
        colour_for_type = Colour()
        self._colours = []

        for c in list_of_colours:
            if type(c) is type(colour_for_type):
                self._colours.append(c)
            else:
                self._colours.append(Colour(c, normalized_rgb))

        self._start = self._colours[0]
        self._end = self._colours[-1]

    def to_image(self, filename='palette.png', band_width=1, length=60,
                 max_width=0, vertical=True, alpha_channel=False):
        """
        Creates an image from the palette.

        Args:
            filename(Optional[string]): filename of saved file. Defaults to
                ``palette.png`` in the current working directory.
            band_width(optional[int]): how wide each colour band should be.
                Defaults to 1 pixel.
            length(Optional[int]): the length of the overall image in pixels.
                This is the dimension orthogonal to ``band_width``. Defaults
                to 60 pixels.
            max_width(Optional[int]): if ``band_width`` is not set and this is,
                this determines how wide the whole image should be.
            vertical(Optional[bool]): if the image runs vertical (``True``,
                default) or horizontal (``False``).
            alpha_channel(Optional[bool]): if ``True``, the created image will
                have an Alpha channel. Defaults to ``False``.
        """
        # max_width is approximate
        # generate output pictures for documentation automatically

        if max_width < 1:
            pass
        else:
            band_width = int(max_width/len(self._colours))

        image_width = band_width * len(self._colours)

        if alpha_channel:
            my_image = Image.new('RGBA', (image_width, length))
        else:
            my_image = Image.new('RGB', (image_width, length))
        image_loaded = my_image.load()

        x = 0
        for my_colour in self._colours:
            for x1 in range(band_width):
                for y in range(length):
                    image_loaded[x, y] = my_colour.rgb()
                x = x + 1

        if vertical:
            my_image = my_image.rotate(270)

        my_image.save(filename)
