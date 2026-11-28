# Question number 65:
# Write a program to print a pyramid pattern of stars of height n.
n=int(input("Enter any number:"))
for i in range(1,n+1):
    for a in range(1,(n-i)+1):
         print(" ",end="")
    for b in range(1,(2*i-1)+1):
         print("*",end="")
    print()