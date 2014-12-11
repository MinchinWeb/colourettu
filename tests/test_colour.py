import unittest
import colourettu


class Test_Colour(unittest.TestCase):

    def test_default_colour(self):
        '''Defaulf colour is white'''
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
