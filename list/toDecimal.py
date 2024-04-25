
def binToDec():
  try:
    inp = int(input("Enter the Binary : "))
  except:
    print("Enter Binary only! Program Out!")
  noB = ['2', '3', '4', '5', '6', '7', '8', '9']
  tmp = str(inp)
  test = [*tmp]
  for i in test:
    if i not in noB:
      return calc(inp, 2, "Binary", 0)
      break
    else:
      print("Enter Binary only! Program Out!")
      break

def ocToDec():
  try:
    inp = int(input("Enter the Octal : "))
  except:
    print("Enter Octal only! Program Out!")
  noB = ['8', '9']
  tmp = str(inp)
  test = [*tmp]
  for i in test:
    if i in noB:
      return "Enter Octal only! Program Out!"
  return calc(inp, 8, "Octal", 0)

def hexToDec():
  try:
    inp = str(input("Enter the Hexadecimal : "))
  except:
    print("Enter Hexadecimal only! Program Out!")
  noB = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  tmp = inp.upper()
  test = [*tmp]
  for i in test:
    if i in noB:
      print("Enter Hexadecimal only! Program Out!")
      break
    else:
      return calc(tmp, 16, "Hexadecimal", 1)
      break
  
def calc(nums, val, pro, det):
  hexa = ['A', 'B', 'C', 'D', 'E', 'F']
  dec = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  pre = []
  counter = 0
  b = nums
  nums = str(nums)
  nums = [*nums]
  nums.reverse()
  if det == 0:
    for i in nums:
      i = int(i)
      x = i * pow(val, counter)
      counter += 1
      pre.append(x)
  elif det == 1:
    for i in nums:
      y = 0
      if i not in hexa:
        try:
          i = int(i)
        except:
          print("SPECIAL CHAR!!!")
        y += i
      elif i in hexa:
        if i == 'A':
          y += 11
        if i == "B":
          y += 12
        if i == "C":
          y += 13
        if i == "D":
          y += 14
        if i == "E":
          y += 15
        if i == "F":
          y += 16
      x = y * pow(val, counter)
      counter += 1
      pre.append(x)
  hasil = sum(pre)
  haha = (f"{pro} \"{b}\" to Decimal is : {hasil}")
  return haha

