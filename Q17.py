# Question number 17:
# Write a program to read a character and check whether it is an alphabet, digit or special symbol.
character=input("Enter any character:")
if character.isalpha():
    print("alphabet")
elif character.isnumeric():
    print("digit")
else:
    print("special charater")