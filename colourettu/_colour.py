'''Base class for dealing with colours'''


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
