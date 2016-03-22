__author__ = 'canivel'

class Solution(object):

    #O(n) loop goes to n cases
    def findCount(self, l, x):
        y=0
        # for w in l:
        #     if(w == x):
        #         y = y +1
        for w in range(len(l)):
            if l[w] == x:
                y = y + 1
            elif w > x:
                break
        return y

    #Better solution = Binary Search = O(logn)

    def findMostRight(self, l, n, c):
        low = 0
        high = c
        result = -1
        while low <= high:
            mid = (low + high)/2
            if n == l[mid]:
                result = mid
                low = mid + 1
            elif n < l[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return result

    def findMostLeft(self, l, n, c):
        low = 0
        high = c
        result = -1
        while low <= high:
            mid = (low + high)/2
            if n == l[mid]:
                result = mid
                high = mid - 1
            elif n > l[mid]:
                low = mid +1
            else:
                high = mid -1
        return result

    def findCountBinarySearch(self, l, n):
        c = len(l) - 1
        high = self.findMostRight(l,n, c)
        low = self.findMostLeft(l,n, c)
        return (high - low) + 1


l = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
x = 11
s = Solution()
print(s.findCountBinarySearch(l, x))