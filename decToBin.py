
try:
  inp = int(input("Masukan Angka: "))
except:
  print("Masukan angka! Program Keluar!")

def decToBin(value):
  pre = []
  counter = 0
  b = value
  while value >= 1:
    c = value % 2
    c = str(c)
    pre.insert(0, c)
    value = int(value / 2)
  hasil = "".join(pre)
  print(f"Desimal \"{b}\" to Binary is : {hasil}")

decToBin(inp)
