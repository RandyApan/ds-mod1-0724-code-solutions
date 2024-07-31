def binary_dict(number):
  d = {}
  _ = 0
  while _ <= number:
    d[_] = bin(number)
    _ = _ + 1
  print(d)
binary_dict(15)
