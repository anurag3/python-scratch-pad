class Solution:
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Best Case -
    Time complexity of O(n) as we have to traverse the given array atleast once.

    Soln 1 -
    Use Hashset for every row and every column
    Checking 3x3 sub square would be tricky but since we know that the board will be 9x9 and subsquare will be 3x3,
    we can use row_num or col_num (0 to 9) and simply perform integer division

    Time complexity of O(n^2) and Space complexity is O(n^2)

    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (rows/3, cols/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3), (c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
