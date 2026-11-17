# Question number 54:
# Write a program to count the number of factors of a number n.
n=int(input("Enter any number:"))
count=0
sum=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
print("The total number of factors of a number n:",count)