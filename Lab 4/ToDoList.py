file = "todo.dat"

def addToList(file):
    item = input("What item do you want added: ")
    with open(file, "r") as toDoList:
        content = toDoList.readlines()
    with open(file, "a") as modifiedList:
        modifiedList.write(f"{len(content)+1}. {item}\n")
    print("\n--------------\nItem Added\n--------------\n")


def deleteFromList(file):
    x = []
    with open(file, "r") as delete:
        content = delete.readlines()
    
    #Checks if any items to delete
    if len(content) == 0:
        print("\n--------------\nNo Item To Delete\n--------------\n")
    
    else:
        showList(file)
        print(f"{len(content)+1}. Nevermind")
        gone = int(input("Which item do you want to get rid of: "))

        #Check if it's a valid Index
        while gone < (0) or gone > (len(content)+1):
            gone = int(input("Which item do you want to get rid of: "))
        #If user doesnt want to delete and changbe their mind
        if gone == len(content)+1:
            print("Ok!")
        else:
            content.pop(gone-1)

        for i in range(len(content)):
            info = content[i].split(" ", 1)
            x.append(info[1])

        with open(file, "w") as modifiedList:
            for i in range(len(content)):
                modifiedList.write(f"{i+1}. {x[i]}")

def showList(file):
    with open(file, "r") as finalList:
        content = finalList.readlines()
    #If Nothing In File!
    if len(content) == 0:
        print("\n--------------\nNo Items to view\n--------------\n")
    else:
        print("\n--------------\nTo-Do List:")
        for i in range(len(content)):
            print(content[i], end="")
        print("--------------\n")

#Choice Identification to Prevent Break
while True:
    #Try to see if it works
    try:
        choice = int(input("0. Quit\n1. Add Task to To-Do List\n2. Remove Task from To-Do List\n3. View To-Do List\nEnter your choice: "))
        if choice == 0:
            print("\n--------------\nExiting\n--------------\n")
            break
        elif choice == 1:
            addToList(file)
        elif choice == 2:
            deleteFromList(file)
        elif choice == 3:
            showList(file)
        #Number other than 0-3
        else:
            print("\n--------------\nInvalid choice. Please select a valid option (0-3).\n--------------\n")
    #Error for a letter
    except ValueError:
        print("\n--------------\nPlease enter a NUMBER!!!\n--------------\n")