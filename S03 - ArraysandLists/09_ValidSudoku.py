from typing import List

class Solution:
    """
    Validate a 9x9 Sudoku board.
    Ensures each row, column, and 3x3 grid contains no duplicate digits.
    Empty cells are represented by '.' and ignored.
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Track seen digits using three arrays of sets:
        - rowSet[i]   → digits seen in row i
        - colSet[j]   → digits seen in column j
        - gridSet[g]  → digits seen in 3x3 grid g

        Return True only if no digit repeats in its row, column, or grid.
        """
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        gridSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue

                # compute 3x3 grid index
                gridNo = (i // 3) * 3 + (j // 3)

                # Inlines three membership checks for duplicates
                if value in rowSet[i] or value in colSet[j] or value in gridSet[gridNo]:
                    return False

                # record digit
                rowSet[i].add(value)
                colSet[j].add(value)
                gridSet[gridNo].add(value)

        return True

# Test Instantiation
s = Solution()

board_valid = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(s.isValidSudoku(board_valid))   # True


board_invalid = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],  # duplicate '8' in column
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(s.isValidSudoku(board_invalid))  # False

        
