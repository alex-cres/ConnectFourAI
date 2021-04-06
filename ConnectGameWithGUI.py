import sys
import ConnectGame as CG
import pygame
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class ConnectGameWithGUI:
    def __init__(self, playerColors=[RED, YELLOW], boardColor=BLUE, row_count=6, column_count=7,
                 connect_number=4):
        pygame.init()
        self.__FONT = pygame.font.SysFont("monospace", 75)
        self.backGroundColor = BLACK
        self.playerColors = playerColors
        self.boardColor = boardColor
        self.__COLOR_PALETTE = [self.backGroundColor]
        self.__COLOR_PALETTE += playerColors
        self.__ROW_COUNT = row_count
        self.__COLUMN_COUNT = column_count
        self.__CONNECT_NUMBER = connect_number
        self.__SQUARESIZE = 100
        self.__RADIUS = int(self.__SQUARESIZE/2 - 5)
        self.__WIDTH = self.__COLUMN_COUNT * self.__SQUARESIZE
        self.__HEIGHT = (self.__ROW_COUNT+1) * self.__SQUARESIZE
        self.__SIZE = (self.__WIDTH, self.__HEIGHT)
        self.__SCREEN = pygame.display.set_mode(self.__SIZE)
        self.__GAME = CG.ConnectGame(row_count, column_count, connect_number)
        self.__EXIT = False

    def renderText(self, text, color):
        self.__SCREEN.blit(self.__FONT.render(text, 1, color), (40, 10))

    def getColFromClickedPos(self, posx):
        return int(math.floor(posx / self.__SQUARESIZE))

    def drawBoard(self):
        board = self.__GAME.getFlippedBoard()
        ss = self.__SQUARESIZE
        cp = self.__COLOR_PALETTE
        rad = self.__RADIUS
        for c in range(self.__COLUMN_COUNT):
            for r in range(self.__ROW_COUNT):
                pygame.draw.rect(self.__SCREEN, self.boardColor, (c*ss, (r+1) * ss, ss, ss))
                pygame.draw.circle(self.__SCREEN, cp[int(board[r][c])],
                                   (int(c*ss + ss/2), int((r+1.5)*ss)), rad)
            pygame.display.update()

    def runGUIGame(self):
        self.drawBoard()
        while not self.__EXIT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__EXIT = True
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.__SCREEN, BLACK, (0, 0, self.__WIDTH, self.__SQUARESIZE))
                    posx = event.pos[0]
                    turn = self.__GAME.getZeroBasedTurn()
                    pygame.draw.circle(self.__SCREEN, self.playerColors[turn],
                                       (posx, int(self.__SQUARESIZE/2)), self.__RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    selected_col = self.getColFromClickedPos(event.pos[0])
                    result = self.__GAME.tryDropPiece(selected_col)
                    # print(self.__GAME.getFlippedBoard(), self.__GAME.getBoardString())
                    self.drawBoard()

                    if result:
                        winner = self.__GAME.concludePlay()
                        if winner != 0:
                            self.__EXIT = True
                            pygame.draw.rect(self.__SCREEN, BLACK,
                                             (0, 0, self.__WIDTH, self.__SQUARESIZE))
                            self.renderText("PLAYER "+str(winner) + " WINS!",
                                            self.__COLOR_PALETTE[winner])
                            pygame.display.update()
                            pygame.time.wait(3000)

                    else:
                        print("Invalid input")


if __name__ == "__main__":
    game = ConnectGameWithGUI()
    game.runGUIGame()
