class Solution:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
    
    Best Case -
    Time complexity of O(n) as we have to traverse the given array atleast once
    
    Soln 1 - 
    Clean string array by converting to lower case and removing non-alphanumeric elements.
    Then we reverse the cleaned string and check if it matches
    """
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = [c for c in s.lower() if c.isalnum()]
        return cleaned_str == cleaned_str[::-1]