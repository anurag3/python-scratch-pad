class Solution:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
    removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.

    Best Case -
    Time complexity of O(n) as we have to traverse the given array atleast once

    Soln 1 -
    Clean string array by converting to lower case and removing non-alphanumeric elements.
    Then we reverse the cleaned string and check if it matches
    Time complexity is O(n) and Space Complexity is O(n)

    Soln 2 -
    Running pointer method. Left running node goes from left to right and
    Right running node goes from right to left. Created a new function to check ASCII values of character is between (A-Z,a-z,0-9)
    Keep matching left pointer to the right pointer till left pointer >= right pointer

    """

    def isPalindrome_soln1(self, s: str) -> bool:
        cleaned_str = [c for c in s.lower() if c.isalnum()]
        return cleaned_str == cleaned_str[::-1]

    def isPalindrome_soln2(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isalphaNum(s[l]):
                l += 1
            while r > l and not self.isalphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def isalphaNum(self, char):
        return (
            (ord("A") <= ord(char) <= ord("Z"))
            or (ord("a") <= ord(char) <= ord("z"))
            or (ord("0") <= ord(char) <= ord("9"))
        )
