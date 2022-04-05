"""
"""

class SudokuSlot:

    __slots__ = ["__notes", "__number"]

    def __init__(self):
        """
        """
        self.__notes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__number = None

    def __str__(self):
        """
        """
        return f"{self.__number} {self.__notes}"
        
    def add_note(self, number):
        """
        """

        if(type(number) == int and not number in self.__notes):
            self.__notes.append(number)

    def clear_notes(self):
        """
        """
        self.__notes = []

    def get_notes(self):
        """
        """
        return self.__notes

    def get_number(self):
        """
        """
        return self.__number

    def remove_note(self, number):
        """
        """
        if type(number) == int and number in self.__notes:
            self.__notes.remove(number)

    def set_number(self, number):
        """
        """

        if(type(number) == int):
            self.__number = number
    

        