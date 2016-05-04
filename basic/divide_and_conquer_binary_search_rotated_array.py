__author__ = 'canivel'


class Solution(object):
    # binary search O(logn) do not work for duplicates
    def findMinElementBinarySearch(self, l, x):
        low = 0
        count = len(l)
        high = count - 1
        while low <= high:

            mid = (low + high) / 2

            if (l[mid] == x):
                return mid

            if(l[mid] <= l[high]):
                if(x > l[mid] and x <= l[high]):
                    low = mid + 1
                else:
                    high = mid - 1
            elif(l[low] <= l[mid]):
                if(x >= l[low] and x < l[mid]):
                    high = mid - 1
                else:
                    low = mid + 1

x = 8
l = [12, 14, 18, 21, 3, 6, 8, 9]
s = Solution()
print(s.findMinElementBinarySearch(l, x))
