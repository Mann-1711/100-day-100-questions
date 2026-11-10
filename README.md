# Day 47: Armstrong Number

## 🎯 Problem Statement
Write a program to check whether a given number is an Armstrong number.

An Armstrong number is a number equal to the sum of its digits, each raised to the power of the total number of digits.

### 🧪 Examples

**Example 1:**
```text
Input: 153
Output: Armstrong Number
```
Explanation: \(1^3 + 5^3 + 3^3 = 153\)

**Example 2:**
```text
Input: 123
Output: Not an Armstrong Number
```
Explanation: \(1^3 + 2^3 + 3^3 = 36\), which is not equal to 123.

**Example 3:**
```text
Input: 1634
Output: Armstrong Number
```
Explanation: \(1^4 + 6^4 + 3^4 + 4^4 = 1634\)

## 💡 Approach
1. Take an integer as input.
2. Preserve the original number for comparison.
3. Count the total number of digits using a `while` loop.
4. Extract each digit using the modulo operator (`% 10`).
5. Raise each digit to the power of the total digit count.
6. Add the powered digits to a running total.
7. Compare the calculated total with the original number.
8. Display whether the number is an Armstrong number.

## 🧠 Concepts Practiced
- `while` loops
- Digit extraction using `%`
- Integer division using `//`
- Dynamic exponentiation using `**`
- Accumulator variables
- Conditional statements
- Number manipulation
- Debugging and edge-case handling

## 📂 File
`Q47.py`

## 📈 Progress
**47 / 100 Questions Completed**

**53 Questions Remaining**

> Every problem solved independently strengthens your ability to think like a programmer. Keep building! 🕷️
