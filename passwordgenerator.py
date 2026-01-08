import random
import string

length=int(input("Enter the length :"))

comp=string.ascii_letters
comp+=string.digits
comp+=string.punctuation 

password=""

for i in range (length):
    generate= random.choice(comp)
    password+=generate


print("The Password is : ", password)
