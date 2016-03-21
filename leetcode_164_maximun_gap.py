__author__ = 'canivel'
'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
'''

'''
def radixSort(self, A):
        for k in xrange(10):
            s=[[] for i in xrange(10)]
            for i in A:
                s[i/(10**k)%10].append(i)
            A=[a for b in s for a in b]
        return A

    def maximumGap(self, nums):
        A = self.radixSort(nums)
        ans = 0
        if len(A) == 0: return 0
        prev = A[0]
        for i in A:
            if i - prev > ans: ans = i - prev
            prev = i
        return ans
'''

class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        gap = 0
        sortedlist = list(set(nums))
        sortedlist.sort()
        print(sortedlist)
        for i in range(len(sortedlist)-1):

            if i <= len(sortedlist):
                 dif = (sortedlist[i+1] - sortedlist[i])
                 if dif > gap:
                     gap = dif



        return gap
matrix = [1,10000000]
#matrix = [3,6,9,1]

s = Solution()
print(s.maximumGap(matrix))
