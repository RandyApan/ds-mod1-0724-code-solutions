def decimal_to_bin(dec):
  binary = ''
  while dec > 0:
    binary = str(dec % 2)+ binary
    dec = dec // 2
  return binary

print(decimal_to_bin(15))

def binary_dict(input):
  binaryD = {}
  _ = 0
  if  _ == 0:
    binaryD[_] = '0'
    _ += 1
  while _ <= input:
    binaryD[_] = decimal_to_bin(_)
    _ += 1
  return binaryD

print(binary_dict(25))
