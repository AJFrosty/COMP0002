import random

m = int(input("Enter the Matrix Format: "))

# from 1 to M we do a random 0 or 1 and based on how many M's we are gonna have m rows
for i in range(m):
    for j in range(m):
        n = random.randint(0,1)
        print(n, end = " ")
    print("")