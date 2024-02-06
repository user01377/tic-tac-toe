import random

boardIndex = {
    "1": 56,
    "2": 64,
    "3": 72,
    "4": 160,
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

userInput = input("place O where: ")
x = list(board)
x[boardIndex[userInput]] = "O"
newString = "".join(x)
print(newString)
