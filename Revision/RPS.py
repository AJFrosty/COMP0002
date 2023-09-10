import random

compChoice = random.randint(0,2)
options = ["Scissors", "Rock", "Paper"]
userWins = compWins = 0

while userWins < 2 and compWins < 2:
    choice = int(input("Choose your option: \n0) Scissors\n1) Rock\n2) Paper\nChoice: "))
    if choice == compChoice:
        print(f"There's a Tie of {options[choice]}")
    elif choice == 0 and compChoice == 1:
        print(f"The Computer Chose: {options[compChoice]}. You chose: {options[choice]}! You Lost!")
        compWins+=1
    elif choice == 0 and compChoice == 2:
        print(f"The Computer Chose: {options[compChoice]}. You chose: {options[choice]}! You Won!")
        userWins+=1
    elif choice == 1 and compChoice == 2:
        print(f"The Computer Chose: {options[compChoice]}. You chose: {options[choice]}! You Lost!")
        compWins+=1
    elif choice == 1 and compChoice == 0:
        print(f"The Computer Chose: {options[compChoice]}. You chose: {options[choice]}! You Won!")
        userWins+=1
    elif choice == 2 and compChoice == 0:
        print(f"The Computer Chose: {options[compChoice]}. You chose: {options[choice]}! You Lost")
        compWins+=1
    else:
        print(f"You chose: {options[choice]}. The Computer Chose: {options[compChoice]}! You Won!")
        userWins+=1
    print(f"User now has {userWins} wins and Computer has {compWins} wins!")
    if userWins == 2:
        print("You won 2 games over the computer!")
        break
    elif compWins == 2:
        print("You lost, the computer won 2 games over you!")
    