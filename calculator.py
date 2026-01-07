print("Welcome to my calculator")

x=float(input("Enter your First Number : "))
comp=input("Enter (*/-+%)")
y=float(input("Enter your Second Number : "))


if comp=="+" :
    result=x+y 
    print(x ,"+",y,"=",result) 

elif comp=="-" :
    result=x- y 
    print(x ,"-",y,"=",result) 

elif comp=="*" :
    result=x *y 
    print( x ,"*",y,"=",result ) 

elif comp=="/" :

    if y==0 :
        print("Can't Solve")

    else :

        result=x/y 
        print(x ,"/",y,"=",result )        



