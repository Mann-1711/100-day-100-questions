# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 39: Find the Smallest Digit in a Number

### 📝 Problem Statement
Write a program to find the smallest digit in a number `n`.

### 🎯 Objective
Use loops, modulus, integer division, and conditional statements to extract digits and identify the smallest digit in a number.

### 💡 Example

**Input:**
```text
Enter any number: 5832
```

**Output:**
```text
The smallest digit in the number is: 2
```

### 📖 Explanation

The number `5832` contains four digits: `5`, `8`, `3`, and `2`.

The smallest among these digits is `2`.

The program repeatedly extracts the last digit using the modulus operator (`% 10`) and compares it with the current smallest digit.

If the extracted digit is smaller than the current smallest digit, the value is updated.

The last digit is then removed using integer division (`// 10`). This process continues until all digits have been checked.

### 🧠 Logic
1. Take an integer `n` as input.
2. Use `abs()` to handle negative numbers.
3. Store the number in a working variable `bc`.
4. Initialize `smallest = 9` to track the smallest possible decimal digit.
5. Handle the special case where `n` is `0`, since its smallest digit is `0`.
6. Use a `while` loop that runs while `bc > 0`.
7. Extract the last digit using `bc % 10`.
8. Compare the extracted digit with `smallest` using an `if` statement.
9. If `digit < smallest`, update `smallest = digit`.
10. Remove the last digit using `bc = bc // 10`.
11. Repeat until `bc` becomes `0`.
12. Display the smallest digit.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements using `if`
- Modulus operator (`%`)
- Integer division (`//`)
- Working variables
- Digit extraction
- Comparison operators (`<`)
- Finding minimum values
- Handling negative numbers using `abs()`
- Handling special cases using conditional statements

### 📂 File
`Q39.py`

### 🚀 Challenge Progress
- **Completed:** 39/100 questions
- **Remaining:** 61 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**
