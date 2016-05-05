# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

#Depth for search

# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
class Solution(object):


    """
        The general idea is to iterate over string s.
        Always put the character c and its location i in the dictionary d.
        1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
        2) Otherwise, we need to remove a character from the sliding window.
           Here's how to find the character to be removed:
           Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T,
           we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
        """


    # def numIslands(self, grid):
    #     """
    #     :type grid: List[List[str]]
    #     :rtype: int
    #     """
    #     if not grid:
    #         return 0
    #
    #     m = len(grid)
    #     n = len(grid[0])
    #     sum = 0
    #
    #     for i in range(m):
    #         for j in range(n):
    #
    #             if grid[i][j] == "0":
    #                 continue
    #             else:
    #
    #                 #sum up only once per chance of meeting "1"
    #                 sum += 1
    #                 stack = list()
    #                 stack.append([i,j])
    #
    #                 #visit each "1" in the adjacent area using a stack
    #                 while len(stack) != 0:
    #
    #                     [p,q] = stack.pop()
    #
    #                     if p >= 1 and grid[p-1][q] == "1":
    #                         stack.append([p-1,q])
    #
    #                     if p < m -1 and grid[p+1][q] == "1":
    #                         stack.append([p+1,q])
    #
    #                     if q >= 1 and grid[p][q-1] == "1":
    #                         stack.append([p,q-1])
    #
    #                     if q < n - 1 and grid[p][q + 1] == "1":
    #                         stack.append([p,q+1])
    #
    #                     #mark as visited
    #                     grid[p][q] = "0"
    #
    #
    #
    #     return sum

    def numIslands(self, grid):

        if not grid:
            return 0


        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in rows:
            for c in cols:

                if grid[r][c] == 0:
                    continue
                else:
                    islands += 1
                    stack = []

                    #TODO


        return islands


g = [[1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 0, 1, 1]]

s =  Solution()
print (s.numIslands(g))