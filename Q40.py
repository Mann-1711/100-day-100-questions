# Question number 40:
# Write a program to count the number of even digits and odd digits in a number n.
n=int(input("Enter any number:"))
n=abs(n)
bc=n
count1=0
count2=0
while bc>0:
    digit=bc%10
    bc=bc//10
    if(digit%2==0):
        count1+=1
    elif(digit%2!=0):
        count2+=1
print("Total number of even digits in n=",count1)
print("Total number of odd digits in n=",count2)