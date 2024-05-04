def test1(a,b): 
        print(a,b)
test1(65,34)
test1("abhay", 45)
def test2(a):
        print(a)
test2("parmar") 
print(type(test2("abhay")))

# print always return none-type.

def test3(a):
        return a
test3("abhay")
print(type(test3("abhay")))
c =test3("bahay")+ "parmar"
print(c)


def test4(a,b,c):
        return a,b,c
d =test4(56,34,98)
print(d)
e =type(d)
print(e)

n = 10,20, 30, "gaur"
print(n)

def test5(a ="sudh",b=2343):
        return a,b
f =test5("abhay")
print(f)
def test6(l):
        """ this function will take list as function"""
        for i in l:
                print(i)

test6(["apple","banana","cherry"])
# test6()
def test7(a,b,c,d):
        return a,b,c,d
t =test7(45,3,87,34)
print(t)
def test8(*args):
        return args
a =test8(0)
b =test8(8)
print(a,b)
def test9(*abhay):
        return abhay
d =test9(45,674,23434,645,98)
print(d)
def test10(*args, email_id="abnljfsds"):
        return args,email_id
e =test10(34,23,54,8923,23)
print(e)

def test11(*args, emial_id):
        return args,emial_id
f =test11(33,34,87,76,56, emial_id="anifh")
print(f)
def test12(**kwargs):
        return kwargs

g=test12(name="abha",fname="gurlj",lname="tihih")
print(g)

# lambda function: without naming 
n = lambda a , b :a + b
m =n(3,6)
print(m)
s = lambda a:a**76
print(s(2))

# def test13():
#         number = int(input("user input :"))
#         remainder = number % 2
#         if (remainder == 0):
#                 print(" number is even")
#         else:
#                 print("number is odd")        
# test13()


# function for all operations:
# n1 = int(input("first number"))
# n2= int(input("second number"))


# def test14(n1,n2):
#         sum = n1 + n2
#         sub = n1 - n2
#         multi = n1 * n2
#         division = n1 / n2
#         return sum, sub, multi, division
# final= test14(n1,n2)
# print(final)

# Package count functions:
# n3 = int(input("first salary"))

# def test15(n3):
#         return 12 * n3
# y = test15(n3)
# print(y)

# birthday guesser:
n6 = int(input("enter your birthmonth"))
n7 = int(input("enter your birthday"))
n8 = int(input("enter your birthyear"))

def test16(n6,n7,n8):
        return n7-n6-n8
u = test16(n6,n7,n8)
print(u)
# faulty code
