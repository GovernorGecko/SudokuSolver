"""

    TODO
    - Notes
    - begin solving

"""


from src.sudoku_board import SudokuBoard

#pods
#rows
#columns

EASY_TEST_BOARD = [
    [9, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 3, 2, 1, 5, 9],
    [0, 0, 0, 9, 1, 7, 8, 0, 6],
    [0, 7, 0, 0, 6, 0, 0, 2, 1],
    [0, 6, 0, 3, 0, 4, 9, 0, 0],
    [5, 3, 0, 0, 2, 0, 6, 0, 7],
    [0, 0, 1, 7, 0, 3, 0, 0, 2],
    [0, 0, 6, 5, 0, 1, 4, 0, 0],
    [3, 4, 0, 2, 0, 0, 0, 1, 0]
]

MEDIUM_TEST_BOARD = [
    [0, 0, 0, 0, 7, 0, 0, 1, 0],
    [3, 0, 2, 0, 0, 9, 0, 0, 7],
    [0, 0, 7, 8, 0, 6, 2, 5, 0],
    [0, 8, 0, 0, 0, 1, 0, 7, 9],
    [0, 0, 0, 9, 0, 0, 0, 6, 2],
    [2, 0, 0, 0, 4, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [4, 7, 0, 5, 0, 0, 0, 0, 0],
    [9, 2, 0, 0, 1, 8, 0, 0, 5]
]

HARD_TEST_BOARD = [
    [5, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [6, 0, 0, 3, 0, 0, 0, 0, 1],
    [0, 6, 0, 0, 3, 0, 7, 0, 0],
    [0, 8, 0, 9, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 8, 0, 7, 0, 0, 0, 4],
    [0, 0, 0, 0, 5, 0, 0, 1, 0],
    [0, 3, 0, 0, 8, 0, 0, 9, 0],
]

EVIL_TEST_BOARD = [
    [0, 1, 0, 7, 0, 0, 2, 0, 8],
    [9, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 2, 0, 0, 7, 0, 0, 0],
    [0, 8, 0, 2, 0, 0, 1, 0, 6],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [1, 0, 0, 0, 0, 9, 6, 0, 3],
    [0, 3, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 6, 0, 0, 0, 4, 0],
]

sudoku_board = SudokuBoard()

test_board = EVIL_TEST_BOARD

for row in range(0, len(test_board)):
    for column in range(0, len(test_board[row])):
        if(test_board[row][column] != 0):
            sudoku_board.set_number_in_slot(
                row, column,
                test_board[row][column]
            )

print(sudoku_board)

while(sudoku_board.solve()):
    print("\n")
    print(sudoku_board)
