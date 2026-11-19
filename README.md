## Q56 – LCM of Two Numbers

**File:** `Q56.py`

### Problem
Write a Python program to find the Least Common Multiple (LCM) of two numbers.

### Concepts Used
- `for` loops
- Lists
- `append()` method
- Membership operator (`in`)
- Conditional statements (`if`, `elif`, `else`)
- `and` and `or` operators
- `max()` function
- Integer division (`//`)

### Logic
1. Take two numbers as input.
2. Check whether both numbers are zero. If so, display that LCM is undefined.
3. If either number is zero, the LCM is zero.
4. Find all factors of both numbers and store them in separate lists.
5. Identify their common factors.
6. Find the maximum common factor to calculate the GCD.
7. Use the relationship between GCD and LCM to calculate the LCM.

### Formula
`LCM = (First Number × Second Number) // GCD`

### Example
**Input:**
```text
Enter any number: 12
Enter any other number: 18
```

**Output:**
```text
36
```

### Edge Cases Tested
- Both numbers are zero → LCM is undefined.
- Either number is zero → LCM is zero.
- Two positive numbers → LCM calculated successfully.

### Progress
**Day 56 / 100** – Completed
