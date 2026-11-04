# Question number 41:
# Write a program to check whether a number n is a palindrome (reads the same reversed).
n=int(input("Enter any number:"))
n=abs(n)
rev=0
bc=n
while bc>0:
    digit=bc%10
    rev=rev*10+digit
    bc=bc//10
print(rev)
if rev==n:
    print("This number is palindrome.")
else:
    print("This number is not a palindrome.")