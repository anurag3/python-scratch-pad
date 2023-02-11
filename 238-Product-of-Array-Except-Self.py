class Solution:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation

    Best Case -
    Time complexity of O(n) as we have to traverse the given array atleast

    Soln 1 -
    Create a prefix and postfix array. Prefix array will be product of all the elements before the ith element.
    Postfix array will be product of all the elements after the ith element.
    For the output array, output_array[i] = prefix_array[i-1] * postfix_array[i+1]
    input_array =       [1,2,3,4]
    prefix_array =      [1,2,6,24]
    postfix_array =     [24,24,12,4]
    output_array =      [24,12,8,4]

    Time complexity of O(n) and Space complexity is O(n)

    To further optimize, we can keep updating the output array for the prefix and postfix passes
    Time complexity of O(n) and Space complexity is O(1) as output does not count for space as per this problem statement

    """

    def productExceptSelf_soln1(self, nums: List[int]) -> List[int]:
        result_array = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            result_array[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result_array[i] *= postfix
            postfix *= nums[i]
        return result_array
