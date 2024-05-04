#6.write a program that will tell whether the number enter by user is odd or
#   even



#7. write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter year"))

b = year % 4

if b == 0:
    print("leap year")
if b != 0:
    print("Normal year")

else:
    pass
