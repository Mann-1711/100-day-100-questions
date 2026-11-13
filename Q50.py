# Question number 50:
# Write a program to check whether a number is a strong number (sum of factorials of its digits).
n=int(input("Enter any number:"))
bc=n
sum=0
while bc>0:
    digit=bc%10
    fact=1
    for i in range(1,digit+1):
     fact=fact*i
    sum=sum+fact
    bc=bc//10
if(sum==n):
   print(n,"is a strong number.")
else:
   print(n,"is not a strong number.")