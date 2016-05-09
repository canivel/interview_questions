# Given an array of size n, find the majority element.
# The majority element is the element that appears more than  n/2  times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

import operator

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = len(nums)

        if not nums:
            return 0

        if c == 1:
            return nums[0]

        t = 1
        nums.sort()
        r = len(nums) - 1
        m = len(nums) / 2
        for i in range(r):
            if nums[i] == nums[i + 1]:
                t = t + 1
                if (t > m):
                    return nums[i]
            else:
                t = 1


l = [1, 1, 3, 3, 5, 5, 5, 5, 5, 5 ,5 ,5, 9, 9, 11]
s = Solution()
print(s.majorityElement(l))


