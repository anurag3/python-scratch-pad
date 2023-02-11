class Solution:
    """
    Question - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Best Case -
    Time complexity of O(n) as we have to traverse through the array atleast once

    Soln 1 -
    Bruteforce solution is to compare every element in the array with every other element.
    Time complexity is O(n^2) and Space Complexity is O(1)

    Soln 2 -
    Sort the array and then check with the adjacent element.
    Time complexity is O(nlogn) and Space Complexity is O(1)

    Soln 3 -
    Convert the list to set and check if their lengths match.
    Time complexity is O(n) and Space Complexity is O(n)

    Soln 4 -
    Create Hashset and check for duplicates while adding elements to it.
    Time complexity is O(n) and Space Complexity is O(n)

    """

    def containsDuplicate_soln3(self, nums: List[int]) -> bool:
        """
        This function converts the list to set and then matches the length of both
        if the length is same returns
        """
        return len(set(nums)) != len(nums)

    def containsDuplicate_soln4(self, nums: List[int]) -> bool:
        """
        Create Hashset and check for duplicates while adding elements to it
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
