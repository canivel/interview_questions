__author__ = 'canivel'
class Solution(object):


    # def transpose_and_yield_top(arr):
    #     while arr:
    #         yield arr[0]
    #         arr = list(reversed(zip(*arr[1:])))

    def printSpiralOrder(self, array, nrows, ncols):
        top = 0
        bottom = nrows - 1
        left = 0
        right = ncols
        direction = 0

        while(top <= bottom and left <= right):
            if(direction == 0):
                for i in range(right):
                    print(array[top][i])
                    direction = 1
            elif(direction == 1):
                for i in range(bottom):
                    print(array[i][right])
                    direction = 2
            elif(direction == 2):
                for i in range(right):
                    print(array[bottom][i])
                    direction = 3
            # elif(direction == 3):
            #     for i in range(-bottom, 0):
            #         print(array[i][left])
            #         direction = 0
            #     left = left + 1


l = [
     [2, 3, 6, 8]
    ,[5, 9, 12, 16]
    ,[2, 11, 5, 9]
    ,[3, 4, 1, 8]
]
s = Solution()
nrows = len(l)
ncols = len(l[0])
s.printSpiralOrder(l, nrows, ncols)

#print list(itertools.chain(*transpose_and_yield_top(array)))