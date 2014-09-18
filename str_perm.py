# Given two strings, determine if they are a permutation of each other.


def perm(string1, string2):
    """Given two strings, determine if they are a permutation of each other.

    Return True if they are permutations of each other, False otherwise.
    This implementation is case and space sensative.

    >>> perm('whatthefudge', 'whatthefudge')
    True

    >>> perm('dog', 'god')
    True

    >>> perm('God', 'dog')
    False

    >>> perm('rubber', 'paper')
    False

    """
    if len(string2) != len(string1):
        return False

    char_set1 = dict()
    char_set2 = dict()

    for char in string1:
        if char in char_set1:
            char_set1[char] += 1
        else:
            char_set1[char] = 1

    for char in string2:
        if char in char_set2:
            char_set2[char] += 1
        else:
            char_set2[char] = 1

    return char_set1 == char_set2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
