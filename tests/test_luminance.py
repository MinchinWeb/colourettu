import unittest


class Test_Luminance(unittest.TestCase):

    @unittest.skip("showing class skipping")
    def test_luminance_white(self):
        '''The Luminance of White should be 1'''
        self.assertTrue(luminance('#FFFFFF'), 1)

    @unittest.skip("showing class skipping")
    def test_luminance_black(self):
        '''The Luminance of Black should be 0'''
        self.assertTrue(luminance('#FFFFFF'), 0)


def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
