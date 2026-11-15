# Question number 52:
# Write a program to check whether a number is a Harshad (Niven) number.
n=int(input("Enter any number:"))
n=abs(n)
bc=n
sum=0
while bc>0:
    digit=bc%10
    sum=sum+digit
    bc=bc//10
if n%sum==0:
    print(n,"is a Harshad (Niven) number.")
else:
    print(n,"is not a Harshad (Niven) number.")
