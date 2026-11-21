## Q58 – Sum of First N Terms of Fibonacci Series

**File:** `Q58.py`

### Problem Statement
Write a Python program to find the sum of the first `n` terms of the Fibonacci series.

### Concepts Used
- Variables
- `for` loop
- Arithmetic operators (`+`)
- Accumulator variable
- Variable updating
- `range()`
- User input

### Logic
1. Take the number of terms (`n`) from the user.
2. Initialize two variables:
   - `a = 0`
   - `b = 1`
3. Initialize `total = 0` to store the sum.
4. Run a loop `n` times.
5. Add the current Fibonacci number (`a`) to `total`.
6. Calculate the next Fibonacci number using `c = a + b`.
7. Update the variables:
   - `a = b`
   - `b = c`
8. Print the final sum after the loop ends.

### Formula

Fibonacci sequence:

\[
F(n)=F(n-1)+F(n-2)
\]

Sum of the first `n` terms:

\[
S_n=F_0+F_1+\cdots+F_{n-1}
\]

### Example

**Input:**
```text
Enter number of terms: 5
```

**Fibonacci Series:**
```text
0 1 1 2 3
```

**Output:**
```text
Sum of Fibonacci series: 7
```

### Key Learning
- Learned how to calculate the sum of a sequence using an accumulator.
- Practised updating variables inside a loop.
- Reused Fibonacci logic to solve a new problem.
- Understood why the accumulator must be updated before changing the current Fibonacci term.

**Day 58 / 100 – Python Coding Challenge**
