def is_anagram(str_1,str_2):
  string1 = sorted(list(str_1))
  string2 = sorted(list(str_2))
  if string1 == string2:
    return True
  else:
    return False
print(is_anagram("cautioned","education"))
print(is_anagram('cat','rat'))
