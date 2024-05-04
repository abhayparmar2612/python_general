#Write a program that will reverse a four digits numbers.also check whether
#the reverse is true.

num= int(input("Enter four digit number"))

#5678
a = num % 10 #(8)
num = num // 10 #(567)
b = num % 10 #(7)
num = num // 10#(56)
c = num % 10 #(6)
d = num // 10#(5)
#e = (a , b , c ,d)
print(a,b,c,d)
print(num == (a,b,c,d))
