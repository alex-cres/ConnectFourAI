import sys
import ConnectGame as CG
import pygame
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)



class ConnectGameWithGUI:
    def __init__(self,playerColors=[RED,YELLOW],boardColor=BLUE,row_count=6,column_count=7,connect_number=4):
        pygame.init()
        self.backGroundColor=(0,0,0)
        self.playerColors = playerColors
        self.boardColor = boardColor
        self.__ROW_COUNT = row_count
        self.__COLUMN_COUNT = column_count
        self.__CONNECT_NUMBER = connect_number
        self.__SQUARESIZE = 100
        self.__RADIUS = int(self.__SQUARESIZE/2 - 5)
        self.__WIDTH = self.__COLUMN_COUNT * self.__SQUARESIZE
        self.__HEIGHT = (self.__ROW_COUNT+1) * self.__SQUARESIZE
        self.__SIZE = (self.__WIDTH,self.__HEIGHT)
        self.__SCREEN = pygame.display.set_mode(self.__SIZE)
        self.__GAME = CG.ConnectGame(row_count,column_count,connect_number)
        self.__EXIT = False
    def getColumnFromClickedPosition(self,posx):
        return int(math.floor(posx / self.__SQUARESIZE))
    def drawBoard(self):
        board=self.__GAME.getFlippedBoard()
        for c in range(self.__COLUMN_COUNT):
            for r in range(self.__ROW_COUNT):
                pygame.draw.rect(self.__SCREEN,self.boardColor,(c*self.__SQUARESIZE,r*self.__SQUARESIZE+self.__SQUARESIZE,self.__SQUARESIZE,self.__SQUARESIZE))
                if self.__GAME.getFlippedBoard()[r][c] == 0:
                    pygame.draw.circle(self.__SCREEN,self.backGroundColor,(int(c*self.__SQUARESIZE+self.__SQUARESIZE/2),int(r*self.__SQUARESIZE+self.__SQUARESIZE+self.__SQUARESIZE/2)),self.__RADIUS)
                elif self.__GAME.getFlippedBoard()[r][c] == 1:
                    pygame.draw.circle(self.__SCREEN,self.playerColors[0],(int(c*self.__SQUARESIZE+self.__SQUARESIZE/2),int(r*self.__SQUARESIZE+self.__SQUARESIZE+self.__SQUARESIZE/2)),self.__RADIUS)
                elif self.__GAME.getFlippedBoard()[r][c] == 2:
                    pygame.draw.circle(self.__SCREEN,self.playerColors[1],(int(c*self.__SQUARESIZE+self.__SQUARESIZE/2),int(r*self.__SQUARESIZE+self.__SQUARESIZE+self.__SQUARESIZE/2)),self.__RADIUS)
            pygame.display.update()

    def runGUIGame(self):
        self.drawBoard()
        
        while not self.__EXIT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__EXIT=True
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selected_col = self.getColumnFromClickedPosition(event.pos[0])
                    result = self.__GAME.tryDropPiece(selected_col)
                    print(self.__GAME.getFlippedBoard(),self.__GAME.getBoardString())
                    self.drawBoard()
                    
                    if result: 
                        winner = self.__GAME.concludePlay()
                        if winner != 0:
                            self.__EXIT=True
                            "PLAYER WINS!"
                    else:
                        print("Invalid input")



if __name__ == "__main__":
    game = ConnectGameWithGUI()
    game.runGUIGame()


