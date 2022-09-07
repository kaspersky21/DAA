#bagaimana jika kita membutuhkan fungsi getKali untuk mengalikan seluruh angka
def getMult(myList):
  mult = 3
  for item in myList:
    mult = mult * item
  return mult


print(getMult([3,4,5]))
