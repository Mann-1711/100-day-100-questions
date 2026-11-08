# Question number 45:
# Write a program to display all prime numbers from 1 to n.
n=int(input("Enter any number:"))
for i in range(1,n+1):
    if i%2==0:
      print(i)