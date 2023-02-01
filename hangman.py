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