board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]


def validate(board, y, x, value):
    # checks if the entered value exists in the column
    for i in range(9):
        if board[y][i] == value:
            return False

    # checks if the entered value exists in the row
    for i in range(9):
        if board[i][x] == value:
            return False

    # checks if the entered value exists in a given 3x3 square
    boxX = (x//3) * 3
    boxY = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if board[boxY + i][boxX + j] == value:
                return False

    # if the entered value is valid, then True is returned
    return True


def solve(board):
    # checks for zeros in the board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                # once an empty square is found, a valid value for it is found
                for value in range(1, 10):
                    if validate(board, y, x, value):
                        board[y][x] = value
                        solve(board)
                        # if a value later turns out to be invalid, it is cleared and a new value will be found
                        board[y][x] = 0

                return
    # displays the board after solving it and asks the user if they would like to search for an alt. solution
    print(board)
    input('Find alternative solution?')


print(board)
print('\n')
solve(board)