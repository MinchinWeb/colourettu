import unittest
import colourettu
from unittest import skip
import os


class Test_Palette(unittest.TestCase):

    def test_repr(self):
        '''Representation of `palette` class'''
        p1 = colourettu.palette()
        self.assertEqual(p1.__repr__(), "<colourettu.palette #FFFFFF to #000000, 2 colours>")

    def test_str(self):
        '''String representation of `palette` class'''
        p1 = colourettu.palette()
        self.assertEqual(p1.__str__(), "#FFFFFF, #000000")

    def test_length(self):
        '''length function on a of `palette` class'''
        p1 = colourettu.palette()
        self.assertEqual(len(p1), 2)

    def test_from_list_list(self):
        my_list = [colourettu.colour('#aaa'), colourettu.colour('#123'), colourettu.colour('#345682')]
        p1 = colourettu.palette()
        p1.from_list(my_list)
        self.assertEqual(len(p1), 3)
        self.assertEqual(p1._start, colourettu.colour('#aaaaaa'))
        self.assertEqual(p1._end, colourettu.colour('#345682'))

    def test_from_list_tuple(self):
        my_tuple = (colourettu.colour('#111'), colourettu.colour('#983'), colourettu.colour('#aabcde'))
        p1 = colourettu.palette()
        p1.from_list(my_tuple)
        self.assertEqual(len(p1), 3)
        self.assertEqual(p1._start, colourettu.colour('#111111'))
        self.assertEqual(p1._end, colourettu.colour('#aabcde'))

    def test_convert_start_colour(self):
        p1 = colourettu.palette(start_colour = '#124')
        self.assertEqual(p1._start, colourettu.colour('#112244'))

    def test_convert_end_colour(self):
        p1 = colourettu.palette(end_colour = '#a7f')
        self.assertEqual(p1._end, colourettu.colour('#aa77ff'))

    def test_invalid_start_colour(self):
        with self.assertRaises(ValueError):
            p1 = colourettu.palette(start_colour="more")

    def test_invalid_end_colour(self):
       with self.assertRaises(ValueError):
            p1 = colourettu.palette(end_colour=[1, 2, 3, 4])

    def test_from_list_convert_list_colour(self):
        my_list = [[194, 229, 174],
                   [146, 149, 192]]

        p1 = colourettu.palette()
        p1.from_list(my_list)
        self.assertEqual(len(p1), 2)
        self.assertEqual(p1._start, colourettu.colour('#c2e5ae'))
        self.assertEqual(p1._end, colourettu.colour('#9295c0'))


class Test_Palette_with_Images(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove('palette.png')
        except:
            pass

    def test_to_image(self):
        p1 = colourettu.palette()
        p1.to_image()
        self.assertTrue(os.path.isfile('palette.png'))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
