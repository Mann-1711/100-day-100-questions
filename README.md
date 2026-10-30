# 💯 100 Days, 100 Questions — Python Challenge

## 📅 Day 36: Product of All Digits

### 📝 Problem Statement
Write a program to find the product of all digits of a number `n`.

### 🎯 Objective
Use loops, modulus, integer division, and a running product to extract and multiply all digits of a number.

### 💡 Example

**Input:**
```text
Enter any number: 234
```

**Output:**
```text
The product of all digits of a number n: 24
```

### 📖 Explanation

The number `234` contains three digits: `2`, `3`, and `4`.

Their product is:

`2 × 3 × 4 = 24`

The program repeatedly extracts the last digit using the modulus operator (`% 10`), multiplies it with the running product, and removes the last digit using integer division (`// 10`). This process continues until no digits remain.

### 🧠 Logic
1. Take an integer `n` as input.
2. Use `abs()` to handle negative numbers.
3. Store the number in a working variable `bc`.
4. Initialize `product = 1`.
5. Handle the special case where `n` is `0`, since its digit product is `0`.
6. Use a `while` loop that runs while `bc > 0`.
7. Extract the last digit using `bc % 10`.
8. Multiply the extracted digit with `product`.
9. Remove the last digit using `bc = bc // 10`.
10. Repeat until `bc` becomes `0`.
11. Display the final product.

### 🧪 Python Concepts Practised
- User input using `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements using `if` and `else`
- Modulus operator (`%`)
- Integer division (`//`)
- Running products and accumulation
- Working variables
- Digit extraction and multiplication
- Handling special cases using conditional statements

### 📂 File
`Q36.py`

### 🚀 Challenge Progress
- **Completed:** 36/100 questions
- **Remaining:** 64 questions

> Every loop builds logic. Every problem builds experience.

**Keep Building! 🐍**
