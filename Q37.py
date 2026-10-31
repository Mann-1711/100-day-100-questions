# Question number 37:
# Write a program to reverse a number n.
n=int(input("Enter any number:"))
rev=0
bc=n
if(n==0):
    print("reversed number:",n)
else:
    while(bc>0):
     digit=bc%10
     rev=rev*10+digit
     bc=bc//10
print("Reversed number:",rev)