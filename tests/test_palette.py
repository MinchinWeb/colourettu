import unittest
import colourettu


class Test_Palette(unittest.TestCase):

    def test_palette_repr(self):
        '''Representation of `palette` class'''
        palette1 = colourettu.palette()
        self.assertEqual(palette1.__repr__(), "<colourettu.palette #FFFFFF to #000000, 2 colours>")

    def test_palette_str(self):
        '''String representation of `palette` class'''
        palette1 = colourettu.palette()
        self.assertEqual(palette1.__str__(), "#FFFFFF, #000000")

    def test_palette_length(self):
        '''length function on a of `palette` class'''
        palette1 = colourettu.palette()
        self.assertEqual(len(palette1), 2)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
