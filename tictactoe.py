def sum(x,y,z):
    return x+y+z
def printboard(xTurn,oTurn):
    zero='X' if xTurn[0] else('O' if oTurn[0] else 0)
    one='X' if xTurn[1] else('O' if oTurn[1] else 1)
    two='X' if xTurn[2] else('O' if oTurn[2] else 2)
    three='X' if xTurn[3] else('O' if oTurn[3]else 3)
    four='X' if xTurn[4] else('O' if oTurn[4] else 4)
    five='X' if xTurn[5] else('O' if oTurn[5] else 5)
    six='X' if xTurn[6] else('O' if oTurn[6] else 6)
    seven='X' if xTurn[7] else('O' if oTurn[7] else 7)
    eight='X' if xTurn[8] else('O' if oTurn[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("__|___|___")
    print(f"{three} | {four} | {five}")
    print("__|___|___")
    print(f"{six} | {seven} | {eight}")
def checkwin(xTurn,oTurn):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xTurn[win[0]],xTurn[win[1]],xTurn[win[2]])==3):
            print("X wins the game")
            return 1
        if(sum(oTurn[win[0]],oTurn[win[1]],oTurn[win[2]])==3):
            print("O wins the game")
            return 0
    return -1
if __name__=="__main__":
    print("welcome to tic-tac-toe game")
    xTurn=[0,0,0,0,0,0,0,0,0]
    oTurn=[0,0,0,0,0,0,0,0,0]
    turn=1
    while(True):
        printboard(xTurn,oTurn)
        if(turn==1):
            print("X's turn")
            choice=int(input("enter a value:"))
            xTurn[choice]=1
        elif(turn==0):
            print("O's turn")
            choice=int(input("enter a value:"))
            oTurn[choice]=1
        win=checkwin(xTurn,oTurn)
        if(win!=-1):
            printboard(xTurn,oTurn)
            print("Game Over")
            break
        turn = 1-turn