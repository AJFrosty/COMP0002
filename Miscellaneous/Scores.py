import os.path

file = input("Enter File Name/Path: ")
while not os.path.isfile(file):
    file = input("Enter File Name/Path: ")

def scoreInfo(file):
    with open(file, "r") as scores:
        content = scores.readlines()
    if len(content) <= 1:
        raise ValueError("There needs to be atleast 2 scores in the file!")
    for i in range(len(content)):
        content[i] = float(content[i])
    print(f"There are {len(content)} scores")
    print(f"The total is {sum(content)}")
    print(f"The average is {sum(content)/len(content)}")

scoreInfo(file)
