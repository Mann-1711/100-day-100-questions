# Question number 19:
# Write a program to read a number and check whether it is divisible by both 3 and 5.
num=float(input("Enter any number:"))
if(num%3==0 and num%5==0):
    print("This number is divisible by both 3 and 5")
else:
    print("This number is not divisible by both 3 and 5")