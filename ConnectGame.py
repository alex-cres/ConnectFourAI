import numpy as np


class ConnectGame:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.CONNECT_NUMBER = 4
        self.GAME_OVER = False
        self.TURN = 0
        self.board = self.createBoard(self.ROW_COUNT,self.COLUMN_COUNT)
        self.board_string=""
    def runGame(self):
        initBoard= input("Init Board? (y/n):")
        if initBoard == "y":
            initBoardStr = input("String based 0 for init:")
            result=self.initializeBoard(initBoardStr)
            if self.GAME_OVER:
                print("PLAYER "+result[0]+" WINS!"," WINING MOVE : ",result[1] , "REMAIN : " , result[2])
            else:
                self.printBoard()
                self.board_string=initBoard
                print(self.board_string)
        while not self.GAME_OVER:
        #Ask Player n input
            selected_col = int(input("Player "+str(self.TURN+1)+" Make your Selection (0-"+str(self.COLUMN_COUNT-1)+"):"))

            if self.isValidLocation(selected_col):
                row=self.getNextOpenRow(selected_col)
                self.dropPiece(row,selected_col,self.TURN+1)
                self.board_string=self.board_string+str(selected_col)
        
            self.printBoard()
            print(self.board_string)
            
            if self.winningMove(self.TURN+1):
                print("PLAYER "+str(self.TURN+1)+" WINS!")
                self.GAME_OVER=True
            
            self.TURN += 1
            self.TURN = self.TURN % 2
    def isGameOver(self):
        return self.GAME_OVER
    def createBoard(self,height,width):
        board = np.zeros((height,width))
        return board
    def dropPiece(self,row,col,piece):
        self.board[row][col] = piece
    def isValidLocation(self,col):
        return self.board[len(self.board)-1][col]==0
    def getNextOpenRow(self,col):
        for row in range(len(self.board)):
            if self.board[row][col]==0:
                return row
    def printBoard(self):
        print(np.flip(self.board,0))
    def getDiagonal(self,subBoard,t="+"):
        array = []
        if t == "+":
            for i in range(len(subBoard)):
                array.append(subBoard[i][i])
        else:
            for i in range(len(subBoard)):
                array.append(subBoard[len(subBoard)-1-i][i]) 
        return array
    def initializeBoard(self,positions):
        positions=[int(char) for char in positions]
        self.TURN = 0
        for i,move in enumerate(positions,start=1):
            if self.isValidLocation(move):
                row=self.getNextOpenRow(move)
                self.dropPiece(row,move,self.TURN+1)
                if self.winningMove(self.TURN+1):
                    self.GAME_OVER=True
                    return [self.TURN+1,i,positions[i:]]
            self.TURN += 1
            self.TURN = self.TURN % 2
        return []
    def winningMove(self,piece):
        #Check horizontal locations for win
        for c in range(self.COLUMN_COUNT-(self.CONNECT_NUMBER-1)):
            for r in range(self.ROW_COUNT):
                #print("Horizontal:",r,c,board[r,c:c+CONNECT_NUMBER])
                if all(x == piece for x in self.board[r,c:c+self.CONNECT_NUMBER]) :
                    return True
        #Check vertical locations for win
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT-(self.CONNECT_NUMBER-1)):
                #print("Vertical:",r,c,board[r:r+CONNECT_NUMBER,c])
                if all(x == piece for x in self.board[r:r+self.CONNECT_NUMBER,c]) :
                    return True

        #Positive Diagonals
        for c in range(self.COLUMN_COUNT-(self.CONNECT_NUMBER-1)):
            for r in range(self.ROW_COUNT-(self.CONNECT_NUMBER-1)):
                #print("Diagonal Pos:",r,c,board[r:r+CONNECT_NUMBER,c:c+CONNECT_NUMBER],getDiagonal(board[r:r+CONNECT_NUMBER,c:c+CONNECT_NUMBER],"+"))
                if all(x == piece for x in self.getDiagonal(self.board[r:r+self.CONNECT_NUMBER,c:c+self.CONNECT_NUMBER],"+")) :
                    return True
                
        #Negative Diagonals
        for c in range(self.COLUMN_COUNT-(self.CONNECT_NUMBER-1)):
            for r in range((self.CONNECT_NUMBER-1),self.ROW_COUNT):
                #print("Diagonal Neg:",r,c,board[r-(CONNECT_NUMBER-1):r+1,c:c+CONNECT_NUMBER],getDiagonal(board[r-(CONNECT_NUMBER-1):r+1,c:c+CONNECT_NUMBER],"-"))
                if all(x == piece for x in self.getDiagonal(self.board[r-(self.CONNECT_NUMBER-1):r,c:c+self.CONNECT_NUMBER],"-")):
                    return True

if __name__ == "__main__":
    game=ConnectGame()
    game.runGame()