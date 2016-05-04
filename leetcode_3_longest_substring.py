__author__ = 'canivel'
'''
Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        cache = {}

        for i in range(len(s)):
            if s[i] in cache and start <= cache[s[i]]:
                start = cache[s[i]] + 1
            else:
                end = max(end, i - start + 1)

            cache[s[i]] = i

        return end

#st = "au"
st = "dvdf"
s = Solution()
print(s.lengthOfLongestSubstring(st))