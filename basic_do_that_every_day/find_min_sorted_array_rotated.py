__author__ = 'canivel'

class Solution(object):

    #simple solution, linear search, O(n)
    def findMinElement(self, l):
        c = len(l) - 1
        m = l[0]
        for i in range(c):
            if l[i] < m:
                m = l[i]

        return m
    #or return min(m)

    #binary search O(logn) do not work for duplicates
    def findMinElementBinarySearch(self, l):
        low = 0
        count = len(l)
        high = count - 1
        while low <= high:
            if(l[low] <= l[high]):
                return low
            mid = (low+high)/2
            next = (mid + 1)%count
            prev = (mid + count-1)%count

            if(l[mid] <= l[next] and l[mid] <= l[prev]):
                return mid
            elif(l[mid] <= l[high]):
                high = mid - 1
            elif(l[mid] >- l[low]):
                low = mid + 1

l = [6, 7, 8, 9, 10, 12, 2, 3, 5]
s = Solution()
print(s.findMinElementBinarySearch(l))