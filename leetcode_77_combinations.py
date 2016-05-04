__author__ = 'canivel'
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:
'''
import itertools

class Solution(object):
    def combine(self, n, k):
        result = list(itertools.combinations([x for x in range(1, n+1)], k))
        return result


#st = "au"
n = 4
k = 2
s = Solution()
print(s.combine(n, k))