import unittest
import colourettu


class Test_Setup(unittest.TestCase):

    def test_we_live(self):
        '''Test we should *always* pass'''
        pass

    @unittest.skip("showing class skipping")
    def test_version(self):
        unittest.assertTure(colourettu.__version__)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
