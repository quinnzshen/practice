def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> ordered_digits(121)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    if x < 10:
        return True
    else:
        last_digit, remaining_digits = x % 10, x // 10
        return (last_digit >= (remaining_digits % 10)) and ordered_digits(remaining_digits)

if __name__ == '__main__':
    import doctest
    doctest.testmod()