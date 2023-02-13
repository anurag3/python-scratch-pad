class Solution:
    """
    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and
    with the smallest space complexity possible.
    """

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums: List[int], startIndex: int, endIndex: int) -> List[int]:
        # base case
        if (endIndex - startIndex + 1) <= 1:
            return nums

        # calculate the center to split the array
        middleIndex = (startIndex + endIndex) // 2

        # Sort the left half
        self.mergeSort(nums, startIndex, middleIndex)

        # Sort the right half
        self.mergeSort(nums, middleIndex + 1, endIndex)

        # Merge the sorted arrays
        self.merge(nums, startIndex, middleIndex, endIndex)

        return nums

    def merge(self, nums: List[int], startIndex: int, middleIndex: int, endIndex: int):
        leftHalf = nums[startIndex : middleIndex + 1]
        rightHalf = nums[middleIndex + 1 : endIndex + 1]

        i = 0  # index for leftHalf
        j = 0  # index for rightHalf
        k = startIndex  # index for original array

        # Merge the two sorted halfs into original array
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                nums[k] = leftHalf[i]
                i += 1
            else:
                nums[k] = rightHalf[j]
                j += 1
            k += 1
        # For case where either halfs have elements remaining
        while i < len(leftHalf):
            nums[k] = leftHalf[i]
            i += 1
            k += 1
        while j < len(rightHalf):
            nums[k] = rightHalf[j]
            j += 1
            k += 1
