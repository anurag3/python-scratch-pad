class Solution:
    """
    You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    Intuition -
    We can do binary search to get the array that the target value lies between and
    we can then do another binary search to search through the array itself
    """

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        targetRow = None
        i = 0
        # Find the target row
        while i < len(matrix):
            if matrix[i][0] <= target <= matrix[i][-1]:
                targetRow = i
            i += 1
        if targetRow is None:
            return False
        else:
            leftPointer = 0
            rightPointer = len(matrix[targetRow])
            middlePointer = 0

            while leftPointer <= rightPointer:
                middlePointer = (leftPointer + rightPointer) // 2

                if target > matrix[targetRow][middlePointer]:
                    leftPointer = middlePointer + 1
                elif target < matrix[targetRow][middlePointer]:
                    rightPointer = middlePointer - 1
                else:
                    return True

            return False
