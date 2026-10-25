# Question number 31:
# Write a program to count how many numbers from 1 to n are divisible by 3.
n=int(input("enter any number:"))
m=0
for i in range(1,n+1):
    if(i%3==0):
        m+=1
print("Total numbers from 1 to n are divisible by 3:",m)