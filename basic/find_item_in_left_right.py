__author__ = 'canivel'


class Solution(object):
    #O(logn)
    def findItemIndex(self, nums, val):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)/2
            if val == nums[mid]:
                return mid
            elif val < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

    #O(logn)
    def findMostLeftIndexItem(self, nums, val):
        low = 0
        high = len(nums) - 1
        result = -1
        while low <= high:
            mid = (low+high)/2
            if val == nums[mid]:
                result = mid
                high = mid - 1
            elif val < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return result

    #O(logn)
    def findMostRightIndexItem(self, nums, val):
        low = 0
        high = len(nums) - 1
        result = -1
        while low <= high:
            mid = (low+high)/2
            if val == nums[mid]:
                result = mid
                low = mid + 1
            elif val < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return result


l = [2,4, 10, 10, 10, 18, 20]
x = 10
s = Solution()
print(s.findMostRightIndexItem(l, x))