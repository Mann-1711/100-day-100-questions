## Day 52: Harshad (Niven) Number

### Problem Statement
Write a Python program to check whether a given number is a **Harshad (Niven) number**.

A Harshad number is a number that is divisible by the sum of its own digits.

### Example

**Input:** `18`

- Sum of digits = 1 + 8 = 9
- 18 % 9 = 0

**Output:** `18 is a Harshad (Niven) number.`

**Input:** `19`

- Sum of digits = 1 + 9 = 10
- 19 % 10 != 0

**Output:** `19 is not a Harshad (Niven) number.`

### Approach
1. Take an integer as input.
2. Convert it to its absolute value.
3. Create a copy of the number to preserve the original value.
4. Extract each digit using the modulo operator (`% 10`).
5. Calculate the sum of all digits.
6. Remove the last digit using integer division (`// 10`).
7. Check whether the original number is divisible by the digit sum.
8. Display whether the number is a Harshad number.

### Concepts Practiced
- `while` loops
- Digit extraction using `%`
- Integer division using `//`
- Accumulator variables
- Conditional statements (`if-else`)
- Divisibility checks
- Preserving original values using a copy variable

### File
`Q52.py`

### Progress
**52/100 Questions Completed**

**48 Questions Remaining**
