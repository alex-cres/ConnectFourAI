import ConnectGame as CG

class TestingBoard:
    def __init__(self,number,testMatrix):
        game=CG.ConnectGame()
        result = game.initBoard(testMatrix[3])
        if game.isGameOver():
            if result[0]!=testMatrix[0] or result[1]!=testMatrix[1] or "".join(str(i) for i in result[2])!=testMatrix[2]:
                print("Test #",str(number),"failed - ",result," - ",testMatrix)
            else:
                print("Test #",str(number),"passed - ",result," - ",testMatrix)
        else:
            if(testMatrix[0]==0):
                print("Test #",str(number),"passed - ",result," - ",testMatrix)
            else:
                print("Test #",str(number),"failed - ",result," - ",testMatrix)

if __name__ == "__main__":
    testingMatrixes=[#winner - 0/1/2,turn 1-based(if winner 0, put 0), remaining string positions, test string   
#        [1,7,"","0011223"],
#        [1,7,"34455","001122334455"],
#        [1,7,"","1122334"],
#        [1,7,"","2233445"],
#        [1,7,"","3344556"],
#        [0,0,"","001122"],
        [0,0,"","001222222110"]

    ]

    for index,item in enumerate(testingMatrixes):
        TestingBoard(index,item)