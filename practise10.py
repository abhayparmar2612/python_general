# making the guess ing game..

import random
Jackpot = random.randint(1,50)

Guessed = int(input("Guess the number"))
counter = 1


while Jackpot != Guessed:
   
    if Jackpot > Guessed:
        print("guess higher")
    else:
        print("guess lower")
    Guessed = int(input("Guess the number"))
    counter += 1
    
    
    
print("sahi jawab")
print("you took ", counter, "attempts")
    

