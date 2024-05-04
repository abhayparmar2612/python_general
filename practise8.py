#13) wrute a programe that will tell whether the given no is divided by 3 and 6;
#14) write a programe that take three digits number and print the square of digits.


#13) by myself

number = int(input("Enter any number"))

a = number % 3
b = number % 6

if (a==0 and b==0):
    print("Number can be divisible by 3 & 6")
else:
    print("sorry this is not possible")



    
#14(by myself)
n = int(input("Enter number : ")) # 567

a = n % 10 #(7)
n = n // 10 #(56)
b = n % 10 # (6)
c = n // 10 # (5)

print(pow(c,2),end=" ")
print(pow(b,2),end=" ")
print(pow(a,2))



