#Question number 14:
# Write a program to read three numbers and find the smallest among them.
a=float(input("enter one number:"))
b=float(input("enter second number:"))
c=float(input("enter thrd number:"))
if(a<b and a<c):
    print("a  is the smallest number")
elif(b<a and b<c):
    print("b is the smallest number")
elif(c<a and c<b):
    print("c is the smallest number")
elif(a==b and  b==c):
    print("all the numbers are equal")