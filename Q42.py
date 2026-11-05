# Question number 42:
# Write a program to replace all zeros in a number n with the digit 5.
n=int(input("enter any number:"))
n=abs(n)
rev=0
bc=n
while bc>0:
    digit=bc%10
    if(digit==0):
        digit=5
    rev=rev*10+digit
    bc=bc//10
while rev>0:
    digit=rev%10
    print(digit,end="")
    rev=rev//10
