# 4.Write a program that will give you the sum of three digits.
# 
# 
# 

#4)my technique:


a = input("Enter any containing atleast 3 number")
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = b + c + d
print(e)
#4) youtube :

num = int(input("Enter three digits number"))

a = num % 10# suppose no. is 456 (456 % 10= 6)
num = num // 10 #(456 // 10 = 45)
b = num % 10#(45 % 10 = 5)
c = num // 10 # 45 // 10 =4)

print(a+b+c)

