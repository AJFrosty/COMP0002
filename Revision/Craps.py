import random

i = int(input("Input a 1 if you're ready: "))
if i == 1:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    sum = die1 + die2

    if sum == 2 or sum == 3 or sum == 12:
        print(f"You rolled a {die1} + {die2} = {sum}")
        print("YOU LOSE!")
    elif sum == 7 or sum == 11:
        print(f"You rolled a {die1} + {die2} = {sum}")
        print("YOU WIN!")
    else:
        print(f"You rolled a {die1} + {die2} = {sum}")
        print(f"Point is {sum}")
        j = int(input("Input a 1 if you're ready: "))
        new1 = random.randint(1,6)
        new2 = random.randint(1,6)
        newSum = new1 + new2
        print(f"You rolled a {new1} + {new2} = {newSum}")

        if newSum == 7:
            print("YOU Lost!")
        elif newSum == sum:
            print("You Win!")

        while newSum != sum and newSum != 7:
            j = int(input("Input a 1 if you're ready: "))
            new1 = random.randint(1,6)
            new2 = random.randint(1,6)
            newSum = new1 + new2
            print(f"You rolled a {new1} + {new2} = {newSum}")

            if newSum == 7:
                print("YOU Lost!")
            elif newSum == sum:
                print("You Win!")
else:
    print("Good Bye!")


