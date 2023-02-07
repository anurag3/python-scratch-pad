class Solution:
    """
    Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    
    Best Case - 
    Time complexity is O(n) since we have to traverse through all the elements of the array atleast once
    
    Soln 1 - 
    Use the 2 pointer method. We can have a left pointer and right pointer. Right pointer will keep on incrementing till it finds the 
    unique value and when it finds a unique value, left pointer will place that unique value in its current position and 
    move to the next spot. We can have a counter for when the left pointer moves
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        left_pointer, right_pointer = 1, 1

        for right_pointer in range(1, len(nums)):
            if nums[right_pointer] != nums[right_pointer - 1]:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
                counter += 1            
        return counter