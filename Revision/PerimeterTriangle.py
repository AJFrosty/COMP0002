a = float(input("Enter Side 1: "))
b = float(input("Enter Side 2: "))
c = float(input("Enter Side 3: "))

if a+b > c and b+c> a and a+c > b:
    perim = a+b+c
    print(perim)
else:
    print("Invalid!")


    