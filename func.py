def is_even(number):
    if type(number) == int:
        if number % 2 == 0:
            return "even"
        else:
            return "odd"
    else:
        print("Not allowed text")
        
# parameter : expect
# argument  : 1) Default, 2) positional, 3) Keyword  ,4)arbiraty

