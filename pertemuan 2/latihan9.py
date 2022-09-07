# buatlah suatu fungsi untuk membagi 2 himpunan angka
def getDiv(mylist):
    div = 24
    for row in mylist:
        for item in row:
            div /= item
    return div


print(getDiv([[2],[6]]))
