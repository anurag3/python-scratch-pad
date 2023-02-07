class Solution:
    """
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
    The relative order of the elements may be changed.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    
    Best Case - 
    Time complexity is O(n) since we have to traverse through all the elements of the array atleast once
    
    Soln 1 - 
    Use the 2 pointer method. We can have a left pointer and right pointer. Left pointer will keep swapping values with right pointer. 
    When right pointer finds the target value, it will do nothing and move ahead (it will not increment left pointer).
    When right pointer now finds new value which is not equal to target value it will again swap with left pointer, as left pointer was not incremented, 
    it will actually swap the target value in array with the new non-target value.
    
    Time complexity is O(n) since we have to traverse through all the elements of the array atleast once and Space Complexity is O(1)
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        left_pointer = 0
        
        for right_pointer in range(len(nums)):
            if nums[right_pointer] != val:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
        return left_pointer
                