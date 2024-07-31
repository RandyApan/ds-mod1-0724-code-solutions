L = 'abcdefghijklmnopqrstuvwxyz'
def lpass(alphabet):
  new_list = [ ]
  b_list = list(range(1,len(alphabet)+1))
  for i in alphabet:
    new_list = new_list + [(b_list[alphabet.index(i)],i)]
  print(new_list)
  return(new_list)
lpass(L)
