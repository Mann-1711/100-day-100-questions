# Questtion 56:
# Write a program to find the LCM of two numbers.
n1=int(input("Enter any number:"))
n2=int(input("Enter any other number:"))
count1=[]
count2=[]
common=[]
if n1==0 and n2==0:
   print("lcm is undefined")
elif n1==0 or n2==0:
   print("lcm is 0")
else:
 for i in range(1,n1+1):
    if n1%i==0:
      count1.append(i)
 for i in range(1,n2+1):
   if n2%i==0:
      count2.append(i)
 for i in range(1,n1+1):
   if i in count1 and i in count2:
      common.append(i)
 ans=max(common)
 lcm=(n1*n2)//ans
 print(lcm)