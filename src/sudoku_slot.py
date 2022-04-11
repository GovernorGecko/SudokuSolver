
class SudokuSlot:

    __slots__ = ["__notes", "__number"]

    def __init__(self):
        """
        Sudoku Slot represents a square on a Sudoku Board for
        holding either a number value, or notes on what number
        it could possibly be.
        """
        self.reset()

    def __str__(self):
        """
        Returns
            String of our number or notes.
        """
        if self.__number == None:
            return str(self.__notes)
        else:
            return str(self.__number)
        
    def add_note(self, number):
        """
        Parameters
            Int representing a number to add to our notes.
        """
        if type(number) == int and self.__number == None and not number in self.__notes:
            self.__notes.append(number)

    def get_notes(self):
        """
        Returns
            List of our notes
        """
        return self.__notes

    def get_number(self):
        """
        Returns
            Int or None
        """
        return self.__number

    def is_number_in_notes(self, number):
        """
        Returns
            Bool of whether the number is in our notes.
        """
        if type(number) == int and self.__number == None and number in self.__notes:
            return True
        return False

    def remove_note(self, number):
        """
        Parameters
            Int if valid and not in our notes.
        """
        if type(number) == int and self.__number == None and number in self.__notes:
            self.__notes.remove(number)

    def reset(self):
        """
        """
        self.__notes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__number = None

    def set_number(self, number):
        """
        Parameters
            Int if valid, sets to our number and clears our notes.
        """
        if type(number) == int:
            self.__notes = []
            self.__number = number
    

        