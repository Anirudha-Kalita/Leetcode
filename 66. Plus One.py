"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = ""
        FinalNumber = 0
        TheList = []
        for i in range(len(digits)):
            number = number + str(digits[i])
            FinalNumber = int(number) + 1
        for j in str(FinalNumber):
            TheList.append(int(j))
        return TheList



obj = Solution()

print(obj.plusOne([1,2,3,5]))

## Retrurns [1,2,3,6]

