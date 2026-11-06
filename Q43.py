# Question number 43:
# Write a program to find the sum of the first and last digit of a number n.
n=int(input("entrer any number:"))
n=abs(n)
bc=n
first=bc%10
while bc>10:
    bc=bc//10
last=bc
sum=first+last
print("First number:",first)
print("Last number:",last)
print("Sum:",sum)