list1 = [4, 7, 2, 8, 9, 1]
list2 = [9, 2, 5, 3, 1]

def isCommon(a,b:list):
    if a == b:
        return True
    return False

def commonElement(x:list, y:list):
    output =[]
    if len(x) >= len(y):
        for i in range(len(y)):
            for j in range(len(x)):
                if isCommon(y[i],x[j]):
                    output.append((x[j], j))
        return output
    
    for i in range(len(x)):
        for j in range(len(y)):
            if isCommon(x[i],y[j]):
                output.append((y[j], j))
    return output

print(commonElement(list1, list2))