"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.


string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""

def string_times(str, n):
    return str * n

"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
 or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""

def front_times(str, n):
    return str[0:3] * n
  

"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
        result += str[i]
    return result

"""
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
def string_splosion(str):
    result = ""
    for i in range(len(str)+1):
        result += str[0:i]
    return result


"""
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""
def last2(str):
    if len(str) < 2:
        return 0
  
    end = str[len(str)-2:len(str)]
    result = 0
  
    for i in range(len(str)-2):
        if str[i:i+2] == end:
            result += 1
  
    return result

"""
Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""

def array_count9(nums):
    result = 0
    for i in nums:
        if i == 9:
            result += 1
    return result


"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
def array_front9(nums):
    if len(nums) <= 4:
        num = len(nums)
    else:
        num = 4
  
    for i in range(num):
        if nums[i] == 9:
            return True
    return False

