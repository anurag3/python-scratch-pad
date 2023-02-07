class Solution:
    """
    Given an integer array nums of length n, you want to create an array ans of length 2n 
    where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    Specifically, ans is the concatenation of two nums arrays.
    Return the array ans.

    Best Case - 
    Time complexity is O(n) since we have to traverse through all the elements of the array atleast once

    Soln 1 -
    Create a new array. This array will be addition of nums
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans