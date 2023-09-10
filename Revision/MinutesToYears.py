mins = int(input("Enter the number of minutes: "))
if mins//525600 >= 1:
    years = mins//525600
    rem = mins - (years*525600)
    days = rem//1440
    print(f"{mins} minutes is approximately {years} years and {days} days")
else:
    days = mins//1440
    print(f"{mins} minutes is approximately 0 years and {days} days")
