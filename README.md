# Day 64 – Inverted Right-Angled Triangle Pattern

### Problem Statement
Write a Python program to print an inverted right-angled triangle pattern of stars using nested `while` loops.

### File
`Day_64.py`

### Concepts Used
- While Loops
- Nested While Loops
- Conditional Statements
- Loop Counters
- `print()` and `end` parameter

### Logic
1. Take the height of the triangle as input from the user.
2. Initialize `i = n` to represent the number of stars in the first row.
3. Use an outer `while` loop to control the rows.
4. Initialize `a = 1` inside the outer loop to reset the star counter for every row.
5. Use an inner `while` loop to print stars until `a` becomes greater than `i`.
6. Use `print()` to move to the next line.
7. Decrease `i` by 1 after every row.

### Code

```python
n = int(input("Enter any number:"))

i = n

while i >= 1:
    a = 1

    while a <= i:
        print("*", end=" ")
        a += 1

    print()
    i -= 1
```

### Example Output

**Input:**
```text
Enter any number: 5
```

**Output:**
```text
* * * * *
* * * *
* * *
* *
*
```

### Key Learning
- Understood how nested `while` loops work.
- Learned how to reset an inner loop counter for every row.
- Practised decreasing the number of iterations in each row.
- Understood how to control rows and columns using two variables.

**Day 64/100 – Consistency over shortcuts.**
