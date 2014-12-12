import unittest
import colourettu


class Test_Contrast(unittest.TestCase):

    def test_contrast_white_white(self):
        '''The Contrast of White and White should be 1'''
        self.assertAlmostEqual(colourettu.contrast('#FFF', '#FFF'), 1)

    def test_contrast_black_black(self):
        '''The Contrast of Black and Black should be 1'''
        self.assertAlmostEqual(colourettu.contrast('#000', '#000'), 1)

    def test_contrast_white_black(self):
        '''The Contrast of White and Black should be 21'''
        self.assertAlmostEqual(colourettu.contrast('#FFF', '#000'), 21)

    def test_contrast_from_colour(self):
        '''The Contrast of a provided colour against White'''
        colour1 = colourettu.colour("#cde")
        self.assertTrue(colour1.contrast("#FFF"))


def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
