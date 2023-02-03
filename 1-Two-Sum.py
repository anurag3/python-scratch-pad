class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Sol 1 -
    Pick element 1 and scan through every element after it and check if they add up to target. Keep repeating till last element.
    Time complexity is O(n^2) and Space Complexity is O(n)
    
    Soln 2 -
    Use Hashmap where k=element and v=index of element
    Time complexity is O(n) and Space Complexity is O(n)
    
    """
    def twoSum_soln2(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}  # val: index
        
        # enumerate returns index and value
        for idx, val in enumerate(nums):
            # calculate the diff between target and current value
            diff = target - val
            # if the diff is in the dict return its value (since v=index of the array) and index from enumerate
            if diff in prevDict:
                return [prevDict[diff], idx]
            # If it doesn't exist add element to dict with k=element and v=index of element
            prevDict[val] = idx
        return
            
            
        