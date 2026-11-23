## Q60: Sum of the Series of Squares

**Problem Statement:**  
Write a program to find the sum of the series:

\[
1^2 + 2^2 + 3^2 + \cdots + n^2
\]

**File:** `Q60.py`

### Concepts Used
- User Input
- Integer (`int`)
- For Loop
- `range()`
- Exponentiation (`**`)
- Accumulator (`total`)

### Logic
1. Take an integer `n` as input.
2. Initialize `total = 0`.
3. Run a loop from `1` to `n`.
4. Square the current number using `i**2`.
5. Add the squared value to `total`.
6. Print the final sum after the loop.

### Example

**Input:**
```text
Enter any number: 4
```

**Calculation:**
```text
1² + 2² + 3² + 4²
= 1 + 4 + 9 + 16
= 30
```

**Output:**
```text
30
```

### Mathematical Formula

The sum of squares can also be calculated using:

\[
S = \frac{n(n+1)(2n+1)}{6}
\]

### Key Learning
- Practised using loops to calculate a mathematical series.
- Learned how to square numbers using the exponentiation operator (`**`).
- Strengthened the understanding of accumulators and iterative calculations.

**Day 60/100 — Completed**
