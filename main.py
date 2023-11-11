import os
import time
from list.decToBin import *
from list.bin_oc_hexToDec import *

if __name__ == '__main__':
  os.system("clear")
  print("1. Decimals to Binary\n2. Binary to Decimals\n3. Octal to Decimals\n4. Hexadecimal to Decimals\n0. Exit")
  try:
    inp = int(input("Choose one : "))
  except:
    print("Enter numbers not else!")
  if inp == 0:
    print("Out!")
  elif inp == 1:
    decToBin()
  elif inp == 2:
    binToDec()
  elif inp == 3:
    ocToDec()
  elif inp == 4:
    hexToDec()
  else:
    print("Please enter number that exist on the list, except 3,4...etc until next update.")