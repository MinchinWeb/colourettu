import os
import unittest
from unittest import skip

import colourettu


class Test_Palette(unittest.TestCase):

    def test_repr(self):
        '''Representation of `palette` class'''
        p1 = colourettu.Palette()
        self.assertEqual(p1.__repr__(), "<colourettu.Palette #FFFFFF to #000000, 2 colours>")

    def test_str(self):
        '''String representation of `palette` class'''
        p1 = colourettu.Palette()
        self.assertEqual(p1.__str__(), "#FFFFFF, #000000")

    def test_length(self):
        '''length function on a of `palette` class'''
        p1 = colourettu.Palette()
        self.assertEqual(len(p1), 2)

    def test_from_list_list(self):
        my_list = [colourettu.Colour('#aaa'), colourettu.Colour('#123'), colourettu.Colour('#345682')]
        p1 = colourettu.Palette()
        p1.from_list(my_list)
        self.assertEqual(len(p1), 3)
        self.assertEqual(p1._start, colourettu.Colour('#aaaaaa'))
        self.assertEqual(p1._end, colourettu.Colour('#345682'))

    def test_from_list_tuple(self):
        my_tuple = (colourettu.Colour('#111'), colourettu.Colour('#983'), colourettu.Colour('#aabcde'))
        p1 = colourettu.Palette()
        p1.from_list(my_tuple)
        self.assertEqual(len(p1), 3)
        self.assertEqual(p1._start, colourettu.Colour('#111111'))
        self.assertEqual(p1._end, colourettu.Colour('#aabcde'))

    def test_convert_start_colour(self):
        p1 = colourettu.Palette(start_colour='#124')
        self.assertEqual(p1._start, colourettu.Colour('#112244'))

    def test_convert_end_colour(self):
        p1 = colourettu.Palette(end_colour='#a7f')
        self.assertEqual(p1._end, colourettu.Colour('#aa77ff'))

    def test_invalid_start_colour(self):
        with self.assertRaises(ValueError):
            p1 = colourettu.Palette(start_colour="more")

    def test_invalid_end_colour(self):
        with self.assertRaises(ValueError):
            p1 = colourettu.Palette(end_colour=[1, 2, 3, 4])

    def test_from_list_convert_list_colour(self):
        my_list = [[194, 229, 174],
                   [146, 149, 192]]

        p1 = colourettu.Palette()
        p1.from_list(my_list)
        self.assertEqual(len(p1), 2)
        self.assertEqual(p1._start, colourettu.Colour('#c2e5ae'))
        self.assertEqual(p1._end, colourettu.Colour('#9295c0'))

    def test_palette_plus_colour(self):
        p1 = colourettu.Palette()
        c2 = colourettu.Colour('#123')
        p2 = p1 + c2
        self.assertEqual(len(p2), 3)
        self.assertEqual(p2._start, colourettu.Colour('#fff'))
        self.assertEqual(p2._end, colourettu.Colour('#112233'))

    def test_colour_plus_palette(self):
        p1 = colourettu.Palette()
        c2 = colourettu.Colour('#abc')
        p2 = c2 + p1
        self.assertEqual(len(p2), 3)
        self.assertEqual(p2._start, colourettu.Colour('#aabbcc'))
        self.assertEqual(p2._end, colourettu.Colour('#000'))

    def test_palette_plus_palette(self):
        p1 = colourettu.Palette()
        p2 = colourettu.Palette('#abc', '#345')
        p3 = p1 + p2
        self.assertEqual(len(p3), 4)
        self.assertEqual(p3._start, colourettu.Colour('#fff'))
        self.assertEqual(p3._end, colourettu.Colour('#345'))

    def test_palette_plus_palette_overlapping_colour(self):
        p1 = colourettu.Palette('#123', '#456')
        p2 = colourettu.Palette('#456', '#789')
        p3 = p1 + p2
        self.assertEqual(len(p3), 3)
        self.assertEqual(p3._start, colourettu.Colour('#123'))
        self.assertEqual(p3._end, colourettu.Colour('#789'))
        self.assertEqual(p3._colours[1], colourettu.Colour('#456'))


class Test_Palette_with_Images(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove('palette.png')
        except:
            pass

    def test_to_image(self):
        p1 = colourettu.Palette()
        p1.to_image()
        self.assertTrue(os.path.isfile('palette.png'))

    @skip('not yet defined')
    def test_to_image_alpha_channel(self):
        pass

    @skip('not yet defined')
    def test_to_image_band_width(self):
        pass

    @skip('not yet defined')
    def test_to_image_max_width(self):
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()
