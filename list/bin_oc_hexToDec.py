
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
      calc(inp, 2, "Binary")
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
    if i not in noB:
      calc(inp, 8, "Octal")
      break
    else:
      print("Enter Octal only! Program Out!")
      break
  
def hexToDec():
  try:
    inp = str(input("Enter the Hexadecimal : "))
  except:
    print("Enter Binary only! Program Out!")
  calc(inp, 16, "Hexadecimal")
  
def calc(nums, val, pro):
  pre = []
  counter = 0
  b = nums
  nums = str(nums)
  nums = [*nums]
  nums.reverse()
  for i in nums:
    i = int(i)
    x = i * pow(val, counter)
    counter += 1
    pre.append(x)
  hasil = sum(pre)
  print(f"{pro} \"{b}\" to Decimal is : {hasil}")