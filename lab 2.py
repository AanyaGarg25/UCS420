#LAB 2 - ASSIGNMENT 6 + 7 + 8

# Assignment 6

def add(a,b):
    c=a+b
    return c

print("Adding 10, 20 = ", add(10,20))
print("Adding 20, 50 = ", add(20,50))
print("Adding 80, 20 = ", add(80,20))

def Isprime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1


n= int(input("enter a number"))
if Isprime(n):
    print("the number is prime number")
else :
    print("the number is not a  prime number")

def addn(n):
    sum = 0
    for i in range (1,n+1):
        sum+=i
    return sum

n=int(input("enter a number : "))
print("sum till n is : ", addn(n))

# assignment 6.1
def Oddsum(n):
    sum=0
    for i in range(1,n+1):
        if i%2==1:
            sum+=i
    return sum

n=int(input("enter a number : "))
print("sum till n is : ", Oddsum(n))

# assignmnet 6.2
def primesum(n):
    total = 0

    for i in range(2, n + 1):
        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break

        if prime:
            total += i

    return total

n = int(input("Enter a number: "))
print(primesum(n))

#assignment 7
import math as m 
print("exponent : ", m.exp(-200))
print("log : ",m.log(100,2))
print("cos ", m.cos(30))
print("sin ",m.sin(30))
print("tan ",m.tan(30))
print("square root" , m.sqrt(25))
print("ceil", m.ceil(89.9))
print("floor ", m.floor(89.9))

#assignment 8 string
#8.1
string='hello world'
print("string : ",string)
print("first letter ", string[0])
print("left words",string[1:5])
print(" string[:-5] ", string[:-5])

#8.2
string = "Im done"
print("strign is : ", string)
print("length of teh string is : ",len(string))
print("upper case of the string : ",string.upper())
print("lower case of the string : ",string.lower())

#8.3
name=input("enter a name : ")
age= int(input("enter age :  "))
price = float(input("enter the salary: "))
s="\n your name is %s, age is %d and book price is %f"%(name.upper(),age,price)
print(s)

# 8.5
var = "   Hello  World!  "
print("string ---> ",var)
print("Length --->",len(var))
print("var strip --->",var.strip())
print("length of var of strip --->", len(var.strip()))

#8.6
var="    hello, ,world!  "
print("String : ", var)
print("length ", len(var))
print("var split ",var.split())
print("var split ", var.split(" "))
print("var split ",var.split(","))

#8.7
var = " indian army "
print("String : ",var)
print("count of ' ' ", var.count(' '))
print("count of 'a' ", var.count('a'))
print("coutn of 'an' ",var.count('an'))

#8.8
var="Indian army"
print ("String    --> ", var)
print ("var[::1]  --> ", var[::1])
print ("var[::2]  --> ", var[::2])
print ("var[::-1] --> ", var[::-1])
print ("var[::-2] --> ", var[::-2])





