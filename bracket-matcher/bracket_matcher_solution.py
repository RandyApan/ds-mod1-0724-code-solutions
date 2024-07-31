s = "(a((kl(mns)t)uvwz)"
def bracket_matcher(strang):
  count_1 = 0
  count_2 = 0
  for i in strang:
    if i == "(":
      count_1 = count_1 + 1
    elif i == ")":
      count_2 = count_2 +1
  if count_1 == count_2:
    print(True)
    return(True)
  else:
    print(False)
    return(False)
bracket_matcher(s)
