# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #overflow
        if x < -2147483647 or x > 2147483647:
            return 0

        if x < 0:
            x = abs(x)
            return -int(''.join(list(str(x))[::-1]))
        else:
            return int(''.join(list(str(x))[::-1]))


x = -123
s = Solution()
print s.reverse(x)