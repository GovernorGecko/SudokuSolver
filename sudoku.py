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
    [9, None, None, 6, None, None, None, None, None],
    [None, 8, None, None, 3, 2, 1, 5, 9],
    [None, None, None, 9, 1, 7, 8, None, 6],
    [None, 7, None, None, 6, None, None, 2, 1],
    [None, 6, None, 3, None, 4, 9, None, None],
    [5, 3, None, None, 2, None, 6, None, 7],
    [None, None, 1, 7, None, 3, None, None, 2],
    [None, None, 6, 5, None, 1, 4, None, None],
    [3, 4, None, 2, None, None, None, 1, None]
]

sudoku_board = SudokuBoard()

for row in range(0, len(EASY_TEST_BOARD)):
    for column in range(0, len(EASY_TEST_BOARD[row])):
        if(EASY_TEST_BOARD[row][column] != None):
            sudoku_board.set_number_in_slot(
                row, column,
                EASY_TEST_BOARD[row][column]
            )

print(sudoku_board)