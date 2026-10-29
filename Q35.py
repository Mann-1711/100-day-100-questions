# Question number 35:
# Write a program to find the sum of all digits of a number n.
n=int(input("enter any number:"))
bc=n
sum=0
if(n==0):
    print(0)
else:
   while bc>0:
    ans=bc%10
    bc=bc//10
    sum=sum+ans
   print("the sum of all digits of a number n:",sum)