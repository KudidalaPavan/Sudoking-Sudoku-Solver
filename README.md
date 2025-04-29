# 🧩 SudoKing Challenge: Sudoku Solver

This project is a solution to the **SudoKing Challenge**, which requires implementing a Sudoku solver that reads a partially filled 9×9 grid and outputs a completed, valid Sudoku board.

---

## 📌 Challenge Overview

The solver must follow these rules:
- Each row must contain digits `1` through `9` without repetition.
- Each column must contain digits `1` through `9` without repetition.
- Each of the nine 3×3 boxes must contain digits `1` through `9` without repetition.
- The final output must be formatted exactly to SudoKing’s specifications.

---

## 🚀 Solution Approach

The project uses a combination of **backtracking** and **constraint propagation**:

### Key Components:
- **Input Parser**: Reads a 9x9 grid from messy input.
- **Constraint Sets**: Efficient validation using sets for rows, columns, and 3x3 boxes.
- **Recursive Backtracking**: Fills empty cells with valid digits and backtracks on conflicts.
- **Grid Formatter**: Outputs the solved Sudoku in a clean, boxed format.

---

## 🧠 Algorithm Details

### ✔ Backtracking with Constraint Propagation
- Cells are filled recursively, trying digits `1–9`.
- If a digit violates Sudoku rules (checked in O(1) using sets), it’s skipped.
- If all cells are validly filled, the solution is printed.

### ✔ Optimization
- Constraint sets (`rows`, `cols`, `boxes`) allow constant-time checks.
- Only unfilled cells are processed.
- Early exits when dead ends are encountered.

---

## 📂 File Structure

