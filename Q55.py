# Question number 53:
#  Write a program to find the GCD (HCF) of two numbers.
n1=int(input("enter any number:"))
n2=int(input("enter any other number:"))
count1=[]
count2=[]
common=[]
for i in range(1,n1+1):
    if n1%i==0:
      count1.append(i)
for i in range(1,n2+1):
   if n2%i==0:
      count2.append(i)
print("common factors of",n1,":",count1)
print("common factors of",n2,":",count2)
for i in range(1,n1+1):
   if i in count1 and i in count2:
      common.append(i)
print("common factors of",n1,"&",n2,":",common)
ans=max(common)
print("The GCD (HCF) of two numbers",n1,"&",n2,"is:",ans)
