# 🐍 Python Assignment 5 — Data Structures & Slicing

Welcome to **Assignment 5** for **Module 6: Data Structures and Strings in Python**. This repository demonstrates essential Python data manipulation techniques through two practical scripts:

- Dictionary operations for student records  
- Advanced list slicing techniques  
- Clean user interaction patterns  

---

## 📂 Contents

- `Task_1/main.py` — Student mark lookup system  
- `Task_2/main.py` — List slicing and reversal demonstrator  

---

## 📚 Task 1: Student Marks Dictionary

### 🔧 Core Features:
- Pre-populated dictionary of 5 student records  
- Case-sensitive name lookup  
- Clear output formatting for both success and failure cases  
- Intuitive user prompts  

**Try This:**  
Test edge cases by entering:  
1. Exact match ("Alice")  
2. Non-existent name  
3. Different casing ("alice")  

**Sample Output:**  
Enter the student's name: Charlie

Charlie's marks: 33


---

## 🔢 Task 2: List Slicing Magic

### 🔧 Core Features:  
- Generates a clean 1-10 number list  
- Demonstrates three key operations:  
  1. Basic slicing (`[:5]`)  
  2. List reversal (`[::-1]`)  
  3. Original list preservation  
- Self-documenting print statements  

**Technical Insight:**  
The reversal operation `[::-1]` creates a new list without modifying the original - a Pythonic best practice!

**Sample Output:**  
Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Reversed first five: [5, 4, 3, 2, 1]


---

## 🚀 Getting Started

### Requirements:  
- Python 3.x  

### How to Run:  
```bash
python Task_1/main.py  # Student records lookup
python Task_2/main.py  # List operations demo
