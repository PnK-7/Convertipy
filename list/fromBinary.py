def fromB():
  try:
    inp = int(input("Enter the Binary : "))
  except:
    return "Enter Binary only! Program Out!"
  decimals = ['2', '3', '4', '5', '6', '7', '8', '9']
  tmp = str(inp)
  counter = 0
  test = [*tmp]
  for i in test:
    if i in decimals:
      print("Enter Binary only! Program Out!")
      break
    else:
      counter += 1
    if counter == len(test):
      result = (f"To Decimal : {toDec(inp)}\nTo Octadecimal : {toOct(inp)}\nTo Hexadecimal : {toHex()}")
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
def toOct(inp):
  decimal = toDec(inp)
  result = []
  counter = 0
  test = str(inp)
  test = [*test]
  while decimal > 0:
    divide = decimal / 8
    decimal = int(divide)
    reminder = divide - decimal
    reminder = str(int(reminder * 8))
    result.insert(0, reminder)
  result = "".join(result)
  return result
def toHex():
  return "toHex"
