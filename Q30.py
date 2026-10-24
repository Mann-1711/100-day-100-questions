# Question number 30:
# Write a program to display all multiples of a number m up to n terms.
m=int(input("Enter any number:"))
n=int(input("Enter upto which number you want your multiplication:"))
for i in range(1,n+1):
    print(m,"x",i,"=",m*i)