# Question number 36:
# Write a program to find the product of all digits of a number n.
n=int(input("Enter any number:"))
n=abs(n)
bc=n
pro=1
if(n==0):
    print(0)
else:
    while(bc>0):
        ans=bc%10
        bc=bc//10
        pro=pro*ans
    print(pro)