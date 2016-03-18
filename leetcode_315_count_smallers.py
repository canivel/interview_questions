__author__ = 'canivel'
'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''

class Solution(object):
    # def getSum(self, T, idx):
    #     ans = 0
    #     while idx:
    #         ans += T[idx]
    #         idx -= idx & (-idx)
    #     return ans
    #
    # def update(self, T, idx, val):
    #     while idx <= len(T)-1:
    #         T[idx] += val
    #         idx += idx & (-idx)
    #
    # def countSmaller(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     if not nums:
    #         return []
    #     n = len(nums)
    #     padding = min(nums)
    #     if padding <= 0:
    #         nums = [a + 1 - padding for a in nums]
    #     m = max(nums)
    #     T = [0] * (m+1)
    #     ans = []
    #     t = 0
    #     for num in nums[::-1]:
    #         ans.append(self.getSum(T, num-1))
    #         self.update(T, num, 1)
    #     return ans[::-1]

    def countSmaller(self, nums):
        if not nums:
            return [0]
        if len(nums) <= 1:
            return [0]
        result = []
        for i in nums:
            s = nums[nums.index(i):]
            for j in s:
                if j < i:
                    result.append(j)

        if len(result) > 0:
            result[-1] = 0
        else:
            return [0]

        return result


if __name__ == "__main__":
    s =  Solution()
    a = [5, 2, 6, 1]
    #a = [-1, -1]
    print (s.countSmaller(a))
