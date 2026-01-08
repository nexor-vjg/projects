import random
numbers=['1','2','3','4','5']

while True :
    if input("Guess Numbers from 1 to 5 : ")==random.choice(numbers):
        print("You're right")
    else :
        print("wrong answer") 
    if input("Do you want to play again ? (y/n)") == "n":
        break 
        
