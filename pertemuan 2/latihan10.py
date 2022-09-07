#buatlah suatu fungsi untuk mengurangi 2 himpunan angka
def getMin(mylist):
    min = 10
    for row in mylist:
        for item in row:
            min -= item
    return min


print(getMin([[5],[2]]))