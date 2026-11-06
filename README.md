# Day 43: Sum of the First and Last Digit of a Number

## 🎯 Problem Statement

Write a Python program to find the sum of the first and last digits of a given number.

### 🧪 Example

**Input:**
```text
Enter any number: 58321
```

**Output:**
```text
First digit: 5
Last digit: 1
Sum: 6
```

### 💡 Approach

The problem uses mathematical digit manipulation to extract the first and last digits.

1. Convert the input into a positive number using `abs()`.
2. Extract the last digit using the modulo operator (`% 10`).
3. Use a `while` loop with the condition `bc >= 10`.
4. Repeatedly divide the number by 10 using integer division (`// 10`).
5. When only one digit remains, that digit is the first digit.
6. Add the first and last digits to calculate the final sum.

### 🧠 Concepts Practiced

- `while` loops and loop conditions
- Digit extraction using `% 10`
- Integer division using `// 10`
- Variables and temporary copies
- Working with first and last digits
- Basic mathematical problem-solving

### 📂 File

`Q43.py`

### 📈 Progress

**43 / 100 Questions Completed**

57 questions remaining.

> Consistency builds logic. Every problem makes the next one easier. 🚀
