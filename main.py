import os
import time
from list.fromBinary import *
#from list.fromDecimal import *

if __name__ == '__main__':
  os.system("rm -rf list/__pycache__")
  os.system("clear")
  print("1. From Binary to any\n2. From Decimal to any\n0. Exit")
  try:
    inp = int(input("Choose one : "))
  except:
    print("Enter numbers not else!")
  if inp == 0:
    print("Out!")
  elif inp == 1:
    print(fromB())
  elif inp == 2:
    print(fromD())
  else:
    print("Please enter number that exist on the list, except 3,4...etc until next update.")
