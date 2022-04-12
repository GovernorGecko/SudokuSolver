
import math

from .sudoku_slot import SudokuSlot


class SudokuBoard:

    __slots__ = ["__board"]

    def __init__(self):
        """
        The Sudoku Board is a 9x9 Board of 3x3 squares in a 3x3
        pattern.  I call these squares, Pods.  Each Pod can have
        a single instance of the numbers 1 - 9.  Each row and column,
        can individually also only contain a single instance of the
        numbers 1 - 9.
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
        Returns
            String simple output of data.
        """
        return '\n'.join(' '.join(str(x) for x in row) for row in self.__board)


    def get_number(self, row, column):
        """
        Parameters
            Int row
            Int column
        Returns
            Int or None
        """

        slot = self.get_slot(row, column)

        if type(slot) == SudokuSlot:
            return slot.get_number()
        
        return None   


    def get_numbers_from_slot_list(self, slots):
        """
        Parameters
            List of SudokuSlot
        Returns
            List of Ints
        """

        numbers = []

        if type(slots) == list:
            for slot in slots:
                if type(slot) == SudokuSlot:
                    numbers.append(slot.get_number())

        return numbers     

    
    def get_pod(self, row, column):
        """
        Parameters
            Int row
            Int column
        Returns
            Int or None
        """

        if self.is_valid_number(row) and self.is_valid_number(column):
            return math.floor(column / 3) + (math.floor(row / 3) * 3)

        return None

    
    def get_slot(self, row, column):
        """
        Parameters
            Int row
            Int column
        Returns
            SudokuSlot or None
        """

        if self.is_valid_number(column) and self.is_valid_number(row):
            return self.__board[row][column]
        
        return None


    def get_slots_in_column(self, column):
        """
        Parameters
            Int column
        Returns
            List of SudokuSlots 
        """

        if self.is_valid_number(column):
            return [self.__board[row][column] for row in range(0, 9)]

        return []

    
    def get_slots_in_pod(self, pod):
        """
        Parameters
            Int pod
        Returns
            List of SudokuSlots
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
        Parameters
            Int row
        Returns
            List of SudokuSlots
        """

        if self.is_valid_number(row):
            return [column for column in self.__board[row]]

        return []


    def is_number_valid_for_slot(self, row, column, number):
        """
        Parameters
            Int row
            Int column
            Int number
        Returns
            Bool
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
        Parameters
            Int number
        Returns
            Bool
        """
        return type(number) == int and number >= 0 and number <= 8


    def set_number_in_slot(self, row, column, number):
        """
        Parameters
            Int row
            Int column
            Int number
        Returns
            Bool  
        """

        if(self.is_number_valid_for_slot(row, column, number)):

            # Set our number
            self.__board[row][column].set_number(number)

            # Column
            for slot in self.get_slots_in_column(column):                
                slot.remove_note(number)

            # Pod
            for slot in self.get_slots_in_pod(self.get_pod(row, column)):
                slot.remove_note(number)

            # Row
            for slot in self.get_slots_in_row(row):
                slot.remove_note(number)

            # Was set
            return True

        # Was not set
        return False
            
    
    def solve(self):
        """
        Returns
            Bool
        """

        # We go row by row, checking on notes.
        for row in range(0, 9):
            for column in range(0, 9):               

                slot = self.get_slot(row, column)

                # Do we need to solve?
                if slot.get_number() != None:
                    continue

                slot_notes = slot.get_notes()     

                # First off, do we only have a single note?
                if len(slot_notes) == 1 and self.set_number_in_slot(row, column, slot_notes[0]):
                    print(f"[{row}, {column}] set to {slot_notes[0]} since it is the only note.")
                    return True

                # Secondly, we will do note comparison.
                pod_slot_notes = []
                for slot_other in self.get_slots_in_pod(self.get_pod(row, column)):
                    if slot != slot_other:
                        pod_slot_notes.extend(slot_other.get_notes())

                for note in slot_notes:
                    if note not in pod_slot_notes and self.set_number_in_slot(row, column, note):
                        print(f"[{row}, {column}] set to {note} since after comparison it is the only note.")
                        return True                    

        return False

