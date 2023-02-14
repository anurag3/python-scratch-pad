class Solution:
    """
    Given an array nums with n objects colored red, white, or blue,
    sort them in-place so that objects of the same color are adjacent,
    with the colors in the order red, white, and blue.
    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    You must solve this problem without using the library's sort function.
    """

    def sortColors_bucketSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_array = [0, 0, 0]
        for i in range(len(nums) - 1):
            temp_array[nums[i]] += 1

        i = 0
        for n in range(len(temp_array) - 1):
            for j in range(0, temp_array[n]):
                nums[i] = n
                i += 1

    def sortColors_quickselectpartition(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftPointer, rightPointer = 0, len(nums) - 1
        i = 0

        while i <= rightPointer:
            if nums[i] == 2:
                nums[i], nums[rightPointer] = nums[rightPointer], nums[i]
                rightPointer -= 1
                i -= 1
            elif nums[i] == 0:
                nums[i], nums[leftPointer] = nums[leftPointer], nums[i]
                leftPointer += 1
            i += 1
