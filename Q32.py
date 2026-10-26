# Question number 32:
# Write a program to display all numbers from 1 to n that are divisible by 3 or 5.
n=int(input("Enter any number:"))
total=0
for i in range(1,n+1):
    if(i%3==0 or i%5==0):
        total+=1
print("The total numbers from 1 to n that are divisible by 3 or 5:",total)