import os
import random


def clear_screen():
    """
    Clear the console based on OS, see credits for more info
    """
    os.system('cls||clear')


class Grid():
    def __init__(self):
        self.grid_marks = [[' ' for columns in range(5)] for rows in range(5)]
        self.player = random.randint(0, 1)

    def print_grid(self):
        """
        Prints the gameboard to the console
        """

        print('     │  A  │  B  │  C  │  D  │  E  │')
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  1  │  {self.grid_marks[0][0]}  │  {self.grid_marks[0][1]}  │  {self.grid_marks[0][2]}  │  {self.grid_marks[0][3]}  │  {self.grid_marks[0][4]}  │")
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  2  │  {self.grid_marks[1][0]}  │  {self.grid_marks[1][1]}  │  {self.grid_marks[1][2]}  │  {self.grid_marks[1][3]}  │  {self.grid_marks[1][4]}  │")
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  3  │  {self.grid_marks[2][0]}  │  {self.grid_marks[2][1]}  │  {self.grid_marks[2][2]}  │  {self.grid_marks[2][3]}  │  {self.grid_marks[2][4]}  │")
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  4  │  {self.grid_marks[3][0]}  │  {self.grid_marks[3][1]}  │  {self.grid_marks[3][2]}  │  {self.grid_marks[3][3]}  │  {self.grid_marks[3][4]}  │")
        print('─────┼─────┼─────┼─────┼─────┼─────┤')
        print(f"  5  │  {self.grid_marks[4][0]}  │  {self.grid_marks[4][1]}  │  {self.grid_marks[4][2]}  │  {self.grid_marks[4][3]}  │  {self.grid_marks[4][4]}  │")
        print('─────┴─────┴─────┴─────┴─────┴─────┘')
    

    def change_player(self) -> int:
        """
        Changes the player from 0 to 1 or vice versa
        """
        # Variable is set to 1 minus the self.player value. This means that if
        # the self.player value is equal to 0, nothing will be subtracted, turning
        # the self.player value into 1. If the self.player value is equal to 1, 
        # Then 1 will be subtracted from 1, turning the self.player value into 0.
        self.player = 1 - self.player


    def check_game_status(self):
        """
        Checks whether the game should still run or stop.
        """
        def full_grid():
            """
            Checks if grid is full
            """
            total_marks = 0
            marks_used = 0
            for list in self.grid_marks:
                for item in list:
                    total_marks += 1
                    if item != ' ':
                        marks_used += 1
            print(f'Total marks used: {marks_used}')
            if marks_used == total_marks:
                print('Grid is full!')
                return 'Game is a tie!'
            else:
                print('Grid not full')
                return False


        def check_for_win():
            """
            Checks if a player has 4 horizontal, vertical or diagonal marks
            """
            result = self.grid_marks

            def check_rows():
                # Check the 1st row
                if result[0][0] and result[0][0] == result[0][1] == result[0][2] == result[0][3] != ' ' or \
                result[0][1] == result[0][2] == result[0][3] == result[0][4] != ' ':
                    print('1st row win!')
                # Check the 2nd row
                elif result[1][0] == result[1][1] == result[1][2] == result[1][3] != ' ' or \
                result[1][1] == result[1][2] == result[1][3] == result[1][4] != ' ':
                    print('2nd row win!')
                # Check the 3rd row
                elif result[2][0] and result[2][0] == result[2][1] == result[2][2] == result[2][3] != ' ' or \
                result[2][1] == result[2][2] == result[2][3] == result[2][4] != ' ':
                    print('3rd row win!')
                # Check the 4th row
                elif result[3][0] == result[3][1] == result[3][2] == result[3][3] != ' ' or \
                result[3][1] == result[3][2] == result[3][3] == result[3][4] != ' ':
                    print('4th row win!')
                # Check the 5th row
                elif result[4][0] == result[4][1] == result[4][2] == result[4][3] != ' ' or \
                result[4][1] == result[4][2] == result[4][3] == result[4][4] != ' ':
                    print('5th row win!')
                print(result)
            
            check_rows()
        
        
        check_for_win()


    def place_mark(self):
        row_text = 'Please select a row (1 to 5): '
        col_text = 'Please select a column (A to E): '
        row = input(row_text)
        # Used to see if row variable has a correct value or not
        row_set = False
        while not row_set:
            try:
                row = int(row)
            except ValueError:
                print(f'You entered {row}, which is not a number.')
                row = input(row_text)
            else:
                row_set = True
                row -= 1

        while 0 < int(row) > 4:
            print(f'You entered {row}, which is not a valid row.')
            row = input(row_text)

        col_raw = input(col_text)
        # Used to see if col_raw variable is empty or not
        col_set = False
        while not col_set:
            if len(col_raw) == 0:
                print('Empty value detected, please try again.')
                col_raw = input(col_text)
            else:
                col_set = True
                
        # Convert the letter into a number using ord(), then 97 is subtracted to
        # get the correct number as 'a' is equal to 97, 'b' is equal to 98 etc.
        col = ord(col_raw.lower()) - 97
        while col < 0 or col > 4:
            print(f'You entered {col_raw.upper()}, which is not a valid column.')
            col_raw = input(col_text)
            col = ord(col_raw.lower()) - 97 

        if self.grid_marks[row][col] != ' ':
            print('A mark is already in place, please select a different location.\n')
            self.place_mark()
        else:
            # If the self.player value is equal to 0, place an 'O' mark. Else, place
            # an 'X' mark
            if self.player == 0:
                self.grid_marks[row][col] = 'O'
                self.change_player()
            else:
                self.grid_marks[row][col] = 'X'
                self.change_player()


