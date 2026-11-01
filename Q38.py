# Question number 38:
# Write a program to find the largest digit in a number n.
n=int(input("Enter any number:"))
n=abs(n)
bc=n
largest=0
while(bc>0):
    digit=bc%10
    bc=bc//10
    if digit>largest:
        largest=digit
        print("The largest number of n is:",largest)
    
    