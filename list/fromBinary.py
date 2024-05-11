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
      result = (f"To Decimal : {toDec(inp)}\nTo Octadecimal : {toOct(inp)}\nTo Hexadecimal : {toHex(inp)}")
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
  while decimal > 0:
    divide = decimal / 8
    decimal = int(divide)
    reminder = divide - decimal
    reminder = str(int(reminder * 8))
    result.insert(0, reminder)
  result = "".join(result)
  return result
def toHex(inp):
  decimal = toDec(inp)
  result = []
  counter = 0
  while decimal > 0:
    divide = decimal / 16
    decimal = int(divide)
    reminder = divide - decimal
    reminder = str(int(reminder * 16))
    result.insert(0, reminder)
  for i in result:
    if i == '10':
      result[counter] = 'A'
    if i == '11':
      result[counter] = 'B'
    if i == '12':
      result[counter] = 'C'
    if i == "13":
      result[counter] = 'D'
    if i == '14':
      result[counter] = 'E'
    if i == '15':
      result[counter] = 'F'
    counter += 1
  result = "".join(result)
  return result
