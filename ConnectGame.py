"""
ConnectGame
=====

Provides the base for an ConnectGame
"""

import numpy as np


class ConnectGame:
    def __init__(self, row_count=6, column_count=7, connect_number=4):
        self.__ROW_COUNT = row_count
        self.__COLUMN_COUNT = column_count
        self.__CONNECT_NUMBER = connect_number
        self.__GAME_OVER = False
        self.__TURN = 0
        self.__BOARD = self.__createBoard(row_count, column_count)
        self.__BOARD_STRING = ""

    def __killGame(self):
        self.__GAME_OVER = True

    def __nextTurn(self):
        self.__TURN += 1
        self.__TURN = self.__TURN % 2

    def __createBoard(self, height, width):
        board = np.zeros((height, width))
        return board

    def __dropPiece(self, row, col, piece):
        self.__BOARD[row][col] = piece

    def __getNextOpenRow(self, col):
        for row in range(len(self.__BOARD)):
            if self.__BOARD[row][col] == 0:
                return row

    def __getDiagonal(self, subBoard, t=1):
        array = []
        if t == 1:
            for i in range(len(subBoard)):
                array.append(subBoard[i][i])
        else:
            for i in range(len(subBoard)):
                array.append(subBoard[len(subBoard)-1-i][i])
        return array

    def isValidLocation(self, col):
        return self.__BOARD[len(self.__BOARD)-1][col] == 0

    def printBoard(self):
        print(np.flip(self.__BOARD, 0))

    def getBoard(self):
        return self.__BOARD

    def getFlippedBoard(self):
        return np.flip(self.__BOARD, 0)

    def initBoard(self, positionsStr):
        positions = [int(char) for char in positionsStr]
        self.__TURN = 0
        for i, move in enumerate(positions, start=1):
            result = self.tryDropPiece(move)
            if result:
                if self.isWinningMove(self.__TURN+1):
                    self.__killGame()
                    return [self.__TURN+1, i, positions[i:]]
                self.__nextTurn()
        return []

    def isWinningMove(self, piece):
        conNum = self.__CONNECT_NUMBER
        colCount = self.__COLUMN_COUNT
        board = self.__BOARD
        getDiagonal = self.__getDiagonal
        rowCount = self.__ROW_COUNT

        # Horizontal
        for c in range(colCount-(conNum-1)):
            for r in range(rowCount):
                if all(x == piece for x in board[r, c:c+conNum]):
                    return True

        # Vertical
        for c in range(colCount):
            for r in range(rowCount-(conNum-1)):
                if all(x == piece for x in board[r:r+conNum, c]):
                    return True

        # Positive Diagonals
        for c in range(colCount-(conNum-1)):
            for r in range(rowCount-(conNum-1)):
                if all(x == piece for x in getDiagonal(board[r:r+conNum, c:c+conNum], 1)):
                    return True

        # Negative Diagonals
        for c in range(colCount-(conNum-1)):
            for r in range((conNum-1), rowCount):
                if all(x == piece for x in getDiagonal(board[r-(conNum-1):r+1, c:c+conNum], 0)):
                    return True

    def getArraysForWinningMove(self):
        pass

    def tryDropPiece(self, selected_col):
        if self.isValidLocation(selected_col):
            row = self.__getNextOpenRow(selected_col)
            self.__dropPiece(row, selected_col, self.__TURN+1)
            self.__BOARD_STRING = self.__BOARD_STRING+str(selected_col)
            return True
        return False

    def getBoardString(self):
        return self.__BOARD_STRING

    def isGameOver(self):
        return self.__GAME_OVER

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

    def getZeroBasedTurn(self):
        return self.__TURN

    def concludePlay(self):
        """
        Action to call after the turn is finished to verify if anyone won and
        to either end the game or pass to the next turn

        Returns 0 is none won, 1/2 if that player won
        """
        if self.isWinningMove(self.__TURN+1):
            self.__killGame()
            return self.__TURN+1
        self.__nextTurn()
        return 0

    def isFirstPlayerTurn(self):
        return self.__TURN == 0


class ConnectGameAI:
    def __init__(self, board, turn=0, depth=3, row_count=6, column_count=7, connect_number=4):
        self.__ROW_COUNT = row_count
        self.__COLUMN_COUNT = column_count
        self.__CONNECT_NUMBER = connect_number
        self.__GAME_OVER = False
        self.__TURN = turn
        self.__BOARD = board
        self.__BOARD_STRING = board.getBoardString()
        self.__DEPTH = depth

    def getNextPossibleMove(self, board_string):
        subBoard = ConnectGame()
        result = subBoard.initBoard(board_string)
        if subBoard.isGameOver():
            return [True, result[0]]
        else:
            possibleMoves = []
            for c in range(self.__COLUMN_COUNT):
                if subBoard.isValidLocation(c):
                    possibleMoves.append(c)
            return [False, possibleMoves]

    def getBestMove(self, board_string, possibleMoves):
        results = []
        for i, c in enumerate(possibleMoves):
            results.append(c)
            pass

    def analyseBoard(self, board_string, turn, move):
        if turn != self.__TURN:
            pass

    def makeMove(self):
        result = self.getNextPossibleMove(self.__BOARD_STRING)
        if not result[0]:
            bestCol = self.getBestMove(self.__BOARD_STRING, result[1])
            selected_col = result[1][bestCol]
            return selected_col
        return None


if __name__ == "__main__":
    import ConnectGameWithConsole as CGWC
    game = CGWC.ConnectGameWithConsole()
    game.runConsoleGame()
