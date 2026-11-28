# Day 65 – Pyramid Pattern of Stars

### Problem Statement
Write a Python program to print a pyramid pattern of stars of height `n` using nested `for` loops.

### File
`Day_65.py`

### Concepts Used
- Nested For Loops
- `range()` Function
- Loop Counters
- String Printing
- `print()` and `end` parameter

### Logic
1. Take the height of the pyramid as input from the user.
2. Use an outer `for` loop to control the rows.
3. Use the first inner loop to print leading spaces.
   - Number of spaces = `n - i`
4. Use the second inner loop to print stars.
   - Number of stars = `2 * i - 1`
5. Use `end=""` to print spaces and stars on the same line.
6. Use `print()` after both inner loops to move to the next row.

### Code

```python
n = int(input("Enter any number:"))

for i in range(1, n + 1):
    for a in range(1, (n - i) + 1):
        print(" ", end="")

    for b in range(1, (2 * i - 1) + 1):
        print("*", end="")

    print()
```

### Example Output

**Input:**
```text
Enter any number: 5
```

**Output:**
```text
    *
   ***
  *****
 *******
*********
```

### Key Learning
- Learned how to create pyramid patterns using nested loops.
- Understood how leading spaces control the alignment of a pyramid.
- Learned that the number of stars increases by 2 in each row.
- Improved understanding of Python's `range()`
