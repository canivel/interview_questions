__author__ = 'canivel'
'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(str(i) for i in digits))
        s = str(num+1)
        return [int(i) for i in list(s)]

        # n = int(''.join(str(i) for i in digits))
        # s = str(n+1)
        # return [int(i) for i in s]
        print digits
        digits[-1] += 1

        print digits
        for i in range(len(digits) - 1, 0, -1):
            print i
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i - 1] += 1

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits

       



l = [3,6,9,1,2,3,4,5,10000000, 23,3333333]
s = Solution()
print(s.plusOne(l))

# class Solution(object):
#     def plusOne(self, digits):
#         num = 0
#         for i in range(len(digits)):
#             num += digits[i] * pow(10, (len(digits)-1-i))
#         return [int(i) for i in str(num+1)]
#
# l = [3,6,9,1,2,3,4,5,10000000, 23,3333333]
# s = Solution()
# print(s.plusOne(l))