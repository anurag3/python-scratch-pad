class Solution:
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target,
    write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
    """

    def search(self, nums: List[int], target: int) -> int:
        leftIndex, rightIndex = 0, len(nums) - 1
        middleIndex = 0
        while leftIndex <= rightIndex:
            middleIndex = abs(leftIndex - rightIndex) // 2

            if target > nums[middleIndex]:
                # search to the right of middleIndex
                leftIndex = middleIndex + 1
            elif target < nums[middleIndex]:
                # search to the left of middleIndex
                rightIndex = middleIndex - 1
            else:
                return middleIndex

        return -1
