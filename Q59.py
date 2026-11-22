# Question number 59:
# Write a program to find the sum of the series 1 + 2 + 3 + ... + n.
n=int(input("Enter any number:"))
n=abs(n)
if n==0:
    print(0)
else:
 total=0
 for i in range(1,n+1):
    total=total+i
 print(total)