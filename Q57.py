# Question number 57:
# Write a program to display the first n terms of the Fibonacci series.
n=int(input("enter number of terms:"))
a=0
b=1
c=0
for i in range (1,n+1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
