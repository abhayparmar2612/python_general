#exercise 1: user will input (3 ages). I have to write a programm to find the
#oldest one.

user1 = int(input("Enter your age"))
user2 = int(input("Enter your age"))
user3 = int(input("Enter your age"))

max_age = user1
if max_age < user2:
    max_age = user2
if max_age < user3:
    max_age = user3
else:
    pass
print("Max age is ", max_age)
    
