__author__ = 'canivel'

'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution(object):
    def searchRange(self, nums, target):

        r = []
        j = 0
        for i in nums:
            if(i == target):
                r.append(j)
            j = j + 1

        if not r:
            return [-1, -1]
        else:
            if(len(r) == 1):
                r.append(r[0])
                return r
            if(len(r) > 2):
                return [r[0], r[-1]]

        return r


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 8, 10]
    target = 8

    s = Solution()
    print s.searchRange(nums, target)