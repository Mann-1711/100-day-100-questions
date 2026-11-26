# Question number 63:
#  Write a program to print a right-angled triangle pattern of stars of height n.
n=int(input("Enter any number:"))
for i in range(1,n+1):
   for a in range(1,i+1):
      print("*",end="")
   print()
