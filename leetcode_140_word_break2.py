__author__ = 'canivel'
'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each
word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return findWords(0, len(s), s, wordDict, {})

def findWords(start, end, s, wordDict, cache):
    #print(start, end, s, wordDict, cache)
    if start in cache:
        #print('start in cache {}'.format(cache[start]))
        return cache[start]
    cache[start] = []
    candidate = ''
    current = start
    #print('current {}'.format(current))
    while current < end:

        candidate += s[current]
        current += 1
        if candidate in wordDict:
            #print('{} {}'.format(candidate, end))
            if current == end:
                cache[start].append(candidate)
            else:
                for x in findWords(current, end, s, wordDict, cache):
                    print('{} {}'.format(candidate, x))
                    cache[start].append(candidate + ' ' + x)
    return cache[start]





s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
sl = Solution()
print (sl.wordBreak(s, dict))