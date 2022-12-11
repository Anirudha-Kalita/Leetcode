"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
class Solution:
    def isValid(self, s):
        dct = {'(': ')', '{': '}', '[': ']'}
        stack = []
        l = len(s)
        if l == 0:
            return True
        if l % 2 != 0:
            return False
        for num, char in enumerate(s):
            if char in dct:
                stack.append(dct[char])
            elif stack and char == stack[-1]:
                stack.pop(-1)
            else:
                return False
            df = not stack
        return df

obj = Solution()
print(obj.isValid("[]"))
