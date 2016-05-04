__author__ = 'canivel'
'''
Given an integer, write a function to determine if it is a power of two.
'''

class Solution(object):
    def isPowerOfTwo(self, n):

        return n > 0 and (n & (n - 1)) == 0

        """
        :type n: int
        :rtype: bool
        single line binary approach return n > 0 and (n & (n - 1)) == 0
        """

if __name__ == "__main__":
    s =  Solution()
    a = 129
    print (s.isPowerOfTwo(a))