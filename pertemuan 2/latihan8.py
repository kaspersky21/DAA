#bagaimana jika kita membutuhkan fungsi getBagi untuk mengalikan seluruh angka
def getDiv(myList):
  div = 24
  for item in myList:
    div = div / item
  return div


print(getDiv([2,6]))