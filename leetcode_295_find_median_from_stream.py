__author__ = 'canivel'
'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
'''

import bisect
class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num):
        bisect.insort(self.nums, num)

    def findMedian(self):
        nums = self.nums
        if len(nums) % 2 == 0:
            return (nums[len(nums)/2] + nums[len(nums)/2-1]) / 2.0
        else:
            return nums[len(nums)/2]


if __name__ == "__main__":

    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.addNum(3)
    mf.addNum(4)
    print mf.findMedian()
