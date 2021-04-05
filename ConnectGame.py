"""
ConnectGame
=====

Provides the base for an ConnectGame
"""

import numpy as np

class ConnectGame:
    def __init__(self,row_count=6,column_count=7,connect_number=4):
        self.__ROW_COUNT = row_count
        self.__COLUMN_COUNT = column_count
        self.__CONNECT_NUMBER = connect_number
        self.__GAME_OVER = False
        self.__TURN = 0
        self.__BOARD = self.__createBoard(self.__ROW_COUNT,self.__COLUMN_COUNT)
        self.__BOARD_STRING = ""
    def __nextTurn(self):
        self.__TURN += 1
        self.__TURN = self.__TURN % 2
    def __createBoard(self,height,width):
        __BOARD = np.zeros((height,width))
        return __BOARD
    def __dropPiece(self,row,col,piece):
        self.__BOARD[row][col] = piece
    def __getNextOpenRow(self,col):
        for row in range(len(self.__BOARD)):
            if self.__BOARD[row][col]==0:
                return row
    def __getDiagonal(self,subBoard,t="+"):
        array = []
        if t == "+":
            for i in range(len(subBoard)):
                array.append(subBoard[i][i])
        else:
            for i in range(len(subBoard)):
                array.append(subBoard[len(subBoard)-1-i][i]) 
        return array
    def isValidLocation(self,col):
        return self.__BOARD[len(self.__BOARD)-1][col]==0
    def printBoard(self):
        print(np.flip(self.__BOARD,0))
    def getBoard(self):
        return self.__BOARD
    def getFlippedBoard(self):
        return np.flip(self.__BOARD,0)
    def initBoard(self,positions):
        positions=[int(char) for char in positions]
        self.__TURN = 0
        for i,move in enumerate(positions,start=1):
            result = self.tryDropPiece(move)
            if result:
                if self.isWinningMove(self.__TURN+1):
                    self.__GAME_OVER=True
                    return [self.__TURN+1,i,positions[i:]]
                self.__nextTurn()
        return []
    def isWinningMove(self,piece):
        #Check horizontal locations for win
        for c in range(self.__COLUMN_COUNT-(self.__CONNECT_NUMBER-1)):
            for r in range(self.__ROW_COUNT):
                if all(x == piece for x in self.__BOARD[r,c:c+self.__CONNECT_NUMBER]) :
                    return True
        #Check vertical locations for win
        for c in range(self.__COLUMN_COUNT):
            for r in range(self.__ROW_COUNT-(self.__CONNECT_NUMBER-1)):
                if all(x == piece for x in self.__BOARD[r:r+self.__CONNECT_NUMBER,c]) :
                    return True

        #Positive Diagonals
        for c in range(self.__COLUMN_COUNT-(self.__CONNECT_NUMBER-1)):
            for r in range(self.__ROW_COUNT-(self.__CONNECT_NUMBER-1)):
                if all(x == piece for x in self.__getDiagonal(self.__BOARD[r:r+self.__CONNECT_NUMBER,c:c+self.__CONNECT_NUMBER],"+")) :
                    return True
                
        #Negative Diagonals
        for c in range(self.__COLUMN_COUNT-(self.__CONNECT_NUMBER-1)):
            for r in range((self.__CONNECT_NUMBER-1),self.__ROW_COUNT):
                if all(x == piece for x in self.__getDiagonal(self.__BOARD[r-(self.__CONNECT_NUMBER-1):r,c:c+self.__CONNECT_NUMBER],"-")):
                    return True
    def tryDropPiece(self,selected_col):
        if self.isValidLocation(selected_col):
                row = self.__getNextOpenRow(selected_col)
                self.__dropPiece(row,selected_col,self.__TURN+1)
                self.__BOARD_STRING = self.__BOARD_STRING+str(selected_col)
                return True
        return False
    def getBoardString(self):
        return self.__BOARD_STRING
    def isGameOver(self):
        return self.__GAME_OVER
    def runConsoleGame(self):
        initBoard = input("Init Board? (y/n):")
        if initBoard == "y":
            initBoardStr = input("String based 0 for init:")
            result = self.initBoard(initBoardStr)
            if self.__GAME_OVER:
                print("PLAYER "+result[0]+" WINS!"," WINING MOVE : ",result[1] , "REMAIN : " , result[2])
            else:
                self.printBoard()
                self.__BOARD_STRING=initBoard
                print(self.__BOARD_STRING)
        while not self.__GAME_OVER:
        #Ask Player n input
            selected_col = int(input("Player "+str(self.__TURN+1)+" Make your Selection (0-"+str(self.__COLUMN_COUNT-1)+"):"))

            result = self.tryDropPiece(selected_col)
        
            self.printBoard()
            print(self.__BOARD_STRING)
            if result : 
                if self.isWinningMove(self.__TURN+1):
                    print("PLAYER "+str(self.__TURN+1)+" WINS!")
                    self.__GAME_OVER=True
                self.__nextTurn()
            else:
                print("Invalid input")
    def getColumnCount(self):
        return self.__COLUMN_COUNT
    def getRowCount(self):
        return self.__ROW_COUNT
    def getConnectNumber(self):
        return self.__CONNECT_NUMBER
    def getTurnNumber(self):
        return len(self.__BOARD_STRING)
    def getTurn(self):
        return self.__TURN+1

if __name__ == "__main__":
    game = ConnectGame()
    game.runConsoleGame()