import random

cWin = 0
pWin = 0

selection = random.randint(0,2)
player_selection = int(input("scissor (0), rock (1), paper (2): "))

while cWin < 2 or pWin < 2:
    while((player_selection <0) or (player_selection>2)):
        player_selection = int(input("scissor (0), rock (1), paper (2): "))
    
    options = ["scissor","rock","paper"]
    output = "The computer is "+options[selection]+". You are "+options[player_selection]+"."

    diff = player_selection -selection
    if diff == 0:
        output+=" It is a draw."
    elif (diff == 1) or (diff == -2):
        output += " You won."
        pWin +=1
    elif (diff == 2) or (diff == -1):
        output += " You Lost."
        cWin +=1
    if cWin > 2:
        print("Computer is the WINNER")
    elif pWin > 2:
        print("Player is the WINNER")

print(output)
