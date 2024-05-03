def fromD():
  try:
    inp = int(input("Enter the Decimal : "))
  except:
    return "Enter Decimal! Program Out!"
  result = (f"To Binary : {toBin(inp)}\nTo Octadecimal : {toOct()}\nTo Hexadecimal : {toHex()}")
  return result

def toBin(inp):
  pre = []
  while inp >= 1:
    c = inp % 2
    c = str(c)
    pre.insert(0, c)
    value = int(inp / 2)
  final = "".join(pre)
  print(pre)
  return pre
