# Question number 46:
# Write a program to display the first n prime numbers.
n=int(input("Enter any number:"))
num=2
count=0
while count<n:
    is_prime=True
    for  i in range (2,n):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
            print(num)
            count+=1
    num+=1