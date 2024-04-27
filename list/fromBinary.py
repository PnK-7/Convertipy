def fromB():
  try:
    inp = int(input("Enter the Binary : "))
  except:
    return "Enter Binary only! Program Out!"
  decimals = ['2', '3', '4', '5', '6', '7', '8', '9']
  tmp = str(inp)
  test = [*tmp]
  for i in test:
    if i in decimals:
      print("Enter Binary only! Program Out!")
      break
    else:
      result = (f"To Decimal : {toDec(inp)}\nTo Octadecimal : {toOct()}\nTo Hexadecimal : {toHex()}")
      return result

def toDec(inp):
  counter = 0
  result = []
  inp = str(inp)
  inp = [*inp]
  inp.reverse()
  for i in inp:
    i = int(i)
    x = i * pow(2, counter)
    counter += 1
    result.append(x)
    final = sum(result)
  return final
def toOct():
  return "toOct"
def toHex():
  return "toHex"
