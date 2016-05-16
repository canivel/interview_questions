# Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        result = []
        nums.append(upper + 1)
        pre = lower - 1
        for i in nums:
            if (i == pre + 2):
                result.append(str(i - 1))
            elif (i > pre + 2):
                result.append(str(pre + 1) + "->" + str(i - 1))
            pre = i
        return result


l = [0, 1, 3, 50, 75]
lower = 0
upper = 99

m = [-1]

print len(m)

s = Solution()
print(s.findMissingRanges(l, lower, upper))