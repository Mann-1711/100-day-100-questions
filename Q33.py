# Question number 33:
# Write a program to count the number of digits in a number n.
n=int(input("Enter anhy number:"))
c=0
if(n==0):
    c==1
else:
    n=abs(n)
    while n>0:
        n=n//10
        c+=1
print(c)