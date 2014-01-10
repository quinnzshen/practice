# Khan Academy Interview
# Hello!

"""
def strtok(input, delimiters):
  ...
  str_input = str_input.lstrip(delimiters)
  for char, idx in enumerate(str_input):
    if char in delims:
      val = str_input[:idx]
      str_input = str_input[idx + 1]
      return val
  # not quite right -- return input or None

# skip leading
# take until delim <- happen to return (until_delim, rest)
"""

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

    >>> strtok("!!!cat,##dog,,,mouse,***", ",.!")
    'cat'
    >>> strtok(None, "#,")
    'dog'
    >>> strtok(None, ",")
    'mouse'
    >>> strtok(None, "*")

    """
    global str_input

    if input is not None:
        str_input = input

    if str_input == "":
        return None

    delims = set(delimiters)
    begin_index = 0
    flag = False
    answer = ""
    for idx, char in enumerate(str_input):
        if flag is False and char not in delims:
            begin_index = idx
            flag = True
        elif flag is True and char in delims:  # elif flag:
            answer = str_input[begin_index:idx]   # [inclusive:exclusive]
            str_input = str_input[idx + 1:]
            return answer
    if flag is not True:  # if not flag:
        return None
    answer = str_input[begin_index:]
    str_input = ""
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
