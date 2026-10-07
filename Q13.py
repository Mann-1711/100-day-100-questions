# Question number 13:
# Write a program to read three numbers and find the largest among them.
a=int(input("Enter one number:"))
b=int(input("Enter seecomd number:"))
c=int(input("Enter third number:"))
if(a>b and a>c):
    print("A is the largest number.")
elif(b>a and b>c):
    print("B is the largest number.")
elif(c>a and c>a):
    print("C is the largest number.")
elif(a==b and b==c):
    print("All the numbers are equal")