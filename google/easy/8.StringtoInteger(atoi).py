# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do
# not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.

import re

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """

        s = s.strip()
        print s
        s = re.findall('(^[\+\-0]*\d+)', s)
        print s
        try:
            result = int(''.join(s))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0

        # pointer = 0
        #
        # isNegative = False
        #
        # while pointer < len(s) and s[pointer] == ' ':
        #     pointer += 1
        #
        # if pointer == len(s):
        #     return 0
        #
        # if s[pointer] == '-':
        #     isNegative = True
        #     pointer += 1
        # elif s[pointer] == '+':
        #     isNegative = False
        #     pointer += 1
        #
        # solution = 0
        # for pointer in range(pointer, len(s)):
        #     if not s[pointer].isdigit():
        #         break
        #     else:
        #         solution *= 10
        #         solution += int(s[pointer])
        #
        # # This is because leetcode question is not prepared to Python but to Java/C so we truncate it
        # if not isNegative and solution > 2147483647:
        #     return 2147483647
        # elif isNegative and solution > 2147483648:
        #     return -2147483648
        #
        # if isNegative:
        #     return -1 * solution;
        # else:
        #     return solution;



l = '23 sds '
s = Solution()
print(s.myAtoi(l))
