"""
"""

import math

from .sudoku_slot import SudokuSlot


class SudokuBoard:

    __slots__ = ["__board"]

    def __init__(self):
        """
        """

        self.__board = []
        for _ in range(0, 9):
            self.__board.append(
                [
                    SudokuSlot(),
                    SudokuSlot(),
                    SudokuSlot(),
                    SudokuSlot(),
                    SudokuSlot(),
                    SudokuSlot(),
                    SudokuSlot(),
                    SudokuSlot(),
                    SudokuSlot(),
                ]
            )                   


    def __str__(self):
        """
        """
        return '\n'.join(' '.join(str(x) for x in row) for row in self.__board)


    def get_number(self, row, column):
        """
        """

        slot = self.get_slot(row, column)

        if type(slot) == SudokuSlot:
            return slot.get_number()
        
        return None   


    def get_numbers_from_slot_list(self, slots):
        """
        """

        numbers = []

        if type(slots) == list:
            for slot in slots:
                if type(slot) == SudokuSlot:
                    numbers.append(slot.get_number())

        return numbers     

    
    def get_pod(self, row, column):
        """
        """

        if self.is_valid_number(row) and self.is_valid_number(column):
            return math.floor(column / 3) + (math.floor(row / 3) * 3)

    
    def get_slot(self, row, column):
        """
        """

        if self.is_valid_number(column) and self.is_valid_number(row):
            return self.__board[row][column]
        
        return None


    def get_slots_in_column(self, column):
        """        
        """

        if self.is_valid_number(column):
            return [self.__board[row][column] for row in range(0, 9)]

        return []

    
    def get_slots_in_pod(self, pod):
        """
        """

        if self.is_valid_number(pod):

            column_offset = (pod % 3) * 3
            row_offset = math.floor(pod / 3) * 3

            pod_numbers = []                    

            for row in range(0 + row_offset, 3 + row_offset):
                for column in range(0 + column_offset, 3 + column_offset):
                    pod_numbers.append(self.get_slot(row, column))

            return pod_numbers

        return []  


    def get_slots_in_row(self, row):
        """
        """

        if self.is_valid_number(row):
            return [column for column in self.__board[row]]

        return []


    def is_number_valid_for_slot(self, row, column, number):
        """
        """
        return(
            self.is_valid_number(row) and
            self.is_valid_number(column) and
            self.is_valid_number(number - 1) and
            (not number in self.get_numbers_from_slot_list(self.get_slots_in_column(column))) and
            (not number in self.get_numbers_from_slot_list(self.get_slots_in_row(row))) and
            (not number in self.get_numbers_from_slot_list(self.get_slots_in_pod(self.get_pod(row, column))))
        )

    def is_valid_number(self, number):
        """        
        """
        return type(number) == int and number >= 0 and number <= 8


    def set_number_in_slot(self, row, column, number):
        """        
        """

        if(self.is_number_valid_for_slot(row, column, number)):

            # Set our number
            self.__board[row][column].set_number(number)

            # Remove our Notes
            self.__board[row][column].clear_notes()

            # Column
            for slot in self.get_slots_in_column(column):
                slot.remove_note(number)

            # Pod
            for slot in self.get_slots_in_pod(self.get_pod(row, column)):
                slot.remove_note(number)

            # Row
            for slot in self.get_slots_in_row(row):
                slot.remove_note(number)
            



