numbers = [30,50,40,60,20,80,70,0,100,10,90]

def swap(list,a,b):
    store = list[a]
    list[a] = list[b]
    list[b] = store

def getSmallest(list,a,b):
    if list[a] > list[b]:
        return True
    return False

for j in range(len(numbers)):
    for i in range(len(numbers)-1):
        if getSmallest(numbers,i,i+1):
            swap(numbers,i,i+1)

print(numbers)