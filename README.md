# Day 46: Display the First N Prime Numbers

## 🎯 Problem Statement

Write a Python program to read a number `n` and display the first `n` prime numbers.

### 🧪 Example

**Input:**
```text
Enter how many prime numbers: 5
```

**Output:**
```text
2
3
5
7
11
```

### 💡 Approach

The problem combines prime-number checking with nested loops and a counter.

1. Read the number `n`, representing how many prime numbers need to be displayed.
2. Initialise `num = 2`, since 2 is the smallest prime number.
3. Initialise `count = 0` to track the number of primes found.
4. Use a `while` loop that continues until `count` reaches `n`.
5. Assume the current number is prime using a Boolean flag (`is_prime = True`).
6. Use an inner `for` loop to check whether the current number has any divisors between 2 and `num - 1`.
7. If a divisor is found, mark the number as non-prime and stop checking using `break`.
8. If the number is prime, display it and increment the counter.
9. Increment `num` to check the next candidate number.
10. Repeat until the required number of prime numbers has been displayed.

### 🧠 Concepts Practiced

- Nested loops (`while` and `for`)
- Prime number identification
- Boolean flags (`True` and `False`)
- Counter variables
- Conditional statements (`if`)
- Modulo operator (`%`)
- `break` statement
- Algorithmic problem-solving

### 📂 File

`Q46.py`

### 📈 Progress

**46 / 100 Questions Completed**

54 questions remaining.

> Moving beyond individual problems and learning to combine logic, loops, and conditions into complete algorithms. 🚀
