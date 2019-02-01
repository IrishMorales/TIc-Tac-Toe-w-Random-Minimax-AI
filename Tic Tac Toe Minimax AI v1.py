def initialize():
    #MAY STILL CONTAIN UNNECESSARY VARIABLES
    print("Loading game...")
    global board
    global turn
    global end_game
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    turn = 0
    end_game = False

def print_board():
    print("o-----------o")
    tmpIndex=0
    
    for a in board:
        #Removes quotation marks & replaces spaces, commas, brackets w/ lines
        a=str(a)
        a=a.replace("'", '')
        a=a.replace("[", "| ")
        a=a.replace("]", " |")
        a=a.replace(", ", " | ")
        print(a)
        if tmpIndex!=2:
            print("|-----------|")
        else:
            print("o-----------o")
        tmpIndex+=1
        
        '''
        For reference:
        o-----------o
        | 1 | 2 | 3 |
        |-----------|
        | 4 | 5 | 6 |
        |-----------|
        | 7 | 8 | 9 |
        o-----------o
        '''
        

def choose_number():
    print("Player ", turn+1, ", make your move!", sep="")
    b = input()
    isValid=False
    
    #while input is invalid, keep asking for input - SHOULD PROBABLY BE A FUNCTION
    while isValid==False:
        if b.isdigit():
            b=int(b)
            board_row=set_board_row(b)
            board_column=set_board_column(b)
            if check_if_valid(b, board_row, board_column)==True:
                isValid=True
            else:
                b = input("You can't make that move! Input another number.\n")
        else:
            b = input("Sorry, that's not a valid number! Choose from 1 to 9!\n")
            
    if turn == 0:
        board[board_row][board_column]= "X"
    else:
        board[board_row][board_column]= "O"

        
def set_board_row(b):
    if(b%3==0):
        return int(b/3)-1
    else:
        return int(b/3)


def set_board_column(b):
    if(b%3==0): 
         return 2
    else:
         return b%3-1


def check_if_valid(b, row, column):
    if b >= 1 and b <= 9 and board[row][column]!="O" and board[row][column]!="X":
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
        #If any of the combinations are true, the current player wins & True is returned
        print("Player", (turn+1), "has won the game! Congratulations!")
        return True
    else:
        return False


def tie():
    isTie=True
    for a in range(1, 10):
        for row in board:
            if a in row:
                isTie=False
                return False

    if isTie:
        print("The game has ended in a tie!")
    return True


def ask_replay():
    response=input("Game Over! Do you want to play again? (Y/N)\n")

    while(response!="Y" and response!="N"):
        print("Please input Y to replay and N to stop playing.")
        response=input("Do you want to play again? (Y/N)\n")

    if response=="Y":
        return True
    else:
        print("Thank you for playing!")
        return False

def ask_AI():
    response=input("Play against advanced AI? (Y/N)\n")
    
    while(response!="Y" and response!="N"):
        print("Please input Y to play against the AI and N to play with a friend.")
        response=input("Play against advanced AI? (Y/N)\n")

    if response=="Y":
        print("You are now playing with advanced AI!")
        return True
    else:
        print("You are now playing with a friend!")
        return False
    
def move_AI():
    #INSERT MINIMAX METHOD
    #NEEDS HEAVY OPTIMIZATION
    #NEEDS  BOARD UPDATE
    #CURRENT: weighted method
    utility=-100
    placed_move=False
    depth=0
    print("The AI is now playing!")

    while depth<=5:
        
        utility=find_winning_move()
        
        if utility!=-100: #if a best move is found to win/tie
            placed_move=place_move_AI(utility)
            break
         
        utility=find_counter_move()

        if utility!=-100: #if a best move is found to counter
            placed_move=place_move_AI(utility)
            break

        depth+=1
                            
def find_winning_move():
    move=-100
    for num in range(1,10): 
        #checks if current num is valid, if not proceed to next num
        if check_if_valid(num, set_board_row(num), set_board_column(num)): 
            board[set_board_row(num)][set_board_column(num)] = "X" #temporarily sets square at current num to X to check outcome
            if win(): #if placing that move will result in a win
                move=num
            board[set_board_row(num)][set_board_column(num)] = num #resets square at current num
    return move

def find_counter_move():
    move=-100
    for num in range(1,10): #cycles through all numbers in board
        if check_if_valid(num, set_board_row(num), set_board_column(num)): #checks if current num is valid, if not proceed to next num
            board[set_board_row(num)][set_board_column(num)] = "O" #sets square at current num to O
            if win(): #if placing that move will result in a win of the opponent
                move=num
            board[set_board_row(num)][set_board_column(num)] = num #resets square at current num
    return move

def check_square(num, board, boardIndex):
    if check_if_valid(num, board, set_board_row(num), set_board_column(num)):
        return place_move_AI(num, board, boardIndex)
    else:
        return False

def place_move_AI(move):
    row=set_board_row(move) 
    column=set_board_column(move)
    board[row][column] = "X"
    print("The AI made a move on cell ", move, "!", sep="")
    return True

#DRIVER PROGRAM-------------------------------------------------------------------------------
replay = True
while replay == True:
    initialize()
    print_board()
    #OPTIMIZATION: end_game loop inside checking ask_AI() or the other way around?

    if ask_AI()==False:        
        while end_game != True:
            choose_number()
            print_board()

            end_game=win()
            if end_game==False:
                end_game=tie()
            
            if turn==0:
                turn+=1
            else:
                turn-=1
    
    else:
        #NEED TO ADD: Choose if AI goes first or second
        #CURRENT: AI always goes first
        while end_game != True:
            if turn==0:
                if board[1][1]==5:
                    place_move_AI(5)
                else:
                    move_AI()
            else:
                choose_number()
            
            print_board()
            end_game=win()
            if end_game==False:
                end_game=tie()
            
            if turn==0:
                turn+=1
            else:
                turn-=1

    replay=ask_replay()
