# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #O(n)

        # if len(nums) == 1:
        #     return nums[0]
        #
        # r = set(nums)
        #
        # for n in r:
        #     if n not in nums:
        #         return n

        return sum(list(set(nums))) * 2 - sum(nums)


s = [1, 1, 2, 3, 3, 3, 4, 2, 5, 3, 1, 5, 6, 1, 6, 4, 8]
so = Solution()
print so.singleNumber(s)