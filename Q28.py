# Question number 28:
# Write a program to find the product of all natural numbers from 1 to n (factorial of n).
n=int(input("enter any number:"))
total=1
for i in range(1,n+1):
    total=total*i
print("Factorial:",total)
