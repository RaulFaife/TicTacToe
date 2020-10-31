import time

valueO = " O "
valueX = " X "
valueNull = "   "
playerTurn = 0

spaces = [valueNull]*9

slotsA = [1,2,3,4,5,6,7,8,9]
playerSlots = []

#Game Start Function
def startGame():
    start = input("Would you like to play Tic Tac Toe?\nPlease type 'Y' to begin: ")
    while(start != "Y"):
        start = input("Please type 'Y' to begin: ")

#Load Board
def printBoard():
    print(spaces[0] + "|" + spaces[1] + "|" + spaces[2])
    print("-----------")
    print(spaces[3] + "|" + spaces[4] + "|" + spaces[5])
    print("-----------")
    print(spaces[6] + "|" + spaces[7] + "|" + spaces[8])


#Player Turn
def playerCtrl(turn):
    print("Please select a slot:")
    print(*slotsA)
    playerInput = input("Type a value here: ")
    
    while(slotsA[int(playerInput)-1] == 0):
        print("Please choose a slot not yet taken: ")
        print(*slotsA)
        playerInput = input("You chose: ")
    
    if(slotsA[int(playerInput)-1] != 0):
        if(turn == 1):
            spaces[int(playerInput)-1] = valueX
        else:
            spaces[int(playerInput)-1] = valueO
    slotsA[int(playerInput)-1] = 0


#GameCode
startGame()
printBoard()
playerCtrl(0)
printBoard()
playerCtrl(1)
printBoard()
playerCtrl(0)
printBoard()
playerCtrl(1)
printBoard()
playerCtrl(0)
printBoard()
playerCtrl(1)
printBoard()
playerCtrl(0)
printBoard()
playerCtrl(1)
printBoard()