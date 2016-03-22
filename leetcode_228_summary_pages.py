__author__ = 'canivel'
'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''
class Solution(object):
    def summaryRanges(self, nums):
        l = []
        for n in nums:
            if not l or n > l[-1][-1] + 1:
                l += [],
            l[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in l]



nums = [0, 1]
s = Solution()
print(s.summaryRanges(nums))