import math
class Solution(object):
    def isPowerOfThree(self, n):
        # while (n % 3 == 0):
        #     n /= 3
        #
        # if n == 1:
        #     return True
        # else:
        #     return False

        #return n > 0 and 1162261467 % n == 0

        if n < 1:
            return False
        x = math.log(n, 3)
        return abs(round(x) - x) < 0.0000000000001
