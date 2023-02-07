class Solution:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    
    Best Case - 
    Time complexity is O(n) since we have to traverse through all the elements of the array atleast once
    
    Soln 1 -
    Create a hashmap for tracking all the closing and opening brackets
    Use a stack to pop values when we encounter a closing brackets to find its opening bracket
    """
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_hashMap = {"}":"{",
                           ")":"(",
                           "]":"["}
        
        for bracket in s:
            if bracket in bracket_hashMap:
                if stack and stack[-1] == bracket_hashMap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
                
        return True if not stack else False