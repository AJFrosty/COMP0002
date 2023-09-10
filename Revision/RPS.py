import random

choice = int(input("Choose your option: \n0) Scissors\n1) Rock\n2) Paper\nChoice: "))
compChoice = random.randint(0,2)
options = ["Scissors", "Rock", "Paper"]
if choice == compChoice:
    print(f"There's a Tie of {options[choice]}")
elif choice == 0 and compChoice == 1:
    print(f"The Computer Chose: {options[compChoice]}. You chose: {options[choice]}! You Lost!")
elif choice == 0 and compChoice == 2:
    print(f"You chose: {options[choice]}. The Computer Chose: {options[compChoice]}! You Won!")
elif choice == 1 and compChoice == 2:
    print(f"The Computer Chose: {options[compChoice]}. You chose: {options[choice]}! You Lost!")
elif choice == 1 and compChoice == 0:
    print(f"You chose: {options[choice]}. The Computer Chose: {options[compChoice]}! You Won!")
elif choice == 2 and compChoice == 0:
    print(f"The Computer Chose: {options[compChoice]}. You chose: {options[choice]}! You Lost")
else:
    print(f"You chose: {options[choice]}. The Computer Chose: {options[compChoice]}! You Won!")