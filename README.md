# Q62: Calculate Power Without Using Inbuilt Power

**File:** `Q62.py`

## Problem Statement
Write a Python program to find the value of `x` raised to the power `y` without using the inbuilt power function.

## Concepts Used
- User input (`int()`)
- Conditional statements (`if`)
- For loops
- Repeated multiplication
- `abs()` function
- Arithmetic operations
- Negative exponents

## Logic
1. Take the base (`x`) and exponent (`y`) as input.
2. Initialize `result = 1`.
3. If the exponent is positive, multiply the result by the base repeatedly.
4. If the exponent is negative:
   - Convert the exponent to its positive value using `abs()`.
   - Perform repeated multiplication.
   - Calculate the reciprocal using `1/result`.
5. Handle special cases such as zero raised to zero and zero raised to a negative exponent.

## Mathematical Formula

For positive exponents:

\[
x^y = \underbrace{x \times x \times \cdots \times x}_{y\text{ times}}
\]

For negative exponents:

\[
x^{-y} = \frac{1}{x^y}
\]

## Example

**Input:**
```text
Enter any number: 2
Enter any exponent: -3
```

**Output:**
```text
0.125
```

## Key Learning
- Understood how exponentiation works through repeated multiplication.
- Learned how to handle negative exponents using reciprocals.
- Practised preserving the sign of the base and handling special cases.
- Improved understanding of loops and conditional statements.

**Day 62/100**
