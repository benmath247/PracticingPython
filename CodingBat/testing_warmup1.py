import unittest

import warmup1_python

def test_sleep_in():
    assert warmup1_python.sleep_in(False, False) == True
    assert warmup1_python.sleep_in(True, False) == False
    assert warmup1_python.sleep_in(False, True) == True

def test_monkey_trouble():
    assert warmup1_python.monkey_trouble(True, True) == True
    assert warmup1_python.monkey_trouble(False, False) == True
    assert warmup1_python.monkey_trouble(True, False) == False

def test_sum_double():
    assert warmup1_python.sum_double(1, 2) == 3
    assert warmup1_python.sum_double(3, 2) == 5
    assert warmup1_python.sum_double(2, 2) == 8

def test_diff21():
    assert warmup1_python.diff21(19) == 2
    assert warmup1_python.diff21(10) == 11
    assert warmup1_python.diff21(21) == 0

def test_parrot_trouble():
    assert warmup1_python.parrot_trouble(True, 6) == True
    assert warmup1_python.parrot_trouble(True, 7) == False
    assert warmup1_python.parrot_trouble(False, 6) == False

def test_makes10():
    assert warmup1_python.makes10(9, 10) == True
    assert warmup1_python.makes10(9, 9) == False
    assert warmup1_python.makes10(1, 9) == True   

def test_near_hundred():
    assert warmup1_python.near_hundred(93) == True
    assert warmup1_python.near_hundred(90) == True
    assert warmup1_python.near_hundred(89) == False

def test_pos_neg():
    assert warmup1_python.pos_neg(1, -1, False) == True
    assert warmup1_python.pos_neg(-1, 1, False) == True
    assert warmup1_python.pos_neg(-4, -5, True) == True

def test_not_string():
    assert warmup1_python.not_string('candy') == 'not candy'
    assert warmup1_python.not_string('x') == 'not x'
    assert warmup1_python.not_string('not bad') == 'not bad'

def test_missing_char():
    assert warmup1_python.missing_char('kitten', 1) == 'ktten'
    assert warmup1_python.missing_char('kitten', 0) == 'itten'
    assert warmup1_python.missing_char('kitten', 4) == 'kittn'

def test_front_back():
    assert warmup1_python.front_back('code') == 'eodc'
    assert warmup1_python.front_back('a') == 'a'
    assert warmup1_python.front_back('ab') == 'ba'

def test_front3():
    assert warmup1_python.front3('Java') == 'JavJavJav'
    assert warmup1_python.front3('Chocolate') == 'ChoChoCho'
    assert warmup1_python.front3('abc') == 'abcabcabc'

if __name__ == "__main__":
    test_sleep_in()
    test_monkey_trouble()
    test_sum_double()
    test_diff21()
    test_parrot_trouble()
    test_makes10()
    test_near_hundred()
    test_pos_neg()
    test_not_string()
    test_missing_char()
    test_front_back()
    test_front3()
    print("everything passed")

