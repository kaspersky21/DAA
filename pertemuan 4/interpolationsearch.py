def BubbleSort(list):
#Exchange the elements to arange in order
	lastElementIndex = len(list)-1
	for passNo in range (lastElementIndex,0,-1):
		for idx in range(passNo):
			if list[idx]>list[idx+1]:
			   list[idx],list[idx+1]=list[idx+1],list[idx]
	return list

def IntPolsearch(list,x):
    idx0 = 0
    idxn = (len(list)-1)
    found = False

    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        mid = idx0 +int(((float(idxn - idx0)/(list[idxn]-list[idx0])) * (x - list[idx0])))
        if list[mid] == x:
            found = True
            return found

        if list[mid] < x:
            idx0 = mid + 1
    return found

list = [12,33,11,99,22,55,90]
sorted_list = BubbleSort(list)
print(IntPolsearch(list,12))
print(IntPolsearch(list,91))
print("")

#latihan
print("Latihan")

def IntPolsearch(list,x):
    idx0 = 0
    idxn = (len(list)-1)
    found = False

    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        mid = idx0 + int(((float(idxn - idx0)/(list[idxn]-list[idx0])) * (x - list[idx0])))
        if list[mid] == x:
            found = True
            return found

        if list[mid] < x:
            idx0 = mid + 1
    return found

#list = ['y','u','i','w','o','a','q','u','j','p']
#sorted_list = BubbleSort(list)
#print(IntPolsearch(list, 'u'))

#tidak bisa bu karena variabel nya bukan integer
