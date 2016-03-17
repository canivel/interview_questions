__author__ = 'canivel'
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''

class Solution(object):
    # def lengthOfLastWord(self, s):
    #     r = s.split(' ')
    #     if not r:
    #         return 0
    #
    #     result = 0
    #     for i in range(len(r), 0, -1):
    #         if len(r[i-1]) == 0:
    #             continue
    #         else:
    #             result = len(r[i-1])
    #             break
    #
    #     return result
    def lengthOfLastWord(self, s):
        return len(s.rstrip(' ').split(' ')[-1])


if __name__ == "__main__":
    s =  Solution()
    st = "a "
    print s.lengthOfLastWord(st)