def lets_to_sym(string):
  encoded_message = ''
  strindex = 0
  while (strindex <= len(string)-1):
    count = 1
    ch = string[strindex]
    j = strindex
    while (j < len(string)-1):
      if (string[j]==string[j+1]):
        count = count+1
        j = j+1
      else:
        break
    encoded_message = encoded_message+str(count)+ch
    strindex = j+1
  return encoded_message
letters = 'AAAABBBCCDAAA'
print(lets_to_sym(letters))
