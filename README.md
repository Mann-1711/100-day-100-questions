# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 34: Display All Digits of a Number

### 📝 Problem Statement
Write a program to display all the digits of a number `n`, with each digit printed on a separate line in the original order.

### 🎯 Objective
Use loops, modulus, integer division, and a temporary variable to extract digits and display them in the correct order.

### 💡 Example

**Input:**
```text
Enter any number: 1234
```

**Output:**
```text
1
2
3
4
```

**Explanation:**

The number `1234` contains four digits: `1`, `2`, `3`, and `4`.

The program first extracts the digits from right to left and builds the reversed number `4321`. It then extracts the digits again to print them in their original order, one per line.

### 🧠 Logic
1. Take an integer `n` as input.
2. Use `abs()` to handle negative numbers.
3. Store the original number in a temporary variable `temp`.
4. Initialize `reverse = 0`.
5. Extract the last digit using the modulus operator (`% 10`).
6. Build the reversed number using `reverse = reverse * 10 + digit`.
7. Remove the last digit from `temp` using integer division (`// 10`) and repeat until `temp` becomes `0`.
8. Handle the special case where the original number is `0`.
9. Extract digits from the reversed number and print each digit on a separate line.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements using `if` and `else`
- Modulus operator using `%`
- Integer division using `//`
- Temporary variables
- Number reversal and digit extraction
- Handling special cases

### 📂 File
`Q34.py`

### 🚀 Challenge Progress
- **Completed:** 34/100 questions
- **Remaining:** 66 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**

