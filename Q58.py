# Question number 58:
# Write a program to find the sum of the first n terms of the Fibonacci series.
n=int(input("Enter any number:"))
a=0
b=1
c=0
sum=0
for i in range(n):
    sum=sum+a
    c=a+b
    a=b
    b=c
print("the sum of the first",n,"terms of the Fibonacci series is :",sum)