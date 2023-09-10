def Prime(n) :
    if n <= 1 or n%2 == 0:
        return False
    if n == 2:
        return True
    for i in range(3,n,2):
        if n%i == 0:
            return False
    return True

n = 0
j = 0
while n < 1001:
    if Prime(n):
        print(n, end=" ")
    n+=1
    j+=1
    