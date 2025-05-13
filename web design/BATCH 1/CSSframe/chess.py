for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
board = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]
for row in board:
    for piece in row:
        print(piece, end=" ")
    print()

board[0][1] = ' ' # clear the source square
board[2][1] = 'N' # place the knight on the destination square