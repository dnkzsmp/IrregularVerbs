import unittest
from process.graphic import check_word
from process.graphic import check_lists
from start.start import open_file


class TestUnits(unittest.TestCase):
    def test_good_name_file(self):
        check = open_file('verbs.txt')
        self.assertEqual(True, check)

    def test_bad_name_file1(self):
        check1 = open_file('verbs.csv')
        self.assertEqual(False, check1)

    def test_bad_name_file2(self):
        check2 = open_file('verbs.dat')
        self.assertEqual(False, check2)

    def test_bad_name_file3(self):
        check3 = open_file('123.txt')
        self.assertEqual(False, check3)

    def test_bad_name_file4(self):
        check4 = open_file('')
        self.assertEqual(False, check4)

    def test_bad_name_file5(self):
        check5 = open_file(' ')
        self.assertEqual(False, check5)

    def test_good_stroke(self):
        word1 = check_word('hello')
        self.assertEqual('hello', word1)

    def test_bad_stroke1(self):
        word1 = check_word(' hello')
        self.assertEqual('-1', word1)

    def test_bad_stroke2(self):
        word2 = check_word('hello ')
        self.assertEqual('-1', word2)

    def test_bad_stroke3(self):
        word3 = check_word('')
        self.assertEqual('-1', word3)

    def test_bad_stroke4(self):
        word4 = check_word(' ')
        self.assertEqual('-1', word4)

    def test_good_stroke5(self):
        word5 = check_word('12345')
        self.assertEqual('-1', word5)

    def test_good_lists(self):
        bool1 = check_lists(['be', 'was', 'been'], ['быть', 'be', 'was', 'been'])
        self.assertEqual(True, bool1)

    def test_bad_lists1(self):
        bool1 = check_lists(['a', 'was', 'been'], ['быть', 'be', 'was', 'been'])
        self.assertEqual(False, bool1)

    def test_bad_lists2(self):
        bool2 = check_lists(['be', 'a', 'been'], ['быть', 'be', 'was', 'been'])
        self.assertEqual(False, bool2)

    def test_bad_lists3(self):
        bool3 = check_lists(['be', 'was', 'a'], ['быть', 'be', 'was', 'been'])
        self.assertEqual(False, bool3)

    def test_bad_lists4(self):
        bool4 = check_lists(['a', 'a', 'a'], ['быть', 'be', 'was', 'been'])
        self.assertEqual(False, bool4)

    def test_bad_lists5(self):
        bool5 = check_lists(['a', 'a', 'been'], ['быть', 'be', 'was', 'been'])
        self.assertEqual(False, bool5)

    def test_bad_lists6(self):
        bool6 = check_lists(['be', 'a', 'a'], ['быть', 'be', 'was', 'been'])
        self.assertEqual(False, bool6)

    def test_bad_lists7(self):
        bool7 = check_lists(['a', 'was', 'a'], ['быть', 'be', 'was', 'been'])
        self.assertEqual(False, bool7)


if __name__ == '__main__':
    unittest.main()
