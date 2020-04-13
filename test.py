import verbs
import unittest


class DefaultVerbsFunctionsTestCase(unittest.TestCase):
    def setUp(self):
        self.verbs = verbs

    def test_correct_all(self):
        self.assertEqual(self.verbs.correct_all(0, 0), (0, 3))

    def test_correct_one(self):
        self.assertEqual(self.verbs.correct_one(0, 0), (2, 1))

    def test_correct_two(self):
        self.assertEqual(self.verbs.correct_two(0, 0), (1, 2))

    def test_wrong_all(self):
        self.assertEqual(self.verbs.wrong_all(0, 0), (3, 0))

    def test_counter_good(self):
        self.assertEqual(self.verbs.counter('5'), 5)

    def test_counter_bad(self):
        self.assertEqual(self.verbs.counter('11'), -1)

    def test_check_sum_good(self):
        self.assertEqual(self.verbs.check_sum(12, 18, 10), 0)

    def test_check_sum_bad(self):
        self.assertEqual(self.verbs.check_sum(13, 17, 10), -1)


if __name__ == '__main__':
    unittest.main()
