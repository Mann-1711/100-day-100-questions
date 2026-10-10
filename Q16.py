# Question number 16:
# Write a program to read a character and check whether it is a vowel or a consonant.
charac=input("Enter any character:").lower()
if charac in ("a","e","i","o","u"):
    print("This Character is a vowel.")
else:
    print("This character is  a consonant.")