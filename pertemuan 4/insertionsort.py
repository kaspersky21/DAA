def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        next = list[i]
        while(list[j]>next) and (j >= 0):
            list[j+1] = list[j]
            j=j-1
        list[j+1] = next
    return list

#masukkan angka dengan urutan lainnya
list = [35,31,32,34,33,37,36]

print(list)
print(InsertionSort(list))

print("")
#latihan
print("latihan")
def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        next = list[i]
        while(list[j]>next) and (j >= 0):
            list[j+1] = list[j]
            j=j-1
        list[j+1] = next
    return list

list = [89,12,57,16,25,11,75]
print(InsertionSort(list))