# Khan Academy Interview
# Hello!

str_input = ""


def strtok(input, delimiters):
    """
    >>> strtok("cat,dog,mouse", ",.")
    'cat'
    >>> strtok(None, ",")
    'dog'
    >>> strtok(None, ",")
    'mouse'
    >>> strtok(None, ",")
    ''

    >>> strtok("!!!cat,##dog,,,mouse,***", ",.!")
    'cat'
    >>> strtok(None, "#,")
    'dog'
    >>> strtok(None, ",")
    'mouse'
    >>> strtok(None, "*")
    ''

    """
    global str_input

    if input is not None:
        str_input = input

    str_input = str_input.lstrip(delimiters)
    delims = set(delimiters)

    for char in str_input:
        if char in delims:
            answer, str_input = str_input.split(char, 1)
            return answer

    answer = str_input
    str_input = ''
    return answer


def strcspn(input, delimiters):
    """
    duck-typing: If it looks like a duck, quacks like a duck...
    then treat it like a duck!

    >>> strcspn("monkeys", "rtk")
    3
    >>> strcspn("monkeys", "rtkm")
    0
    >>> strcspn("monkeys", "rt")
    7
    """

    delims = set()   # delims = set(delimiters)
    for char in delimiters:
        delims.add(char)

    counter = 0
    for char in input:   # for char, idx in enumerate(input):
        if char in delims:
            return counter
        counter += 1
    return counter

if __name__ == "__main__":
    import doctest
    doctest.testmod()
