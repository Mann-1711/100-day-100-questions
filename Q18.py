# Question number 18:
# Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).
m=float(input("Enter student's marks in math:"))
e=float(input("Enter student's marks in english:"))
s=float(input("Enter student's  marks in science:"))
result=(m+e+s)/300*100
print("THE AGREEGATE %:",result)
if(result>=80 and result<=100):
    print("A")
elif(result>=70 and result<80):
    print("B")
elif(result>=60 and result<70):
    print("C")
elif(result>=33 and result<60):
    print("D")
elif(result<33):
    print("FAIL")
else:
    ("INVALID NUMBER")