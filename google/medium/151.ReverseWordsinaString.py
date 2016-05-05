# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(s.strip().split()[::-1])
        #print ' '.join(r)



s = "the sky is blue"
s = "    "
so = Solution()
print so.reverseWords(s)