import random
lower=int(input("enter lower no.: "))
higher=int(input("enter higher no.:"))
x=random.randint(lower,higher)
count=0
while(True):
    count+=1
    print("guess the number: ")
    a=int(input())
    if(a>x):
        print("you guessed too high!")
    elif(a<x):
        print("you guessed too low!")
    else:
        print("you guessed the correct number!\nThe number is "+str(a))
        print("number of counts needed="+str(count))
        break