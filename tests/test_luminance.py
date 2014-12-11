import unittest
import colourettu


class Test_Luminance(unittest.TestCase):

    def test_luminance_white_hex(self):
        '''The Luminance of White (as hex) should be 1'''
        self.assertTrue(colourettu.luminance('#FFFFFF'), 1)

    def test_luminance_white_tuple(self):
        '''The Luminance of White (as a tuple) should be 1'''
        self.assertTrue(colourettu.luminance((255, 255, 255)), 1)

    def test_luminance_black(self):
        '''The Luminance of Black should be 0'''
        self.assertTrue(colourettu.luminance('#FFFFFF'), 0)

    def test_luminance_colour_provided(self):
        '''The Luminance of a provided colour'''
        colour1 = colourettu.colour()
        self.assertTrue(colourettu.luminance(colour1), 1)

    def test_luminance_as_colour_property(self):
        '''The Luminance of as a property of a colour'''
        colour1 = colourettu.colour()
        self.assertTrue(colour1.luminance(), 1)


def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
