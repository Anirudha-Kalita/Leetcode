"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        i = 1
        while i * i <= x:
            i += 1
        return i - 1

obj = Solution()
print(obj.mySqrt(8))
## return result 2 (round of of 2.8)