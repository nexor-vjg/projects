# Printing The Game Board
# Take Player input
# Check for Win or Tie
# switch the player 
#check for win or tie again 
print("Welcome to TicTacToe")

board = ["-", "-" , "-", 
         "-", "-" , "-",
         "-", "-" , "-"]


CurrentPlayer="X"
winner=True
Gamerunning= True 


def printboard(board) :
    print(board[0] ," | ", board[1] ," | ", board[2])
    print(board[3] ," | ", board[4] ," | ", board[5])
    print(board[6] ," | ", board[7] ," | ", board[8])



def PlayerInput(board) :
    inp = int(input("Enter a number 1-9 : "))

    #the most important code
    if inp >= 1 and inp <= 9 and board[inp-1] == "-" :
        board[inp-1]=CurrentPlayer

    else :
        print("Oops Try Again")


def horizontal(board) :
    global winner    
    if board[0] ==board[1] == board[2] and board[0] != "-"  : 
        winner=board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-" :
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6] != "-" :
        winner=board[6]
        return True 
    
def checkColumn(board) :
    global winner 
    if board[0] == board[3] == board[6] and board [0] != "-" :
        winner = board[0] 
        return True 
    
    elif board[1] == board[4] == board[7] and board [1] != "-" :
        winner=board[1]
        return True
    
    elif board[2] == board[5] == board[8] and board [2] != "-" :
        winner=board[2]
        return True 
    

def Diagonalcheck(board) :
    global winner 

    if board[0]==board[4]==board[8] and board[0] != "-" :
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6]  and board[2] != "-":
        winner=board[2]
        return True 
    

def Tie(board):
    if "-" not in board :
        printboard(board)

        print("Tie!!!!") 

        Gamerunning=False


def Win() :
    if checkColumn(board) or Diagonalcheck(board) or horizontal(board) :
        print(f"the winner is {winner}")


def switchplayer():
    global CurrentPlayer 
    if CurrentPlayer =="X" :
        CurrentPlayer="O"        
    else :
        CurrentPlayer="X" 


while Gamerunning :
    printboard(board)
    PlayerInput(board)
    if Win(board) :
        break

    if Tie(board) :
        break
    switchplayer(board)

