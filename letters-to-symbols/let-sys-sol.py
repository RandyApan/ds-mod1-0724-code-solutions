def lets_to_sym(string):#defines function
  message = ''#initiates string
  strindex = 0#intiates index count
  while (strindex <= len(string)-1):#while loop to iterate through the input
    count = 1#stores count of any letter
    ch = string[strindex]#stores which index position
    j = strindex#index for next while loop
    while (j < len(string)-1):#will iterate over string from j
      if (string[j]==string[j+1]):#compares current index pos with next in line
        count = count+1#updates count
        j = j+1#updates next index
      else:
        break#takes us out of for loop
    message = message+str(count)+ch#appends to message
    strindex = j+1#updates index to start at next letter
  return message
letters = 'AAAABBBCCDAAA'
print(lets_to_sym(letters))
