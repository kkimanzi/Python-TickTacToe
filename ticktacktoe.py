from contextlib import nullcontext
import random
import time

# Constants 
USER = "user"
USERMOVE = "X"
COMPUTER = "computer"
COMPUTERMOVE = "O"

# List containing winning combinations
WINNINGCOMBINATIONS = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16],[1,6,11,16],[4,7,10,13],[2,7,12],[3,6,9],[5,10,15],[8,11,14]]

#initialize availableList and boardList
availableList = list(range(1,17))
boardList = list(range(1,17))

#function to get user input
def getUserInput():
    validInput = False

    while not validInput:
        userInput = input("Enter a number: ")
        
        # check if input is number
        if not userInput.isdigit():
            print("Enter Number")
            continue
            
        userInput = int(userInput)

        #check if number is in available list
        if (userInput not in availableList):
                print("Option not available")
                continue

        return userInput

# function to get random input from available list
def getComputerInput():
    return random.choice(availableList)

# function to update lists used in program
def updateLists(player, position):
    # remove the player's position from available list
    availableList.remove(position)

    # mark the user's position on the boards array
    boardList[position-1] = (USERMOVE if player == USER else COMPUTERMOVE)

# check if a player won the game
def checkWin(player):
    # list containing the moves currently played by the player
    playerMoves = []
    # populate the list with the player's moves
    for x in range(16):
        if (boardList[x] == (USERMOVE if player == USER else COMPUTERMOVE)):
            playerMoves.append(x+1)

    #checking for if the playerMoves has a winning combination
    won = False
    for combination in WINNINGCOMBINATIONS:
        won = all(item in playerMoves for item in combination)
        if won:
            break

    # return status whether won or not as per check above        
    return won

# function to print the board on console        
def printBoard():
    position = 1
    row = ""
    for x in range(16):
        row += "|"
        row += "\t" + str(boardList[x]) + "\t"
        if (position == 4):
            for i in range (25):
                print("-",end="")
            print()
            
            row += "|"
            print (row.expandtabs(3))
            
            row = ""
            position = 1
            continue 

        position += 1
    for i in range (25):
        print("-",end="")
    print()

def handlePlayer(player):
    playerInput = getUserInput() if player == USER else getComputerInput()
    if (player == COMPUTER):
        print(f"Computer selected: {playerInput}")
    updateLists(player, playerInput)


# ****************************
# ***** Begin Execution ******
# ****************************

# 1st look of the board   
printBoard()

# random get first player
player = USER if (random.randint(0,1) == 0) else COMPUTER
print(f"First player is {player}")
# a little sleep    
time.sleep(2)

won = False
atMove = 1

# run the program while there are available moves to play

while (len(availableList) > 0):
    handlePlayer(player)
    printBoard()

    # check if player won after 6 moves have been made
    # since 3 is the minimum combination length that can win
    if (atMove >= 5):
        won = checkWin(player)
        if won:
            print (f"{player} won the match!")
            break

    # a little sleep    
    time.sleep(2)    
    #toggle to the next player
    player = USER if player == COMPUTER else COMPUTER
    #increment the moves played in the game
    atMove += 1

if (not won):
    print("Moves exhausted! Tie")
