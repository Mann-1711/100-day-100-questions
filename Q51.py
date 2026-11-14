# Question number 51:
# Write a program to check whether a number is an automorphic number.
n=int(input("Enter any number:"))
n=abs(n)
bc=n
sq=bc*bc
count=0
last=0
while(bc>0):
    bc=bc//10
    count=count+1
last=sq%(10**count)
print(last)
if(last==n):
    print(n,"is an automorphic number.")
else:
    print(n,"is not an automorphic number.")