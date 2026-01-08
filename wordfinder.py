while True:
    sentence=input("Enter your sentence : ").split()
    choice=input("enter the word you want to search : ")

    if choice in sentence :
        print(f"the word you picked '{choice}' exists")
    else: 
        print("you picked wrong!!!try again")
    
    if input("do you want to quit ?") == "y":
        quit()

    
