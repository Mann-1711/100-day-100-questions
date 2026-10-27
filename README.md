# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 33: Count the Number of Digits

### 📝 Problem Statement
Write a program to count the number of digits in a number `n`.

### 🎯 Objective
Use loops, counter variables, and integer division to determine how many digits a number contains.

### 💡 Example

**Input:**
```text
Enter a number: 583
```

**Output:**
```text
Number of digits: 3
```

**Explanation:**

The number `583` contains three digits: `5`, `8`, and `3`.

Therefore, the total number of digits is `3`.

### 🧠 Logic
1. Take an integer `n` as input.
2. Handle the special case where `n` is `0`, since zero has one digit.
3. Use the absolute value of `n` to handle negative numbers.
4. Initialize a counter variable `count = 0`.
5. Repeatedly divide the number by `10` using integer division (`//`).
6. Increase the counter by `1` for each digit removed.
7. Display the final count.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements using `if` and `else`
- Counter variables and `count += 1`
- Absolute value using `abs()`
- Integer division using `//`

### 📂 File
`Q33.py`

### 🚀 Challenge Progress
- **Completed:** 33/100 questions
- **Remaining:** 67 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**
