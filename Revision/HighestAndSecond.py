#Find the Two Highest Scores from a list of grades of studentsS

count = int(input("Enter the number of students: "))
while count < 2:
    count = int(input("Enter the number of students: "))
n = 0
max = 0
sec = 0

for i in range(count):
    score = float(input("Enter the student Score: "))
    while score < 0 or score > 100:
        score = float(input("Enter the student Score: "))
    if score > max:
        sec = max
        max = score
    if score < max and score > sec:
        sec = score
    n +=1
print(f"Highest is {max}, Second Highest is {sec}")
