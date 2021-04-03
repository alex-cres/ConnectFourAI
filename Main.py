import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
CONNECT_NUMBER = 4
GAME_OVER = False
TURN = 0

def create_board(height,width):
    board = np.zeros((height,width))
    return board

def drop_piece(board,row,col,piece):
    board[row][col] = piece
def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]==0
def get_next_open_row(board,col):
    for row in range(ROW_COUNT):
        if board[row][col]==0:
            return row
def print_board(board):
    print(np.flip(board,0))
def get_diagonal(board,t="+"):
    array = []
    if t == "+":
        for i in range(len(board)):
            array.append(board[i][i])
    else:
        for i in range(len(board)):
            array.append(board[len(board)-1-i][i]) 
    return array
def initialize_board(positions,board):
    global TURN , GAME_OVER
    positions=[int(char) for char in positions]
    TURN = 0
    for move in positions:
        if is_valid_location(board,move):
            row=get_next_open_row(board,move)
            drop_piece(board,row,move,TURN+1)
            if winning_move(board,TURN+1):
                print("PLAYER "+str(TURN+1)+" WINS!")
                GAME_OVER=True
        if GAME_OVER:
            break
        TURN += 1
        TURN = TURN % 2
def winning_move(board,piece):
    #Check horizontal locations for win
    for c in range(COLUMN_COUNT-(CONNECT_NUMBER-1)):
        for r in range(ROW_COUNT):
            #print("Horizontal:",r,c,board[r,c:c+CONNECT_NUMBER])
            if all(x == piece for x in board[r,c:c+CONNECT_NUMBER]) :
                return True
    #Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-(CONNECT_NUMBER-1)):
            #print("Vertical:",r,c,board[r:r+CONNECT_NUMBER,c])
            if all(x == piece for x in board[r:r+CONNECT_NUMBER,c]) :
                return True

    #Positive Diagonals
    for c in range(COLUMN_COUNT-(CONNECT_NUMBER-1)):
        for r in range(ROW_COUNT-(CONNECT_NUMBER-1)):
            #print("Diagonal Pos:",r,c,board[r:r+CONNECT_NUMBER,c:c+CONNECT_NUMBER],get_diagonal(board[r:r+CONNECT_NUMBER,c:c+CONNECT_NUMBER],"+"))
            if all(x == piece for x in get_diagonal(board[r:r+CONNECT_NUMBER,c:c+CONNECT_NUMBER],"+")) :
                return True
            
    #Negative Diagonals
    for c in range(COLUMN_COUNT-(CONNECT_NUMBER-1)):
        for r in range((CONNECT_NUMBER-1),ROW_COUNT):
            #print("Diagonal Neg:",r,c,board[r-(CONNECT_NUMBER-1):r+1,c:c+CONNECT_NUMBER],get_diagonal(board[r-(CONNECT_NUMBER-1):r+1,c:c+CONNECT_NUMBER],"-"))
            if all(x == piece for x in get_diagonal(board[r-(CONNECT_NUMBER-1):r,c:c+CONNECT_NUMBER],"-")):
                return True


board = create_board(ROW_COUNT,COLUMN_COUNT)


print_board(board)
while not GAME_OVER:
    #Ask Player n input
    initBoard= input("Init Board? (y/n):")
    if initBoard == "y":
        initBoardStr = input ("String based 0 for init:")
        initialize_board(initBoardStr,board)
        print_board(board)
        if GAME_OVER:
            break
    selected_col = int(input("Player "+str(TURN+1)+" Make your Selection (0-"+str(COLUMN_COUNT)+"):"))
        
    if is_valid_location(board,selected_col):
        row=get_next_open_row(board,selected_col)
        drop_piece(board,row,selected_col,TURN+1)
   
    print_board(board)
    
    if winning_move(board,TURN+1):
        print("PLAYER "+str(TURN+1)+" WINS!")
        GAME_OVER=True
    
    TURN += 1
    TURN = TURN % 2

    #0011223  - 1
    #00112233 - 1 
    #001122   - n/A
