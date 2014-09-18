# Implement an algorithm to determine if a string has all unique characters.


def unique(string):
    """Return True if string is completely unique. Return False otherwise.

    >>> unique('abc')
    True
    >>> unique('abca')
    False
    """
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True

# What if you can't use additional data structures?

if __name__ == "__main__":
    import doctest
    doctest.testmod()
