# Question number 39:
# Write a program to find the smallest digit in a number n.
n=int(input("Enter any number:"))
n=abs(n)
smallest=9
bc=n
digit=0
while bc>0:
    digit=bc%10
    bc=bc//10
    if digit<smallest:
        smallest=digit
print("The smallest digit in a number n:",smallest)