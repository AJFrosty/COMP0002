#Procedural
import random 
answer = random.randint(1,100)
prevGuess = 0
count = 0

while count < 10:
    guess = int(input("Enter your guess: "))
    curDif = abs(answer-guess)
    preDiff = abs(answer - prevGuess)
    if prevGuess == 0:
        print("You guessed Incorrectly")
        prevGuess = guess
    elif guess == answer:
        print(f"You WIN! The number was: {answer}")
        break
    elif curDif > preDiff:
        print("You're getting Colder")
        prevGuess = guess
    elif curDif < preDiff:
        print("You're getting Hotter")
        prevGuess = guess
    count +=1

if count == 10:
    print(f"You Lossed! The answer was {answer}")