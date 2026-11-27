# Question number 64:
# Write a program to print an inverted right-angled triangle pattern of stars of height n.
n = int(input("Enter any number:"))

i = n

while i >= 1:
    a = 1

    while a <= i:
        print("*", end=" ")
        a += 1

    print()
    i -= 1