class Solution:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    You must solve it in O(n) time complexity.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        kLargest = len(nums) - k
        nums = self.quickSort(nums, 0, len(nums) - 1, kLargest)
        return nums[kLargest]

    def quickSort(self, inputArray, startIndex, endIndex, kLargest):
        # define Pivot
        pivotValue = inputArray[endIndex]
        # define swap pointer
        swapPointer = startIndex

        for i in range(startIndex, endIndex):
            if inputArray[i] < pivotValue:
                inputArray[i], inputArray[swapPointer] = (
                    inputArray[swapPointer],
                    inputArray[i],
                )
                swapPointer += 1

        # Move the pivot to swapPointer
        inputArray[swapPointer], inputArray[endIndex] = (
            inputArray[endIndex],
            inputArray[swapPointer],
        )

        # check if pivot is k largest
        if swapPointer > kLargest:
            # sort the leftarray
            return self.quickSort(inputArray, startIndex, swapPointer - 1)
        elif swapPointer < kLargest:
            # sort the rightarray
            return self.quickSort(inputArray, swapPointer + 1, endIndex)
        else:
            return inputArray
