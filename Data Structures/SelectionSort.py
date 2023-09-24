numbers = [2,9,5,4,8,1,6]

def swap(list,a,b):
    store = list[a]
    list[a] = list[b]
    list[b] = store

def getSmallest(list,a,b):
    if list[a] < list[b]:
        return True
    return False

def selectionSort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if getSmallest(list,i,j):
                swap(list,i,j)

selectionSort(numbers)
print(numbers)
            

