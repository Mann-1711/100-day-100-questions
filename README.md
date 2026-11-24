## Q61: Sum of the Harmonic Series

**Problem Statement:**  
Write a program to find the sum of the series:

\[
1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}
\]

**File:** `Q61.py`

### Concepts Used
- User Input (`input()`)
- Integer Conversion (`int()`)
- For Loop
- `range()`
- Floating-Point Division (`/`)
- Accumulator (`total`)

### Logic
1. Take an integer `n` as input.
2. Initialize `total = 0`.
3. Run a loop from `1` to `n`.
4. Calculate the reciprocal of the current number using `1/i`.
5. Add the calculated value to `total`.
6. Print the final sum after the loop.

### Example

**Input:**
```text
Enter any number: 4
```

**Calculation:**
```text
1 + 1/2 + 1/3 + 1/4
= 1 + 0.5 + 0.3333 + 0.25
= 2.0833
```

**Output:**
```text
2.083333333333333
```

### Key Learning
- Practised calculating mathematical series using a `for` loop.
- Understood floating-point division in Python.
- Learned to accumulate fractional values using a variable.
- Strengthened loop-based mathematical problem-solving skills.

**Day 61/100 — Completed**
