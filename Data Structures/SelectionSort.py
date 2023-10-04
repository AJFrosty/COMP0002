numbers = [2,9,5,4,8,1,6]

def swap(list,a,b):
    store = list[a]
    list[a] = list[b]
    list[b] = store

def getSmallest(list,a,b):
    smallest = a
    for i in range(a,b):
        if list[smallest] > list[i]:
            smallest = i
    return smallest

def selectionSort(list):
        for i in range(len(list)-1):
            swap(list,i,getSmallest(list,i,len(list)))

selectionSort(numbers)
print(numbers)