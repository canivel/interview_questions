__author__ = 'canivel'

'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]


if __name__ == '__main__':
    triangle2 = [
        [-1],
        [2,3],
        [1,-1,-3]
    ]


    triangle = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3],
        [4,1,8,3,5]
    ]
    s = Solution()
    print s.minimumTotal(triangle2)