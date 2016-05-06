# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        #
        # check = {}
        # for i, num in enumerate(nums):
        #     if num not in check:
        #         check[target - num] = i
        #     else:
        #         return [min(i, check[num]), max(i, check[num])]

        cache = {}
        for i, num in enumerate(nums):
            if num not in cache:
                cache[target-num] = i
            else:
                print i, cache[num]
                return [min(i, cache[num]), max(i, cache[num])]


l = [2, 8, 6, 7, 11, 15]
target = 9
s = Solution()
print s.twoSum(l, target)