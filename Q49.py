# Question number 49:
# Write a program to check whether a number is a perfect number.
n=int(input("Enter any number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if(n==sum):
    print(n,"is a perfect number.")
else:
     print(n,"is not a perfect number.")
