## Q57 – Fibonacci Series (First N Terms)

**File:** `Q57.py`

### Problem Statement
Write a Python program to display the first `n` terms of the Fibonacci series.

### Concepts Used
- Variables
- `for` loop
- Arithmetic operators (`+`)
- Multiple assignment
- Variable updating
- `range()`
- `print()` with `end=" "`

### Logic
1. Take the number of terms (`n`) from the user.
2. Initialize two variables:
   - `a = 0`
   - `b = 1`
3. Run a loop `n` times.
4. Print the current value of `a`.
5. Calculate the next Fibonacci number using `c = a + b`.
6. Update the variables:
   - `a = b`
   - `b = c`
7. Repeat until all `n` terms are displayed.

### Formula
\[
F(n)=F(n-1)+F(n-2)
\]

The first two terms are 0 and 1.

### Example

**Input:**
```text
Enter number of terms: 7
```

**Output:**
```text
0 1 1 2 3 5 8
```

### Key Learning
- Understood how the Fibonacci sequence is generated.
- Practised updating variables inside a loop.
- Learned how to use multiple assignment in Python.
- Understood how to print exactly `n` terms using `range(n)`.

**Day 57 / 100 – Python Coding Challenge**
