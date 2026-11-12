# Day 49: Perfect Number

## 🎯 Problem Statement
Write a program to check whether a given number is a Perfect Number.

A Perfect Number is a positive integer that is equal to the sum of all its positive factors (divisors), excluding the number itself.

### 🧪 Examples

**Example 1:**
```text
Input: 6
Output: 6 is a perfect number.
```
Explanation:
The factors of 6 excluding itself are 1, 2, and 3.

1 + 2 + 3 = 6

**Example 2:**
```text
Input: 28
Output: 28 is a perfect number.
```
Explanation:
The factors of 28 excluding itself are 1, 2, 4, 7, and 14.

1 + 2 + 4 + 7 + 14 = 28

**Example 3:**
```text
Input: 12
Output: 12 is not a perfect number.
```
Explanation:
The factors of 12 excluding itself are 1, 2, 3, 4, and 6.

1 + 2 + 3 + 4 + 6 = 16

Since 16 is not equal to 12, it is not a perfect number.

## 💡 Approach
1. Take an integer as input.
2. Initialize a variable `total` to 0.
3. Use a `for` loop to iterate from 1 to n-1.
4. Check whether each number divides n completely using the modulo operator (`%`).
5. If the remainder is 0, the number is a factor.
6. Add each factor to the running total.
7. Compare the total sum with the original number.
8. If both are equal, display that the number is a Perfect Number; otherwise, display that it is not.

## 🧠 Concepts Practiced
- `for` loops
- Conditional statements (`if-else`)
- Modulo operator (`%`)
- Factor identification
- Accumulator variables
- Running sum
- Number manipulation
- Logical comparisons

## 📂 File
`Q49.py`

## 📈 Progress
**49 / 100 Questions Completed**

**51 Questions Remaining**

> Small steps, stronger logic. Every problem brings you closer to thinking like a programmer! 🕷️
