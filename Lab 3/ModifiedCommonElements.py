list1 = [4, 7, 2, 8, 9, 1]
list2 = [9, 2, 5, 3, 1]

def commonItems(x,y):
    output = []
    for i in x:
        if i in y:
            output.append((i, x.index(i)))
    return output

print(commonItems(list1,list2))