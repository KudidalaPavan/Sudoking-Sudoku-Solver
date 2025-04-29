def parse_input():
    grid = []
    for _ in range(100):
        row = [c for c in input().strip() if c in '123456789.']
        if len(row) != 9:
            continue
        grid.append(row)
        if len(grid) == 9:
            break
    return grid

def solve_puzzle(grid):
    # Pre-compute possible values for each cell
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Initialize with existing numbers
    empty_cells = []
    for r in range(9):
        for c in range(9):
            if grid[r][c] != '.':
                digit = grid[r][c]
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[(r // 3) * 3 + c // 3].add(digit)
            else:
                empty_cells.append((r, c))

    return backtrack(grid, empty_cells, 0, rows, cols, boxes)

def backtrack(grid, empty_cells, idx, rows, cols, boxes):
    if idx == len(empty_cells):
        return True

    r, c = empty_cells[idx]
    box_idx = (r // 3) * 3 + c // 3

    for digit in '123456789':
        # Check if placement is valid in O(1) time
        if (digit not in rows[r] and
            digit not in cols[c] and
            digit not in boxes[box_idx]):

            # Place the digit
            grid[r][c] = digit
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box_idx].add(digit)

            # Recurse
            if backtrack(grid, empty_cells, idx + 1, rows, cols, boxes):
                return True

            # Backtrack
            grid[r][c] = '.'
            rows[r].remove(digit)
            cols[c].remove(digit)
            boxes[box_idx].remove(digit)

    return False

def display_grid(grid):
    print("+-------+-------+-------+")
    for i, row in enumerate(grid):
        print(f"| {' '.join(row[:3])} | {' '.join(row[3:6])} | {' '.join(row[6:])} | ")
        if i % 3 == 2:
            print("+-------+-------+-------+")

if __name__ == "__main__":
    grid = parse_input()
    if solve_puzzle(grid):
        display_grid(grid)
    else:
        print("No solution exists")
