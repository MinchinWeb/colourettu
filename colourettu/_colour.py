'''Base class for dealing with colours'''

from math import sqrt, pow


class colour:

    _r = _g = _b = None

    def __init__(self, mycolour="#FFF"):
        if type(mycolour) is str and mycolour.startswith("#"):
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
        elif type(mycolour) in(list, tuple) and len(mycolour) == 3:
            self._r, self._g, self._b = mycolour

    def hex(self):
        return "#{:02x}{:02x}{:02x}".format(self._r, self._g, self._b).upper()

    def red(self):
        return self._r

    def green(self):
        return self._g

    def blue(self):
        return self._b

    def rgb(self):
        return(self._r, self._g, self._b)

    def normalized_rgb(self):
        '''returns the rgb values as a tuple, normalized between 0 and 1'''
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
        return _luminance(self)


def _luminance(mycolour):
    '''Determine relative luminance of colours'''

    '''Determine relative luminance of colours.
    Uses the formula:  sqrt( .299 R^2 + .587 G^2 + .114 B^2 )'''

    if type(mycolour) is colour:
        mycolour2 = mycolour
    else:
        try:
            mycolour2 = colour(mycolour)
        except:
            raise TypeError("Must supply a colourettu.colour")

    (r1, g1, b1) = mycolour2.normalized_rgb()

    return sqrt(0.299*pow(r1, 2) + 0.587*pow(g1, 2) + 0.114*pow(b1, 2))
