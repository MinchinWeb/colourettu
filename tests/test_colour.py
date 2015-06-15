import unittest
from unittest import expectedFailure
import colourettu


class Test_Colour(unittest.TestCase):

    def test_default_colour(self):
        '''Default colour is white'''
        colour1 = colourettu.colour()
        self.assertEqual(colour1._r, 255)
        self.assertEqual(colour1._g, 255)
        self.assertEqual(colour1._b, 255)

    def test_3hex_colour(self):
        '''Set the colour as like #dc8'''
        colour1 = colourettu.colour('#dc8')
        self.assertEqual(colour1._r, 221)
        self.assertEqual(colour1._g, 204)
        self.assertEqual(colour1._b, 136)

    def test_6hex_colour(self):
        '''Set the colour as like #123456'''
        colour1 = colourettu.colour('#123456')
        self.assertEqual(colour1._r, 18)
        self.assertEqual(colour1._g, 52)
        self.assertEqual(colour1._b, 86)

    def test_colour_red(self):
        '''Get red of colour'''
        colour1 = colourettu.colour('#D00')
        self.assertEqual(colour1.red(), 221)

    def test_colour_green(self):
        '''Get green of colour'''
        colour1 = colourettu.colour('#0B0')
        self.assertEqual(colour1.green(), 187)

    def test_colour_blue(self):
        '''Get blue of colour'''
        colour1 = colourettu.colour('#00A')
        self.assertEqual(colour1.blue(), 170)

    def test_colour_rgb(self):
        '''Get rgb tuple of colour'''
        colour1 = colourettu.colour('#345')
        self.assertEqual(colour1.rgb(), (51, 68, 85))

    def test_colour_hex(self):
        '''Get hex value of colour'''
        colour1 = colourettu.colour()
        self.assertEqual(colour1.hex(), "#FFFFFF")

    def test_colour_hex_black(self):
        '''Get hex value of colour with leading zeros'''
        colour1 = colourettu.colour("#0102DD")
        self.assertEqual(colour1.hex(), "#0102DD")

    def test_colour_list(self):
        '''Get value of colour given as a list'''
        colour1 = colourettu.colour([5, 10, 25])
        self.assertEqual(colour1.hex(), "#050A19")

    def test_colour_tuple(self):
        '''Get value of colour given as a tuple'''
        colour1 = colourettu.colour((35, 60, 128))
        self.assertEqual(colour1.hex(), "#233C80")

    @expectedFailure
    def test_colour_vs_color(self):
        '''test alternate spelling
        Removed in v1.0.0'''
        self.assertEqual(colourettu.color, colourettu.colour)

    def test_bad_colour(self):
        '''Invalid colour should raise error'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour("#dddd")

    def test_colour_rgb_normalized_white(self):
        '''Get normalized rgb tuple of white'''
        colour1 = colourettu.colour('#FFF')
        self.assertEqual(colour1.normalized_rgb(), (1, 1, 1))

    def test_colour_rgb_nomralized_black(self):
        '''Get normalize rgb tuple of black'''
        colour1 = colourettu.colour('#000')
        self.assertEqual(colour1.normalized_rgb(), (0, 0, 0))

    def test_colour_repr(self):
        '''Representation of `colour` class'''
        colour1 = colourettu.colour()
        self.assertEqual(colour1.__repr__(), "<colourettu.colour #FFFFFF>")

    def test_colour_str(self):
        '''String representation of `colour` class'''
        colour1 = colourettu.colour()
        self.assertEqual(colour1.__str__(), "#FFFFFF")
