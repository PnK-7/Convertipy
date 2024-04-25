
def decToBin():
  try:
    inp = int(input("Enter the Decimal : "))
    return cal(inp, "Decimal", inp)
  except:
    print("Enter decimal only! Program Out!")

def ocToBin():
  try:
    inp = int(input("Enter the Octal: "))
  except:
    print("Enter octal only! Program Out!")
  deDec = calDec(inp, 8)
  test = ["8", "9"]
  form = str(inp)
  tmp = [*form]
  for i in tmp:
    if i in test:
      print("Enter octal only! Program Out!")
      return 0
    else:
      return cal(deDec, "Octal", inp)

def calDec(nums, val):
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
  return hasil

def cal(value, pro, ori):
  pre = []
  b = value
  while value >= 1:
    c = value % 2
    c = str(c)
    pre.insert(0, c)
    value = int(value / 2)
  hasil = "".join(pre)
  final = (f"{pro} \"{ori}\" to Binary is : {hasil}")
  return final
