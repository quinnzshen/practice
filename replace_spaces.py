SPACE = " "

def replace_spaces(string):
    """Given a string, replace all of the spaces with "%20".

    >>> replace_spaces('The dog jumped over the cat!')
    'The%20dog%20jumped%20over%20the%20cat!'
    """
    new_string = ""
    for char in string:
        if char == SPACE:
            new_string += "%20"
        else:
            new_string += char
    return new_string