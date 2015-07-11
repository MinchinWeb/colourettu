import unittest
import colourettu
from unittest import skip


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

def main():
    unittest.main()

if __name__ == '__main__':
    main()
