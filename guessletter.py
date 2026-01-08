import random
import string
while True :

    computer=random.choice(string.ascii_lowercase)
    if str(input("Guess letters from a to z : "))== computer :
        print("You're right! ")
    else :
        print(f"wrong answer , the guess was {computer}")
         
    if input("Do you want to play again ? (y/n)") == "n":
        break
        
