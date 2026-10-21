# Questtion number 27:
# Write a program to find the sum of all odd numbers from 1 to n.
n=int(input("Enter any number:"))
total=0
for i in range(1,n+1):
    if(i%2!=0):
        total=total+i
print(total)