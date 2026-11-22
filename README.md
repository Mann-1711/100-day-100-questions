# Q59: Sum of the Series (1 + 2 + 3 + ... + n)

### Problem Statement
Write a Python program to find the sum of the series:

`1 + 2 + 3 + ... + n`

### File
`Q59.py`

### Concepts Used
- `input()` and `int()`
- `abs()` function
- `if-else` condition
- `for` loop
- `range()` function
- Accumulator variable

### Code
```python
n = int(input("Enter any number:"))
n = abs(n)

if n == 0:
    print(0)
else:
    total = 0
    for i in range(1, n+1):
        total = total + i
    print(total)
```

### Logic
1. Take an integer input from the user.
2. Use `abs()` to convert a negative number into its positive equivalent.
3. If the number is zero, print `0`.
4. Otherwise, initialize `total = 0`.
5. Use a `for` loop from `1` to `n`.
6. Add each value of `i` to `total`.
7. Print the final sum.

### Example

**Input:**
```text
Enter any number: 5
```

**Calculation:**
```text
1 + 2 + 3 + 4 + 5 = 15
```

**Output:**
```text
15
```

### Mathematical Formula
The sum of the first `n` natural numbers can also be calculated using:

`S = n * (n + 1) / 2`

### Key Learning
Learned how to use an accumulator variable inside a loop to calculate the sum of a series. Also practised handling negative inputs using `abs()`.

**Day 59/100**
