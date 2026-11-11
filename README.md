# Day 48: Display All Armstrong Numbers from 1 to n

## 🎯 Problem Statement
Write a program to display all Armstrong numbers within a given range from 1 to n.

An Armstrong number is a number equal to the sum of its digits, each raised to the power of the total number of digits.

### 🧪 Examples

**Example 1:**
```text
Input: 10
Output: 1 2 3 4 5 6 7 8 9
```

**Example 2:**
```text
Input: 100
Output: 1 2 3 4 5 6 7 8 9
```

**Example 3:**
```text
Input: 500
Output: 1 2 3 4 5 6 7 8 9 153 370 371 407
```

## 💡 Approach
1. Take the upper limit n as input.
2. Use a `for` loop to iterate through every number from 1 to n.
3. Reset the digit count and total for each candidate number.
4. Preserve the current number in a temporary variable.
5. Use a `while` loop to count the number of digits.
6. Reset another temporary variable to the original candidate.
7. Extract each digit using the modulo operator (`% 10`).
8. Raise each digit to the power of the total digit count using (`**`).
9. Add the powered digits to a running total.
10. Compare the calculated total with the current candidate.
11. Print the number if both values are equal.

## 🧠 Concepts Practiced
- `for` and nested `while` loops
- Loop nesting and indentation
- Digit extraction using `%`
- Integer division using `//`
- Dynamic exponentiation using `**`
- Accumulator variables
- Variable initialization and resetting
- Temporary variables
- Conditional statements
- Number manipulation
- Debugging logical errors

## 📂 File
`Q48.py`

## 📈 Progress
**48 / 100 Questions Completed**

**52 Questions Remaining**

> Learning to control loops is learning to control logic. Every debugging session makes you a better problem solver! 🕷️
