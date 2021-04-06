import ConnectGame as CG
import ConnectGameAI as CGAI


class ConnectGameWithConsole:
    def __init__(self, row_count=6, column_count=7, connect_number=4):
        self.__GAME = CG.ConnectGame(row_count, column_count, connect_number)
        self.__ROBOT = None

    def runConsoleGame(self):
        withRobot = input("With AI (y/n):")
        if withRobot == "y":
            self.__GAME.setSecondPlayerRobot()
            self.__ROBOT = CGAI.ConnectGameAI("", 1)
        initBoard = input("Init Board? (y/n):")
        if initBoard == "y":
            initBoardStr = input("String based 0 for init:")
            result = self.__GAME.initBoard(initBoardStr)
            if self.__GAME.isGameOver():
                self.__GAME.printBoard()
                print("PLAYER "+str(result[0])+" WINS!",
                      "WINING MOVE : ", result[1], "REMAIN : ", result[2])
            else:
                if self.__ROBOT is not None:
                    self.__ROBOT.setBoard(self.__GAME.getBoardString())
                self.__GAME.printBoard()
        while not self.__GAME.isGameOver():
            # Ask Player n input
            selected_col = int(input("Player " +
                                     str(self.__GAME.getTurn()) +
                                     " Make your Selection (0-" +
                                     str(self.__GAME.getColumnCount()-1)+"):"))
            result = self.__GAME.tryDropPiece(selected_col)
            self.__GAME.printBoard()
            if result:
                winner = self.__GAME.concludePlay()
                if winner != 0:
                    print("PLAYER "+str(winner)+" WINS!")
                else:
                    # ROBOT'S TURN
                    if self.__ROBOT is not None:
                        self.__ROBOT.setBoard(self.__GAME.getBoardString())
                        move = self.__ROBOT.makeMove()
                        self.__GAME.tryDropPiece(move)
                        self.__GAME.printBoard()
                        winner = self.__GAME.concludePlay()
                        if winner != 0:
                            print("PLAYER "+str(winner)+" WINS!")

            else:
                print("Invalid input")


if __name__ == "__main__":
    game = ConnectGameWithConsole()
    game.runConsoleGame()
