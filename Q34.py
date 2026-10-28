# Question number 34:
# Write a program to display all the digits of a number n (one per line).
n=int(input("enter any number:"))
n=abs(n)
reverse=0
temp=n
while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
if(n==0):
    print(0)
else:
    while reverse>0:
        digit=reverse%10
        print(digit)
        reverse=reverse//10