def menu(page) -> str:
    """
    Shows a menu that changes depending on what parameter 'page' is set to.
    When set to 'main menu', allow users to start the game or read the game 
    instructions. When set to 'game instructions', allow users to start the
    game or call this function again, setting parameter 'page' to 'main menu'.
    :param page: string
    """
    if page == 'main menu':
        print('Welcome to 5x5 Tic-Tac-Toe!\n')
        print('Would you like to start the game or read the game instructions?')
        menu_options = '1. Start the game\n2. Read game instructions\n'
        menu_input = input(menu_options)
    elif page == 'game instructions':
        print('Would you like to start the game or go back to the main menu?')
        menu_options = '1. Start the game\n2. Back to main menu\n'
        menu_input = input(menu_options)

    while menu_input != '1' and menu_input != '2':
        print(f'\nYou entered {menu_input}, which is not a valid option.\n')
        print('Please select one of the two options:')
        menu_input = input(menu_options)

    if menu_input == '1':
        clear_screen()
        # Create the game grid using Grid class to access its attributes and methods
        grid = Grid()
        grid_marks = grid.grid_marks
        print(grid.check_game_status())

        # Keep running the game until game_over is equal to True
        game_over = False
        while not game_over:
            grid.print_grid()
            grid.place_mark()
            grid.check_game_status()
    elif menu_input == '2':
        if page == 'main menu':
            clear_screen()
            game_instructions()
        elif page == 'game instructions':
            clear_screen()
            menu('main menu')


def game_instructions():
    """
    Shows the game instructions, then call menu function
    """
    print('As the name implies, 5x5 Tic-Tac-Toe is a the same as the Tic-Tac-Toe we all know and love,')
    print('except that it uses a 5x5 grid instead of a 3x3 grid. To win the game, you have to get 4 marks')
    print('in a row, either horizontally, vertically or diagonally. If no one is able to get 4 marks in a')
    print('row, then the game is a draw.\n')
    print('To play the game, you first have to pick a row, then a column. For example, if you are playing')
    print('with the X marks, picking row 2 and column D would look like this:\n')
    # Set the board mark on row 2, column D to X
    grid_marks[1][3] = 'X'
    grid.print_grid()
    # Reset the board mark on row 2, column D back to a space
    grid_marks[1][3] = ' '
    print("\nYou cannot overwrite another players' mark, trying to do so will result in the game asking")
    print('you to pick a different location instead. Good luck and have fun playing!\n')
    input('Press any key to clear the screen and continue.\n')
    clear_screen()
    menu('game instructions')


def main():
    """
    Runs the retuired functions to start the program
    """
    menu('main menu')

main()