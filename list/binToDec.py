

def binToDec():
  noB = ['2', '3', '4', '5', '6', '7', '8', '9']
  try:
    inp = int(input("Enter the Binary : "))
  except:
    print("Enter Binary only! Program Out!")
  
  def calc(nums):
    pre = []
    counter = 0
    b = nums
    nums = str(nums)
    nums = [*nums]
    nums.reverse()
    for i in nums:
      if i in noB:
        print("Enter Binary only! Program Out!")
        break
      i = int(i)
      x = i * pow(2, counter)
      counter += 1
      pre.append(x)
    hasil = sum(pre)
    print(f"Binary \"{b}\" to Decimal is : {hasil}")
  calc(inp)