

def x_wing_solver(sudoku_board, row, column):
    """
    Parameters
        SudokuBoard Board
        Int row
        Int column
    Returns
        Bool
    """

    # Validation.  Primarily to ensure we can make a box.
    if (
        type(row) != int or row < 0 or row > 7 or
        type(column) != int or column < 0 or column > 7
    ):
        return False

    # Grab our Slot information
    slot = sudoku_board.get_slot(row, column)
    slot_notes = slot.get_notes()

    # We'll check each note in turn
    for note in slot_notes:

        bottom_right_tuple = None

        for row_next in range(row, 9):

            if note in sudoku_board.get_slot(row_next, column).get_notes():

                for column_next in range(column, 9):

                    if note in sudoku_board.get_slot(row_next, column_next).get_notes():
                        
                        bottom_right_tuple = (row_next, column_next)

        if type(bottom_right_tuple) == tuple:
            print(bottom_right_tuple)
        

