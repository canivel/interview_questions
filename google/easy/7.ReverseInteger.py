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
        r = 0
        if x < 0:
            x = abs(x)
            r = -int(''.join(list(str(x))[::-1]))
        else:
            r = int(''.join(list(str(x))[::-1]))

        if r < -2147483647 or r > 2147483647:
            return 0
        else:
            return r


x = -123
s = Solution()
print s.reverse(x)