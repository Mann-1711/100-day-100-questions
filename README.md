## Day 63 – Right-Angled Triangle Star Pattern

### Problem Statement
Write a program to print a right-angled triangle pattern of stars (`*`) of height `n`.

### File
`Day_63.py`

### Concepts Used
- Nested `for` loops
- `range()` function
- `print()` function
- `end=""` parameter
- Pattern printing

### Logic
1. Take the height `n` as input from the user.
2. Use the outer loop to control the number of rows.
3. Use the inner loop to print stars in each row.
4. The number of stars in each row is equal to the current row number.
5. Use `end=""` to print stars on the same line.
6. Use an empty `print()` after the inner loop to move to the next row.

### Code

```python
n = int(input("Enter any number:"))

for i in range(1, n+1):
    for a in range(1, i+1):
        print("*", end="")
    print()
```

### Example

**Input:**
```text
4
```

**Output:**
```text
*
**
***
****
```

### Key Learning
- Understood how nested loops work together.
- Learned how the outer loop controls rows and the inner loop controls columns.
- Understood the importance of indentation in nested loops.
- Learned how `end=""` prevents automatic line breaks.

### Day 63/100
