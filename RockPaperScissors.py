print("Welcome to Rock Paper Scissors")

x=["Rock","Paper","Scissors"]


player1=input("Choose Rock Paper Scissors : ")
player2=input("Choose Rock Paper Scissors : ")


if player2==x[0] and player1==x[1] :
    print("Player 1 win")

elif player2==x[1] and player1==x[0] :
    print("Player 2 win")

elif player2==x[2] and player1==x[0] :
    print("Player 1 win")


elif player2==x[0] and player1==x[2] :
    print("Player 2 win")


elif player2==x[2] and player1==x[1] :
    print("Player 2 win")

elif player2==x[1] and player1==x[2] :
    print("Player 1 win")



else : 
    print("Please Choose Rock Paper Scissors")