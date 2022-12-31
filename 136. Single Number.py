"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if not (nums.count(nums[i]) > 1):
                return nums[i]

obj= Solution()
print(obj.singleNumber([4,1,2,1,2]))

## Returns 4