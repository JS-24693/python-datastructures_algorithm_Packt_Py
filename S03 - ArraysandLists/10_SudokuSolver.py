from typing import List

class Solution:
    """
    Solve a 9x9 Sudoku puzzle using backtracking.
    The solver fills the board in-place and ensures each placement
    satisfies row, column, and 3x3 grid constraints.
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Backtracking search:
        - find next empty cell
        - try digits 1–9
        - place digit only if valid
        - recurse; undo placement if it leads to failure
        """
        self.backtrack(board)

    def backtrack(self, board: List[List[str]]) -> bool:
        # locate next empty cell
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    # try digits 1–9
                    for digit in "123456789":
                        if self.isValid(board, i, j, digit):
                            board[i][j] = digit
                            if self.backtrack(board):
                                return True
                            board[i][j] = '.'  # undo
                    return False
        return True  # solved

    def isValid(self, board: List[List[str]], r: int, c: int, val: str) -> bool:
        """
        Check row, column, and 3x3 grid for conflicts.
        """
        # row
        for j in range(9):
            if board[r][j] == val:
                return False

        # column
        for i in range(9):
            if board[i][c] == val:
                return False

        # grid
        gridRow = (r // 3) * 3
        gridCol = (c // 3) * 3
        for i in range(gridRow, gridRow + 3):
            for j in range(gridCol, gridCol + 3):
                if board[i][j] == val:
                    return False

        return True

# Test Instantiation
s = Solution()

board = [
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

s.solveSudoku(board)

for row in board:
    print(row)

# ['5', '3', '4', '6', '7', '8', '9', '1', '2']
# ['6', '7', '2', '1', '9', '5', '3', '4', '8']
# ['1', '9', '8', '3', '4', '2', '5', '6', '7']
# ['8', '5', '9', '7', '6', '1', '4', '2', '3']
# ['4', '2', '6', '8', '5', '3', '7', '9', '1']
# ['7', '1', '3', '9', '2', '4', '8', '5', '6']
# ['9', '6', '1', '5', '3', '7', '2', '8', '4']
# ['2', '8', '7', '4', '1', '9', '6', '3', '5']
# ['3', '4', '5', '2', '8', '6', '1', '7', '9']