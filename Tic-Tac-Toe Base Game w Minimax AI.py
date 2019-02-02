def print_intro():
    print(
'''

 ______   __    ______     ______   ______    ______     ______   ______    ______    
/\__  _\ /\ \  /\  ___\   /\__  _\ /\  __ \  /\  ___\   /\__  _\ /\  __ \  /\  ___\   
\/_/\ \/ \ \ \ \ \ \____  \/_/\ \/ \ \  __ \ \ \ \____  \/_/\ \/ \ \ \/\ \ \ \  __\   
   \ \_\  \ \_\ \ \_____\    \ \_\  \ \_\ \_\ \ \_____\    \ \_\  \ \_____\ \ \_____\ 
    \/_/   \/_/  \/_____/     \/_/   \/_/\/_/  \/_____/     \/_/   \/_____/  \/_____/ 
                                                                                         
                                 BASE GAME + MINIMAX AI
                               By Irish Danielle Morales
                        Originally made with Jarod Angelo Lustre

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
        cell = input("Invalid input! Please enter a valid cell to make a move on. (1-9): ")

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
            return False

    #runs if input is not a number
    else:
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
        #print_board()
        #print("Player", switch_turn(turn), "has won the game! Congratulations!")
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


def ask_ai():
    response = input("Play with Minimax AI? (Y/N): ")

    #while response is invalid, keep asking for input
    while(response != "Y" and response != "N"):
        print("Please input Y to play with Minimax AI and N to play with a friend.")
        response = input("Play with Minimax AI? (Y/N): ")

    if response == "Y":
        print("You are now playing with Minimax AI!")
        return True
    else:
        print("You are now playing with a friend!")
        return False


def move_player_first():
    response = input("Would you like to make the first move? (Y/N): ")

    #while response is invalid, keep asking for input
    while(response != "Y" and response != "N"):
        print("Please input Y to move first and N to let Minimax AI move first.")
        response = input("Would you like to make the first move? (Y/N): ")

    if response == "Y":
        print("You are now Player 1! You will now move first.")
        ai_turn = 2
        return True
    else:
        print("You are now Player 2! You will now move last.")
        ai_turn = 1
        return False

    
def minimax_ai():
    best_move = -100
    best_cell = 0
    
    for cell in range(1, 10):
        if check_if_empty_cell(cell, set_board_row(cell), set_board_col(cell)) == True:
            tmp_board = board
            if turn == 1:
                tmp_board[set_board_row(cell)][set_board_col(cell)]= "X"
            else:
                tmp_board[set_board_row(cell)][set_board_col(cell)]= "O"
            print(cell, win(), "OUTSIDE LOOP", ai_turn)
            while win() == False:
                print(cell, False, "INSIDE LOOP BEFORE MINIMAX")
                minimax(tmp_board, cell)
            current_move = evaluate()
            
            if current_move > best_move:
                best_move = current_move
                best_cell = cell

            print('CURRENT', current_move, ' ', cell, 'BEST', best_move, ' ', best_cell)
            print(tmp_board)
            print_board()

    print("Player ", turn, " (Minimax AI) made a move on cell ", best_cell, "!", sep="")

    #sets cell to X or O depending on turn (P1 = 'X', P2 = 'O')    
    #if turn == 1:
    #    board[set_board_row(best_cell)][set_board_col(best_cell)]= "X"
    #else:
    #    board[set_board_row(best_cell)][set_board_col(best_cell)]= "O"


def minimax(tmp_board, cell):
    for cell in range(1, 10):
        if check_if_empty_cell(cell, set_board_row(cell), set_board_col(cell)) == True:
            if turn == 1:
                tmp_board[set_board_row(cell)][set_board_col(cell)]= "X"
            else:
                tmp_board[set_board_row(cell)][set_board_col(cell)]= "O"


def evaluate():
    if win() and turn == ai_turn:
        return 10
    elif win() and turn != ai_turn:
        return -10
    else:
        return 0

    
#DRIVER PROGRAM====================================================================

print_intro()
replay = True

while replay == True:
    #resets variables
    board = [[1,2,3],
             ['X',5,6],
             ['X',8,9]]
    turn = 1
    ai_turn = 0

    #actual game if playing without AI
    if ask_ai() == False:
        while (win() or tie()) == False:
            print_board()
            choose_cell()
            turn = switch_turn(turn)

    #actual game if playing with minimax AI
    else:
        #game if player moves first
        if move_player_first() == True:
            ai_turn = 2
            while (win() or tie()) == False:
                #player move
                print_board()
                choose_cell()
                turn = switch_turn(turn)

                #checks for win or tie after player move
                if (win() or tie()) == True:
                    break

                #minimax ai move
                print_board()
                minimax_ai()            
                turn = switch_turn(turn)

        #game if player moves last
        else:
            ai_turn = 1
            while (win() or tie()) == False:
                #minimax ai move
                print_board()
                minimax_ai()            
                turn = switch_turn(turn)

                #checks for win or tie after minimax ai move
                if (win() or tie()) == True:
                    break
                
                #player move
                print_board()
                choose_cell()
                turn = switch_turn(turn)

    #asks to replay
    replay = ask_replay()
