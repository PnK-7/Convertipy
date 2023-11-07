
def decToBin():
  try:
    inp = int(input("Enter the Decimal : "))
  except:
    print("Enter decimal only! Program Out!")
  def cal(value):
    pre = []
    b = value
    while value >= 1:
      c = value % 2
      c = str(c)
      pre.insert(0, c)
      value = int(value / 2)
    hasil = "".join(pre)
    print(f"Desimal \"{inp}\" to Binary is : {hasil}")

  cal(inp)
