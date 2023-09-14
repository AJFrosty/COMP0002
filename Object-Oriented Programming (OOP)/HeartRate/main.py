from HeartRate import HeartRates

fname = input("First Name: ")
lname = input("Last Name: ")
month = int(input("Month of Birth: "))
day = int(input("Day of Birth: "))
year = int(input("Year of Birth: "))

print("------------------------------------------------------------------------")
user = HeartRates(fname,lname,month,day,year)

print(f"Name: {user.getFirstName()} {user.getLastName()} \nAge: {user.age()} \nMax Heart Rate: {user.maxHeartRate()} bpm \nTarget Heart Rate: {user.targetHeartRate()} bpm")