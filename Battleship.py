from random import randint

board = []
#Inicializa um array com 5 posições com "O"
ocean = ["O"] * 5

#Inicializa a matriz de duas dimensões
for i in range(5):
    board.append(ocean)

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    row = randint(0, len(board) - 1)
    print(row)
    return row
     
def random_col(board):
    col = randint(0, len(board) - 1)
    print(col)
    return col

print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(3):

    guess_row = int(input("Guess row: "))
    guess_col = int(input("Guess col: "))

    if guess_row not in range(len(board)) or \
        guess_col not in range(len(board)):
        print("Oops, that's not even in the ocean.")
    else:
        if guess_row == ship_row and guess_col == ship_col:
            print("Right!")
        else:
            if board[guess_row][guess_col] == "X":
                print("You guessed that one already")
            else:
                print("Wrong..")
                board[guess_row][guess_col] = 'X'
                print_board(board)







