__author__ = 'canivel'
'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]

l = [3,6,9,1,2,3,4,5,10000000, 23,3333333]
s = Solution()
print(s.plusOne(l))