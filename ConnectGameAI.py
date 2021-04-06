import ConnectGame as CG
import numpy
import operator


class Eval:
    @staticmethod
    def evalArray(array, turn):
        evaluation = 0
        other = int((turn + 1) % 2 + 1)
        turn = turn + 1
        unique, counts = numpy.unique(numpy.array(array), return_counts=True)
        evalDict = dict(zip(unique, counts))
        turnEval = evalDict.get(turn) or 0
        otherEval = evalDict.get(other) or 0
        evaluation += 2*turnEval + -(2*otherEval)
        return evaluation


class ConnectGameAI:
    def __init__(self, board_string, turn=0, depth=3, row_count=6, column_count=7,
                 connect_number=4):
        self.__ROW_COUNT = row_count
        self.__COLUMN_COUNT = column_count
        self.__CONNECT_NUMBER = connect_number
        self.__GAME_OVER = False
        self.__TURN = turn
        self.__DEPTH = depth
        self.__BOARD = CG.ConnectGame()
        self.__BOARD.initBoard(board_string)
        self.__BOARD_STRING = self.__BOARD.getBoardString()

    def setBoard(self, board_string):
        self.__BOARD = CG.ConnectGame()
        self.__BOARD.initBoard(board_string)
        self.__BOARD_STRING = self.__BOARD.getBoardString()

    def getNextPossibleMove(self, board_string):
        subBoard = CG.ConnectGame()
        result = subBoard.initBoard(board_string)
        if subBoard.isGameOver():
            return [True, result[0]]
        else:
            possibleMoves = []
            for c in range(self.__COLUMN_COUNT):
                if subBoard.isValidLocation(c):
                    possibleMoves.append(c)
            return [False, possibleMoves]

    def getBestMove(self, board_string, possibleMoves, turn, depth_limit=3, depth=1):
        results = []
        for i, c in enumerate(possibleMoves):
            if depth < depth_limit:
                result = self.getNextPossibleMove(board_string+str(c))
                if not result[0]:
                    results.append(self.getBestMove(board_string+str(c),
                                                    result[1], (turn+1) % 2, depth_limit, depth+1))
            else:
                results.append(self.evaluator(board_string+str(c), self.__TURN))
        evalDict = dict(zip(possibleMoves, results))
        if self.__TURN == turn:
            choice = max(evalDict.items(), key=operator.itemgetter(1))[0]
        else:
            choice = min(evalDict.items(), key=operator.itemgetter(1))[0]
        if depth != 1:
            return evalDict.get(choice)
        else:
            return choice

    def evaluator(self, board_string, turn):
        state = CG.ConnectGame()
        state.initBoard(board_string)
        arrays = state.getArraysForWinningMove()
        evaluate = 0
        for i, x in enumerate(arrays):
            evaluate += Eval.evalArray(x[1], turn)
        return evaluate

    def makeMove(self):
        result = self.getNextPossibleMove(self.__BOARD_STRING)
        if not result[0]:
            return self.getBestMove(self.__BOARD_STRING, result[1], self.__TURN, self.__DEPTH)
        return None
