dict_of_words = ["aaa", "a", "is", "name"]

def min_space(string):
  if string in dict_of_words:
    return 1
  elif len(string) == 1:
    return float('inf')
  else:
    min_space_counter = float('inf')
    for i in xrange(1, len(string)):
      attempt = min_space(string[:i]) + min_space(string[i:])
      if min_space_counter > attempt:
        min_space_counter = attempt
    return min_space_counter
