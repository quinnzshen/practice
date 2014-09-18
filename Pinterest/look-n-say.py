def look_n_say(string):
  "Given a string '122232233' give back '1132132223'"
  answer = ""
  if string:
    current_char = string[0]
    counter = 1

    for next_char in string[1:]:
      if next_char == current_char:
        counter += 1
      else:
        answer += str(counter) + current_char
        current_char = next_char
        counter = 1
    answer += str(counter) + current_char
  return answer