"""
string -> f -> largest palindrome within that string

f("abbacheese") -> "abba"
f("adbacheese") -> "ese"
f("abcdefghijk") -> "a" OR "b" OR "c" OR ... OR "k"
f("a") -> "a"
f("aabb") -> "aa" OR "bb"
"""

def f(str):
    answer = "" #Longest palindrome found
    size = 0
    for str in find_substrings(str):
        if is_palindrome(str) and len(str) > size:
            answer = str
            size = len(str)
    return answer

def is_palindrome(str):
    return str == str[::-1]

def find_substrings(str):
    answer = set()
    for i in xrange(len(str)+1):
        for j in xrange(i, len(str)+1):
            answer.add(str[i:j])
    return answer