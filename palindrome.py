import string

def palindrome(str, counter):
  """ 
  Returns the amount of characters needed in the 
  beginning of a string to make it a palindrome.
  """
  if str == str[::-1]:
    return counter
  elif counter > len(str)/2:
    return float('inf')
  else:
    min_chars = float('inf')
    for char in string.ascii_lowercase:
      attempt = palindrome(char + str, counter + 1)
      if min_chars > attempt:
        min_chars = attempt
    return min_chars