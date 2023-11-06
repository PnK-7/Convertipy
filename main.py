import os
import time
from list.decToBin import *
#from list.binToDec import *
#from list.ocToDec import *
#from list.hexToDec import *

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
  else:
    print("Please enter number that exist on the list, except 2,3,4...etc until next update.")