# Question number 48:
# Write a program to display all Armstrong numbers from 1 to n.
n=int(input("Enter any number:"))
for i in range(1,n+1):
    digit=0
    digits=0
    total=0
    bc=i
    while bc>0:
     digit=bc%10
     bc=bc//10
     digits+=1

    bc1=i
    while bc1>0:
         digit=bc1%10
         cube=digit**digits
         total=total+cube
         bc1=bc1//10
    if total==i:
       print(i)