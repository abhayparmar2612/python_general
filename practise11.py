import random

jackpot = random.randint(1,100)

guessed_number = int(input("Guess the number between 1 to 100"))
counter = 1

while jackpot != guessed_number:
    if jackpot < guessed_number:
        print("guess lower")

    else:
        print("guess higher")
    guessed_number = int(input("Guess the number between 1 to 100"))
    counter += 1
print("you guessed right, and took",counter," attempts")
    
