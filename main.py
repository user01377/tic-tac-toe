import random

boardIndex = {
    "1": 56,
    "2": 64,
    "3": 72,
    "4": 160,
    "5": 168,
    "6": 176,
    "7": 264,
    "8": 272,
    "9": 280
}

board = '''+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+'''

listBoard = list(board)
print(board)

def userMove():
    userInput = input("place O where: ")
    
    checkValid("human", userInput)
    listBoard[boardIndex[userInput]] = "O"

    global updatedBoard
    updatedBoard = "".join(listBoard)
    print(updatedBoard)

    if checkVictory("human") == "Player":
        print("Player Wins!")
    else:
        computerMove()

def computerMove():
    computerInput = random.randint(1,9)


    checkValid("computer",computerInput)
    listBoard[boardIndex[str(computerInput)]] = "X"
    updatedBoard = "".join(listBoard)
    print("Computers Move:")
    print(updatedBoard)

    if checkVictory("computer") == "computer":
        print("Computer Wins!")
    else:
        userMove()
          

def checkVictory(player):
    currentBoard = []

    #updating board to latest info
    for position in range(1,10):
        currentBoard.append(board[boardIndex[str(position)]])

    if player == "human": 

        #only 4 win conditions
        if currentBoard[0] == "O" and currentBoard[1] == "O" and currentBoard[2] == "O" or currentBoard[6] == "O" and currentBoard[7] == "O" and currentBoard[8] == "O": 
            return "Player"
        elif currentBoard[0] == "O" and currentBoard[3] == "O" and currentBoard[6] == "O" or currentBoard[2] == "O" and currentBoard[5] == "O" and currentBoard[8] == "O":
            return "Player"
        else:
            return "NoWin"

    elif player == "computer": #must check all 8 win conditions because players first move is not a constant
        if currentBoard[0] == "X" and currentBoard[1] == "X" and currentBoard[2] == "X" or currentBoard[3] == "X" and currentBoard[4] == "X" and currentBoard[5] == "X" or currentBoard[6] == "X" and currentBoard[7] == "X" and currentBoard[8] == "X":
             return "computer"
        elif currentBoard[0] == "X" and currentBoard[3] == "X" and currentBoard[6] == "X" or currentBoard[1] == "X" and currentBoard[4] == "X" and currentBoard[7] == "X" or currentBoard[2] == "X" and currentBoard[5] == "X" and currentBoard[8] == "X":
             return "computer"
        else:
             return "NoWin"
             
def checkValid(player,playerInput): 
    
    if player == "human":
        if listBoard[boardIndex[str(playerInput)]] == "X" or listBoard[boardIndex[str(playerInput)]] == "O":
            print("INVALID MOVE")
            
            userMove()
    elif player == "computer":
        if listBoard[boardIndex[str(playerInput)]] == "O" or listBoard[boardIndex[str(playerInput)]] == "X":
            print("invalid computer")
            computerMove()
        
userMove()
