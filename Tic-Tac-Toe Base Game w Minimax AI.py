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
                        Originally made with Jarod Anjelo Lustre

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

    mark_cell(int(cell), turn)
    
    
def mark_cell(cell, turn):
    #sets cell to X or O depending on turn (P1 = 'X', P2 = 'O')    
    if turn == 1:
        board[set_board_row(cell)][set_board_col(cell)] = "X"
    else:
        board[set_board_row(cell)][set_board_col(cell)] = "O"


def check_if_valid_cell(cell):
    #checks and runs if input is a number
    if cell.isdigit():

        #checks if input cell is empty
        if int(cell) in find_avail_cells():
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
        return True
    
    else:
        return False


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


def ask_player_first():
    response = input("Would you like to make the first move? (Y/N): ")

    #while response is invalid, keep asking for input
    while(response != "Y" and response != "N"):
        print("Please input Y to move first and N to let Minimax AI move first.")
        response = input("Would you like to make the first move? (Y/N): ")

    if response == "Y":
        print("You will now move first.")
        return True
    else:
        print("You will now move last.")
        return False

    
def minimax_ai():
    best_val = -100
    best_cell = 0
    
    #iterate over cells
    for cell in range(1, 10):
        #if cell is empty:
        if cell in find_avail_cells():
            #mark cell
            mark_cell(cell, 2)
            #minimax on cell
            cell_val = minimax(0, False)
            #reset cell
            board[set_board_row(cell)][set_board_col(cell)] = cell
            
            if cell_val > best_val:
                best_cell = cell
                best_val = cell_val

    print("Player 2 (Minimax AI) made a move on cell ", best_cell, "!", sep="")
    mark_cell(best_cell, 2)
        
        
def minimax(depth, isMaximizing):
    #if at terminal state, evaluate
    if win() or not find_avail_cells():
        #subtract depth
        if eval_terminal(not isMaximizing) == 10:
            return eval_terminal(not isMaximizing) - depth
        elif eval_terminal(not isMaximizing) == -10:
            return eval_terminal(not isMaximizing) + depth
        else:
            return eval_terminal(not isMaximizing)
            
    #if maximizing
    if isMaximizing:
        best_val = -100
        for cell in range(1, 10):
            if cell in find_avail_cells():
                initcell = board[set_board_row(cell)][set_board_col(cell)]
            
                mark_cell(cell, isMaximizing+1)
                    
                best_val = max(best_val, minimax(depth+1, not isMaximizing))
                
                board[set_board_row(cell)][set_board_col(cell)] = initcell
        return best_val
        
    #if minimizing
    else:
        best_val = 100
        for cell in range(1, 10):
            if cell in find_avail_cells():
                initcell = board[set_board_row(cell)][set_board_col(cell)]
            
                mark_cell(cell, isMaximizing+1)
                    
                best_val = min(best_val, minimax(depth+1, not isMaximizing))
                
                board[set_board_row(cell)][set_board_col(cell)] = initcell
        return best_val
        
        
def find_avail_cells():
    avail_cells = []
    
    for cell in range(1, 10):
        if board[set_board_row(cell)][set_board_col(cell)]!="O" and board[set_board_row(cell)][set_board_col(cell)]!="X":
            avail_cells.append(cell)
            
    return avail_cells
    
    
def eval_terminal(isMaximizing):
    if win():
        #if AI won
        if isMaximizing:
            return 10
        #if player won
        else:
            return -10
    elif not find_avail_cells():
        return 0

        
#DRIVER PROGRAM====================================================================

print_intro()
replay = True

while replay == True:
    #resets variables
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    turn = 1

    #actual game if playing without AI
    if ask_ai() == False:
        while not win() and find_avail_cells():
            print_board()
            choose_cell()
            turn = switch_turn(turn)

    #actual game if playing with Minimax AI
    else:
        #game if player moves first
        if ask_player_first():
            while not win() and find_avail_cells():
                #player move
                print_board()
                choose_cell()
                turn = switch_turn(turn)

                #checks for win or tie after player move
                if win() or not find_avail_cells():
                    break

                #minimax ai move
                print_board()
                minimax_ai()
                turn = switch_turn(turn)

        #game if player moves last
        else:
            turn = 2
            while not win() and find_avail_cells():
                #minimax ai move
                print_board()
                minimax_ai()            
                turn = switch_turn(turn)

                #checks for win or tie after minimax ai move
                if win() or not find_avail_cells():
                    break
                
                #player move
                print_board()
                choose_cell()
                turn = switch_turn(turn)

    print_board()
    
    if win():
        print("Player", switch_turn(turn), "has won the game! Congratulations!")
    else:
        print("The game has ended in a tie!")
    
    #asks to replay
    replay = ask_replay()