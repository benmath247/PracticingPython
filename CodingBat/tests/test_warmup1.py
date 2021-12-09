import unittest

import warmup1_python


class TestWarmup1(unittest.TestCase):
    def test_sleep_in(self):
        self.assertEqual(warmup1_python.sleep_in(False, False), True)
        self.assertEqual(warmup1_python.sleep_in(True, False), False)
        self.assertEqual(warmup1_python.sleep_in(False, True), True)

    def test_monkey_trouble(self):
        self.assertEqual(warmup1_python.monkey_trouble(True, True), True)
        self.assertEqual(warmup1_python.monkey_trouble(False, False), True)
        self.assertEqual(warmup1_python.monkey_trouble(True, False), False)

    def test_sum_double(self):
        self.assertEqual(warmup1_python.sum_double(1, 2), 3)
        self.assertEqual(warmup1_python.sum_double(3, 2), 5)
        self.assertEqual(warmup1_python.sum_double(2, 2), 8)

    def test_diff21(self):
        self.assertEqual(warmup1_python.diff21(19), 2)
        self.assertEqual(warmup1_python.diff21(10), 11)
        self.assertEqual(warmup1_python.diff21(21), 0)

    def test_parrot_trouble(self):
        self.assertEqual(warmup1_python.parrot_trouble(True, 6), True)
        self.assertEqual(warmup1_python.parrot_trouble(True, 7), False)
        self.assertEqual(warmup1_python.parrot_trouble(False, 6), False)

    def test_makes10(self):
        self.assertEqual(warmup1_python.makes10(9, 10), True)
        self.assertEqual(warmup1_python.makes10(9, 9), False)
        self.assertEqual(warmup1_python.makes10(1, 9), True)

    def test_near_hundred(self):
        self.assertEqual(warmup1_python.near_hundred(93), True)
        self.assertEqual(warmup1_python.near_hundred(90), True)
        self.assertEqual(warmup1_python.near_hundred(89), False)

    def test_pos_neg(self):
        self.assertEqual(warmup1_python.pos_neg(1, -1, False), True)
        self.assertEqual(warmup1_python.pos_neg(-1, 1, False), True)
        self.assertEqual(warmup1_python.pos_neg(-4, -5, True), True)

    def test_not_string(self):
        self.assertEqual(warmup1_python.not_string("candy"), "not candy")
        self.assertEqual(warmup1_python.not_string("x"), "not x")
        self.assertEqual(warmup1_python.not_string("not bad"), "not bad")

    def test_missing_char(self):
        self.assertEqual(warmup1_python.missing_char("kitten", 1), "ktten")
        self.assertEqual(warmup1_python.missing_char("kitten", 0), "itten")
        self.assertEqual(warmup1_python.missing_char("kitten", 4), "kittn")

    def test_front_back(self):
        self.assertEqual(warmup1_python.front_back("code"), "eodc")
        self.assertEqual(warmup1_python.front_back("a"), "a")
        self.assertEqual(warmup1_python.front_back("ab"), "ba")

    def test_front3(self):
        self.assertEqual(warmup1_python.front3("Java"), "JavJavJav")
        self.assertEqual(warmup1_python.front3("Chocolate"), "ChoChoCho")
        self.assertEqual(warmup1_python.front3("abc"), "abcabcabc")


if __name__ == "__main__":
    unittest.main()
