def commonElement(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append((element, list1.index(element)))
    return common_elements

list1 = [4, 7, 2, 8, 9, 1]
list2 = [9, 2, 5, 3, 1]
result = commonElement(list1, list2)
print(result)
