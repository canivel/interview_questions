__author__ = 'canivel'
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a,2) + int(b,2))[2:]

if __name__ == "__main__":
    s =  Solution()
    a = "11"
    b = "1"
    print (s.addBinary(a, b))