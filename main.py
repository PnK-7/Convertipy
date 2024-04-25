import os
import time
from list.toBinary import *
from list.toDecimal import *

if __name__ == '__main__':
  os.system("rm -rf list/__pycache__")
  os.system("clear")
  print("1. Binary to Decimals\n2. Octal to Decimals\n3. Hexadecimal to Decimals\n4. Decimal to Binary\n5. Octal to Binary\n0. Exit")
  try:
    inp = int(input("Choose one : "))
  except:
    print("Enter numbers not else!")
  if inp == 0:
    print("Out!")
  elif inp == 1:
    print(binToDec())
  elif inp == 2:
    print(ocToDec())
  elif inp == 3:
    print(hexToDec())
  elif inp == 4:
    print(decToBin())
  elif inp == 5:
    print(ocToBin())
  else:
    print("Please enter number that exist on the list, except 3,4...etc until next update.")
