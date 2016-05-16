# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        r = []
        for i in sorted(intervals, key=lambda i: i.start):
            if not r or i.start > r[-1].end:
                r.append(i)
            elif i.end > r[-1].end:
                r[-1].end = i.end
        return r