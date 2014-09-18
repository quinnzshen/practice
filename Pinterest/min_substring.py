def min_substring(string, required_chars):
  """
  >>> string = "abeecbxagc"
  >>> required_chars = set(['a', 'b', 'c'])
  >>> min_substring (string, required_chars)
  >>> 4 # len('cbxa')
  """
  answer = float('inf')
  char_location = dict()
  for x in xrange(len(string)):
    char = string[x]
    if char in required_chars:
        char_location[char] = x
        if len(required_chars) == len(char_location):
          new_size = max(char_location.values()) - min(char_location.values()) + 1
          if new_size < answer:
            answer = new_size
  return answer
