# Question number 47:
# Write a program to check whether a number is an Armstrong number.
n=int(input("Enter any number:"))
n=abs(n)
total=0
digits=0
digit=0
bc=n
while bc>0:
    digit=bc%10
    bc=bc//10
    digits+=1
bc1=n
while bc1>0:
    digit=bc1%10
    cube=digit**digits
    total=total+cube
    bc1=bc1//10
if total==n:
    print(n,"is an Armstrong number.")
else:
    print(n,"is not an Armstrong number.")
