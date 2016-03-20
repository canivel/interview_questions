__author__ = 'canivel'
'''
Given an array of integers and an integer k, find out whether there are
 two distinct indices i and j in the array such that nums[i] = nums[j] and
 the difference between i and j is at most k.
'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}

        for i in range(len(nums)):
            if nums[i] in d:
                j = d[nums[i]]
                if i - j <= k:
                    return True
            d[nums[i]] = i
        return False


matrix = [1, 2, 3, 3, 2, 1, 0, 1, 4, 5]

s = Solution()
print(s.containsNearbyDuplicate(matrix, 122))
