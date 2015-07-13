import unittest
from unittest import expectedFailure, skip
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

    def test_red(self):
        '''Get red of colour'''
        colour1 = colourettu.colour('#D00')
        self.assertEqual(colour1.red(), 221)

    def test_green(self):
        '''Get green of colour'''
        colour1 = colourettu.colour('#0B0')
        self.assertEqual(colour1.green(), 187)

    def test_blue(self):
        '''Get blue of colour'''
        colour1 = colourettu.colour('#00A')
        self.assertEqual(colour1.blue(), 170)

    def test_rgb(self):
        '''Get rgb tuple of colour'''
        colour1 = colourettu.colour('#345')
        self.assertEqual(colour1.rgb(), (51, 68, 85))

    def test_hex(self):
        '''Get hex value of colour'''
        colour1 = colourettu.colour()
        self.assertEqual(colour1.hex(), "#FFFFFF")

    def test_hex_black(self):
        '''Get hex value of colour with leading zeros'''
        colour1 = colourettu.colour("#0102DD")
        self.assertEqual(colour1.hex(), "#0102DD")

    def test_list(self):
        '''Get value of colour given as a list'''
        colour1 = colourettu.colour([5, 10, 25])
        self.assertEqual(colour1.hex(), "#050A19")

    def test_tuple(self):
        '''Get value of colour given as a tuple'''
        colour1 = colourettu.colour((35, 60, 128))
        self.assertEqual(colour1.hex(), "#233C80")

    def test_list_normalized_rgb(self):
        '''Get value of colour given as a list of normalized rgb values'''
        colour1 = colourettu.colour([0.24287275804811442, 0.4339925778684171, 0.16562176715691224], normalized_rgb=True)
        self.assertEqual(colour1.hex(), "#3D6E2A")

    def test_tuple_normalized_rgb(self):
        '''Get value of colour given as a tuple of normalized rgb values'''
        colour1 = colourettu.colour((0.5656023325553875, 0.8070789468680986, 0.8006291331865334), normalized_rgb=True)
        self.assertEqual(colour1.hex(), "#90CDCC")

    def test_tuple_normalized_rgb_value_too_big(self):
        '''Fail on invalid normalized RGB values (too big, tuple)'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour((1.2, 0.4, 0.378), normalized_rgb=True)

    def test_tuple_normalized_rgb_value_too_small(self):
        '''Fail on invalid normalized RGB values (too small, tuple)'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour((0.28, -0.4, 0.378), normalized_rgb=True)

    def test_list_normalized_rgb_value_too_big(self):
        '''Fail on invalid normalized RGB values (too big, list)'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour([0.289, 0.289, 1.33], normalized_rgb=True)

    def test_list_normalized_rgb_value_too_small(self):
        '''Fail on invalid normalized RGB values (too small, list)'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour([-0.289, 0.289, 0.33], normalized_rgb=True)

    def test_tuple_not_normalized(self):
        '''Fail if something other than `True` or `False` is passed for `normalized_rgb`'''
        with self.assertRaises(TypeError):
            colour1 = colourettu.colour(normalized_rgb='stuff')

    @skip('Not yet defined')
    def test_list_not_normalized(self):
        pass

    @skip('Not yet defined')
    def test_tuple_for_normalized_rgb_too_long(self):
        pass

    @skip('Not yet defined')
    def test_tuple_for_normalized_rgb_too_short(self):
        pass

    def test_normalized_value_zero_float(self):
        '''Pass a value of 0 for a normalized RGB value'''
        colour1 = colourettu.colour([0.0, 0.0, 0.0], normalized_rgb=True)
        colour2 = colourettu.colour('#000')
        self.assertEqual(colour1, colour2)

    def test_normalized_value_one_float(self):
        '''Pass a value of 1 for a normalized RGB value'''
        colour1 = colourettu.colour([1.0, 1.0, 1.0], normalized_rgb=True)
        colour2 = colourettu.colour('#FFF')
        self.assertEqual(colour1, colour2)

    def test_normalized_value_zero_int(self):
        '''Pass a value of 0 for a normalized RGB value'''
        colour1 = colourettu.colour([0, 0, 0], normalized_rgb=True)
        colour2 = colourettu.colour('#000')
        self.assertEqual(colour1, colour2)

    def test_normalized_value_one_int(self):
        '''Pass a value of 1 for a normalized RGB value'''
        colour1 = colourettu.colour([1, 1, 1], normalized_rgb=True)
        colour2 = colourettu.colour('#FFF')
        self.assertEqual(colour1, colour2)

    @expectedFailure
    def test_colour_vs_color(self):
        '''test alternate spelling
        Removed in v1.0.0'''
        self.assertEqual(colourettu.color, colourettu.colour)

    def test_bad_hex_string_length(self):
        '''Invalid hex string should raise error'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour("#dddd")

    def test_not_hex_string(self):
        '''Stings must start with '#', otherwiser raise Error'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour("dddd")

    def test_bad_hex_chars(self):
        '''Hex strings that don't contain only hex characters [0-9a-f] should raise error'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour('#asdfgh')

    def test_bad_list_legnth(self):
        '''Lists must be 3 long, otherwise raise error'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour([1,1,1,1])

    def test_bad_tuple_legnth(self):
        '''Tuples must be 3 long, otherwise raise error'''
        with self.assertRaises(ValueError):
            colour1 = colourettu.colour((1,1,1,1))

    def test_bad_list_value(self):
        '''Lists my contain integer, otherwise raise error'''
        with self.assertRaises(TypeError):
            colour1 = colourettu.colour([1,2,"stuff"])

    def test_bad_Tuple_value(self):
        '''Tuples my contain integer, otherwise raise error'''
        with self.assertRaises(TypeError):
            colour1 = colourettu.colour((1,2,"stuff"))

    def test_rgb_normalized_white(self):
        '''Get normalized rgb tuple of white'''
        colour1 = colourettu.colour('#FFF')
        self.assertEqual(colour1.normalized_rgb(), (1, 1, 1))

    def test_rgb_nomralized_black(self):
        '''Get normalize rgb tuple of black'''
        colour1 = colourettu.colour('#000')
        self.assertEqual(colour1.normalized_rgb(), (0, 0, 0))

    def test_repr(self):
        '''Representation of `colour` class'''
        colour1 = colourettu.colour()
        self.assertEqual(colour1.__repr__(), "<colourettu.colour #FFFFFF>")

    def test_str(self):
        '''String representation of `colour` class'''
        colour1 = colourettu.colour()
        self.assertEqual(colour1.__str__(), "#FFFFFF")

    def test_eq(self):
        '''Equality operator'''
        c1 = colourettu.colour()
        c2 = colourettu.colour()
        c3 = colourettu.colour('#abc')
        c4 = colourettu.colour('#abc')
        c5 = colourettu.colour('#123456')
        c6 = c5
        c7 = colourettu.colour('#000000')
        c8 = colourettu.colour([0,0,0])
        
        self.assertEqual(c1, c2)
        self.assertEqual(c3, c4)
        self.assertEqual(c5, c6)
        self.assertEqual(c7, c8)



