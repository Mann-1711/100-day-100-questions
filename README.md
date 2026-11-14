## Day 51: Automorphic Number

**Problem:** Write a program to check whether a number is an automorphic number.

### What is an Automorphic Number?
An automorphic number is a number whose square ends with the number itself.

**Examples:**
- 5 → 5² = 25 → Automorphic
- 6 → 6² = 36 → Automorphic
- 25 → 25² = 625 → Automorphic
- 76 → 76² = 5776 → Automorphic
- 12 → 12² = 144 → Not Automorphic

### Approach
1. Take an integer as input.
2. Calculate its square.
3. Count the digits in the original number using a `while` loop.
4. Use modulo (`%`) and exponentiation (`**`) to extract the last digits of the square.
5. Compare the extracted digits with the original number.
6. Display whether the number is automorphic.

### Concepts Practiced
- `while` loops
- Digit counting using integer division (`//`)
- Modulo operator (`%`)
- Exponentiation (`**`)
- Conditional statements (`if-else`)
- Variables and temporary copies
- Mathematical problem-solving

### Python File
`Q51.py`

### Progress
**51/100 Questions Completed** 🎯

49 questions remaining.
