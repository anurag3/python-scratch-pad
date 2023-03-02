class Solution:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Best Case -
    Time complexity of O(n) as we have to traverse through all the elements of s and t atleast once

    Soln 1 -
    Convert s and t to list and then check if they are equal.
    Time complexity is O(n) and Space Complexity is O(n)

    Soln 2 -
    Use collections.Counter(). This measures frequency of the elements but ignores the order.
    Time complexity is O(n) and Space Complexity is O(n)

    Soln 3 -
    Build hashmap with key-value pair for both strings where key is the letter and value is frequency. Then match the key value pairs for both
    Time complexity is O(s+t) -> O(n) and Space Complexity is O(s+t) -> O(n)

    Soln 4 -
    Sort the arrays and compare them. Considering avg time complexity for sorting algorithms
    Time complexity is O(nlogn) and Space Complexity is O(1)

    """

    # def isAnagram_soln1(self, s: str, t: str) -> bool:
    #     # Not the right solution
    #     return list(s) == list(t)

    def isAnagram_soln2(self, s: str, t: str) -> bool:
        import collections

        return collections.Counter(list(s)) == collections.Counter(list(t))

    def isAnagram_soln3(self, s: str, t: str) -> bool:
        # check len if not equal they can't be anagrams
        if len(s) != len(t):
            return False

        # Creating dict/hashmaps for k, v where k=letter and v=frequency of that letter
        dictS, dictT = {}, {}

        for i in range(len(s)):
            # to add elements to dict -> dict["color"] = "red"
            # we use `.get()` so that we can handle case of KeyDoesNotExist
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)

        for c in dictS:
            if dictS[c] != dictT.get([c], 0):
                return False

        return True

    def isAnagram_soln4(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


sol = Solution()
print(sol.isAnagram_soln2("madam", "daamm"))