class Test_Contrast(unittest.TestCase):

    def test_white_white(self):
        '''The Contrast of White and White should be 1'''
        self.assertAlmostEqual(colourettu.contrast('#FFF', '#FFF'), 1)

    def test_black_black(self):
        '''The Contrast of Black and Black should be 1'''
        self.assertAlmostEqual(colourettu.contrast('#000', '#000'), 1)

    def test_white_black(self):
        '''The Contrast of White and Black should be 21'''
        self.assertAlmostEqual(colourettu.contrast('#FFF', '#000'), 21)

    def test_from_colour(self):
        '''The Contrast of a provided colour against White'''
        colour1 = colourettu.colour("#cde")
        self.assertTrue(colour1.contrast("#FFF"))


class Test_Luminance(unittest.TestCase):

    def test_white_hex(self):
        '''The Luminance of White (as hex) should be 1'''
        self.assertAlmostEqual(colourettu.luminance('#FFFFFF'), 1)

    def test_white_tuple(self):
        '''The Luminance of White (as a tuple) should be 1'''
        self.assertAlmostEqual(colourettu.luminance((255, 255, 255)), 1)

    def test_black(self):
        '''The Luminance of Black should be 0'''
        self.assertAlmostEqual(colourettu.luminance('#000'), 0)

    def test_colour_provided(self):
        '''The Luminance of a provided colour'''
        colour1 = colourettu.colour()
        self.assertAlmostEqual(colourettu.luminance(colour1), 1)

    def test_as_colour_property(self):
        '''The Luminance of as a property of a colour'''
        colour1 = colourettu.colour()
        self.assertAlmostEqual(colour1.luminance(), 1)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
