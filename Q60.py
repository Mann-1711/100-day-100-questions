# Question number 60:
# Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.
n=int(input("Enter any number:"))
total=0
for i in range(1,n+1):
    square=i**2
    total=total+square
print(total)