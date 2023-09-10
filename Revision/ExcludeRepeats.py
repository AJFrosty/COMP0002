list = []
def Repeats(num):
    for i in range(0,len(list)):
        if num == list[i]:
            return False
    list.append(num)

for i in range(10):
    n = int(input(f"Enter Number {i+1}: "))
    Repeats(n)

list.sort()
for i in range(len(list)):
    print(list[i], end=" ")
