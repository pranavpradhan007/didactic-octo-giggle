"""
In this game, there is a list of words present, out of which our interpreter will choose 1 random word.
The user first has to input their names and then, will be asked to guess any alphabet.
If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet.
The user will be given 12 turns(which can be changed accordingly) to guess the complete word.
"""


import random
name=input("what is your name?\n")
print("Hello! "+name+" Best of luck!")
words=['guerrilla','set','manual','sink','sensation','uncertainty','close']
word=random.choice(words)
print("guess the word ")
guesses=''
count=12
while(count>0):
    failed=0    
   
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed+=1
    if failed==0:
        print("yayyyyy you won!!")
        print("the word is "+word)
        break
    print()
    guess=input("guess a character: ")
    guesses+=guess
    if guess not in word:
        count-=1
        print("wrong")
        print("you have ", +count," more guesses")
    if count==0:
        print("you lose")
