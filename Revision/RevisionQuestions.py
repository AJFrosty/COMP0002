# One
print("Welcome to Python")
print("Welcome to Computer Science")
print("Programming is Fun")

#Two
math = ((9.5 * 4-5) -(2.5 * 3)) / (45.5-3.5)
print(math)

#Four
temp = float(input("Whats the Temp in Celcius: "))
fah = (9/5) * temp + 32
print(fah)

#Five
rem = 0
years = days = 0
mins = int(input("Enter the number of minutes: "))
if mins//525600 >= 1:
    years = mins//525600
    rem = mins - (years*525600)
    days = rem//1440
    print(f"{mins} minutes is approximately {years} and {days} days")
else:
    days = mins//1440
    print(f"{mins} minutes is approximately {years} and {days} days")

#Six (Not Correct)
v = float(input("Enter the velocity: "))
a = float(input("Enter the Acceleration: "))
l = v**2 / 2*a
print(l)
