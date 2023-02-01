"""
If the User inputs range, let’s say from 1 to 100. And compiler randomly selected 42 as the integer.
And now the guessing game started, so the user entered 50 as his/her first guess. 
The compiler shows “Try Again! You guessed too high”. That’s mean the random number (i.e., 42) doesn’t fall in the range from 50 to 100. 
That’s the importance of guessing half of the range. And again, the user guesses half of 50 (Could you tell me why?). So the half of 50 is 25. 
The user enters 25 as his/her second guess. This time compiler will show, “Try Again! You guessed too small”.
That’s mean the integers less than 25 (from 1 to 25) are useless to be guessed.
Now the range for user guessing is shorter, i.e., from 25 to 50. 
Intelligently! The user guessed half of this range, so that, user guessed 37 as his/her third guess.
This time again the compiler shows the output, “Try Again! You guessed too small”. For the user, the guessing range is getting smaller by each guess.
Now, the guessing range for user is from 37 to 50, for which the user guessed 43 as his/her fourth guess. 
This time the compiler will show an output “Try Again! You guessed too high”. 
So, the new guessing range for users will be from 37 to 43, again for which the user guessed the half of this range, that is, 40 as his/her fifth guess. 
This time the compiler shows the output, “Try Again! You guessed too small”. Leaving the guess even smaller such that from 41 to 43. 
And now the user guessed 41 as his/her sixth guess. Which is wrong and shows output “Try Again! You guessed too small”.
And finally, the User Guessed the right number which is 42 as his/her seventh guess.
Total Number of Guesses = 7
"""


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
