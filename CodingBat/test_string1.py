import unittest

import string1_python


class TestString1(unittest.TestCase):
    def test_hello_name(self):
        self.assertEqual(string1_python.hello_name("Bob"), "Hello Bob!")
        self.assertEqual(string1_python.hello_name("Alice"), "Hello Alice!")
        self.assertEqual(string1_python.hello_name("x"), "Hello x!")

    def test_make_abba(self):
        self.assertEqual(string1_python.make_abba("Hi", "Bye"), "HiByeByeHi")
        self.assertEqual(string1_python.make_abba("Yo", "Alice"), "YoAliceAliceYo")
        self.assertEqual(string1_python.make_abba("What", "Up"), "WhatUpUpWhat")

    def test_make_tags(self):
        self.assertEqual(string1_python.make_tags("i", "Yay"), "<i>Yay</i>")
        self.assertEqual(string1_python.make_tags("i", "Hello"), "<i>Hello</i>")
        self.assertEqual(string1_python.make_tags("cite", "word"), "<cite>word</cite>")

    def test_make_out_word(self):
        self.assertEqual(string1_python.make_out_word("<<>>", "Yay"), "<<Yay>>")
        self.assertEqual(string1_python.make_out_word("<<>>", "WooHoo"), "<<WooHoo>>")
        self.assertEqual(string1_python.make_out_word("[[]]", "word"), "[[word]]"),

    def test_extra_end(self):
        self.assertEqual(string1_python.extra_end("Hello"), "lololo")
        self.assertEqual(string1_python.extra_end("ab"), "ababab")
        self.assertEqual(string1_python.extra_end("Hi"), "HiHiHi")

    def test_first_two(self):
        self.assertEqual(string1_python.first_two("Hello"), "He")
        self.assertEqual(string1_python.first_two("abcdefg"), "ab")
        self.assertEqual(string1_python.first_two("ab"), "ab")

    def test_first_half(self):
        self.assertEqual(string1_python.first_half("WooHoo"), "Woo")
        self.assertEqual(string1_python.first_half("HelloThere"), "Hello")
        self.assertEqual(string1_python.first_half("abcdef"), "abc")

    def test_without_end(self):
        self.assertEqual(string1_python.without_end("Hello"), "ell")
        self.assertEqual(string1_python.without_end("java"), "av")
        self.assertEqual(string1_python.without_end("coding"), "odin")

    def test_combo_string(self):
        self.assertEqual(string1_python.combo_string("Hello", "hi"), "hiHellohi")
        self.assertEqual(string1_python.combo_string("hi", "Hello"), "hiHellohi")
        self.assertEqual(string1_python.combo_string("aaa", "b"), "baaab")

    def test_non_start(self):
        self.assertEqual(string1_python.non_start("Hello", "There"), "ellohere")
        self.assertEqual(string1_python.non_start("java", "code"), "avaode")
        self.assertEqual(string1_python.non_start("shotl", "java"), "hotlava")

    def test_left2(self):
        self.assertEqual(string1_python.left2("Hello"), "lloHe")
        self.assertEqual(string1_python.left2("java"), "vaja")
        self.assertEqual(string1_python.left2("Hi"), "Hi")


if __name__ == "__main__":
    unittest.main()
