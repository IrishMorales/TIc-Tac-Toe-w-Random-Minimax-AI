def print_intro():
    print(
'''

 ______   __    ______     ______   ______    ______     ______   ______    ______    
/\__  _\ /\ \  /\  ___\   /\__  _\ /\  __ \  /\  ___\   /\__  _\ /\  __ \  /\  ___\   
\/_/\ \/ \ \ \ \ \ \____  \/_/\ \/ \ \  __ \ \ \ \____  \/_/\ \/ \ \ \/\ \ \ \  __\   
   \ \_\  \ \_\ \ \_____\    \ \_\  \ \_\ \_\ \ \_____\    \ \_\  \ \_____\ \ \_____\ 
    \/_/   \/_/  \/_____/     \/_/   \/_/\/_/  \/_____/     \/_/   \/_____/  \/_____/ 
                                                                                         
                                       BASE GAME


                           Welcome to the game of Tic Tac Toe!
''')


def print_sep():
    print("\n<====================================================================================>\n")


def print_board():
    print_sep()

    #prints line at top of board
    print("o-----------o")
    row_index=0
    
    for row in board:
        #removes quotation marks & replaces spaces, commas, brackets w/ lines
        for c in (("'", ''), ("[", "| "), ("]", " |"), (", ", " | ")):
            row=str(row).replace(*c)
            
        print(row)

        #prints lines inside board or line at bottom of board
        print("|-----------|") if row_index!=2 else print("o-----------o\n")
        row_index+=1
        
        '''
        For reference:
        
        board:
        [1,2,3]
        [4,5,6]
        [7,8,9]
        
        print:
        o-----------o
        | 1 | 2 | 3 |
        |-----------|
        | 4 | 5 | 6 |
        |-----------|
        | 7 | 8 | 9 |
        o-----------o
        '''


def choose_cell():
    cell = input("Player " + str(turn) + ", what cell will you make a move on? (1-9): ")
    
    #while input cell is invalid, keep asking for input
    while check_if_valid_cell(cell) == False:
        cell = input("Player " + str(turn) + ", what cell will you make a move on? (1-9): ")

    cell=int(cell)

    #sets cell to X or O depending on turn (P1 = 'X', P2 = 'O')    
    if turn == 1:
        board[set_board_row(cell)][set_board_col(cell)]= "X"
    else:
        board[set_board_row(cell)][set_board_col(cell)]= "O"


def check_if_valid_cell(cell):
    #checks and runs if input is a number
    if cell.isdigit():
        cell=int(cell)

        #checks if input cell is empty
        if check_if_empty_cell(cell, set_board_row(cell), set_board_col(cell)) == True:
            return True
        else:
            cell = print("That cell is already taken! Please input a valid cell number.")
            return False

    #runs if input is not a number
    else:
        cell = print("Sorry, that's not a valid number! Please input a number from 1 to 9.")
        return False

        
def set_board_row(cell):
    #returns row index of cell (0-2)
    if cell%3 == 0:
        return int(cell/3)-1
    else:
        return int(cell/3)


def set_board_col(cell):
    #returns column index of cell (0-2)
    if cell%3 == 0: 
         return 2
    else:
         return (cell%3)-1


def check_if_empty_cell(cell, row, col):
    if cell >= 1 and cell <= 9 and board[row][col]!="O" and board[row][col]!="X":
        return True
    else:
        return False

    
def win():
    if (#Horizontal combinations
        board[0][0]==board[0][1]==board[0][2] or
        board[1][0]==board[1][1]==board[1][2] or
        board[2][0]==board[2][1]==board[2][2] or
        #Vertical combinations
        board[0][0]==board[1][0]==board[2][0] or
        board[0][1]==board[1][1]==board[2][1] or
        board[0][2]==board[1][2]==board[2][2] or
        #Diagonal combinations
        board[0][0]==board[1][1]==board[2][2] or
        board[0][2]==board[1][1]==board[2][0]):
        
        #If any of the combinations are true, the last player to move wins
        print_board()
        print("Player", switch_turn(turn), "has won the game! Congratulations!")
        return True
    
    else:
        return False


def tie():
    is_tie = True
    
    #checks if any number exists in board
    #if any number exists in board, board is not tied
    for a in range(1, 10):
        for row in board:
            if a in row:
                is_tie = False
                return False

    #runs if board is tied
    if is_tie:
        print_board()
        print("The game has ended in a tie!")
        return True


def switch_turn(turn):
    #switches turn from 1 to 2 and vice versa
    if turn == 1:
        turn+=1
    else:
        turn-=1
        
    return turn


def ask_replay():
    print_sep()
    response = input("Game Over! Do you want to play again? (Y/N): ")

    #while response is invalid, keep asking for input
    while(response != "Y" and response != "N"):
        print("Please input Y to replay and N to stop playing.")
        response=input("Do you want to play again? (Y/N): ")

    if response == "Y":
        return True
    else:
        print("Thank you for playing!")
        return False

    
#DRIVER PROGRAM====================================================================

print_intro()
replay = True

while replay == True:
    #resets variables
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    turn = 1

    #actual game
    while (win() or tie()) == False:
        print_board()
        choose_cell()
        turn = switch_turn(turn)
            
    #asks to replay
    replay = ask_replay()
