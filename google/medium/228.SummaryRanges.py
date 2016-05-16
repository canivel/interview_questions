# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if not nums:
            return []

        nums = nums + [nums[-1] + 2]
        res = []
        head = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if head == nums[i - 1]:
                    res.append(str(head))
                else:
                    res.append(str(head) + "->" + str(nums[i - 1]))
                head = nums[i]
        return res

l = [0,1,2,4,5,7]

s = Solution()
print(s.summaryRanges(l))