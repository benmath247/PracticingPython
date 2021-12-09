import unittest
import warmup2_python


class TestWarmup2(unittest.TestCase):
    def test_string_times(self):
        self.assertEqual(warmup2_python.string_times("Hi", 2), "HiHi")
        self.assertEqual(warmup2_python.string_times("Hi", 3), "HiHiHi")
        self.assertEqual(warmup2_python.string_times("Hi", 1), "Hi")

    def test_front_times(self):
        self.assertEqual(warmup2_python.front_times("Chocolate", 2), "ChoCho")
        self.assertEqual(warmup2_python.front_times("Chocolate", 3), "ChoChoCho")
        self.assertEqual(warmup2_python.front_times("Abc", 3), "AbcAbcAbc")

    def test_string_bits(self):
        self.assertEqual(warmup2_python.string_bits("Hello"), "Hlo")
        self.assertEqual(warmup2_python.string_bits("Hi"), "H")
        self.assertEqual(warmup2_python.string_bits("Heeololeo"), "Hello")

    def test_string_explosion(self):
        self.assertEqual(warmup2_python.string_splosion("Code"), "CCoCodCode")
        self.assertEqual(warmup2_python.string_splosion("abc"), "aababc")
        self.assertEqual(warmup2_python.string_splosion("ab"), "aab")

    def test_last2(self):
        self.assertEqual(warmup2_python.last2("hixxhi"), 1)
        self.assertEqual(warmup2_python.last2("xaxxaxaxx"), 1)
        self.assertEqual(warmup2_python.last2("axxxaaxx"), 2)

    def test_array_count9(self):
        self.assertEqual(warmup2_python.array_count9([1, 2, 9]), 1)
        self.assertEqual(warmup2_python.array_count9([1, 9, 9]), 2)
        self.assertEqual(warmup2_python.array_count9([1, 9, 9, 3, 9]), 3)

    def test_array_front9(self):
        self.assertEqual(warmup2_python.array_front9([1, 2, 9, 3, 4]), True)
        self.assertEqual(warmup2_python.array_front9([1, 2, 3, 4, 9]), False)
        self.assertEqual(warmup2_python.array_front9([1, 2, 3, 4, 5]), False)

    def test_array123(self):
        self.assertEqual(warmup2_python.array123([1, 1, 2, 3, 1]), True)
        self.assertEqual(warmup2_python.array123([1, 1, 2, 4, 1]), False)
        self.assertEqual(warmup2_python.array123([1, 1, 2, 1, 2, 3]), True)

    def test_string_match(self):
        self.assertEqual(warmup2_python.string_match("xxcaazz", "xxbaaz"), 3)
        self.assertEqual(warmup2_python.string_match("abc", "abc"), 2)
        self.assertEqual(warmup2_python.string_match("abc", "axc"), 0)


if __name__ == "__main__":
    unittest.main()
