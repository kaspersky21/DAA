list = [25,21,22,24,23,27,26]
#modifikasikan sesuai angka favorit anda

#proses penukaran bubble sort
lastElementIndex = len(list)-1
print(0,list)
for idx in range(lastElementIndex):
                if list[idx]>list[idx+1]:
                    list[idx],list[idx+1]=list[idx+1],list[idx]
                print(idx+1,list)
print("")
def BubbleSort(list):
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex,0,-1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1]=list[idx+1],list[idx]
        return list

#masukkan angka dengan urutan lainnya
list = [25,21,22,24,23,27,26]

print(BubbleSort(list))
print(list)

print("")
#latihan
print("latihan")
list = [100,20,60,90,40,30,10]

def BubbleSort(list):
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex,0,-1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1]=list[idx+1],list[idx]
        return list

print(BubbleSort(list))