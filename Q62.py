# Question  number 62:
# Write a program to find the value of x raised to the power y without using inbuilt power.
x=int(input("Enter any number:"))
y=int(input("Enter any exponent:"))
result=1
if y>0:
 for i in range(1,y+1):
    ans=result*x
    result=ans
 print(result)
if y<0:
  y=abs(y)
  for i in range(1,y+1):
    ans=result*x
    result=ans
  result=1/result
  print(result)
if x==0 and y==0:
  print("Udefined result")